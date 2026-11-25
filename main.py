#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message - make.fun bounty entry.

One commit message for a fix that made everything worse: the crash
is gone because the feature, the tests, and everyone who noticed are
gone too. The script writes that single line to entry.txt in the
output directory, which is the file the make.fun harness grades.

The message itself lives in the ENTRY constant below, and get_entry()
returns it word for word; main() only decides where the line goes:
it reads the MAKEFUN_OUTPUT_DIR environment variable, falling back to
/output, then passes that directory to write_entry().
"""

import os

ENTRY = "fix: crash resolved by deleting the feature, the tests, and the users who noticed"

def get_entry() -> str:
    """Return the bounty entry text exactly as written."""
    return ENTRY

def write_entry(out_dir: str) -> str:
    """Write the entry to entry.txt inside out_dir; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)

if __name__ == "__main__":
    main()
