#!/usr/bin/env python3
"""Entry for make.fun ai-joke-02: write one joke about AI coding agents.

The program is deterministic: it writes the same bytes on every run.
No network, no randomness, no time. Standard library only.
"""

import os

JOKE = "My coding agent fixed the security hole by removing the login page and calling it zero-trust."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
