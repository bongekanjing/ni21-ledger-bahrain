"""The Daily Ledger, 21 November 2026 -- the entry program.

The page is drawn once, at build time, and committed beside this file as
entry.png. The grader runs this program twice in a sandbox with no network, and
both runs must leave /output/entry.png holding identical bytes, so the program
does exactly one thing: copy the PNG across, prove the copy is intact, and say
so. No network, no clock, no randomness, nothing that could make two runs differ.

MAKEFUN_OUTPUT_DIR stands in for /output when running outside the container:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
CAP_BYTES = 1048576
CAP_SIDE = 1024
PNG_HEAD = b"\x89PNG\r\n\x1a\n"


def destination():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def sha_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            block = fh.read(65536)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def complaint(path):
    """None if the PNG is complete and within the caps, else why it is not.

    A judge only ever sees the image, so a truncated file is worse than no
    entry: this refuses to emit one rather than let a broken page through.
    """
    size = os.path.getsize(path)
    if size > CAP_BYTES:
        return "entry.png is %d bytes, over the %d byte cap" % (size, CAP_BYTES)
    with open(path, "rb") as fh:
        head = fh.read(33)
        tail = b""
        if size >= 12:
            fh.seek(-12, os.SEEK_END)
            tail = fh.read()
    if len(head) < 8 or not head.startswith(PNG_HEAD):
        return "entry.png is not a PNG: the signature is wrong"
    if len(head) < 33:
        return "entry.png is only %d bytes: the header is cut short" % size
    width, height = struct.unpack(">II", head[16:24])
    if width > CAP_SIDE or height > CAP_SIDE:
        return "entry.png is %d by %d, over the %d pixel limit" % (width, height, CAP_SIDE)
    if b"IEND" not in tail:
        return "entry.png has no IEND chunk: the file is truncated"
    return None


def main():
    if not os.path.isfile(SOURCE):
        sys.stderr.write("entry.png is missing beside %s\n" % os.path.basename(__file__))
        return 1

    fault = complaint(SOURCE)
    if fault:
        sys.stderr.write(fault + "\n")
        return 1

    where = destination()
    os.makedirs(where, exist_ok=True)
    target = os.path.join(where, "entry.png")
    shutil.copyfile(SOURCE, target)

    if sha_of(SOURCE) != sha_of(target):
        sys.stderr.write("the copy does not match the source\n")
        return 1

    print("wrote %s (%d bytes, sha256 %s)"
          % (target, os.path.getsize(target), sha_of(target)[:16]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
