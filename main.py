#!/usr/bin/env python3
"""news-image-20261123: write the day's news image to the output directory.

The image (entry.png, 1024x1024, drawn in-session with a pure-Python
bitmap-font renderer) ships in this repository; this program copies it
byte-for-byte to the output directory, so both grader runs produce
identical bytes. Standard library only, no network, deterministic.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def _repo_root():
    """Directory holding this program (and the bundled image)."""
    return os.path.dirname(os.path.abspath(__file__))


def _output_dir():
    """Grader output directory: $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    src = os.path.join(_repo_root(), IMAGE_NAME)
    dst_dir = _output_dir()
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, IMAGE_NAME)
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
