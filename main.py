#!/usr/bin/env python3
"""Copy the entry image to the output directory.

The image itself is the entry; this program only places it where the
grader reads it. Deterministic: the same bytes every run.

The entry image lives next to this file (entry.png, in the repository),
so the program finds it relative to its own location rather than the
working directory -- the grader may run it from anywhere.
"""
import os
import shutil

# The image bundled with this entry, resolved against this file's own
# directory so the copy works from any working directory.
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    """Copy entry.png into the output directory as entry.png."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    # Entry point: the grader runs `python3 main.py` and reads
    # /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png).
    main()
