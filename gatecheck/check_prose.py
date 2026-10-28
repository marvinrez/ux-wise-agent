#!/usr/bin/env python3
"""The damage an anchored edit does to prose, which nothing else here reads.

Every other check in this directory reads code, counts, or manifests. None of
them reads a paragraph, and an edit script that matches its anchor and mangles
the sentence around it prints success. That happened four times in one pass of
this repository: a prefix anchor split a document title and left its tail
dangling, and three insertions duplicated a sentence or broke one in half.

Two signals, both of which caught real damage here and neither of which needs
to understand English:

  1. a line far wider than the file it sits in, which is what an insertion into
     hard-wrapped prose leaves behind
  2. a long run of words repeated inside one file

The first fails the run. The second only reports, because a repeat is sometimes
the point: this repository quotes the same statute in an entry and again in its
sources section, and that is not damage. Read the notes, do not gate on them.

Exit 1 on a finding, 0 on none. No network, no model, standard library only.

    python gatecheck/check_prose.py
"""

from __future__ import annotations

import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP = {".git", ".venv", "node_modules", "__pycache__", "runlog"}
GRAM = 10
WIDE = 100
# Below this, a file is not hard-wrapped and a long line means nothing.
WRAPPED_AT = 88


def _files() -> list[pathlib.Path]:
    out = []
    for p in sorted(ROOT.rglob("*.md")):
        if not SKIP & set(p.relative_to(ROOT).parts):
            out.append(p)
    return out


def _prose_lines(text: str) -> list[str]:
    """Markdown prose only: no fenced code, no tables, no reference lines."""
    out, fenced = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced or line.lstrip().startswith("|") or "](" in line:
            continue
        out.append(line)
    return out


def repeated_sentences(path: pathlib.Path) -> list[str]:
    lines = _prose_lines(path.read_text(encoding="utf-8"))
    words = re.findall(r"[A-Za-z'’]+", " ".join(lines))
    grams = collections.Counter(
        " ".join(words[i : i + GRAM]).lower() for i in range(len(words) - GRAM + 1)
    )
    # Every window here is the same length, so no window contains another and
    # containment cannot collapse them. Group by position instead: consecutive
    # repeated windows are one repeat, reported once, at its full extent.
    repeated = {g for g, c in grams.items() if c > 1}
    hot = [
        i
        for i in range(len(words) - GRAM + 1)
        if " ".join(words[i : i + GRAM]).lower() in repeated
    ]
    runs: list[tuple[int, int]] = []
    for i in hot:
        if runs and i == runs[-1][1] + 1:
            runs[-1] = (runs[-1][0], i)
        else:
            runs.append((i, i))
    return [" ".join(words[a : b + GRAM]) for a, b in runs]


def broke_the_wrap(path: pathlib.Path) -> list[tuple[int, int]]:
    lines = _prose_lines(path.read_text(encoding="utf-8"))
    # The ninetieth percentile, not the median. A file of long paragraphs has a
    # low median too, because its headings and bullets are short, and that read
    # 510 ordinary lines of this repository as damage.
    widths = sorted(len(x) for x in lines if len(x.strip()) > 40)
    if len(widths) < 5:
        return []
    if widths[int(len(widths) * 0.9)] > WRAPPED_AT:
        return []
    # A heading or a long link is not an insertion scar.
    return [
        (i, len(x))
        for i, x in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
        if len(x) > WIDE and not x.lstrip().startswith(("#", ">", "|", "`"))
        and "](" not in x
    ]


def main() -> int:
    findings: list[str] = []
    notes: list[str] = []
    for path in _files():
        rel = path.relative_to(ROOT)
        for line, width in broke_the_wrap(path):
            findings.append(f"{rel}:{line}: {width} columns in a wrapped file")
        for gram in repeated_sentences(path):
            notes.append(f"{rel}: repeated: {gram[:70]}")
    print()
    print(f"  gatecheck prose · {len(_files())} markdown file(s)")
    for n in notes:
        print(f"    ~ {n}")
    if findings:
        print(f"  {len(findings)} finding(s):")
        for f in findings:
            print(f"    - {f}")
        print()
        return 1
    print(f"  no line breaks its file's wrap · {len(notes)} repeat(s) to read")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
