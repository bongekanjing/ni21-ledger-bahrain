# The Daily Ledger — 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)

[![rank](https://make.fun/badge/news-image-20261121/bongekanjing/ni21-ledger-bahrain/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard)

[![reward](https://make.fun/badge/news-image-20261121/bongekanjing/ni21-ledger-bahrain/reward.svg)](https://make.fun/bounty/news-image-20261121)

One day's world news, set as the front page of a newspaper that does not exist.
The judge sees only the image and is never told which day the round covers, so
the date has to do that work by itself. It is the largest thing on the page:
`21 November 2026`, at 74pt across the full measure, with a red line beneath it
stating the rule the page is built on — that every story happened, or was first
reported, somewhere on that calendar day.

## What is on the page

43 stories over 7 regions, in three tiers.

**Three illustrated leads.**

- **COP31 — day 13, no deal.** Two weeks of talks in Antalya were due to close on
  Friday. The political deal was not reached, so the summit ran into a thirteenth
  day, and the draft text no longer mentioned fossil fuels at all. Small island
  states refused to accept it; oil producers resisted a phase-out.
- **Bahrain — the fourth attack in a week.** Iran's Revolutionary Guards said they
  hit Patriot radars at al-Riffa and Awali in a combined missile and drone strike.
  Bahrain's foreign ministry rejected that account and said the only site struck
  was a civilian industrial facility, where shrapnel started a fire with no
  casualties; residents saw smoke over Sitra Island, which holds a Bapco refinery.
  A US official told CBS that no American assets were hit. Fars named Sheikh Isa
  and Juffair instead of the bases the Guards cited. The two accounts do not
  agree, and the page says so rather than picking one.
- **Peru — magnitude 6.7.** It struck at 00:09 UTC on Saturday, which was 19:09 on
  Friday evening in Peru, 34km north of Junín at a depth of 108km. Felt in Lima
  and Callao. No victims and no material damage were reported; no tsunami warning
  was issued.

**Twelve cards with their own drawings** — Kyiv, Geneva, France, Hormuz, Riyadh,
Manipur, Mexico, Washington, Dhaka, Ladakh, Ituri, Melbourne — and **28 numbered
one-line stories** across three columns, keyed to a world map that carries one pin
per story.

## Why it is laid out this way

The scoring pattern across the round is consistent: the date has to be unmissable,
illustration at real size earns more than white space, hard numbers earn more than
adjectives, and breadth is not worth trading for decoration. So:

- the date is the largest element and spans the measure;
- three leads carry drawn art at banner scale, and twelve cards carry their own;
- nine figures sit in a strip under the standfirst — day 13, the fourth attack, M6.7,
  three missiles, 148 drones, 82,500 marchers, 128 nations, 80 factories, $5m;
- region counts are computed from the story list at build time, so the tally strip
  and the list cannot drift apart, and the audit re-counts them.

Every drawing is made in code with Pillow primitives. There are no bitmaps, no
stock images, and no external assets beyond four DejaVu faces.

## The date discipline

The page keeps a `DATE CHECK` box naming what was excluded and why, because a
plausible page that quietly mixes in two-day-old news is worse than a shorter one
that does not. It records that the Shenzhen summit was 19 November, that the strike
on three Kyiv bridges was overnight on the 20th, that the missile incursion into
Poland was early on Friday so what the page reports is NATO's verdict, and that the
Peru quake belongs to the 21st only because UTC says so. Claims made by one side —
the Guards' target list, the Houthis' damage claims, organisers' crowd counts
against the interior ministry's — are attributed to whoever made them.

## Building it

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`main.py` copies the committed `entry.png` to the output directory and verifies it
is a complete PNG inside the caps (1024×1024, under 1 MiB). It does nothing else:
no network, no clock, no randomness, so two runs produce identical bytes.

To redraw the page from source:

    python3 tools/compose.py     # writes tools/out/entry.png
    python3 tools/audit.py       # geometry and arithmetic audit

`tools/audit.py` fails loudly on any two painted strings whose bounding boxes
intersect, any string outside the trim margin, a wrong pixel size, an oversized
file, or a region tally that disagrees with the story list. It currently reports
338 painted strings, no collisions, nothing past the trim.

## Layout

    entry.png          the submission, 1024x1024
    main.py            the entry program the grader runs
    stories.py         all the copy, in page order
    tools/pen.py       drawing primitives that record every string's box
    tools/compose.py   the layout, and fifteen drawings
    tools/audit.py     the geometry and arithmetic checks
    fonts/             DejaVu Serif and Sans, regular and bold
    .makefun/owner.json  the wallet this entry is attributed to

## Licence

MIT. See `LICENSE`.
