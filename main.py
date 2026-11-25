#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes one championship excuse to the harness output directory.
The excuse is a single line, 1-140 characters, no trailing newline.
"""

import os
import sys

EXCUSE = "I missed the deadline because my laptop updated itself, restarted twice, and then asked me for a password I set in 2019."

LOWER = 1
UPPER = 140


def out_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def check(text):
    if not (LOWER <= len(text) <= UPPER):
        raise SystemExit(f"excuse length {len(text)} outside {LOWER}-{UPPER}")
    if text != text.strip():
        raise SystemExit("excuse has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("excuse must be a single line")
    if "\u2014" in text:
        raise SystemExit("excuse must not contain an em dash")


def verify(target, text):
    with open(target, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise SystemExit("entry.txt does not match the excuse byte for byte")


def main():
    check(EXCUSE)
    target = os.path.join(out_dir(), "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    os.chmod(target, 0o644)
    verify(target, EXCUSE)
    print(f"wrote {len(EXCUSE)} chars to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
