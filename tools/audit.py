"""Fail loudly if the 21 November page breaks a rule we cannot see.

Three checks, in the order they can bite:
  1. any two painted strings whose boxes intersect (the layout is dense)
  2. any string outside the trim margin
  3. the file and pixel constraints the competition imposes
Plus a recount of the region arithmetic, because the strip and the list are
generated from different code paths and could drift apart.
"""

import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import stories  # noqa: E402

BYTE_CAP = 1048576


def audit(png_path, sheet=None):
    if sheet is None:
        import compose
        compose.compose(png_path)
        sheet = compose.LAST_SHEET

    notes = []
    rows = sheet.log.rows

    clashes = sheet.log.hits(slack=2.0)
    if clashes:
        notes.append(f"{len(clashes)} collision(s)")
        for a, b, ba, bb in clashes[:10]:
            notes.append(f"    {a[:38]!r} x {b[:38]!r}")

    outside = sheet.log.outside()
    if outside:
        notes.append(f"{len(outside)} string(s) beyond the trim")
        for text, box in outside[:10]:
            notes.append(f"    {text[:44]!r} at {box}")

    if not os.path.exists(png_path):
        notes.append("no image at " + png_path)
        return notes, 0
    im = Image.open(png_path)
    if im.size != (1024, 1024):
        notes.append(f"wrong pixel size {im.size}")
    size = os.path.getsize(png_path)
    if size > BYTE_CAP:
        notes.append(f"{size} bytes exceeds the {BYTE_CAP} cap")

    counted = stories.counts()
    total = sum(counted.values())
    if total != len(stories.stories()):
        notes.append(f"region tally {total} != {len(stories.stories())} stories")
    if len(stories.MAP) != len(stories.stories()):
        notes.append(f"{len(stories.MAP)} map pins for {len(stories.stories())} stories")

    return notes, len(rows)


def main():
    png = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "out", "entry.png")
    notes, n = audit(png)
    print(f"file       {png}")
    print(f"bytes      {os.path.getsize(png) if os.path.exists(png) else 0} / {BYTE_CAP}")
    print(f"pixels     {Image.open(png).size if os.path.exists(png) else '-'}")
    print(f"strings    {n} painted")
    print(f"stories    {len(stories.stories())} = {stories.counts()}")
    print()
    if notes:
        print("PROBLEMS")
        for x in notes:
            print("  - " + x)
        sys.exit(1)
    print("clean: no collisions, nothing past the trim, arithmetic agrees")


if __name__ == "__main__":
    main()
