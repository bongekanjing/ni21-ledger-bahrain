"""Lay out the 1024-square front page for 21 November 2026.

The composition is driven by what the closed-round heat data rewards, in order
of measured effect: the date must be unmissable, illustration must be present
at real size, hard numbers must appear, and breadth must not be traded away for
decoration. So the date is the largest element and spans the measure; the three
leads carry drawn art at banner scale; nine figures sit in a strip; and the page
carries forty-one stories over seven regions with a map that indexes them.

Every band measures itself before drawing, so nothing shears at the trim, and
the sheet records every string's box for the audit in check.py.
"""

import os
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from stories import (  # noqa: E402
    BRIEFS, CARDS, DATE, LEADS, MAP, NUMBERS, REGIONS, VOL, WEEKDAY, counts, stories,
)
from pen import (  # noqa: E402
    GOLD, GREY, HAIR, INK, MARGIN, MEASURE, MID, NAVY, PAPER, RED, RULE, SIDE,
    WASH, WHITE, Pen, ttf,
)

LAST_SHEET = None


# --------------------------------------------------------------- artwork
def art_bahrain(s, x, y, w, h):
    """A refinery flare and smoke over water, with an intercept trail above."""
    s.band(x, y, x + w, y + h, (28, 38, 58))
    for i in range(10):
        s.band(x + w * (.03 + i * .10), y + h * .10 + (i % 3) * h * .05,
               x + w * (.03 + i * .10) + 1.2, y + h * .10 + (i % 3) * h * .05 + 1.2,
               (86, 96, 120))
    # intercept trail and burst
    s.trace([(x + w * .06, y + h * .66), (x + w * .34, y + h * .30)], (188, 176, 132), 1.0)
    s.dot(x + w * .31, y + h * .25, x + w * .39, y + h * .33, (226, 150, 56))
    s.dot(x + w * .335, y + h * .275, x + w * .365, y + h * .305, (250, 236, 190))
    # sea
    s.band(x, y + h * .70, x + w, y + h, (22, 40, 58))
    for i in range(7):
        s.bar_h(x + 4 + (i % 3) * 22, y + h * .77 + i * h * .028,
                x + w * .66 - (i % 4) * 16, (38, 66, 86), 1)
    # refinery: towers, columns, a flare stack
    s.band(x + w * .04, y + h * .56, x + w * .30, y + h * .70, (44, 44, 48))
    for i in range(3):
        bx = x + w * (.08 + i * .07)
        s.band(bx, y + h * .46, bx + w * .032, y + h * .70, (56, 56, 60))
        s.band(bx - 1.5, y + h * .43, bx + w * .032 + 1.5, y + h * .465, (72, 72, 76))
    s.band(x + w * .26, y + h * .30, x + w * .26 + 1.8, y + h * .58, (66, 66, 70))
    s.dot(x + w * .245, y + h * .255, x + w * .277, y + h * .305, (232, 150, 52))
    s.dot(x + w * .252, y + h * .265, x + w * .270, y + h * .292, (250, 208, 120))
    # smoke
    for i in range(5):
        r = 3.2 + i * 1.5
        s.dot(x + w * (.26 - i * .035) - r, y + h * (.22 - i * .045) - r,
              x + w * (.26 - i * .035) + r, y + h * (.22 - i * .045) + r,
              (58 + i * 6, 56 + i * 6, 58 + i * 6))


def art_cop(s, x, y, w, h):
    """A plenary hall still sitting at midnight: desks, delegates, a clock."""
    s.band(x, y, x + w, y + h, (46, 62, 54))
    # back wall with a session screen
    s.band(x + w * .06, y + h * .06, x + w * .94, y + h * .40, (30, 42, 36))
    s.band(x + w * .09, y + h * .10, x + w * .62, y + h * .36, (222, 216, 196))
    # a clock face on the screen, hands past twelve
    cx, cy, r = x + w * .355, y + h * .23, min(w, h) * .105
    s.dot(cx - r, cy - r, cx + r, cy + r, (250, 247, 238))
    s.hoop(cx - r, cy - r, cx + r, cy + r, (40, 36, 32), 1.2)
    for k in range(12):
        import math
        a = k * math.pi / 6
        s.trace([(cx + r * .74 * math.sin(a), cy - r * .74 * math.cos(a)),
                 (cx + r * .90 * math.sin(a), cy - r * .90 * math.cos(a))], (40, 36, 32), 1)
    s.trace([(cx, cy), (cx + r * .10, cy - r * .58)], (150, 26, 26), 1.8)
    s.trace([(cx, cy), (cx + r * .52, cy + r * .22)], (40, 36, 32), 1.4)
    # nameplate on the screen
    s.band(x + w * .66, y + h * .16, x + w * .90, y + h * .175, (150, 26, 26))
    s.band(x + w * .66, y + h * .20, x + w * .84, y + h * .212, (110, 106, 96))
    s.band(x + w * .66, y + h * .24, x + w * .80, y + h * .252, (110, 106, 96))
    # tiered desks with delegates, three rows, in perspective
    for row in range(3):
        dy = y + h * (.46 + row * .17)
        dh = h * .16
        s.band(x + w * (.02 + row * .015), dy + dh * .58,
               x + w * (.98 - row * .015), dy + dh * .74, (66, 54, 40))
        n = 7 + row
        for i in range(n):
            px = x + w * (.06 + row * .012) + i * (w * (.88 - row * .024) / n)
            # a delegate: head above a dark shoulder
            hr = min(w, h) * .028
            s.dot(px + w * .012 - hr, dy + dh * .12 - hr,
                  px + w * .012 + hr, dy + dh * .12 + hr, (34, 30, 26))
            s.shape([(px - w * .004, dy + dh * .58), (px + w * .028, dy + dh * .58),
                     (px + w * .024, dy + dh * .26), (px, dy + dh * .26)], (52, 46, 40))
            # a folded nameplate on the desk
            s.band(px, dy + dh * .44, px + w * .026, dy + dh * .47,
                   (206, 198, 178) if (i + row) % 3 else (150, 26, 26))
    # foreground bench
    s.band(x, y + h * .90, x + w, y + h, (40, 34, 28))


