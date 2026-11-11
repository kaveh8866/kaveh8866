"""Validate the concise bilingual profile and project metadata offline."""
import json
import re
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
for page in ["README.md", "README.de.md", "PORTFOLIO.md", "PORTFOLIO.de.md"]:
    text = (root / page).read_text(encoding="utf-8")
    assert "SAA-C03" not in text and "micro-lab" not in text.lower(), page
    assert len(text) < 4800, f"Page too long for concise hiring portfolio: {page}"
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if "://" not in link and not link.startswith("#"):
            assert (root / link.split("#", 1)[0]).exists(), f"Broken local link {link} in {page}"
for listed in data["featured_public_repositories"]:
    assert listed["repository"].startswith("https://github.com/"), listed
assert data["certifications"] == [], "Do not invent or pre-list certifications"
print("Bilingual profile links, concise content and portfolio registry: OK")
