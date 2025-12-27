#!/usr/bin/env python3
"""
Test: Executive Relief validation for chapter_blueprints in working architecture version.

Validates:
- Each blueprint has an 'executive_relief' field
- The field is a non-empty string (>= 20 characters)
- Contains at least one term from the whitelist (executive language)
- Does NOT contain any term from the blacklist (forbidden consulting-speak)

Whitelist (must contain at least one):
  ["riesgo", "exposición", "cobertura", "junta", "estatus", "no pasa",
   "veredicto", "condicionado", "no listo", "protección", "protege"]

Blacklist (must NOT contain any):
  ["madurez", "framework", "best practices", "mejores prácticas",
   "evangelizar", "concientizar"]

Usage:
  python tests/test_executive_relief.py
  python tests/test_executive_relief.py path/to/book-state.yaml
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is not installed. Install with: pip install pyyaml")
    sys.exit(2)


WHITELIST_TERMS = [
    "riesgo",
    "exposición",
    "cobertura",
    "junta",
    "estatus",
    "no pasa",
    "veredicto",
    "condicionado",
    "no listo",
    "protección",
    "protege",
]

BLACKLIST_TERMS = [
    "madurez",
    "framework",
    "best practices",
    "mejores prácticas",
    "evangelizar",
    "concientizar",
]


def die(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def get_working_blueprints(data: dict) -> list:
    """Extract chapter_blueprints from architecture_versions[working]."""
    arch_versions = data.get("architecture_versions")
    if not isinstance(arch_versions, list):
        die("Missing architecture_versions list")

    for v in arch_versions:
        if isinstance(v, dict) and v.get("status") == "working":
            blueprints = v.get("chapter_blueprints")
            if not isinstance(blueprints, list) or not blueprints:
                die("architecture_versions[working].chapter_blueprints missing or empty")
            return blueprints

    die("No architecture_versions entry found with status: working")


def has_whitelist_term(text: str) -> bool:
    """Check if text contains at least one whitelist term (case-insensitive)."""
    text_lower = text.lower()
    return any(term in text_lower for term in WHITELIST_TERMS)


def find_blacklist_terms(text: str) -> list:
    """Return list of blacklist terms found in text (case-insensitive)."""
    text_lower = text.lower()
    return [term for term in BLACKLIST_TERMS if term in text_lower]


def main():
    yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("book-state.yaml")
    if not yaml_path.exists():
        die(f"YAML file not found: {yaml_path}")

    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        die("Top-level YAML is not a mapping/dict")

    blueprints = get_working_blueprints(data)

    missing_relief = []
    short_relief = []
    no_whitelist = []
    has_blacklist = []

    for bp in blueprints:
        if not isinstance(bp, dict):
            die("chapter_blueprints contains a non-mapping item")

        bp_id = bp.get("id", "<missing id>")
        bp_title = bp.get("title", "<missing title>")
        relief = bp.get("executive_relief")

        # Check existence
        if relief is None:
            missing_relief.append(bp_id)
            continue

        # Check type and length
        if not isinstance(relief, str) or len(relief.strip()) < 20:
            short_relief.append({
                "id": bp_id,
                "title": bp_title,
                "relief": relief,
                "length": len(str(relief).strip()) if relief else 0,
            })
            continue

        # Check whitelist
        if not has_whitelist_term(relief):
            no_whitelist.append({
                "id": bp_id,
                "title": bp_title,
                "relief": relief,
            })

        # Check blacklist
        found_blacklist = find_blacklist_terms(relief)
        if found_blacklist:
            has_blacklist.append({
                "id": bp_id,
                "title": bp_title,
                "relief": relief,
                "forbidden_terms": found_blacklist,
            })

    # Report issues
    if missing_relief:
        die(f"Missing 'executive_relief' in blueprints: {missing_relief}")
    ok("All blueprints have 'executive_relief' field")

    if short_relief:
        print("\nFAIL: The following blueprints have executive_relief too short (< 20 chars):")
        for item in short_relief:
            print(f"  - {item['id']}: {item['title']}")
            print(f"    relief: \"{item['relief']}\" (length: {item['length']})")
            print()
        sys.exit(1)
    ok("All 'executive_relief' values have length >= 20")

    if no_whitelist:
        print("\nFAIL: The following blueprints lack executive language in relief:")
        print(f"      (must contain at least one of: {WHITELIST_TERMS})\n")
        for item in no_whitelist:
            print(f"  - {item['id']}: {item['title']}")
            print(f"    relief: \"{item['relief']}\"")
            print()
        sys.exit(1)
    ok("All 'executive_relief' values contain executive language (whitelist)")

    if has_blacklist:
        print("\nFAIL: The following blueprints contain forbidden consulting-speak:")
        print(f"      (must NOT contain any of: {BLACKLIST_TERMS})\n")
        for item in has_blacklist:
            print(f"  - {item['id']}: {item['title']}")
            print(f"    relief: \"{item['relief']}\"")
            print(f"    forbidden terms found: {item['forbidden_terms']}")
            print()
        sys.exit(1)
    ok("All 'executive_relief' values avoid forbidden consulting-speak (blacklist)")

    print(f"\nPASS: Executive relief validated for {len(blueprints)} blueprints.")


if __name__ == "__main__":
    main()