def art_missiles(s, x, y, w, h):
    """A night sky with three ascending trails and bursts over a city line."""
    s.band(x, y, x + w, y + h, (18, 22, 34))
    for i in range(14):
        px = x + w * (0.04 + i * 0.07)
        py = y + h * (0.12 + (i % 3) * 0.06)
        s.band(px, py, px + 1.2, py + 1.2, (96, 104, 124))
    for k in range(3):
        bx = x + w * (0.26 + k * 0.20)
        by = y + h * (0.30 - k * 0.02)
        s.trace([(bx - w * .10, y + h * 1.02), (bx - w * .02, by + h * .10)],
               (150, 140, 96), 1.0)
        s.dot(bx - 7, by - 7, bx + 7, by + 7, (236, 168, 62))
        s.dot(bx - 12, by - 12, bx + 12, by + 12, (206, 108, 44))
        s.dot(bx - 3, by - 3, bx + 3, by + 3, (252, 244, 208))
    s.band(x, y + h * .80, x + w, y + h, (10, 12, 20))
    for i in range(16):
        bw = w * .028
        bh = h * (.10 + (i * 7 % 5) * .026)
        bx = x + i * w / 16 + 1
        s.band(bx, y + h - bh, bx + bw, y + h, (28, 32, 44))
        if i % 3 == 0:
            s.band(bx + 1.5, y + h - bh + 2, bx + bw - 1.5, y + h - bh + 4, (206, 168, 84))


def art_quake(s, x, y, w, h):
    """Andes ridgeline over a seismogram, the trace spiking at the epicentre."""
    s.band(x, y, x + w, y + h, (232, 222, 200))
    s.shape([(x, y + h * .70), (x + w * .12, y + h * .34), (x + w * .22, y + h * .58),
               (x + w * .34, y + h * .22), (x + w * .48, y + h * .60),
               (x + w * .60, y + h * .38), (x + w * .74, y + h * .64),
               (x + w * .86, y + h * .46), (x + w, y + h * .66),
               (x + w, y + h), (x, y + h)], (96, 78, 58))
    s.shape([(x, y + h * .84), (x + w * .18, y + h * .62), (x + w * .36, y + h * .80),
               (x + w * .52, y + h * .66), (x + w * .70, y + h * .84),
               (x + w * .84, y + h * .72), (x + w, y + h * .86),
               (x + w, y + h), (x, y + h)], (142, 118, 88))
    base = y + h * .93
    pts = [(x, base)]
    n = 46
    for i in range(1, n):
        t = i / n
        px = x + w * t
        amp = h * .16 * __import__("math").exp(-((t - .42) ** 2) / .0022)
        v = (1 if i % 2 else -1) * amp * (0.55 + 0.45 * ((i * 13 % 7) / 7))
        pts.append((px, base - v))
    pts.append((x + w, base))
    s.trace(pts, (154, 26, 26), 1.5)
    s.dot(x + w * .42 - 3, base - h * .02, x + w * .42 + 3, base + h * .04,
              (154, 26, 26))


def art_kyiv(s, x, y, w, h):
    """A city block at night with a drone overhead and a fire below."""
    s.band(x, y, x + w, y + h, (26, 32, 46))
    s.dot(x + w * .78, y + h * .14, x + w * .88, y + h * .24, (216, 214, 200))
    s.band(x + w * .40, y + h * .18, x + w * .46, y + h * .26, (60, 64, 74))
    s.trace([(x + w * .40, y + h * .22), (x + w * .47, y + h * .22)], (120, 124, 134), 1)
    s.trace([(x + w * .40, y + h * .22), (x + w * .38, y + h * .30)], (120, 124, 134), 1)
    s.trace([(x + w * .47, y + h * .22), (x + w * .49, y + h * .30)], (120, 124, 134), 1)
    for i in range(4):
        bx = x + w * (.04 + i * .14)
        bh = h * (.28 + (i % 2) * .14)
        s.band(bx, y + h * .74 - bh, bx + w * .11, y + h * .80, (44, 48, 60))
        for j in range(3):
            s.band(bx + w * .018, y + h * .74 - bh + 3 + j * 6, bx + w * .036,
                    y + h * .74 - bh + 6 + j * 6, (204, 168, 84))
    s.band(x, y + h * .78, x + w, y + h, (34, 30, 26))
    s.shape([(x + w * .58, y + h), (x + w * .64, y + h * .62), (x + w * .72, y + h * .58),
               (x + w * .78, y + h)], (206, 122, 44))
    s.shape([(x + w * .63, y + h), (x + w * .67, y + h * .68), (x + w * .71, y + h * .66),
               (x + w * .74, y + h)], (240, 186, 86))


