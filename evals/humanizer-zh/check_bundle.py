"""Verify the pinned humanizer-zh bundle offline; not a writing-quality test."""

import hashlib
import json
from pathlib import Path
import re


def main():
    root = Path(__file__).resolve().parents[2]
    manifest = json.loads(
        (root / "references/humanizer-zh-source.json").read_text(encoding="utf-8")
    )
    checks = {}
    for entry in manifest["files"]:
        path = (root / entry["path"]).resolve()
        if not path.is_relative_to(root):
            raise ValueError("Bundle file outside repository")
        checks[entry["path"]] = (
            path.is_file()
            and hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
        )

    guide = (root / "references/humanizer-zh.md").read_text(encoding="utf-8")
    numbers = re.findall(r"^### (\d+)\. ", guide, re.M)
    checks["all_31_patterns"] = numbers == [str(n) for n in range(1, 32)]
    cases = json.loads(
        (root / "evals/humanizer-zh/upstream/fixtures/cases.json").read_text(
            encoding="utf-8"
        )
    )
    checks["18_unique_upstream_cases"] = (
        len(cases) == len({case["id"] for case in cases}) == 18
    )
    passed = all(checks.values())
    print(json.dumps({"checks": checks, "passed": passed}, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
