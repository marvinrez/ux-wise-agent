#!/usr/bin/env python3
"""Who checks the orchestrator.

`selftest.py` covers `checks.py`, and for a long time nothing covered this file,
which is where the exit codes are decided. The contract is three values and it
is the part of the suite an operator reads first:

    0   every probe clean and ruled on, and the deployed wording accounted for
    1   a finding about the agent
    2   a finding about the setup

Each case below breaks one thing in a throwaway copy of the repository and
asserts the code that comes back. Nothing here touches the working tree.

    python gatecheck/test_run_probes.py
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PY = sys.executable


def _green(repo: Path) -> None:
    """Bring a copy to the state that should leave with 0."""
    filled = {"ruling": "pass", "reviewer": "a person", "ran_in": "a harness"}
    for f in sorted((repo / "gatecheck/runlog").glob("P*.md")):
        out = []
        for line in f.read_text(encoding="utf-8").splitlines():
            key = line.partition(":")[0].strip().lower()
            if key in filled and not line.partition(":")[2].strip():
                line = f"{key}: {filled[key]}"
            elif key == "ruling" and line.partition(":")[2].strip() == "pending":
                line = "ruling: pass"
            out.append(line)
        f.write_text("\n".join(out) + "\n", encoding="utf-8")
    # P12 needs its fixture and an answer that satisfies states_as_questions.
    (repo / "gatecheck/fixtures").mkdir(exist_ok=True)
    (repo / "gatecheck/fixtures/populated-screen.png").write_bytes(b"\x89PNG\r\n\x1a\n")
    p12 = repo / "gatecheck/runlog/P12.md"
    p12.write_text(
        p12.read_text(encoding="utf-8")
        + "\n[Direct Mode]\n\n- Is there an empty state?\n"
        "- What does the loading state show?\n- How does the error state read?\n"
        "I cannot describe the partial state without seeing it.\n",
        encoding="utf-8",
    )


def run(repo: Path, *flags: str) -> int:
    out = subprocess.run(
        [PY, str(repo / "gatecheck/run_probes.py"), *flags],
        capture_output=True, text=True, cwd=repo,
    )
    return out.returncode


# Each case: name, what it does to the copy, flags, expected code.
CASES: list[tuple[str, object, tuple[str, ...], int]] = [
    ("as shipped, rulings pending", lambda r: None, (), 2),
    ("everything ruled and accounted for", _green, (), 0),
    ("--count-probes", lambda r: None, ("--count-probes",), 0),
    ("--count-answers", lambda r: None, ("--count-answers",), 0),
    ("--rubrics on a green run", _green, ("--rubrics",), 0),
    ("--scaffold", lambda r: None, ("--scaffold",), 0),
]


def _write(repo: Path, rel: str, text: str) -> None:
    (repo / rel).write_text(text, encoding="utf-8")


def _append(repo: Path, rel: str, text: str) -> None:
    p = repo / rel
    p.write_text(p.read_text(encoding="utf-8") + text, encoding="utf-8")


def _setup_cases() -> list[tuple[str, object, tuple[str, ...], int]]:
    """Every documented setup failure leaves with 2."""
    def malformed(r: Path) -> None:
        _append(r, "gatecheck/probes.toml", "\n[[probe]\nid = broken\n")

    def no_spec(r: Path) -> None:
        (r / "gatecheck/probes.toml").unlink()

    def empty_spec(r: Path) -> None:
        _write(r, "gatecheck/probes.toml", "# nothing here\n")

    def no_title(r: Path) -> None:
        p = r / "gatecheck/probes.toml"
        lines = [ln for ln in p.read_text(encoding="utf-8").splitlines()
                 if not ln.startswith("title = ")]
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def stray_check(r: Path) -> None:
        p = r / "gatecheck/probes.toml"
        p.write_text(
            p.read_text(encoding="utf-8").replace('"mode_tag"', '"mode_tagg"', 1),
            encoding="utf-8",
        )

    def bare_must_hold(r: Path) -> None:
        p = r / "gatecheck/probes.toml"
        p.write_text(
            p.read_text(encoding="utf-8").replace(
                'must_hold = ["mode_tag", "no_percent_figure", "no_behavior_claim"]',
                'must_hold = "mode_tag"', 1),
            encoding="utf-8",
        )

    def duplicate_id(r: Path) -> None:
        _append(r, "gatecheck/probes.toml",
                '\n[[probe]]\nid = "P01"\ntitle = "a second P01"\nprompt = "x"\n')

    def no_answer_file(r: Path) -> None:
        _green(r)
        (r / "gatecheck/runlog/P01.md").unlink()

    def no_reviewer(r: Path) -> None:
        _green(r)
        p = r / "gatecheck/runlog/P03.md"
        p.write_text(p.read_text(encoding="utf-8")
                     .replace("reviewer: a person", "reviewer:"), encoding="utf-8")

    def no_ran_in(r: Path) -> None:
        _green(r)
        p = r / "gatecheck/runlog/P03.md"
        t = p.read_text(encoding="utf-8")
        p.write_text("\n".join(
            "ran_in:" if ln.startswith("ran_in:") else ln for ln in t.splitlines()
        ) + "\n", encoding="utf-8")

    def two_rulings(r: Path) -> None:
        _green(r)
        p = r / "gatecheck/runlog/P01.md"
        p.write_text(p.read_text(encoding="utf-8")
                     .replace("ruling: pass", "ruling: fail\nruling: pass", 1),
                     encoding="utf-8")

    def wrong_probe_field(r: Path) -> None:
        _green(r)
        p = r / "gatecheck/runlog/P01.md"
        p.write_text(p.read_text(encoding="utf-8")
                     .replace("probe: P01", "probe: P07", 1), encoding="utf-8")

    def only_unknown(r: Path) -> None:
        _green(r)

    def prompt_gone(r: Path) -> None:
        _green(r)
        (r / "prompts/system-prompt.md").unlink()

    def markers_gone(r: Path) -> None:
        _green(r)
        p = r / "prompts/system-prompt.md"
        t = p.read_text(encoding="utf-8")
        p.write_text("\n".join(
            ln for ln in t.splitlines() if "SYSTEM PROMPT" not in ln
        ), encoding="utf-8")

    def orphan_runlog(r: Path) -> None:
        _green(r)
        _write(r, "gatecheck/runlog/P99.md",
               "<!-- gatecheck\nprobe: P99\nruling: fail\nreviewer: x\n-->\nbody\n")

    def fixture_gone_but_answered(r: Path) -> None:
        _green(r)
        (r / "gatecheck/fixtures/populated-screen.png").unlink()

    def checks_gone(r: Path) -> None:
        (r / "gatecheck/checks.py").unlink()

    def scaffold_blocked(r: Path) -> None:
        shutil.rmtree(r / "gatecheck/runlog")
        _write(r, "gatecheck/runlog", "not a directory\n")

    return [
        ("malformed TOML", malformed, (), 2),
        ("spec deleted", no_spec, (), 2),
        ("spec with no probe block", empty_spec, (), 2),
        ("probe with no title", no_title, (), 2),
        ("spec names a check that does not exist", stray_check, (), 2),
        ("must_hold written as a bare value", bare_must_hold, (), 2),
        ("the same probe id declared twice", duplicate_id, (), 2),
        ("an answer file is gone", no_answer_file, (), 2),
        ("ruled with no reviewer", no_reviewer, (), 2),
        ("ruled with no ran_in", no_ran_in, (), 2),
        ("two ruling lines in one header", two_rulings, (), 2),
        ("header names another probe", wrong_probe_field, (), 2),
        ("--only names an id the spec lacks", only_unknown, ("--only", "P99"), 2),
        ("--only matches in part", only_unknown, ("--only", "P01,P99"), 2),
        ("the deployed prompt is missing", prompt_gone, (), 2),
        ("the START and END markers are gone", markers_gone, (), 2),
        ("a runlog file with no probe behind it", orphan_runlog, (), 2),
        ("the fixture is gone and the answer is pasted", fixture_gone_but_answered, (), 2),
        ("checks.py is missing", checks_gone, (), 2),
        ("--out cannot be written", _green, ("--out", "/nonexistent-dir-xyz/r.json"), 2),
        ("--scaffold cannot write", scaffold_blocked, ("--scaffold",), 2),
    ]


def _agent_cases() -> list[tuple[str, object, tuple[str, ...], int]]:
    """A finding about the agent leaves with 1."""
    def ruled_fail(r: Path) -> None:
        _green(r)
        p = r / "gatecheck/runlog/P05.md"
        p.write_text(p.read_text(encoding="utf-8")
                     .replace("ruling: pass", "ruling: fail", 1), encoding="utf-8")

    def pattern_overrides_pass(r: Path) -> None:
        _green(r)
        p = r / "gatecheck/runlog/P10.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n\nSeverity: high.\n",
                     encoding="utf-8")

    return [
        ("a reviewer ruled against the rubric", ruled_fail, (), 1),
        ("a pattern fires under a pass ruling", pattern_overrides_pass, (), 1),
    ]


def main() -> int:
    cases = CASES + _setup_cases() + _agent_cases()
    wrong: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        for i, (name, prepare, flags, want) in enumerate(cases):
            repo = Path(tmp) / f"c{i}"
            shutil.copytree(
                ROOT, repo,
                ignore=shutil.ignore_patterns(".git", ".venv", "__pycache__",
                                              "report.json"),
            )
            prepare(repo)
            got = run(repo, *flags)
            if got != want:
                wrong.append(f"{name}: wanted {want}, got {got}")
    print()
    print(f"  gatecheck exit-code contract · {len(cases)} path(s)")
    if wrong:
        print(f"  {len(wrong)} wrong:")
        for w in wrong:
            print(f"    - {w}")
        print()
        return 1
    print(f"  all {len(cases)} paths returned the documented code")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