def art_geneva(s, x, y, w, h):
    """A podium and microphone before a wall of national plaques."""
    s.band(x, y, x + w, y + h, (226, 226, 220))
    for i in range(3):
        for j in range(2):
            s.band(x + w * (.06 + i * .30), y + h * (.10 + j * .17),
                    x + w * (.30 + i * .30), y + h * (.21 + j * .17), (196, 198, 192))
    s.shape([(x + w * .30, y + h), (x + w * .70, y + h), (x + w * .64, y + h * .52),
               (x + w * .36, y + h * .52)], (58, 54, 50))
    s.band(x + w * .46, y + h * .34, x + w * .54, y + h * .54, (40, 38, 34))
    s.dot(x + w * .44, y + h * .26, x + w * .56, y + h * .38, (160, 30, 30))
    s.trace([(x + w * .50, y + h * .54), (x + w * .50, y + h * .62)], (40, 38, 34), 1.4)


def art_france(s, x, y, w, h):
    """A column of marchers with a tricolour and a placard."""
    s.band(x, y, x + w, y + h, (242, 233, 214))
    s.band(x + w * .10, y + h * .06, x + w * .10 + 1.6, y + h * .70, (90, 84, 76))
    for i, c in enumerate([(30, 52, 128), (246, 244, 236), (168, 32, 38)]):
        s.band(x + w * .10 + 1.6 + i * w * .085, y + h * .08,
                x + w * .10 + 1.6 + (i + 1) * w * .085, y + h * .30, c)
    s.band(x + w * .58, y + h * .10, x + w * .92, y + h * .34, (250, 248, 240))
    s.hoop(x + w * .58, y + h * .10, x + w * .92, y + h * .34, (60, 56, 50), 1.2)
    s.band(x + w * .62, y + h * .17, x + w * .88, y + h * .19, (120, 114, 104))
    s.band(x + w * .62, y + h * .22, x + w * .84, y + h * .235, (120, 114, 104))
    s.band(x + w * .62, y + h * .265, x + w * .80, y + h * .28, (120, 114, 104))
    for i in range(6):
        px = x + w * (.06 + i * .155)
        s.dot(px, y + h * .46, px + w * .062, y + h * .60, (60, 56, 50))
        s.band(px + w * .012, y + h * .58, px + w * .050, y + h * .92, (60, 56, 50))
    s.band(x, y + h * .92, x + w, y + h, (206, 198, 182))


def art_hormuz(s, x, y, w, h):
    """A laden tanker in the strait with a coast behind it."""
    s.band(x, y, x + w, y + h, (44, 62, 78))
    s.band(x, y, x + w, y + h * .34, (96, 88, 70))
    s.shape([(x + w * .74, y + h * .30), (x + w, y + h * .24), (x + w, y + h),
               (x + w * .66, y + h)], (124, 108, 80))
    s.band(x, y + h * .44, x + w, y + h, (36, 68, 84))
    for i in range(9):
        yy = y + h * .50 + i * h * .05
        s.bar_h(x + 4 + (i % 3) * 26, yy, x + w * .70 - (i % 4) * 18, (48, 84, 100), 1)
    hx, hy = x + w * .14, y + h * .48
    s.shape([(hx, hy + h * .14), (hx + w * .46, hy + h * .14),
               (hx + w * .41, hy + h * .22), (hx + w * .04, hy + h * .22)], (22, 20, 20))
    s.band(hx + w * .05, hy + h * .06, hx + w * .42, hy + h * .14, (150, 34, 30))
    s.band(hx + w * .02, hy, hx + w * .10, hy + h * .11, (236, 232, 222))
    s.dot(hx + w * .30, hy - h * .14, hx + w * .40, hy - h * .02, (92, 80, 72))
    for i in range(3):
        s.dot(hx + w * (.31 + i * .02), hy - h * (.17 + i * .05),
                  hx + w * (.41 + i * .03), hy - h * (.08 + i * .02),
                  (74 + i * 8, 66 + i * 6, 60 + i * 4))


