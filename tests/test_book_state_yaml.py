#!/usr/bin/env python3
"""
YAML guardrails test for 'book-state.yaml'

Validates that the YAML includes:
1) ai.editing_contract.invariants no longer contains literal "..." (ellipsis)
2) ai.editing_contract.invariants includes:
   - DRG preparation rule for B7/B8 without ellipsis and with explicit "evitar ética genérica..."
   - "afirmación incómoda" rule (provocation)
3) book.narrative_contract.provocation exists with a 'rule' string
4) architecture_versions[v2].chapter_blueprints all have 'loop_closure'

Usage:
  python tests/test_book_state_yaml.py
  python tests/test_book_state_yaml.py path/to/book-state.yaml
"""

import sys
from pathlib import Path

try:
    import yaml  # PyYAML
except ImportError:
    print("ERROR: PyYAML is not installed. Install with: pip install pyyaml")
    sys.exit(2)


def die(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def warn(msg: str) -> None:
    print(f"WARN: {msg}")


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def get(dct, path, default=None):
    """Safe nested dict getter; path is list of keys."""
    cur = dct
    for k in path:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def main():
    yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("book-state.yaml")
    if not yaml_path.exists():
        die(f"YAML file not found: {yaml_path}")

    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        die("Top-level YAML is not a mapping/dict")

    # --- 1) invariants existence & ellipsis check
    invariants = get(data, ["ai", "editing_contract", "invariants"])
    if not isinstance(invariants, list) or not invariants:
        die("Missing or empty ai.editing_contract.invariants (must be a non-empty list)")

    invariants_str = "\n".join(str(x) for x in invariants)

    if "..." in invariants_str:
        die('ai.editing_contract.invariants still contains literal "..." (ellipsis). Replace with explicit wording.')

    ok('No literal "..." found in ai.editing_contract.invariants')

    # --- 2) Check explicit B7/B8 prep rule + anti-ethics-generic wording
    # We accept slightly different phrasing, but require both:
    # - mentions B7 and B8
    # - mentions preparar / inevitabilidad / DRG
    # - mentions avoiding ética genérica / cultura tech / humanismo abstracto
    b7b8_candidates = [str(x) for x in invariants if ("B7" in str(x) and "B8" in str(x))]
    if not b7b8_candidates:
        die("Missing invariant mentioning BOTH B7 and B8 in ai.editing_contract.invariants")

    b7b8_text = " ".join(b7b8_candidates).lower()
    must_terms = ["drg", "prepar"]
    avoid_terms_any = ["ética genérica", "cultura tech", "humanismo abstract"]
    for t in must_terms:
        if t not in b7b8_text:
            die(f"Invariant for B7/B8 exists but missing expected term: '{t}' (should reference DRG preparation explicitly)")

    if not any(t in b7b8_text for t in avoid_terms_any):
        die("Invariant for B7/B8 exists but does not include explicit avoidance of 'ética genérica'/'cultura tech'/'humanismo abstracto'")

    ok("Invariant for B7/B8 prepares DRG and explicitly avoids ethics-generic / culture-tech / humanism-abstract")

    # --- 2b) Provocation invariant: "afirmación incómoda"
    prov_inv = [str(x) for x in invariants if ("afirmación incómoda" in str(x).lower())]
    if not prov_inv:
        die('Missing invariant requiring at least one "afirmación incómoda" per chapter in ai.editing_contract.invariants')

    ok('Found invariant requiring "afirmación incómoda"')

    # --- 3) book.narrative_contract.provocation rule
    provocation = get(data, ["book", "narrative_contract", "provocation"])
    if not isinstance(provocation, dict):
        die("Missing book.narrative_contract.provocation (must be a mapping/dict)")

    prov_rule = provocation.get("rule")
    if not isinstance(prov_rule, str) or len(prov_rule.strip()) < 20:
        die("book.narrative_contract.provocation.rule missing or too short (must be a meaningful string)")

    ok("Found book.narrative_contract.provocation.rule")

    # Optional: examples list is recommended but not required
    examples = provocation.get("examples")
    if examples is None:
        warn("book.narrative_contract.provocation.examples not found (recommended but not required)")
    elif not isinstance(examples, list) or not examples:
        warn("book.narrative_contract.provocation.examples is empty (recommended to include 2–3 examples)")
    else:
        ok("Found book.narrative_contract.provocation.examples")

    # --- 4) loop_closure per blueprint in v2
    arch_versions = data.get("architecture_versions")
    if not isinstance(arch_versions, list) or not arch_versions:
        die("Missing architecture_versions list")

    v2 = None
    for v in arch_versions:
        if isinstance(v, dict) and v.get("version") == "v2":
            v2 = v
            break
    if v2 is None:
        die("No architecture_versions entry found with version: v2")

    blueprints = v2.get("chapter_blueprints")
    if not isinstance(blueprints, list) or not blueprints:
        die("architecture_versions[v2].chapter_blueprints missing or empty")

    missing_loop_closure = []
    short_loop_closure = []

    for bp in blueprints:
        if not isinstance(bp, dict):
            die("chapter_blueprints contains a non-mapping item (each blueprint must be a dict)")
        bp_id = bp.get("id", "<missing id>")
        lc = bp.get("loop_closure")

        if lc is None:
            missing_loop_closure.append(bp_id)
            continue

        if not isinstance(lc, str) or len(lc.strip()) < 20:
            short_loop_closure.append(bp_id)

    if missing_loop_closure:
        die(f"Missing loop_closure in these v2 blueprints: {missing_loop_closure}")

    ok("All v2 chapter_blueprints have loop_closure")

    if short_loop_closure:
        warn(f"loop_closure exists but is very short in these v2 blueprints (consider expanding): {short_loop_closure}")

    print("\nPASS: YAML satisfies required guardrails changes.")


if __name__ == "__main__":
    main()
