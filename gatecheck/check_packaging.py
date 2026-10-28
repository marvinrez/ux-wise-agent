#!/usr/bin/env python3
"""Two invariants about the plugin that nothing else holds.

`claude plugin validate` is the authority on the manifests and it needs the CLI,
which CI does not have. This does not imitate it. It checks the two things that
can be checked from the files alone, one of which has already been wrong once:

  1. both manifests parse as JSON
  2. the version in .claude-plugin/plugin.json is the version in SKILL.md
  3. git is tracking all three, because a manifest that exists only on the
     author's disk is a manifest nobody can install from

A plugin shipped with a stale version installs under that stale version, and the
mismatch is invisible until someone reads both files side by side.
"""

from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
MARKET = ROOT / ".claude-plugin" / "marketplace.json"
SKILL = ROOT / "SKILL.md"


def main() -> int:
    wrong: list[str] = []
    # None means absent or unparseable. An empty dict is a manifest that parsed
    # and holds nothing, and conflating the two printed "the versions agree"
    # over a plugin.json of {}, which is a false sentence.
    data: dict | None = None
    for path in (PLUGIN, MARKET):
        if not path.exists():
            wrong.append(f"{path.relative_to(ROOT)} is missing")
            continue
        try:
            parsed = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            wrong.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
            continue
        if path is PLUGIN:
            data = parsed

    if not SKILL.exists():
        wrong.append(f"{SKILL.relative_to(ROOT)} is missing")
        print("  ! " + wrong[-1])
        return 1
    head = SKILL.read_text(encoding="utf-8").split("---")
    frontmatter = head[1] if len(head) > 2 else ""
    found = re.search(r"^version:\s*[\"\']?([\w.+-]+)", frontmatter, re.M)
    skill_version = found.group(1) if found else ""

    plugin_version = "" if data is None else str(data.get("version", ""))

    if data is None:
        pass  # the manifest already failed above; one cause, one finding
    elif not skill_version:
        wrong.append("SKILL.md frontmatter has no version")
    elif not plugin_version:
        wrong.append("plugin.json has no version")
    elif skill_version != plugin_version:
        wrong.append(
            f"plugin.json says {plugin_version} and SKILL.md says {skill_version}"
        )

    # The failure that actually stops an install is a file git never saw. This
    # repository announced an install command for a manifest that was untracked,
    # and both invariants above passed the whole time, because they read the
    # disk and an install reads what was pushed.
    try:
        subprocess.run(
            ["git", "ls-files", "--error-unmatch",
             str(PLUGIN.relative_to(ROOT)), str(MARKET.relative_to(ROOT)),
             str(SKILL.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, check=True,
        )
    except subprocess.CalledProcessError:
        wrong.append(
            "git is not tracking all of plugin.json, marketplace.json and "
            "SKILL.md, so the announced install cannot reach them"
        )
    except (OSError, FileNotFoundError):
        print("  ? no git here, so the tracking check did not run")

    print(f"  plugin.json {plugin_version or '(none)'} · "
          f"SKILL.md {skill_version or '(none)'}")
    if wrong:
        for w in wrong:
            print(f"  ! {w}")
        return 1
    print("  manifests parse and the versions agree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