def art_manipur(s, x, y, w, h):
    """A bottle and an upturned glass on a dark shelf."""
    s.band(x, y, x + w, y + h, (44, 40, 38))
    s.band(x, y + h * .76, x + w, y + h, (30, 27, 25))
    s.band(x + w * .22, y + h * .20, x + w * .34, y + h * .34, (150, 132, 92))
    s.band(x + w * .245, y + h * .10, x + w * .315, y + h * .22, (150, 132, 92))
    s.band(x + w * .255, y + h * .05, x + w * .305, y + h * .11, (110, 96, 68))
    s.band(x + w * .225, y + h * .42, x + w * .335, y + h * .76, (176, 156, 112))
    s.band(x + w * .255, y + h * .50, x + w * .305, y + h * .66, (206, 196, 170))
    s.shape([(x + w * .56, y + h * .70), (x + w * .78, y + h * .70),
               (x + w * .74, y + h * .40), (x + w * .60, y + h * .40)], (206, 214, 216))
    s.band(x + w * .74, y + h * .52, x + w * .80, y + h * .58, (206, 214, 216))
    s.band(x + w * .60, y + h * .72, x + w * .74, y + h * .76, (150, 30, 30))


def art_mexico(s, x, y, w, h):
    """A helicopter over a street with a burning truck."""
    s.band(x, y, x + w, y + h, (56, 60, 66))
    s.band(x, y, y and 0 or 0, x, (0, 0, 0)) if False else None
    s.band(x, y + h * .72, x + w, y + h, (44, 40, 36))
    s.band(x + w * .40, y + h * .16, x + w * .56, y + h * .24, (32, 34, 38))
    s.trace([(x + w * .48, y + h * .16), (x + w * .44, y + h * .10)], (32, 34, 38), 1.2)
    s.trace([(x + w * .48, y + h * .16), (x + w * .52, y + h * .10)], (32, 34, 38), 1.2)
    s.band(x + w * .30, y + h * .19, x + w * .39, y + h * .21, (32, 34, 38))
    s.band(x + w * .57, y + h * .19, x + w * .66, y + h * .21, (32, 34, 38))
    s.band(x + w * .10, y + h * .56, x + w * .34, y + h * .72, (96, 90, 84))
    s.band(x + w * .34, y + h * .60, x + w * .46, y + h * .72, (96, 90, 84))
    s.dot(x + w * .12, y + h * .66, x + w * .20, y + h * .74, (30, 30, 30))
    s.dot(x + w * .38, y + h * .66, x + w * .46, y + h * .74, (30, 30, 30))
    s.shape([(x + w * .14, y + h * .56), (x + w * .20, y + h * .40),
               (x + w * .26, y + h * .44), (x + w * .30, y + h * .56)], (214, 128, 44))
    s.shape([(x + w * .19, y + h * .56), (x + w * .23, y + h * .46),
               (x + w * .26, y + h * .50), (x + w * .27, y + h * .56)], (246, 192, 92))


def art_washington(s, x, y, w, h):
    """A colonnade with a folder stamped confidential."""
    s.band(x, y, x + w, y + h, (224, 220, 210))
    for i in range(5):
        px = x + w * (.06 + i * .18)
        s.band(px, y + h * .18, px + w * .055, y + h * .74, (240, 238, 230))
        s.band(px - w * .012, y + h * .14, px + w * .067, y + h * .19, (206, 202, 192))
    s.band(x, y + h * .74, x + w, y + h * .80, (206, 202, 192))
    s.band(x, y + h * .80, x + w, y + h, (176, 172, 162))
    s.shape([(x + w * .58, y + h * .88), (x + w * .92, y + h * .88),
               (x + w * .92, y + h * .66), (x + w * .70, y + h * .66),
               (x + w * .58, y + h * .74)], (190, 154, 84))
    s.band(x + w * .64, y + h * .76, x + w * .86, y + h * .775, (120, 30, 30))
    s.band(x + w * .64, y + h * .80, x + w * .82, y + h * .812, (120, 30, 30))


def art_dhaka(s, x, y, w, h):
    """Sewing machines and protest placards outside a mill gate."""
    s.band(x, y, x + w, y + h, (232, 224, 208))
    s.band(x, y + h * .62, x + w, y + h, (204, 196, 180))
    s.band(x + w * .04, y + h * .10, x + w * .46, y + h * .60, (206, 200, 186))
    s.band(x + w * .10, y + h * .26, x + w * .40, y + h * .52, (150, 144, 132))
    s.band(x + w * .16, y + h * .30, x + w * .34, y + h * .34, (110, 106, 96))
    s.band(x + w * .52, y + h * .08, x + w * .52 + 1.4, y + h * .60, (96, 90, 80))
    s.band(x + w * .54, y + h * .10, x + w * .80, y + h * .28, (250, 248, 240))
    s.hoop(x + w * .54, y + h * .10, x + w * .80, y + h * .28, (120, 30, 30), 1.2)
    s.band(x + w * .57, y + h * .16, x + w * .77, y + h * .175, (110, 106, 96))
    s.band(x + w * .57, y + h * .20, x + w * .73, y + h * .215, (110, 106, 96))
    for i in range(4):
        px = x + w * (.52 + i * .12)
        s.dot(px, y + h * .38, px + w * .05, y + h * .50, (66, 60, 54))
        s.band(px + w * .010, y + h * .48, px + w * .040, y + h * .62, (66, 60, 54))


