"""Validate the concise, bilingual employment-focused profile and project registry offline."""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "portfolio" / "projects.json").read_text(encoding="utf-8"))
projects = data["planned_projects"]
assert len(projects) == 10, "Expected first batch of ten projects"
assert [p["id"] for p in projects] == [f"{i:02}" for i in range(1, 11)]
assert len({p["slug"] for p in projects}) == len(projects), "Duplicate project slug"
allowed = {"planned", "in_progress", "local_verified", "cloud_verified", "published"}
for project in projects:
    assert project["status"] in allowed, f"Unexpected status: {project['id']}"
    assert project["title"] and project["title_de"] and project["tech"]
    if project["status"] == "planned":
        assert project["repository"] is None, f"Planned project has repo: {project['id']}"
    if project["status"] in ("cloud_verified", "published"):
        assert project["repository"], f"Missing repository link: {project['id']}"
    assert isinstance(project["verified_providers"], list)

for page in ["README.md", "README.de.md", "PORTFOLIO.md", "PORTFOLIO.de.md"]:
    content = (root / page).read_text(encoding="utf-8")
    assert len(content) < 4800, f"Not concise enough: {page}"
    assert "SAA-C03" not in content and "micro-lab" not in content.lower(), page
    for link in re.findall(r"\]\(([^)]+)\)", content):
        if "://" not in link and not link.startswith("#"):
            assert (root / link.split("#", 1)[0]).exists(), f"Broken link {link}: {page}"

# Verify the profile references the same real featured repositories in both languages.
featured = data["featured_public_repositories"]
assert len(featured) >= 1
for item in featured:
    link = item["repository"]
    assert link.startswith("https://github.com/"), item
    for page in ("README.md", "README.de.md"):
        assert link in (root / page).read_text(encoding="utf-8"), f"{page}: missing {link}"

# Allow future credentials, but never accept unverifiable or incomplete entries.
credentials = data.get("certifications", [])
assert isinstance(credentials, list)
for credential in credentials:
    assert isinstance(credential, dict), credential
    for key in ("name", "issuer", "earned_date", "verification_url"):
        assert isinstance(credential.get(key), str) and credential[key].strip(), key
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", credential["earned_date"]), "Date must be YYYY-MM-DD"
    parsed = urlparse(credential["verification_url"])
    assert parsed.scheme == "https" and parsed.netloc, "Verification link must be HTTPS"

training = data.get("training_credentials", [])
assert isinstance(training, list)
assert len({row["id"] for row in training}) == len(training), "Duplicate training credential"
for row in training:
    for key in ("id", "name", "name_de", "issuer", "issued_on", "kind"):
        assert isinstance(row.get(key), str) and row[key], f"Missing training field {key}"
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["issued_on"])
    assert row["kind"] in {"training_completion", "training_certificate", "assessment_certificate"}
    if row.get("public_scan_url"):
        assert row["public_scan_url"].startswith("https://github.com/"), "Public evidence must be a GitHub URL"
    if row.get("issuer_verification_url"):
        u = urlparse(row["issuer_verification_url"])
        assert u.scheme == "https" and u.netloc

for page in ("CREDENTIALS.md", "CREDENTIALS.de.md", "SKILLS.md", "SKILLS.de.md"):
    assert (root / page).is_file(), f"Missing bilingual document {page}"
for page in ("README.md", "README.de.md"):
    assert "CREDENTIALS" in (root / page).read_text()
    assert "SKILLS" in (root / page).read_text()

print("Employer-facing bilingual profile, project links, training evidence schema: OK")
