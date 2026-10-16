"""Offline smoke tests. Never contact AWS."""
import json
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]


class TestPortfolio(unittest.TestCase):
    def test_domains_and_levels(self):
        labs = json.loads((BASE / "data/labs.json").read_text(encoding="utf-8"))["labs"]
        self.assertEqual(len(labs), 16)
        for week in range(1, 5):
            self.assertEqual({x["domain"] for x in labs if x["week"] == week},
                             {"D1", "D2", "D3", "D4"})

    def test_planned_not_fabricated(self):
        labs = json.loads((BASE / "data/labs.json").read_text(encoding="utf-8"))["labs"]
        self.assertTrue(all(x["status"] == "planned" and not x["aws_tested"]
                            for x in labs))

    def test_profile(self):
        text = (BASE / "README.md").read_text(encoding="utf-8")
        self.assertIn("@kaveh8866", text)
        self.assertIn("SAA-C03", text)


if __name__ == "__main__":
    unittest.main()