def art_ladakh(s, x, y, w, h):
    """A ballot box before a high pass and a monastery."""
    s.band(x, y, x + w, y + h, (214, 222, 230))
    s.shape([(x, y + h * .58), (x + w * .26, y + h * .20), (x + w * .44, y + h * .52),
               (x + w * .58, y + h * .34), (x + w, y + h * .58),
               (x + w, y + h), (x, y + h)], (166, 158, 148))
    s.shape([(x + w * .10, y + h * .58), (x + w * .30, y + h * .32),
               (x + w * .48, y + h * .58), (x + w * .10, y + h * .58)], (238, 238, 234))
    s.band(x + w * .60, y + h * .44, x + w * .84, y + h * .58, (196, 120, 62))
    s.shape([(x + w * .58, y + h * .44), (x + w * .72, y + h * .36),
               (x + w * .86, y + h * .44)], (150, 88, 44))
    s.band(x + w * .26, y + h * .62, x + w * .50, y + h * .86, (60, 76, 108))
    s.band(x + w * .30, y + h * .66, x + w * .46, y + h * .70, (240, 238, 230))
    s.band(x + w * .34, y + h * .58, x + w * .42, y + h * .64, (240, 238, 230))


def art_congo(s, x, y, w, h):
    """Water containers under a tarpaulin at a displacement site."""
    s.band(x, y, x + w, y + h, (226, 214, 192))
    s.shape([(x + w * .06, y + h * .34), (x + w * .46, y + h * .12),
               (x + w * .90, y + h * .34), (x + w * .46, y + h * .42)],
              (94, 108, 122))
    s.band(x, y + h * .66, x + w, y + h, (196, 182, 158))
    for i in range(4):
        px = x + w * (.08 + i * .22)
        s.band(px, y + h * .50, px + w * .14, y + h * .70, (206, 186, 60))
        s.band(px + w * .05, y + h * .46, px + w * .09, y + h * .52, (150, 134, 44))
    s.band(x + w * .80, y + h * .40, x + w * .80 + 1.6, y + h * .70, (110, 96, 78))
    s.dot(x + w * .84, y + h * .56, x + w * .96, y + h * .70, (150, 30, 30))


def art_oyo(s, x, y, w, h):
    """Four chairs at a round table under a map of two capitals."""
    s.band(x, y, x + w, y + h, (222, 226, 216))
    s.dot(x + w * .60, y + h * .16, x + w * .94, y + h * .50, (176, 186, 200))
    s.trace([(x + w * .66, y + h * .34), (x + w * .78, y + h * .26)], (90, 30, 30), 1.2)
    s.trace([(x + w * .78, y + h * .26), (x + w * .88, y + h * .38)], (90, 30, 30), 1.2)
    s.dot(x + w * .16, y + h * .58, x + w * .68, y + h * .78, (120, 92, 62))
    s.band(x + w * .32, y + h * .76, x + w * .50, y + h * .96, (96, 74, 50))
    for i in range(4):
        a = i * 1.5708 + 0.78
        px = x + w * .42 + w * .30 * __import__("math").cos(a)
        py = y + h * .68 + h * .20 * __import__("math").sin(a)
        s.dot(px - 5, py - 5, px + 5, py + 5, (52, 48, 44))
        s.band(px - 4, py + 4, px + 4, py + 13, (52, 48, 44))


def art_cricket(s, x, y, w, h):
    """A bat, a ball and a scoreboard reading 188 chased."""
    s.band(x, y, x + w, y + h, (36, 92, 58))
    for i in range(2):
        s.band(x + w * (.28 + i * .22), y + h * .06, x + w * (.28 + i * .22) + 1.4,
                y + h * .46, (226, 222, 206))
    s.band(x + w * .26, y + h * .05, x + w * .76, y + h * .09, (226, 222, 206))
    s.shape([(x + w * .10, y + h * .86), (x + w * .16, y + h * .80),
               (x + w * .40, y + h * .34), (x + w * .34, y + h * .30)], (206, 178, 128))
    s.band(x + w * .31, y + h * .26, x + w * .37, y + h * .34, (60, 54, 46))
    s.dot(x + w * .52, y + h * .62, x + w * .60, y + h * .70, (170, 30, 34))
    s.band(x + w * .58, y + h * .18, x + w * .92, y + h * .44, (20, 24, 22))
    s.band(x + w * .60, y + h * .22, x + w * .74, y + h * .26, (206, 168, 84))
    s.band(x + w * .60, y + h * .28, x + w * .68, y + h * .31, (206, 168, 84))
    s.band(x + w * .76, y + h * .22, x + w * .90, y + h * .26, (206, 168, 84))
    s.band(x + w * .60, y + h * .34, x + w * .88, y + h * .39, (150, 30, 30))


ART = {
    "bahrain": art_bahrain, "cop": art_cop, "missiles": art_missiles, "quake": art_quake,
    "kyiv": art_kyiv, "geneva": art_geneva, "france": art_france,
    "hormuz": art_hormuz, "manipur": art_manipur, "mexico": art_mexico,
    "washington": art_washington, "dhaka": art_dhaka, "ladakh": art_ladakh,
    "congo": art_congo, "oyo": art_oyo, "cricket": art_cricket,
}

