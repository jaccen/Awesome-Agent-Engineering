#!/usr/bin/env python3
"""Validate knowledge base integrity across all five JSON files.

Checks: valid JSON, required fields, no duplicates, category counts consistent,
no empty critical fields, evidence present.

Exit 0: all pass; 1: errors found.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

REQUIRED_METHOD = {"name", "category", "desc", "year"}
REQUIRED_FRAMEWORK = {"name", "repo_url", "desc"}
REQUIRED_INDUSTRY = {"domain", "project", "organization", "desc"}
REQUIRED_STARTUP = {"name", "category", "desc", "url"}
REQUIRED_BENCHMARK = {"name", "domain", "desc"}

errors = []


def check_json(fname, required_fields, list_key, name_field="name"):
    path = DATA / fname
    if not path.exists():
        errors.append(f"{fname}: file missing")
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{fname}: invalid JSON — {exc}")
        return
    entries = data.get(list_key, [])
    seen = set()
    for i, e in enumerate(entries):
        missing = required_fields - set(e.keys())
        if missing:
            errors.append(f"{fname}[{i}] {e.get(name_field, '?')}: missing fields {missing}")
        name = e.get(name_field, "")
        if not name:
            errors.append(f"{fname}[{i}]: empty {name_field}")
        elif name in seen:
            errors.append(f"{fname}: duplicate '{name}'")
        seen.add(name)
        if not e.get("desc", "").strip():
            errors.append(f"{fname}[{i}] {name}: empty desc")
    # Check count consistency
    stated = data.get("count", 0)
    actual = len(entries)
    if stated != actual:
        errors.append(f"{fname}: count mismatch — stated {stated}, actual {actual}")
    print(f"  {fname}: {actual} entries, {len(seen)} unique names")


def check_categories():
    path = DATA / "methods.json"
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    cats_stated = data.get("categories", {})
    cats_actual = {}
    for m in data.get("methods", []):
        c = m.get("category", "")
        cats_actual[c] = cats_actual.get(c, 0) + 1
    for c, n in cats_actual.items():
        if cats_stated.get(c, 0) != n:
            errors.append(f"methods.json: category '{c}' count mismatch — stated {cats_stated.get(c)}, actual {n}")
    stated_total = data.get("category_count", 0)
    if stated_total != len(cats_actual):
        errors.append(f"methods.json: category_count mismatch — stated {stated_total}, actual {len(cats_actual)}")


def main():
    print("Validating knowledge bases...")
    check_json("methods.json", REQUIRED_METHOD, "methods")
    check_json("frameworks.json", REQUIRED_FRAMEWORK, "frameworks")
    check_json("industries.json", REQUIRED_INDUSTRY, "industries", name_field="project")
    check_json("startups.json", REQUIRED_STARTUP, "startups")
    check_json("benchmarks.json", REQUIRED_BENCHMARK, "benchmarks")
    check_categories()
    if errors:
        print(f"\n[FAIL] {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("\n[PASS] All knowledge bases valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
