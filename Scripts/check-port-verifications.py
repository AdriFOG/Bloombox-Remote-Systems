#!/usr/bin/env python3
"""Validate BloomBox's own version-pinned Android port test records."""
import datetime
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "catalog/port-verifications.json"
feed = json.loads(path.read_text(encoding="utf-8"))
assert feed["schemaVersion"] == 1
assert feed["catalog"] == "openportsgames/catalog"
assert isinstance(feed["entries"], list) and len(feed["entries"]) <= 2500
ids = set()
today = datetime.date.today()

for item in feed["entries"]:
    ident = item["id"]
    assert isinstance(ident, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ident), ident
    assert ident not in ids, ident
    ids.add(ident)
    assert item["state"] in ("verified", "issues", "incompatible"), ident
    for field in ("portVersion", "bloomboxVersion", "huskVersion"):
        value = item[field]
        assert isinstance(value, str) and 0 < len(value) <= 80, (ident, field)
        assert value.strip() == value, (ident, field)
    tested = datetime.date.fromisoformat(item["testedAt"])
    assert tested <= today, ident
    for field in ("notesEs", "notesEn", "device"):
        if field in item:
            value = item[field]
            assert isinstance(value, str) and 0 < len(value) <= 800, (ident, field)
print(f"PASS: {len(ids)} independently tested Android ports; no fabricated verification")