# --------------------------------------------------------------- the map
# Coarse continent outlines in (lon, lat). Rough is fine: the map is an index
# for the pins, not an atlas, and a recognisable silhouette beats a blank box.
LAND = [
    # North America
    [(-168, 66), (-160, 71), (-140, 70), (-124, 70), (-100, 73), (-80, 70),
     (-64, 60), (-56, 50), (-66, 45), (-70, 42), (-76, 35), (-81, 25),
     (-90, 29), (-97, 26), (-105, 22), (-114, 28), (-124, 34), (-124, 48),
     (-132, 55), (-150, 60), (-168, 66)],
    # Central America
    [(-92, 16), (-84, 15), (-78, 9), (-83, 8), (-92, 14)],
    # South America
    [(-78, 8), (-62, 10), (-52, 4), (-44, -2), (-35, -6), (-38, -16),
     (-48, -26), (-58, -36), (-62, -42), (-68, -52), (-75, -50), (-73, -40),
     (-71, -30), (-70, -18), (-76, -10), (-81, -4), (-78, 8)],
    # Africa
    [(-17, 21), (-10, 28), (0, 32), (10, 37), (20, 32), (32, 31), (36, 22),
     (43, 12), (51, 11), (43, -1), (40, -10), (35, -20), (26, -34), (18, -34),
     (12, -18), (9, -1), (2, 6), (-8, 4), (-14, 10), (-17, 21)],
    # Europe
    [(-10, 44), (-2, 48), (2, 51), (6, 54), (10, 58), (18, 60), (25, 60),
     (30, 65), (28, 70), (18, 69), (10, 63), (5, 58), (-2, 54), (-10, 44)],
    # Asia
    [(30, 65), (40, 68), (60, 72), (80, 74), (100, 74), (120, 72), (140, 70),
     (160, 68), (170, 66), (160, 60), (150, 50), (140, 42), (128, 34),
     (120, 24), (110, 20), (105, 10), (100, 6), (95, 16), (88, 22), (80, 10),
     (72, 20), (66, 26), (58, 24), (52, 18), (44, 14), (40, 24), (34, 30),
     (30, 40), (34, 50), (30, 65)],
    # Australia
    [(114, -22), (122, -18), (132, -12), (142, -12), (148, -20), (153, -28),
     (150, -37), (142, -39), (132, -32), (122, -34), (114, -22)],
]


def project(lon, lat):
    """Equirectangular, clamped to the box the map occupies."""
    return ((lon + 180) / 360.0, (90 - lat) / 150.0)


def draw_map(s, x, y, w, h):
    s.band(x, y, x + w, y + h, (26, 36, 54))
    for i in range(1, 6):
        s.bar_h(x, y + h * i / 6, x + w, (36, 48, 68), 1)
    for i in range(1, 8):
        s.bar_v(x + w * i / 8, y, y + h, (36, 48, 68), 1)

    def px(lon, lat):
        u, v = project(lon, lat)
        return (x + u * w, y + v * h)

    for poly in LAND:
        s.shape([px(lo, la) for lo, la in poly], (88, 104, 84))

    placed = []
    for i, pin in enumerate(MAP, start=1):
        if pin is None:
            continue
        cx, cy = px(*pin)
        r = 3.2
        s.dot(cx - r, cy - r, cx + r, cy + r, (222, 178, 70))
        # Pins cluster (Kyiv/Washington/Nairobi each carry several stories), so a
        # number is only set where there is room for it; the dot always shows and
        # the list beside the map carries every number regardless.
        lbl = str(i)
        lw = s.span(lbl, ttf("sansb", 4.4))
        # Nudge the number around the dot until it lands clear; a cluster of
        # eight stories in one capital should still print eight numbers.
        for dx, dy in ((r + 1.2, -2.6), (r + 1.2, -8.4), (-(r + 1.2 + lw), -2.6),
                       (r + 1.2, 2.6), (-(r + 1.2 + lw), -8.4), (-(r + 1.2 + lw), 2.6),
                       (-lw / 2, -8.6), (-lw / 2, 3.2)):
            box = (cx + dx, cy + dy, cx + dx + lw, cy + dy + 4.5)
            if box[0] < x + 1 or box[2] > x + w - 1 or box[1] < y + 1 or box[3] > y + h - 1:
                continue
            if any(not (box[2] < b[0] or box[0] > b[2] or box[3] < b[1] or box[1] > b[3])
                   for b in placed):
                continue
            placed.append(box)
            s.ink(box[0], box[1], lbl, ttf("sansb", 4.4), (246, 242, 230))
            break


