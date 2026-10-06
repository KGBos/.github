import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDERER = ROOT / "scripts/render-agent-instructions.py"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RenderAgentInstructionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.shared = self.root / "shared.md"
        self.local = self.root / "local.md"
        self.output = self.root / "AGENTS.md"
        self.lock = self.root / "policy.lock.json"
        self.shared.write_text("# Shared\n\nShared rule.\n", encoding="utf-8")
        self.local.write_text("# Local\n\nLocal rule.\n", encoding="utf-8")

    def run_renderer(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", str(RENDERER), "--shared", str(self.shared), "--local", str(self.local),
             "--output", str(self.output), *args],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_render_then_check(self) -> None:
        rendered = self.run_renderer("--source-label", "example@revision")
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        checked = self.run_renderer("--source-label", "example@revision", "--check")
        self.assertEqual(checked.returncode, 0, checked.stderr)
        contents = self.output.read_text(encoding="utf-8")
        self.assertIn("# Shared", contents)
        self.assertIn("# Local", contents)

    def test_check_fails_after_source_changes(self) -> None:
        self.run_renderer("--source-label", "example@revision")
        self.local.write_text("# Local\n\nChanged.\n", encoding="utf-8")
        checked = self.run_renderer("--source-label", "example@revision", "--check")
        self.assertEqual(checked.returncode, 1)
        self.assertIn("out of date", checked.stderr)

    def test_lock_pins_source_and_renderer_digests(self) -> None:
        lock_data = {
            "source_repository": "KGBos/.github",
            "source_revision": "a" * 40,
            "source_path": "agent-policy/AGENTS.shared.md",
            "renderer_path": "scripts/render-agent-instructions.py",
            "shared_sha256": digest(self.shared),
            "renderer_sha256": digest(RENDERER),
        }
        self.lock.write_text(json.dumps(lock_data), encoding="utf-8")
        rendered = self.run_renderer("--lock", str(self.lock))
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertIn(f"KGBos/.github@{'a' * 40}", self.output.read_text(encoding="utf-8"))
        self.shared.write_text("tampered\n", encoding="utf-8")
        checked = self.run_renderer("--lock", str(self.lock), "--check")
        self.assertEqual(checked.returncode, 2)
        self.assertIn("does not match shared_sha256", checked.stderr)


if __name__ == "__main__":
    unittest.main()
