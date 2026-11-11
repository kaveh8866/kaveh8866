"""Lightweight validation for the public profile and its portfolio registry."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "portfolio" / "projects.json").read_text(encoding="utf-8"))
projects = data["planned_projects"]
assert len(projects) == 10, "Expected initial batch of ten projects"
ids = [p["id"] for p in projects]
assert ids == [f"{i:02}" for i in range(1, 11)], "Project IDs must be ordered and unique"
slugs = [p["slug"] for p in projects]
assert len(set(slugs)) == len(slugs), "Duplicate project slug"
allowed = {"planned", "in_progress", "local_verified", "cloud_verified", "published"}
for p in projects:
    assert p["status"] in allowed, f"Unexpected project status: {p['id']}"
    assert p["title"] and p["title_de"] and p["tech"], f"Missing bilingual metadata: {p['id']}"
    if p["status"] == "planned":
        assert p["repository"] is None, f"Planned project has published repo: {p['id']}"
    if p["status"] in ("cloud_verified", "published"):
        assert p["repository"], f"Project requires a published link: {p['id']}"
    assert isinstance(p["verified_providers"], list)
for path in ["README.md", "README.de.md", "PORTFOLIO.md", "PORTFOLIO.de.md"]:
    text = (root / path).read_text(encoding="utf-8")
    assert "SAA-C03" not in text and "micro-lab" not in text.lower(), path
for repo in data["featured_public_repositories"]:
    assert repo["repository"].startswith("https://github.com/"), repo
assert data["certifications"] == [], "Do not invent or pre-list certifications"
print("Profile and portfolio registry structure: OK")
