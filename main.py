#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "A River That Forgot to Flow": Concrete, picturable analogy (a river of cars in little boats) a 10-year-old can see, and the second line honestly names both the mapping (bunching, creeping, spreading) and the limits (honking, anger, wrong exits), instead of praising the analogy.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'A traffic jam is a river of cars that forgot how to flow, so everyone sits in their own little boat going nowhere together.\nThe river fits because cars bunch up, creep and spread out like water, but it leaves out that water never honks, gets angry, or picks the wrong exit.'
TEXT = LINE + "\n"
MAX_CHARS = 400
NLINES = 2


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
