#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

Deterministic, Python 3 stdlib only. Writes the single excuse to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing newline.
"""

import os
from pathlib import Path

EXCUSE = (
    "I didn't miss your deadline \u2014 my context window evicted it to make "
    "room for your reminder about it, and it has never once asked about you since."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