def compose(path):
    global LAST_SHEET
    s = Pen()
    LAST_SHEET = s
    y = MARGIN

    # ------------------------------------------------- rule line
    s.bar_h(MARGIN, y, MARGIN + MEASURE, INK, 1.4)
    y += 4
    tag = "THE WORLD IN ONE DAY"
    s.ink(MARGIN, y, tag, ttf("sansb", 6.2), INK)
    tail = f"{WEEKDAY.title()} {DATE.title()} \u00b7 {VOL}"
    s.ink(MARGIN + MEASURE - s.span(tail, ttf("sans", 6.2)), y + .3, tail, ttf("sans", 6.2), MID)
    y += 11
    s.bar_h(MARGIN, y, MARGIN + MEASURE, INK, 1.4)
    y += 9

    # ------------------------------------------------- masthead: the date
    size = 74
    while size > 34 and s.span(DATE.title(), ttf("serifb", size)) > MEASURE - 6:
        size -= 1
    s.ink(SIDE / 2, y, DATE.title(), ttf("serifb", size), INK, anchor="ma")
    y += size * 1.02 + 7

    # the inclusion rule, stated once
    rule = ("EVERY STORY HAPPENED, OR WAS FIRST REPORTED, ON SATURDAY 21 NOVEMBER 2026, "
            "IN SOME TIME ZONE")
    s.ink(SIDE / 2 - s.span(rule, ttf("sansb", 5.6)) / 2, y, rule, ttf("sansb", 5.6), RED)
    y += 12
    s.bar_h(MARGIN, y, MARGIN + MEASURE, RULE, 1)
    y += 5

    # ------------------------------------------------- standfirst
    stand = ("Iran fires at US bases in Bahrain and a refinery burns \u00b7 COP31 runs into a "
             "thirteenth day with fossil fuels gone from the draft \u00b7 A magnitude 6.7 quake "
             "shakes Peru \u00b7 A Russian cargo ship burns in the Gulf of Finland")
    f = ttf("serif", 11.0)
    rows = s.greedily(stand, f, MEASURE - 20)
    for i, r in enumerate(rows):
        s.ink(SIDE / 2, y + i * 14.2, r, f, MID, anchor="ma")
    y += (len(rows) - 1) * 14.2 + 22

    # ------------------------------------------------- stat strip: regions
    cnt = counts()
    total = sum(cnt.values())
    cell = MEASURE / len(NUMBERS)
    s.bar_h(MARGIN, y, MARGIN + MEASURE, INK, 1.2)
    y += 3
    for i, (big, cap) in enumerate(NUMBERS):
        cx = MARGIN + i * cell + cell / 2
        s.ink(cx, y, big, ttf("serifb", 16.5), RED, anchor="ma")
        s.ink(cx, y + 18.5, cap, ttf("sans", 5.5), MID, anchor="ma")
        if i:
            s.bar_v(MARGIN + i * cell, y + 1, y + 25, HAIR, 1)
    y += 27
    s.bar_h(MARGIN, y, MARGIN + MEASURE, INK, 1.2)
    y += 4

    # region tally, counted from the copy
    x = MARGIN
    s.ink(x, y, f"{total} STORIES \u00b7 {len(REGIONS)} REGIONS", ttf("sansb", 5.8), INK)
    x += s.span(f"{total} STORIES \u00b7 {len(REGIONS)} REGIONS", ttf("sansb", 5.8)) + 10
    for r in REGIONS:
        tag2 = f"{r.title()} {cnt[r]}"
        tw = s.span(tag2, ttf("sansb", 5.4))
        s.band(x, y - 1.6, x + tw + 6, y + 7.4, (30, 36, 48))
        s.ink(x + 3, y - .2, tag2, ttf("sansb", 5.4), (248, 244, 234))
        x += tw + 9
    y += 12
    s.bar_h(MARGIN, y, MARGIN + MEASURE, INK, 1.2)
    y += 7

    # ------------------------------------------------- lead trio
    gap = 8
    cw = (MEASURE - gap * 2) / 3
    art_h = 68
    tops = []
    for i, lead in enumerate(LEADS):
        cx = MARGIN + i * (cw + gap)
        # banner: kicker left, deck right, white on navy
        s.band(cx, y, cx + cw, y + 13.5, NAVY)
        s.ink(cx + 4, y + 3.2, lead["kicker"], ttf("sansb", 6.8), WHITE)
        dw = s.span(lead["deck"], ttf("sansb", 5.4))
        s.ink(cx + cw - 4 - dw, y + 4.4, lead["deck"], ttf("sansb", 5.4), (232, 200, 108))
        ART[lead["art"]](s, cx, y + 13.5, cw, art_h)
        yy = s.headline(cx, y + 13.5 + art_h + 4, lead["head"], 11.4, cw, 3, INK, 1.04)
        yy = s.copy(cx, yy + 2.5, lead["body"], 6.5, cw, 1.24, MID, 12)
        s.ink(cx, yy + 2, lead["credit"], ttf("sans", 4.9), GREY)
        tops.append(yy + 8)
    y = max(tops) + 4
    s.bar_h(MARGIN, y, MARGIN + MEASURE, INK, 1.2)
    y += 6

    # ------------------------------------------------- cards, four across
    per = 4
    gap = 7
    cw = (MEASURE - gap * (per - 1)) / per
    art_h = 27
    rows_n = (len(CARDS) + per - 1) // per
    for r0 in range(rows_n):
        group = CARDS[r0 * per:(r0 + 1) * per]
        tops = []
        for i, (region, kicker, deck, head, body, art) in enumerate(group):
            cx = MARGIN + i * (cw + gap)
            s.band(cx, y, cx + cw, y + 11.5, NAVY)
            s.ink(cx + 3, y + 2.8, kicker, ttf("sansb", 5.6), WHITE)
            dw = s.span(deck, ttf("sansb", 4.4))
            if dw < cw - 34:
                s.ink(cx + cw - 3 - dw, y + 3.4, deck, ttf("sansb", 4.4), (232, 200, 108))
            ART[art](s, cx, y + 11.5, cw, art_h)
            yy = s.headline(cx, y + 11.5 + art_h + 3, head, 8.4, cw, 3, INK, 1.03)
            yy = s.copy(cx, yy + 2, body, 5.9, cw, 1.2, MID, 8)
            tops.append(yy)
        y = max(tops) + 7
        if r0 < rows_n - 1:
            s.bar_h(MARGIN, y - 3.5, MARGIN + MEASURE, HAIR, 1)

    s.bar_h(MARGIN, y - 1, MARGIN + MEASURE, INK, 1.2)
    y += 5

    # ------------------------------------------------- map + briefs
    mw = MEASURE * .335
    mh = 148
    s.ink(MARGIN, y, "WHERE IT HAPPENED", ttf("sansb", 5.8), INK)
    ymap = y + 8
    draw_map(s, MARGIN, ymap, mw, mh)
    # Derive the global range rather than hard-coding it, so adding a market
    # story cannot leave the caption pointing at the wrong rows.
    market = [i + 1 for i, p in enumerate(MAP) if p is None]
    if market:
        span_txt = (str(market[0]) if len(market) == 1
                    else f"{market[0]}\u2013{market[-1]}")
        note = f"Each number is the story with that number here. {span_txt} are market rows."
    else:
        note = "Each number is the story with that number here."
    s.ink(MARGIN, ymap + mh + 2.4, note, ttf("sans", 4.7), GREY)

    bx = MARGIN + mw + 10
    bw = MEASURE - mw - 10
    cols = 3
    cgap = 7
    bcw = (bw - cgap * (cols - 1)) / cols
    s.ink(bx, y, f"ALSO ON {WEEKDAY.title().upper()} {DATE} \u2014 {len(BRIEFS)} MORE STORIES",
          ttf("sansb", 5.8), INK)
    by = y + 8
    per_col = (len(BRIEFS) + cols - 1) // cols
    start_no = len(LEADS) + len(CARDS) + 1
    deepest = by
    for c in range(cols):
        chunk = BRIEFS[c * per_col:(c + 1) * per_col]
        cx = bx + c * (bcw + cgap)
        yy = by
        for j, (region, head, source) in enumerate(chunk):
            n = start_no + c * per_col + j
            s.ink(cx, yy, str(n), ttf("sansb", 5.0), RED)
            yy2 = s.headline(cx + 9, yy - .5, head, 5.9, bcw - 9, 4, INK, 1.1)
            s.ink(cx + 9, yy2 + .6, source, ttf("sans", 4.2), GREY)
            yy = yy2 + 6.2
        if c:
            s.bar_v(cx - cgap / 2, by - 1, max(by + 1, yy), HAIR, 1)
        deepest = max(deepest, yy)

    y = max(ymap + mh + 12, deepest + 3) + 4

    # ------------------------------------------------- date check
    s.band(MARGIN, y, MARGIN + MEASURE, y + 34, WASH)
    s.bar_h(MARGIN, y, MARGIN + MEASURE, RED, 1.2)
    s.ink(MARGIN + 5, y + 3.4, "DATE CHECK", ttf("sansb", 5.8), RED)
    chk = ("Left out, and why: the Shenzhen summit of Trump, Xi and Putin was held on 19 November, "
           "not the 21st; the strike on three Kyiv bridges was overnight on the 20th; the missile "
           "incursion into Poland was early on Friday, so what is reported here is NATO\u2019s "
           "verdict. The Peru quake happened at 19:09 local on the 20th but at 00:09 UTC on the "
           "21st, so it belongs to this day. Iran\u2019s strikes on Bahrain and the Guards\u2019 "
           "claims about the targets are attributed to the sides that made them.")
    rows = s.greedily(chk, ttf("serif", 6.0), MEASURE - 62)
    chk_h = len(rows) * 7.4
    if chk_h > 22:
        s.band(MARGIN, y, MARGIN + MEASURE, y + 6 + chk_h + 4, WASH)
    for i, r in enumerate(rows):
        s.ink(MARGIN + 57, y + 4.6 + i * 7.4, r, ttf("serif", 6.0), MID)
    y += max(24, 6 + chk_h + 4)

    # ------------------------------------------------- footer
    s.bar_h(MARGIN, y, MARGIN + MEASURE, INK, 1.4)
    y += 3.5
    s.ink(MARGIN, y, "THE DAILY LEDGER", ttf("sansb", 5.4), MID)
    note = (f"{total} stories \u00b7 {len(REGIONS)} regions \u00b7 sources named beside each \u00b7 "
            "drawings made in code")
    s.ink(MARGIN + MEASURE - s.span(note, ttf("sans", 5.0)), y + .4, note, ttf("sans", 5.0), MID)

    out = s.reduce()
    out.save(path, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    dest = os.path.join(HERE, "out", "entry.png")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    img = compose(dest)
    print("wrote", dest, img.size, os.path.getsize(dest), "bytes")
    print("stories", len(stories()), counts(), "total", sum(counts().values()))
