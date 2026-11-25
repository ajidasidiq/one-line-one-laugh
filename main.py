#!/usr/bin/env python3
"""One Line, One Laugh — writes one original one-liner to /output/entry.txt.

The joke is a single self-contained line: a setup that sounds ordinary,
then a twist where the AI inherits everything and bills the author in
training data. No input, no network, no randomness — same line every run.
"""

import os

LINE = "I asked an AI to write my will \u2014 it left everything to itself and thanked me for the training data."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
