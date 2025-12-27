#!/usr/bin/env python3
"""
Test: Nonnegotiable Claim validation for chapter_blueprints in working architecture version.

Validates:
- Each blueprint has a 'nonnegotiable_claim' field
- The claim is a string with length >= 25 characters
- The claim does not contain "?" or "¿" (must be affirmative, not interrogative)
- The claim contains at least one action verb (heuristic):
  ["es", "reduce", "aumenta", "invita", "obliga", "expone", "corta", "reinicia", "amplifica", "elimina"]

Usage:
  python tests/test_nonnegotiable_claim.py
  python tests/test_nonnegotiable_claim.py path/to/book-state.yaml
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is not installed. Install with: pip install pyyaml")
    sys.exit(2)


ACTION_VERBS = [
    "es",
    "son",
    "reduce",
    "aumenta",
    "invita",
    "obliga",
    "expone",
    "corta",
    "reinicia",
    "amplifica",
    "elimina",
    "produce",
    "tiene",
    "tienen",
    "requiere",
    "depende",
    "dependen",
    "pueden",
    "puede",
    "será",
    "determina",
    "supera",
    "han",
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


def has_action_verb(text: str) -> bool:
    """Check if text contains at least one action verb (case-insensitive, word boundary)."""
    text_lower = text.lower()
    for verb in ACTION_VERBS:
        # Simple heuristic: check if verb appears as word (surrounded by spaces or punctuation)
        if f" {verb} " in f" {text_lower} ":
            return True
    return False


def main():
    yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("book-state.yaml")
    if not yaml_path.exists():
        die(f"YAML file not found: {yaml_path}")

    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        die("Top-level YAML is not a mapping/dict")

    blueprints = get_working_blueprints(data)

    missing_claim = []
    short_claim = []
    interrogative_claim = []
    no_verb_claim = []

    for bp in blueprints:
        if not isinstance(bp, dict):
            die("chapter_blueprints contains a non-mapping item")

        bp_id = bp.get("id", "<missing id>")
        bp_title = bp.get("title", "<missing title>")
        claim = bp.get("nonnegotiable_claim")

        # Check existence
        if claim is None:
            missing_claim.append(bp_id)
            continue

        # Check type and length
        if not isinstance(claim, str) or len(claim.strip()) < 25:
            short_claim.append({
                "id": bp_id,
                "title": bp_title,
                "claim": claim,
                "length": len(str(claim).strip()) if claim else 0,
            })
            continue

        # Check no interrogative marks
        if "?" in claim or "¿" in claim:
            interrogative_claim.append({
                "id": bp_id,
                "title": bp_title,
                "claim": claim,
            })
            continue

        # Check for action verb
        if not has_action_verb(claim):
            no_verb_claim.append({
                "id": bp_id,
                "title": bp_title,
                "claim": claim,
            })

    # Report issues
    if missing_claim:
        die(f"Missing 'nonnegotiable_claim' in blueprints: {missing_claim}")
    ok("All blueprints have 'nonnegotiable_claim' field")

    if short_claim:
        print("\nFAIL: The following blueprints have nonnegotiable_claim too short (< 25 chars):")
        for item in short_claim:
            print(f"  - {item['id']}: {item['title']}")
            print(f"    claim: \"{item['claim']}\" (length: {item['length']})")
            print()
        sys.exit(1)
    ok("All 'nonnegotiable_claim' values have length >= 25")

    if interrogative_claim:
        print("\nFAIL: The following blueprints have interrogative nonnegotiable_claim (contains '?' or '¿'):")
        for item in interrogative_claim:
            print(f"  - {item['id']}: {item['title']}")
            print(f"    claim: \"{item['claim']}\"")
            print()
        sys.exit(1)
    ok("All 'nonnegotiable_claim' values are affirmative (no question marks)")

    if no_verb_claim:
        print("\nFAIL: The following blueprints have nonnegotiable_claim without action verb:")
        print(f"      (must contain at least one of: {ACTION_VERBS})")
        for item in no_verb_claim:
            print(f"  - {item['id']}: {item['title']}")
            print(f"    claim: \"{item['claim']}\"")
            print()
        sys.exit(1)
    ok("All 'nonnegotiable_claim' values contain at least one action verb")

    print(f"\nPASS: Nonnegotiable claim validated for {len(blueprints)} blueprints.")


if __name__ == "__main__":
    main()
