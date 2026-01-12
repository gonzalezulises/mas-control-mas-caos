#!/usr/bin/env python3
"""
Test: Forbidden Language validation for /chapters/*.md files.

Validates:
- No forbidden phrases appear in chapter text (case-insensitive)
- Final block does not end with interrogative (question mark or open question)

Forbidden phrases:
  ["deberíamos", "es importante", "mejores prácticas", "best practices",
   "madurez", "alineación estratégica", "transformación cultural",
   "concientizar", "evangelizar"]

Usage:
  python3 tests/test_forbidden_language.py
  python3 tests/test_forbidden_language.py path/to/chapters/
"""

import sys
import re
from pathlib import Path


FORBIDDEN_PHRASES = [
    "deberíamos",
    "es importante",
    "mejores prácticas",
    "best practices",
    "madurez",
    "alineación estratégica",
    "transformación cultural",
    "concientizar",
    "evangelizar",
]


def die(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def find_forbidden_phrases(content: str) -> list:
    """Find all forbidden phrases in content (case-insensitive). Returns list of matches."""
    content_lower = content.lower()
    found = []
    for phrase in FORBIDDEN_PHRASES:
        if phrase.lower() in content_lower:
            # Find the actual match with context
            pattern = re.compile(re.escape(phrase), re.IGNORECASE)
            for match in pattern.finditer(content):
                # Get surrounding context (up to 40 chars before and after)
                start = max(0, match.start() - 40)
                end = min(len(content), match.end() + 40)
                context = content[start:end].replace("\n", " ").strip()
                found.append({
                    "phrase": phrase,
                    "context": f"...{context}...",
                })
    return found


def ends_with_question(content: str) -> tuple:
    """Check if content ends with a question. Returns (bool, last_line)."""
    # Get last non-empty lines (last meaningful block)
    lines = [line.strip() for line in content.strip().split("\n") if line.strip()]
    if not lines:
        return False, ""

    # Check last 3 non-empty lines for question patterns
    last_lines = lines[-3:] if len(lines) >= 3 else lines
    last_block = " ".join(last_lines)

    # Check for question mark
    if "?" in last_block:
        return True, last_block

    # Check for interrogative patterns (Spanish)
    interrogative_starters = [
        r"\b¿",
        r"\bqué\b",
        r"\bcómo\b",
        r"\bpor qué\b",
        r"\bcuándo\b",
        r"\bdónde\b",
        r"\bquién\b",
        r"\bcuál\b",
    ]

    for pattern in interrogative_starters:
        if re.search(pattern, last_block, re.IGNORECASE):
            return True, last_block

    return False, last_block


def main():
    chapters_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("chapters")

    if not chapters_path.exists():
        die(f"Chapters directory not found: {chapters_path} (no chapters written yet)")

    if not chapters_path.is_dir():
        die(f"Path is not a directory: {chapters_path}")

    md_files = sorted(chapters_path.glob("**/*.md"))

    if not md_files:
        die(f"No .md files found in {chapters_path} (no chapters written yet)")

    forbidden_found = []
    interrogative_endings = []

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        filename = md_file.name

        # Check for forbidden phrases
        found = find_forbidden_phrases(content)
        if found:
            forbidden_found.append({
                "file": filename,
                "matches": found,
            })

        # Check for interrogative ending
        ends_question, last_block = ends_with_question(content)
        if ends_question:
            interrogative_endings.append({
                "file": filename,
                "last_block": last_block[:100] + "..." if len(last_block) > 100 else last_block,
            })

    # Report forbidden phrases
    if forbidden_found:
        print("\nFAIL: Forbidden language detected in chapters:")
        for item in forbidden_found:
            print(f"\n  - {item['file']}")
            for match in item["matches"]:
                print(f"    phrase: \"{match['phrase']}\"")
                print(f"    context: {match['context']}")
        print()
        sys.exit(1)
    ok("No forbidden phrases found in chapters")

    # Report interrogative endings
    if interrogative_endings:
        print("\nFAIL: Chapters ending with questions (forbidden):")
        for item in interrogative_endings:
            print(f"  - {item['file']}")
            print(f"    ends with: \"{item['last_block']}\"")
            print()
        sys.exit(1)
    ok("No chapters end with interrogative/open questions")

    print(f"\nPASS: Language validation passed for {len(md_files)} file(s).")


if __name__ == "__main__":
    main()
