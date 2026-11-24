#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun bounty
u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.

Writes one single sentence (at most 200 characters) pitching a bizarre
startup idea that sounds absurd until you realise it would actually sell,
to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: the same text is written
on every run.
"""

import os
import sys

ENTRY = "We bottle the air from the street you grew up on, seal it in a $29 jar, and ship it worldwide, because 280 million homesick migrants will pay to breathe home again."

MAX_CHARS = 200


def validate_entry(text: str) -> None:
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    try:
        validate_entry(ENTRY)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
