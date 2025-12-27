#!/usr/bin/env python3
"""
Test: Chapter Structure Blocks validation for /chapters/*.md files.

Validates:
- Each chapter contains 5 required HTML comment blocks (audit markers)
- Blocks appear exactly once each
- Blocks appear in the correct order:
  1. <!-- block: reconocimiento -->
  2. <!-- block: alivio -->
  3. <!-- block: causa -->
  4. <!-- block: riesgo -->
  5. <!-- block: proteccion -->

Usage:
  python3 tests/test_chapter_structure_blocks.py
  python3 tests/test_chapter_structure_blocks.py path/to/chapters/
"""

import sys
import re
from pathlib import Path


REQUIRED_BLOCKS = [
    "<!-- block: reconocimiento -->",
    "<!-- block: alivio -->",
    "<!-- block: causa -->",
    "<!-- block: riesgo -->",
    "<!-- block: proteccion -->",
]


def die(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def find_block_positions(content: str) -> dict:
    """Find positions of each block in content. Returns {block: position} or {block: -1} if not found."""
    positions = {}
    for block in REQUIRED_BLOCKS:
        pos = content.find(block)
        positions[block] = pos
    return positions


def main():
    chapters_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("chapters")

    if not chapters_path.exists():
        die(f"Chapters directory not found: {chapters_path} (no chapters written yet)")

    if not chapters_path.is_dir():
        die(f"Path is not a directory: {chapters_path}")

    md_files = sorted(chapters_path.glob("**/*.md"))

    if not md_files:
        die(f"No .md files found in {chapters_path} (no chapters written yet)")

    missing_blocks = []
    wrong_order = []
    duplicate_blocks = []

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        filename = md_file.name

        # Check for missing blocks
        positions = find_block_positions(content)
        missing = [block for block, pos in positions.items() if pos == -1]

        if missing:
            missing_blocks.append({
                "file": filename,
                "missing": [b.replace("<!-- block: ", "").replace(" -->", "") for b in missing],
            })
            continue

        # Check for duplicates
        duplicates = []
        for block in REQUIRED_BLOCKS:
            count = content.count(block)
            if count > 1:
                duplicates.append(block.replace("<!-- block: ", "").replace(" -->", ""))

        if duplicates:
            duplicate_blocks.append({
                "file": filename,
                "duplicates": duplicates,
            })
            continue

        # Check order
        block_positions = [(block, positions[block]) for block in REQUIRED_BLOCKS]
        sorted_by_position = sorted(block_positions, key=lambda x: x[1])
        expected_order = [(block, positions[block]) for block in REQUIRED_BLOCKS]

        if sorted_by_position != expected_order:
            actual_order = [b.replace("<!-- block: ", "").replace(" -->", "") for b, _ in sorted_by_position]
            wrong_order.append({
                "file": filename,
                "found_order": actual_order,
            })

    # Report missing blocks
    if missing_blocks:
        print("\nFAIL: The following chapters are missing required blocks:")
        for item in missing_blocks:
            print(f"  - {item['file']}")
            print(f"    missing: {item['missing']}")
            print()
        sys.exit(1)
    ok("All chapters have required structure blocks")

    # Report duplicates
    if duplicate_blocks:
        print("\nFAIL: The following chapters have duplicate blocks:")
        for item in duplicate_blocks:
            print(f"  - {item['file']}")
            print(f"    duplicates: {item['duplicates']}")
            print()
        sys.exit(1)
    ok("No duplicate blocks found")

    # Report wrong order
    if wrong_order:
        expected = ["reconocimiento", "alivio", "causa", "riesgo", "proteccion"]
        print("\nFAIL: The following chapters have blocks in wrong order:")
        print(f"      Expected: {expected}")
        for item in wrong_order:
            print(f"  - {item['file']}")
            print(f"    found: {item['found_order']}")
            print()
        sys.exit(1)
    ok("All blocks appear in correct order")

    print(f"\nPASS: Chapter structure validated for {len(md_files)} file(s).")


if __name__ == "__main__":
    main()
