"""Layout primitives for the 21 November front page.

The design of this module is driven by one requirement: every string that gets
painted must be auditable afterwards. So drawing never happens through a bare
ImageDraw handle; it happens through a Pen, and the Pen keeps a ledger. The
geometry audit then reads that ledger rather than trusting the layout code.

Wrapping is the other thing worth care. Greedy wrapping is fine for copy but
wrong for display type, so headlines go through a shrink-and-fit loop that
searches for the largest size at which the line count still matches the slot.
"""

import os

from PIL import Image, ImageDraw, ImageFont

SCALE = 2
SIDE = 1024
MARGIN = 22
MEASURE = SIDE - 2 * MARGIN

PAPER = (250, 247, 238)
INK = (18, 16, 14)
MID = (62, 58, 52)
GREY = (112, 106, 96)
RULE = (96, 90, 80)
HAIR = (196, 189, 175)
RED = (154, 26, 26)
NAVY = (24, 34, 52)
WASH = (238, 231, 216)
WHITE = (253, 251, 244)
GOLD = (232, 200, 108)

_FACES = {
    "serif": "DejaVuSerif.ttf",
    "serifb": "DejaVuSerif-Bold.ttf",
    "sans": "DejaVuSans.ttf",
    "sansb": "DejaVuSans-Bold.ttf",
}
_HOME = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "fonts")
_cache = {}


def ttf(kind, pt):
    """A font at `pt`, cached. Sizes are quantised to 0.1pt to bound the cache."""
    slot = (kind, int(round(pt * 10)))
    got = _cache.get(slot)
    if got is None:
        path = os.path.join(_HOME, _FACES[kind])
        got = ImageFont.truetype(path, max(1, int(round(pt * SCALE))))
        _cache[slot] = got
    return got


class Leadger:
    """Collects (text, box) for every painted string."""

    def __init__(self):
        self.rows = []

    def note(self, text, box):
        if text.strip():
            self.rows.append((text, tuple(round(v, 2) for v in box)))

    def hits(self, slack=2.0):
        """Every pair of strings whose boxes intersect more than `slack`."""
        out = []
        n = len(self.rows)
        for i in range(n):
            ta, ba = self.rows[i]
            for j in range(i + 1, n):
                tb, bb = self.rows[j]
                dx = min(ba[2], bb[2]) - max(ba[0], bb[0])
                dy = min(ba[3], bb[3]) - max(ba[1], bb[1])
                if dx > slack and dy > slack:
                    out.append((ta, tb, ba, bb))
        return out

    def outside(self, lo=18, hi=None):
        hi = SIDE - 18 if hi is None else hi
        bad = []
        for text, b in self.rows:
            if b[0] < MARGIN - 1 or b[2] > SIDE - MARGIN + 1 or b[1] < lo or b[3] > hi:
                bad.append((text, b))
        return bad


