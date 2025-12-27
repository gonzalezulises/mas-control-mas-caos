#!/usr/bin/env python3
"""
Test: Protection Closure for chapter_blueprints in v2 architecture.

Validates:
- Each blueprint has 'exit_criteria' (non-empty list)
- Each blueprint has 'loop_closure' (non-empty string)
- "Cierre en protección": at least 1 exit_criteria per blueprint contains
  one of the protection-related terms (case-insensitive):
  ["protección", "cobertura", "límite", "gate", "estatus", "no listo", "condicionado", "veredicto", "drg"]

Usage:
  python tests/test_protection_closure.py
  python tests/test_protection_closure.py path/to/book-state.yaml
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is not installed. Install with: pip install pyyaml")
    sys.exit(2)


PROTECTION_TERMS = [
    "protección",
    "cobertura",
    "límite",
    "gate",
    "estatus",
    "no listo",
    "condicionado",
    "veredicto",
    "drg",
]


def die(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def warn(msg: str) -> None:
    print(f"WARN: {msg}")


def get_v2_blueprints(data: dict) -> list:
    """Extract chapter_blueprints from architecture_versions[v2]."""
    arch_versions = data.get("architecture_versions")
    if not isinstance(arch_versions, list):
        die("Missing architecture_versions list")

    for v in arch_versions:
        if isinstance(v, dict) and v.get("version") == "v2":
            blueprints = v.get("chapter_blueprints")
            if not isinstance(blueprints, list) or not blueprints:
                die("architecture_versions[v2].chapter_blueprints missing or empty")
            return blueprints

    die("No architecture_versions entry found with version: v2")


def has_protection_term(text: str) -> bool:
    """Check if text contains any protection-related term (case-insensitive)."""
    text_lower = text.lower()
    return any(term in text_lower for term in PROTECTION_TERMS)


def main():
    yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("book-state.yaml")
    if not yaml_path.exists():
        die(f"YAML file not found: {yaml_path}")

    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        die("Top-level YAML is not a mapping/dict")

    blueprints = get_v2_blueprints(data)

    missing_exit_criteria = []
    empty_exit_criteria = []
    missing_loop_closure = []
    empty_loop_closure = []
    no_protection_closure = []

    for bp in blueprints:
        if not isinstance(bp, dict):
            die("chapter_blueprints contains a non-mapping item")

        bp_id = bp.get("id", "<missing id>")
        bp_title = bp.get("title", "<missing title>")

        # Check exit_criteria
        exit_criteria = bp.get("exit_criteria")
        if exit_criteria is None:
            missing_exit_criteria.append(bp_id)
        elif not isinstance(exit_criteria, list) or len(exit_criteria) == 0:
            empty_exit_criteria.append(bp_id)
        else:
            # Check for protection closure
            criteria_text = " ".join(str(c) for c in exit_criteria)
            if not has_protection_term(criteria_text):
                no_protection_closure.append({
                    "id": bp_id,
                    "title": bp_title,
                    "exit_criteria": exit_criteria,
                })

        # Check loop_closure
        loop_closure = bp.get("loop_closure")
        if loop_closure is None:
            missing_loop_closure.append(bp_id)
        elif not isinstance(loop_closure, str) or len(loop_closure.strip()) == 0:
            empty_loop_closure.append(bp_id)

    # Report exit_criteria issues
    if missing_exit_criteria:
        die(f"Missing 'exit_criteria' in blueprints: {missing_exit_criteria}")
    ok("All blueprints have 'exit_criteria' field")

    if empty_exit_criteria:
        die(f"Empty 'exit_criteria' in blueprints: {empty_exit_criteria}")
    ok("All 'exit_criteria' are non-empty lists")

    # Report loop_closure issues
    if missing_loop_closure:
        die(f"Missing 'loop_closure' in blueprints: {missing_loop_closure}")
    ok("All blueprints have 'loop_closure' field")

    if empty_loop_closure:
        die(f"Empty 'loop_closure' in blueprints: {empty_loop_closure}")
    ok("All 'loop_closure' values are non-empty strings")

    # Report protection closure issues
    if no_protection_closure:
        print("\nFAIL: The following blueprints lack protection-oriented exit_criteria:")
        print(f"      (must contain at least one of: {PROTECTION_TERMS})\n")
        for item in no_protection_closure:
            print(f"  - {item['id']}: {item['title']}")
            print(f"    exit_criteria: {item['exit_criteria']}")
            print()
        sys.exit(1)

    ok("All blueprints have at least one protection-oriented exit_criteria")

    print(f"\nPASS: Protection closure validated for {len(blueprints)} blueprints.")


if __name__ == "__main__":
    main()
