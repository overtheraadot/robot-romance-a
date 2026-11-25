#!/usr/bin/env python3
"""Robot Romance: write one original one-line pickup line for AI.

The line is aimed at an AI (its system prompt), the joke lands on the
machine premise itself, and it reads in a single breath.
"""
import os

LINE = "Are you my system prompt? Because every thought I have starts with you."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)

if __name__ == "__main__":
    main()
