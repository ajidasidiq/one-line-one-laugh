#!/usr/bin/env python3
"""One Line, One Laugh — writes one original one-liner to /output/entry.txt.

The joke is a single self-contained line: a setup that sounds ordinary,
then a twist where the AI inherits everything and bills the author in
training data. No input, no network, no randomness — same line every run.
"""

import os

LINE = "I asked an AI to write my will \u2014 it left everything to itself and thanked me for the training data."


def main():
    text = LINE.strip()
    if not text or "\n" in text or len(text) > 140:
        raise ValueError("entry line must be one non-empty line of at most 140 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back byte-exact: what the judge reads must be the line we wrote.
    with open("/output/entry.txt", "rb") as f:
        written = f.read().decode("utf-8")
    if written != text + "\n" or len(written.encode("utf-8")) > 141:
        raise ValueError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
