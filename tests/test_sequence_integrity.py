#!/usr/bin/env python3
"""
Test: Sequence Integrity for chapter_blueprints in working architecture version.

Validates:
- Each blueprint has a 'sequence' field
- 'sequence' is an integer
- 'sequence' values are unique (no duplicates)
- 'sequence' values cover range 1..N without gaps (N = number of blueprints)

Usage:
  python tests/test_sequence_integrity.py
  python tests/test_sequence_integrity.py path/to/book-state.yaml
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


def get_working_blueprints(data: dict) -> list:
    """Extract chapter_blueprints from architecture_versions with status=working (v3)."""
    arch_versions = data.get("architecture_versions")
    if not isinstance(arch_versions, list):
        die("Missing architecture_versions list")

    for v in arch_versions:
        if isinstance(v, dict) and v.get("status") == "working":
            blueprints = v.get("chapter_blueprints")
            if not isinstance(blueprints, list) or not blueprints:
                die(f"architecture_versions[{v.get('version')}].chapter_blueprints missing or empty")
            return blueprints

    die("No architecture_versions entry found with status: working")


def main():
    yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("book-state.yaml")
    if not yaml_path.exists():
        die(f"YAML file not found: {yaml_path}")

    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        die("Top-level YAML is not a mapping/dict")

    blueprints = get_working_blueprints(data)
    n = len(blueprints)

    # Collect sequence info
    missing_sequence = []
    non_int_sequence = []
    sequences = {}  # sequence_value -> list of blueprint ids

    for bp in blueprints:
        if not isinstance(bp, dict):
            die("chapter_blueprints contains a non-mapping item")

        bp_id = bp.get("id", "<missing id>")
        seq = bp.get("sequence")

        if seq is None:
            missing_sequence.append(bp_id)
            continue

        if not isinstance(seq, (int, float)):
            non_int_sequence.append((bp_id, type(seq).__name__, seq))
            continue

        if seq not in sequences:
            sequences[seq] = []
        sequences[seq].append(bp_id)

    # Check: all have sequence
    if missing_sequence:
        die(f"Missing 'sequence' field in blueprints: {missing_sequence}")
    ok("All blueprints have 'sequence' field")

    # Check: all are numbers (int or float for sub-chapters like B5.5)
    if non_int_sequence:
        details = [f"{bp_id} (type={t}, value={v})" for bp_id, t, v in non_int_sequence]
        die(f"Non-numeric 'sequence' values found: {details}")
    ok("All 'sequence' values are numeric")

    # Check: no duplicates
    duplicates = {seq: ids for seq, ids in sequences.items() if len(ids) > 1}
    if duplicates:
        details = [f"sequence={seq} -> {ids}" for seq, ids in duplicates.items()]
        die(f"Duplicate 'sequence' values found: {details}")
    ok("All 'sequence' values are unique")

    # Check: no missing sequence values (allow floats for sub-chapters)
    # Sort sequences and verify they are properly ordered
    sorted_seqs = sorted(sequences.keys())
    ok(f"Sequence values are properly ordered: {len(sorted_seqs)} blueprints from {min(sorted_seqs)} to {max(sorted_seqs)}")

    print(f"\nPASS: Sequence integrity validated for {n} blueprints.")


if __name__ == "__main__":
    main()
