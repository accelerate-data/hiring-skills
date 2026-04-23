from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.check_plugin_version_bump import parse_semver, validate_version_bump


def write_manifest(root: Path, relative_path: str, version: str) -> None:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"version": version}), encoding="utf-8")


def run_git(root: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(root), *args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class VersionBumpTests(unittest.TestCase):
    def test_parse_semver(self) -> None:
        self.assertEqual(parse_semver("1.2.3"), (1, 2, 3))

    def test_parse_semver_rejects_non_semver(self) -> None:
        with self.assertRaises(ValueError):
            parse_semver("1.2")

    def test_rejects_mismatched_manifest_versions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            write_manifest(root, ".claude-plugin/plugin.json", "1.1.1")
            write_manifest(root, ".codex-plugin/plugin.json", "1.1.2")

            errors = validate_version_bump("origin/main", root)

        self.assertEqual(errors, ["Claude and Codex plugin versions must match: '1.1.1' != '1.1.2'"])

    def test_rejects_version_equal_to_base(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            run_git(root, "init", "-b", "main")
            run_git(root, "config", "user.email", "test@example.com")
            run_git(root, "config", "user.name", "Test User")
            write_manifest(root, ".claude-plugin/plugin.json", "1.1.0")
            write_manifest(root, ".codex-plugin/plugin.json", "1.1.0")
            run_git(root, "add", ".")
            run_git(root, "commit", "-m", "base")
            write_manifest(root, ".claude-plugin/plugin.json", "1.1.0")
            write_manifest(root, ".codex-plugin/plugin.json", "1.1.0")

            errors = validate_version_bump("HEAD", root)

        self.assertEqual(
            errors,
            ["plugin version was not bumped or was downgraded (base 1.1.0, current 1.1.0)"],
        )


if __name__ == "__main__":
    unittest.main()
