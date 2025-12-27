#!/usr/bin/env python3
"""
Test: Loop Graph Integrity for chapter_blueprints in v2 architecture.

Validates:
- Each blueprint has a 'feeds_into' field (list of IDs)
- All referenced IDs exist as valid blueprint IDs
- The graph forms a complete cycle: sequence 1 → 2 → ... → N → 1
- No orphan nodes (every blueprint is reachable)

Usage:
  python tests/test_loop_graph_integrity.py
  python tests/test_loop_graph_integrity.py path/to/book-state.yaml
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is not installed. Install with: pip install pyyaml")
    sys.exit(2)


def die(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


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


def main():
    yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("book-state.yaml")
    if not yaml_path.exists():
        die(f"YAML file not found: {yaml_path}")

    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        die("Top-level YAML is not a mapping/dict")

    blueprints = get_v2_blueprints(data)
    n = len(blueprints)

    # Build lookup structures
    id_to_bp = {}
    seq_to_id = {}

    for bp in blueprints:
        if not isinstance(bp, dict):
            die("chapter_blueprints contains a non-mapping item")
        bp_id = bp.get("id")
        seq = bp.get("sequence")
        if bp_id:
            id_to_bp[bp_id] = bp
        if seq is not None:
            seq_to_id[seq] = bp_id

    all_ids = set(id_to_bp.keys())

    # Check: all blueprints have feeds_into
    missing_feeds_into = []
    empty_feeds_into = []
    invalid_refs = []

    for bp in blueprints:
        bp_id = bp.get("id", "<missing id>")
        feeds_into = bp.get("feeds_into")

        if feeds_into is None:
            missing_feeds_into.append(bp_id)
            continue

        if not isinstance(feeds_into, list) or len(feeds_into) == 0:
            empty_feeds_into.append(bp_id)
            continue

        # Check all referenced IDs exist
        for ref_id in feeds_into:
            if ref_id not in all_ids:
                invalid_refs.append({
                    "from": bp_id,
                    "invalid_ref": ref_id,
                })

    if missing_feeds_into:
        die(f"Missing 'feeds_into' field in blueprints: {missing_feeds_into}")
    ok("All blueprints have 'feeds_into' field")

    if empty_feeds_into:
        die(f"Empty 'feeds_into' in blueprints: {empty_feeds_into}")
    ok("All 'feeds_into' are non-empty lists")

    if invalid_refs:
        details = [f"{r['from']} → {r['invalid_ref']}" for r in invalid_refs]
        die(f"Invalid blueprint references in feeds_into: {details}")
    ok("All 'feeds_into' references point to valid blueprint IDs")

    # Build directed graph: id -> list of target ids
    graph = {}
    for bp in blueprints:
        bp_id = bp.get("id")
        feeds_into = bp.get("feeds_into", [])
        graph[bp_id] = feeds_into

    # Check: graph forms a complete cycle following sequence order
    # Expected: seq 1 → seq 2 → ... → seq N → seq 1
    cycle_errors = []

    for seq in range(1, n + 1):
        current_id = seq_to_id.get(seq)
        if not current_id:
            continue

        # Expected next: seq + 1 (or 1 if seq == n)
        expected_next_seq = (seq % n) + 1
        expected_next_id = seq_to_id.get(expected_next_seq)

        actual_feeds_into = graph.get(current_id, [])

        if expected_next_id not in actual_feeds_into:
            cycle_errors.append({
                "sequence": seq,
                "id": current_id,
                "expected_feeds_into": expected_next_id,
                "actual_feeds_into": actual_feeds_into,
            })

    if cycle_errors:
        print("\nFAIL: Loop graph does not form complete cycle (seq 1 → 2 → ... → N → 1):")
        for err in cycle_errors:
            print(f"  - Sequence {err['sequence']} ({err['id']})")
            print(f"    Expected feeds_into: {err['expected_feeds_into']}")
            print(f"    Actual feeds_into: {err['actual_feeds_into']}")
            print()
        sys.exit(1)
    ok(f"Loop graph forms complete cycle: 1 → 2 → ... → {n} → 1")

    # Check: all nodes reachable (no orphans)
    # Start from sequence 1 and traverse
    start_id = seq_to_id.get(1)
    visited = set()
    current = start_id

    for _ in range(n):
        if current in visited:
            break
        visited.add(current)
        feeds_into = graph.get(current, [])
        if feeds_into:
            current = feeds_into[0]  # Follow first edge

    orphans = all_ids - visited
    if orphans:
        die(f"Orphan blueprints not reachable from sequence 1: {orphans}")
    ok("All blueprints are reachable in the loop (no orphans)")

    print(f"\nPASS: Loop graph integrity validated for {n} blueprints.")


if __name__ == "__main__":
    main()