class Pen:
    """Draws onto a Scale-times canvas and logs what it drew."""

    def __init__(self):
        self.canvas = Image.new("RGB", (SIDE * SCALE, SIDE * SCALE), PAPER)
        self.draw = ImageDraw.Draw(self.canvas)
        self.log = Leadger()

    def reduce(self):
        return self.canvas.resize((SIDE, SIDE), Image.LANCZOS)

    # -------------------------------------------------------------- measure
    def span(self, text, font):
        return self.draw.textlength(text, font=font) / SCALE

    def extent(self, text, font, anchor="la"):
        return tuple(v / SCALE for v in
                     self.draw.textbbox((0, 0), text, font=font, anchor=anchor))

    # ---------------------------------------------------------------- paint
    def ink(self, x, y, text, font, colour=INK, anchor="la"):
        self.draw.text((x * SCALE, y * SCALE), text, font=font, fill=colour, anchor=anchor)
        if text.strip():
            box = self.draw.textbbox((x * SCALE, y * SCALE), text, font=font, anchor=anchor)
            self.log.note(text, [v / SCALE for v in box])

    def band(self, x1, y1, x2, y2, colour):
        if x2 <= x1 or y2 <= y1:
            return
        self.draw.rectangle([x1 * SCALE, y1 * SCALE, x2 * SCALE, y2 * SCALE], fill=colour)

    def bar_h(self, x1, y, x2, colour=RULE, thick=1):
        if x2 > x1:
            self.band(x1, y, x2, y + thick, colour)

    def bar_v(self, x, y1, y2, colour=HAIR, thick=1):
        if y2 > y1:
            self.band(x, y1, x + thick, y2, colour)

    def dot(self, x1, y1, x2, y2, colour):
        if x2 > x1 and y2 > y1:
            self.draw.ellipse([x1 * SCALE, y1 * SCALE, x2 * SCALE, y2 * SCALE], fill=colour)

    def hoop(self, x1, y1, x2, y2, colour, thick=1):
        if x2 > x1 and y2 > y1:
            self.draw.ellipse([x1 * SCALE, y1 * SCALE, x2 * SCALE, y2 * SCALE],
                              outline=colour, width=max(1, int(thick * SCALE)))

    def shape(self, pts, colour):
        self.draw.polygon([(a * SCALE, b * SCALE) for a, b in pts], fill=colour)

    def trace(self, pts, colour, thick=1):
        self.draw.line([(a * SCALE, b * SCALE) for a, b in pts],
                       fill=colour, width=max(1, int(thick * SCALE)), joint="curve")

    # ------------------------------------------------------------ line breaking
    def greedily(self, text, font, room, most=99):
        """Fill each row as far as it will go."""
        out, cur = [], ""
        for word in text.split():
            if not cur:
                cur = word
                continue
            if self.span(cur + " " + word, font) <= room:
                cur = cur + " " + word
            else:
                out.append(cur)
                cur = word
                if len(out) >= most:
                    return out
        if cur and len(out) < most:
            out.append(cur)
        return out

    def evenly(self, text, font, room, rows_wanted):
        """Break into exactly `rows_wanted` rows, keeping their widths close.

        Binary-searches the narrowest width that still yields the wanted row
        count, then rebuilds at the true measure. This avoids the ragged
        single-word last line that makes set display type look accidental.
        """
        words = text.split()
        if rows_wanted <= 1:
            return [text] if self.span(text, font) <= room else None

        def build(cap):
            rows, cur = [], ""
            for word in words:
                nxt = word if not cur else cur + " " + word
                if not cur or self.span(nxt, font) <= cap:
                    cur = nxt
                else:
                    rows.append(cur)
                    cur = word
            if cur:
                rows.append(cur)
            return rows

        lo, hi, found = 1.0, room, None
        for _ in range(20):
            test = (lo + hi) / 2
            rows = build(test)
            if len(rows) <= rows_wanted and all(self.span(r, font) <= room for r in rows):
                found, hi = rows, test
            else:
                lo = test
        if found is not None and len(found) == rows_wanted:
            return found
        rows = build(room)
        return rows if len(rows) <= rows_wanted else None

    def headline(self, x, y, text, pt, room, rows_wanted, colour=INK, lead=1.03, kind="serifb"):
        """Set a headline to occupy a fixed number of rows; step down until it fits."""
        size = pt
        while size > 6:
            font = ttf(kind, size)
            rows = self.evenly(text, font, room, rows_wanted)
            if rows:
                for k, row in enumerate(rows):
                    self.ink(x, y + k * size * lead, row, font, colour)
                return y + len(rows) * size * lead
            size -= 0.4
        font = ttf(kind, size)
        rows = self.greedily(text, font, room, rows_wanted + 1)
        for k, row in enumerate(rows):
            self.ink(x, y + k * size * lead, row, font, colour)
        return y + len(rows) * size * lead

    def copy(self, x, y, text, pt, room, lead=1.2, colour=MID, most=99, kind="serif"):
        font = ttf(kind, pt)
        rows = self.greedily(text, font, room, most)
        for k, row in enumerate(rows):
            self.ink(x, y + k * lead * pt, row, font, colour)
        return y + len(rows) * lead * pt
