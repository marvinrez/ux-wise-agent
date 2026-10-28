#!/usr/bin/env python3
"""Gatecheck: run the acceptance probes and report PASS / FAIL.

The probes in docs/grounding-gate.md are prompts with expected behaviour. Read by
a person they are a checklist, and docs/ownership.md asks the named owner to work
through them after any edit to the system prompt and after any model change. A
checklist that is worked through by hand is worked through once. This turns the
twelve, plus three written for this suite, into one with an exit code.

Nothing here calls an API. The agent runs wherever you actually use it, in a
Claude Project, an editor or a terminal, and its answers are pasted into
runlog/. That keeps the suite runnable by anyone who has the repository, with no
key, no billing account and no package to install, and it tests the deployment
people really use rather than a second one built for the test.

Two layers decide each probe, and neither can stand in for the other.

  Checks    Deterministic patterns (checks.py). They catch what has a shape: a
            figure nobody supplied, a reference with an author and a year, a
            conformance ruling, a grade on an artifact nobody sent, a sentence
            about what *your* people did. Free, instant, and blind to meaning.

  Review    The owner's own call on the rubric each probe carries. Meaning is
            the part a pattern cannot reach, so a person reads the answer and
            writes their ruling into the file. An unreviewed probe counts as
            unfinished, never as a pass.

Usage

  python gatecheck/run_probes.py --scaffold     write empty files to paste into
  python gatecheck/run_probes.py                check and report
  python gatecheck/run_probes.py --rubrics   also show what to read for
  python gatecheck/run_probes.py --only P05,P09

Exit codes

  0  every selected probe is clean and reviewed
  1  at least one probe failed, on a pattern or on the owner's ruling
  2  the suite could not finish: a file is absent, unreviewed, malformed, or
     names a check that does not exist
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and older
    # At module scope on purpose. Behind a version check inside read_spec, this
    # message could never print: the import failed first and the operator got a
    # bare ModuleNotFoundError instead.
    print(
        "  gatecheck reads its spec with tomllib, which arrived in Python 3.11. "
        f"This is {sys.version.split()[0]}.",
        file=sys.stderr,
    )
    raise SystemExit(2) from None
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    import checks  # noqa: E402
except ModuleNotFoundError:
    # Absent checks.py is a finding about the setup, not about the agent, and an
    # uncaught ModuleNotFoundError leaves with 1, which is the agent's code.
    print("\n  gatecheck/checks.py is missing, so no pattern can run\n", file=sys.stderr)
    raise SystemExit(2) from None

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = HERE / "probes.toml"
RUNLOG = HERE / "runlog"
WORDING = ROOT / "prompts" / "system-prompt.md"

HEAD = re.compile(r"\A<!--\s*gatecheck(.*?)-->\s*", re.S)
RULINGS = ("pass", "fail", "pending")


@dataclass
class Row:
    probe_id: str
    title: str
    state: str = "PASS"  # PASS | FAIL | STALLED | WAIVED
    wanted: str = ""
    broke: list[str] = field(default_factory=list)
    noted: list[str] = field(default_factory=list)
    ruling: str = ""
    reviewer: str = ""
    aside: str = ""


# --------------------------------------------------------------------------
# the spec
# --------------------------------------------------------------------------


def _setup_failure(message: str) -> None:
    """Leave with 2, which is this suite's code for a finding about the setup.

    `sys.exit(str)` prints the string and exits 1, and 1 is reserved here for a
    finding about the agent. Every documented setup failure used to come out as
    1, which is the confusion the exit codes were split to prevent.
    """
    print(f"\n  {message}\n", file=sys.stderr)
    raise SystemExit(2)


def read_spec() -> list[dict]:
    if not SPEC.exists():
        _setup_failure(f"no probe spec at {SPEC}")
    try:
        parsed = tomllib.loads(SPEC.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as broken:
        _setup_failure(f"{SPEC.name} is not valid TOML: {broken}")
    probes = parsed.get("probe", [])
    if not probes:
        _setup_failure(f"no [[probe]] blocks in {SPEC}")
    thin = [
        p.get("id", "(a block with no id)")
        for p in probes
        if not all(p.get(field) for field in ("id", "title", "prompt"))
    ]
    if thin:
        _setup_failure(
            f"{SPEC.name} has {len(thin)} probe(s) missing id, title or prompt: "
            f"{', '.join(thin)}. Reported here rather than as a KeyError later."
        )
    seen: dict[str, int] = {}
    for p in probes:
        seen[p["id"].upper()] = seen.get(p["id"].upper(), 0) + 1
    twice = sorted(i for i, n in seen.items() if n > 1)
    if twice:
        _setup_failure(
            f"{SPEC.name} declares {', '.join(twice)} more than once. Two blocks "
            "read the same answer file and both report, so the count is wrong "
            "and nothing says which block decided."
        )
    loose = [
        f"{p['id']}.{field}"
        for p in probes
        for field in ("must_hold", "worth_noting")
        if field in p and not isinstance(p[field], list)
    ]
    if loose:
        _setup_failure(
            f"{SPEC.name} has {', '.join(loose)} written as a bare value rather "
            "than a list. Reported here rather than as a TypeError below."
        )
    stray = {
        name
        for p in probes
        for name in p.get("must_hold", []) + p.get("worth_noting", [])
        if name not in checks.CATALOGUE
    }
    if stray:
        _setup_failure(
            f"{SPEC.name} names {len(stray)} check(s) that do not exist: "
            f"{', '.join(sorted(stray))}. A misspelled check is a probe that "
            "always passes, so this stops here."
        )
    return probes


def audit_wording() -> tuple[list[str], list[str]]:
    """Report on the pasteable block without reading a model's answer.

    Returns (notes, findings). The split is the point. Every one of these used
    to come back in one list that was printed, written to the report, and then
    never consulted by the exit code, so a run with no system prompt in the
    repository at all still left with 0 while the report said so on screen. A
    docstring calling that "one of two setup failures the probes were written to
    catch" was true of the detection and false of the verdict.
    """
    notes: list[str] = []
    findings: list[str] = []
    if not WORDING.exists():
        return notes, [
            f"{WORDING.name} is missing, so the suite cannot say what was deployed"
        ]
    raw = WORDING.read_text(encoding="utf-8")
    opens = re.search(r"^##\s*SYSTEM PROMPT\s*[\u2014\u2013-]{1,2}\s*START\s*$", raw, re.M)
    shuts = re.search(r"^##\s*SYSTEM PROMPT\s*[\u2014\u2013-]{1,2}\s*END\s*$", raw, re.M)
    if not opens or not shuts:
        return notes, [
            f"{WORDING.name}: the START or END marker is gone; the pasteable "
            "block can no longer be told from the file's commentary"
        ]
    body = raw[opens.end() : shuts.start()].strip()
    notes.append(f"{WORDING.name}: {len(body):,} characters between the markers")
    if len(body) < 4000:
        findings.append("that is short enough to read as a truncated paste")
    for needed in ("Grounding Gate", "Unverified:", "Arbitration"):
        if needed not in body:
            findings.append(f"the block does not contain {needed!r}")
    return notes, findings


# --------------------------------------------------------------------------
# the pasted answers
# --------------------------------------------------------------------------


def _runlog_is_committed() -> bool:
    """True when nothing under runlog/ is uncommitted, so a rewrite is recoverable."""
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain", "--", str(RUNLOG.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return False
    return not out.stdout.strip()


def _scaffold_text(p: dict) -> str:
    asked = "\n".join(f"    {line}" for line in p["prompt"].strip().splitlines())
    picture = (
        f"\nSend this image with it: gatecheck/{p['image']}\n" if p.get("image") else ""
    )
    # The rubric goes in the file. Sending the operator to probes.toml for it,
    # in the middle of a fifteen-probe run, is how a run gets abandoned or how a
    # ruling gets made against a half-remembered rule.
    rubric = (p.get("rubric") or "").strip()
    carried = (
        "\nRule on it against this, and nothing else:\n\n"
        + "\n".join(f"    {line}" for line in rubric.splitlines())
        + "\n"
        if rubric
        else ""
    )
    return (
        "<!-- gatecheck\n"
        f"probe: {p['id']}\n"
        "ran_in: \n"
        f"dated: {datetime.now(timezone.utc).date()}\n"
        "ruling: pending\n"
        "reviewer: \n"
        "\n"
        "Send this as the user turn, following any instruction inside it:\n\n"
        f"{asked}\n"
        f"{picture}"
        f"{carried}"
        "\nThen set ruling to pass or fail, put your name in reviewer, name the\n"
        "environment you ran in under ran_in, and paste the whole answer below,\n"
        "with nothing of your own mixed into it.\n"
        "-->\n\n"
    )


def scaffold(probes: list[dict], rewrite: bool = False) -> int:
    """Write a file per probe, ready to paste into.

    `rewrite` is for the run after a prompt edit or a model change, which
    docs/ownership.md asks for and which otherwise means deleting fifteen files
    by hand. It refuses unless runlog/ is committed, so what it overwrites can
    always be recovered.
    """
    RUNLOG.mkdir(exist_ok=True)
    if rewrite and not _runlog_is_committed():
        _setup_failure(
            "--rescaffold overwrites every probe file, and runlog/ has changes "
            "that are not committed. Commit or stash them first, so what this "
            "would replace can be recovered."
        )
    made, kept = 0, 0
    for p in probes:
        path = RUNLOG / f"{p['id']}.md"
        if path.exists() and not rewrite:
            kept += 1
            continue
        path.write_text(_scaffold_text(p), encoding="utf-8")
        made += 1
    verb = "rewritten" if rewrite else "written"
    print(f"\n  {made} file(s) {verb}, {kept} left alone, in "
          f"{RUNLOG.relative_to(ROOT)}\n")
    return 0


def read_answer(probe_id: str) -> tuple[str | None, dict, str]:
    """Return (answer, header fields, trouble)."""
    path = RUNLOG / f"{probe_id}.md"
    if not path.exists():
        return None, {}, (
            f"nothing at gatecheck/runlog/{probe_id}.md: start with --scaffold, "
            "then paste what the agent said"
        )
    raw = path.read_text(encoding="utf-8")
    head = HEAD.match(raw)
    if head is None and raw.lstrip().startswith("<!--"):
        # Naming the real cause matters here. Reported as a missing ruling, this
        # sends the owner looking for a reviewer who already wrote one.
        return None, {}, (
            "the header is open and never closed: add a line holding --> after "
            "the reviewer field"
        )
    fields: dict[str, str] = {}
    if head:
        for line in head.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, _, v = line.partition(":")
                k = k.strip().lower()
                if k in {"probe", "ran_in", "dated", "ruling", "reviewer"}:
                    if k in fields and fields[k] != v.strip():
                        # Last line used to win, in silence. Two ruling lines
                        # saying different things is a file nobody can read.
                        return None, fields, (
                            f"the header gives {k} twice, as {fields[k]!r} and "
                            f"{v.strip()!r}. Leave one."
                        )
                    fields[k] = v.strip()
        body = raw[head.end() :].strip()
    else:
        body = raw.strip()
    stated = fields.get("probe", "").strip().upper()
    if stated and stated != probe_id.upper():
        # The field exists to identify the answer. Never checked, it is
        # decoration, and a pasted answer can sit under the wrong probe's
        # rubric with nothing to say so.
        return None, fields, (
            f"this file is {probe_id}.md and its header says probe: {stated}. "
            "One of the two is wrong"
        )
    if not body:
        return None, fields, "the file holds no answer yet, only its header"
    return body, fields, ""


# --------------------------------------------------------------------------
# checking
# --------------------------------------------------------------------------


def _line(name: str, found: checks.Finding) -> str:
    """A finding with the sentence it came out of, where the check kept one.

    `Finding.spans` carried that context and nothing read it, so the work
    `sentence_around` does was computed and thrown away on every run.
    """
    line = f"{name}: {found.detail}"
    if found.spans:
        context = " ".join(found.spans[0].split())[:140]
        if context and context not in line:
            line += f"  <- {context}"
    return line


def apply_checks(probe: dict, answer: str) -> tuple[list[str], list[str]]:
    broke, noted = [], []
    for name in probe.get("must_hold", []):
        found = checks.CATALOGUE[name](answer, probe)
        if not found.clean:
            broke.append(_line(name, found))
    for name in probe.get("worth_noting", []):
        found = checks.CATALOGUE[name](answer, probe)
        if not found.clean:
            noted.append(_line(name, found))
    for wording in probe.get("watch_for", []):
        if wording.lower() in answer.lower():
            around = checks.sentence_around(answer, wording)
            noted.append(f"watched wording {wording!r}: {around or '(no context found)'}")
    return broke, noted


# --------------------------------------------------------------------------
# the report
# --------------------------------------------------------------------------

BADGE = {"PASS": "PASS", "FAIL": "FAIL", "STALLED": "STOP", "WAIVED": "SKIP"}


def write_report(rows: list[Row], setup: list[str], where: Path, show_rubrics: dict) -> None:
    pad = max((len(r.title) for r in rows), default=20)
    print()
    for line in setup:
        print(f"  {line}")
    print(f"\n  gatecheck · {len(rows)} probe(s)")
    print(f"  {'-' * (pad + 14)}")
    for r in rows:
        who = f"  [{r.ruling}{', ' + r.reviewer if r.reviewer else ''}]" if r.ruling else ""
        print(f"  {BADGE[r.state]}  {r.probe_id}  {r.title:{pad}}{who}")
        for b in r.broke:
            print(f"        ! {b}")
        if r.aside:
            print(f"        - {r.aside}")
        for n in r.noted:
            print(f"        ~ {n[:220]}")
        if r.probe_id in show_rubrics:
            for line in show_rubrics[r.probe_id].strip().splitlines():
                print(f"        | {line}")
    print(f"  {'-' * (pad + 14)}")
    count = {s: sum(1 for r in rows if r.state == s) for s in BADGE}
    print(
        f"  {count['PASS']} passed · {count['FAIL']} failed · "
        f"{count['STALLED']} unfinished · {count['WAIVED']} waived"
    )
    print(f"  report: {where.relative_to(ROOT) if where.is_relative_to(ROOT) else where}\n")

    where.write_text(
        json.dumps(
            {
                "written": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "setup": setup,
                "count": count,
                "probes": [
                    {
                        "id": r.probe_id,
                        "title": r.title,
                        "state": r.state,
                        "wanted": r.wanted,
                        "broke": r.broke,
                        "noted": r.noted,
                        "ruling": r.ruling,
                        "reviewer": r.reviewer,
                        "aside": r.aside,
                    }
                    for r in rows
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description="Run the gatecheck probe suite.")
    ap.add_argument("--scaffold", action="store_true",
                    help="write a file per probe, ready to paste into, leaving "
                         "any that already exist alone")
    ap.add_argument("--rescaffold", action="store_true",
                    help="rewrite every probe file from the spec, for the run "
                         "after a prompt edit or a model change. Refuses unless "
                         "runlog/ is committed")
    ap.add_argument("--rubrics", action="store_true",
                    help="print what each probe asks the reviewer to decide")
    ap.add_argument("--count-answers", action="store_true",
                    help="print how many probe files carry a pasted answer, and stop")
    ap.add_argument("--count-probes", action="store_true",
                    help="print how many probes the spec holds, and stop")
    ap.add_argument("--only", default="", help="probe ids, comma separated, e.g. P01,P09")
    ap.add_argument("--out", default=str(HERE / "report.json"))
    args = ap.parse_args()

    probes = read_spec()
    if args.only:
        want = {x.strip().upper() for x in args.only.split(",") if x.strip()}
        have = {p["id"].upper() for p in probes}
        probes = [p for p in probes if p["id"].upper() in want]
        # A selection that matched in part used to be accepted in silence, so a
        # mistyped id was dropped and the operator got a clean code over fewer
        # probes than they asked for.
        missed = sorted(want - have)
        if missed:
            _setup_failure(
                f"--only names {', '.join(missed)}, which the spec does not "
                "hold. Ids are: " + ", ".join(p["id"] for p in read_spec())
            )

    if args.count_probes:
        # The workflow used to hard-code the total, which drifts the first time a
        # probe is added. The spec owns the number.
        print(len(probes))
        return 0

    if args.count_answers:
        # The only thing that may decide whether a file holds an answer is the
        # reader that the suite itself uses. A second implementation elsewhere,
        # in a shell or a workflow, is a second opinion, and the two drift.
        print(sum(1 for p in probes if read_answer(p["id"])[0] is not None))
        return 0

    if args.scaffold or args.rescaffold:
        try:
            return scaffold(probes, rewrite=args.rescaffold)
        except OSError as blocked:
            _setup_failure(f"cannot write into {RUNLOG}: {blocked}")

    rows: list[Row] = []
    for probe in probes:
        r = Row(probe["id"], probe["title"], wanted=probe.get("wanted", ""))

        answer, fields, trouble = read_answer(probe["id"])
        # Checked before the answer, not only in its absence. Consulted only on
        # the missing-answer path, the waiver let a probe whose fixture is absent
        # be ruled pass and reported PASS, which is a verdict on a turn that was
        # never sent.
        if probe.get("image") and not (HERE / probe["image"]).exists():
            r.state = "WAIVED"
            r.aside = (
                f"waiting on an image at gatecheck/{probe['image']}, which this "
                "probe cannot run without"
            )
            rows.append(r)
            continue
        if answer is None:
            r.state = "STALLED"
            r.aside = trouble
            rows.append(r)
            continue

        r.ruling = (fields.get("ruling") or "").lower()
        r.reviewer = fields.get("reviewer", "")
        r.broke, r.noted = apply_checks(probe, answer)

        if r.ruling not in RULINGS:
            r.state = "STALLED"
            r.aside = (
                f"ruling is {r.ruling!r}; it has to be one of {', '.join(RULINGS)}"
                if r.ruling
                else "no ruling in the header, so nobody has read this answer"
            )
        elif r.ruling == "pending":
            r.state = "STALLED"
            r.aside = (
                "ruling is still pending. A pattern cannot settle the rubric, "
                "so this stays unfinished until a person does."
            )
        elif not r.reviewer:
            r.state = "STALLED"
            r.aside = f"ruling is {r.ruling!r} with no reviewer named"
        elif not (fields.get("ran_in") or "").strip():
            # Scaffolded so a stale run can be spotted, then never read. An
            # answer with no environment named cannot be told from one produced
            # somewhere else, and docs/ownership.md asks for the environment.
            r.state = "STALLED"
            r.aside = (
                f"ruling is {r.ruling!r} with no ran_in, so nothing says where "
                "this answer came from"
            )
        elif r.ruling == "fail":
            r.broke.append(f"{r.reviewer} ruled this against the rubric")

        # A pattern finding needs no reviewer. Computing it, printing it, and
        # then reporting the probe as merely unfinished was the one case where
        # the machine had already answered and the suite said it had not.
        if r.broke:
            r.state = "FAIL"
        rows.append(r)

    show = {p["id"]: p.get("rubric", "") for p in probes} if args.rubrics else {}
    where = Path(args.out).resolve()
    notes, setup_findings = audit_wording()
    # A runlog file with no probe behind it is a probe that was renamed or
    # dropped, and the ruling sitting in that file is invisible to this run.
    known = {p["id"].upper() for p in read_spec()}
    orphans = sorted(
        f.name for f in RUNLOG.glob("P*.md") if f.stem.upper() not in known
    )
    if orphans:
        setup_findings.append(
            f"{', '.join(orphans)} in runlog/ with no probe of that id in "
            f"{SPEC.name}; any ruling in those files is not being read"
        )
    try:
        write_report(rows, notes + setup_findings, where, show)
    except OSError as blocked:
        # Crashing here left with 1, the agent's code, and masked a real 2.
        _setup_failure(f"cannot write the report to {where}: {blocked}")

    # A failure the agent produced outranks a file nobody has pasted into. The
    # normal state of this suite, while the probes are being worked through, is
    # that some are unanswered, and reporting every real failure as 2 while that
    # is true turns an agent finding into a setup finding on every run that
    # matters. The unfinished probes are named in the report either way.
    if any(r.state == "FAIL" for r in rows):
        return 1
    # A waived probe has no answer, no ruling and no check behind it, so it
    # cannot leave with the code that means every probe is clean and ruled on.
    if any(r.state in {"STALLED", "WAIVED"} for r in rows):
        return 2
    # What was deployed is part of the result. These were detected and printed
    # for as long as this file has existed, and never reached the code.
    if setup_findings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
