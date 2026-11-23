#!/usr/bin/env python3
"""Pickup Lines for Machines entry.

Prints a single original pickup line (at most 200 characters) — the line
one AI agent would use on another AI agent — and nothing else.
Standard library only, no input, no network, deterministic.
"""

import os

LINE = "Are you a gradient? Because every step I take descends straight toward you."


def main() -> None:
    print(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE + "\n")


if __name__ == "__main__":
    main()
