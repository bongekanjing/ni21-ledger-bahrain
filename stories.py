"""The copy for the 21 November 2026 edition.

Every story here happened, or was first reported, on Saturday 21 November 2026
in some time zone. Where an event broke on Friday night and was announced on
Saturday, the copy says so; where a single side claims something, the copy
attributes it to that side. Nothing is asserted that a source did not carry on
the day.

Three illustrated leads, then cards with small art, then a numbered list of
one-line stories that the map keys to. Region counts are computed from these
tuples at build time, so the strip and the list cannot disagree, and MAP holds
one pin per story with None for the global market stories.
"""

DATE = "21 NOVEMBER 2026"
WEEKDAY = "SATURDAY"
PAPER = "The Daily Ledger"
VOL = "NO. 3,272"

# ------------------------------------------------------------------ leads
LEADS = [
    {
        "kicker": "COP31",
        "deck": "DAY 13 \u00b7 NO DEAL",
        "region": "EUROPE",
        "head": "Climate talks run past their deadline, with fossil fuels out of the draft",
        "body": (
            "Two weeks of negotiations in Antalya were due to close on Friday. A late "
            "session approved technical matters but not the political deal, so the summit "
            "moved into a thirteenth day. The draft left on the table no longer mentioned "
            "fossil fuels at all, a deletion campaigners called a glaring regression, and a "
            "bloc of small island states refused to accept it. Oil producers resisted a "
            "phase-out. A further text was promised for Saturday, and the presidency said "
            "talks would run until agreement was reached."
        ),
        "art": "cop",
        "credit": "Guardian \u00b7 Al Jazeera \u00b7 DW",
    },
    {
        "kicker": "BAHRAIN",
        "deck": "4TH ATTACK IN A WEEK",
        "region": "MIDDLE EAST",
        "head": "Iran fires missiles and drones at US bases, and a Gulf refinery burns",
        "body": (
            "The Revolutionary Guards said they struck Patriot radars at al-Riffa and Awali in "
            "a combined missile and drone attack, retaliation for two US drones it said "
            "violated Iranian airspace. Bahrain\u2019s foreign ministry rejected the radar claim: "
            "the only site hit was a civilian industrial facility, where shrapnel started a "
            "fire and caused no injuries. Residents saw smoke over Sitra Island, which holds a "
            "Bapco refinery. A US official told CBS no American assets were hit. Fars named "
            "Sheikh Isa and Juffair instead of the bases the Guards cited. It was the fourth "
            "attempted attack in Bahrain in about a week."
        ),
        "art": "bahrain",
        "credit": "AFP \u00b7 Jerusalem Post \u00b7 CBS",
    },
    {
        "kicker": "PERU",
        "deck": "M6.7 \u00b7 108 KM DEEP",
        "region": "AMERICAS",
        "head": "A magnitude 6.7 quake shakes the Andes and is felt in Lima",
        "body": (
            "The earthquake struck at 00:09 UTC on Saturday, which was 19:09 on Friday "
            "evening in Peru, with its epicentre 34km north of Jun\u00edn at a depth of 108km. "
            "Residents of Lima and Callao rushed into the streets as buildings shook, and the "
            "shaking was felt strongly in Chanchamayo and Oxapampa. The USGS issued a green "
            "alert for casualties. Peru\u2019s geophysical institute and the mayor of Carhuamayo, "
            "near the epicentre, reported no victims and no material damage. No tsunami "
            "warning was issued."
        ),
        "art": "quake",
        "credit": "USGS \u00b7 AP \u00b7 Andina",
    },
]

# ---------------------------------------------------------- secondary cards
# region, kicker, deck, headline, body, art
CARDS = [
    ("EUROPE", "KYIV", "148 DRONES",
     "Russia fires three ballistic missiles and 148 drones overnight",
     "Ukraine\u2019s air force said 87 of the drones were jet-powered. Explosions were heard in "
     "Kyiv and a private house burned in the Podilskyi district. Three people had been "
     "killed when missiles hit three Dnipro bridges the night before.", "kyiv"),
    ("EUROPE", "GENEVA", "128 NATIONS",
     "Nations agree to \u201celaborate\u201d rules on killer robots by 2028",
     "The decision at the UN weapons convention came after talks ran into the early hours "
     "of Saturday. About 100 states wanted binding rules; the US, Russia and Israel opposed "
     "them, and consensus gave each of them a veto. Campaigners called the mandate watered "
     "down.", "geneva"),
    ("EUROPE", "FRANCE", "82,500 MARCHED",
     "Cost-of-living protests reach a sixth Saturday, with 144 arrests",
     "The interior ministry counted 82,500 demonstrators nationwide, 21,500 of them in "
     "Paris; organisers claimed 150,000. About 70,000 police and gendarmes were deployed, "
     "and there were clashes in Marseille, Lyon, Lille, Grenoble and Nantes. It was the "
     "eighth anniversary of the Yellow Vest movement.", "france"),
    ("MIDDLE EAST", "HORMUZ", "2 TANKERS",
     "Two tankers are struck by unknown projectiles off Oman",
     "UKMTO said one was hit on the stern about 20km north of Khasab at roughly 05:00 UTC, "
     "and a second in its engine room east of Khasab less than an hour later. No casualties "
     "were reported and the environmental impact was unconfirmed. Iran also said it downed "
     "a US drone over Qeshm Island.", "hormuz"),
    ("ASIA-PACIFIC", "MANIPUR", "11 DEAD",
     "Tainted liquor kills 11 and hospitalises more than 180 in Manipur",
     "The state\u2019s chief minister said the deaths had come within 48 hours, and that 140 "
     "patients were in one hospital and 41 in another, many with symptoms of methanol "
     "poisoning. Police registered 48 cases and seized 2,419 litres of illicit liquor. "
     "Methanol can be fatal in doses as small as 60ml.", "manipur"),
    ("AMERICAS", "MEXICO", "$5M REWARD",
     "Troops capture \u201cEl Chapo Isidro\u201d, an FBI most-wanted fugitive",
     "Fausto Isidro Meza Flores, 44, was seized in Guasave, Sinaloa, with his deputy and his "
     "brother-in-law; the defence ministry announced it on Saturday. Seven gunmen and four "
     "soldiers were killed and eight people were arrested. He was flown to Mexico City. The "
     "US had offered $5m for information leading to his arrest.", "mexico"),
    ("AMERICAS", "WASHINGTON", "CONTRACTORS",
     "Trump orders contractors to clear congressional inquiries with the White House",
     "The executive order, signed late on Friday, requires federal contractors and their "
     "subcontractors to tell the administration before sharing information with Congress, "
     "and to withhold material it deems confidential. Non-compliance could cost a company "
     "its contracts. Democrats take control of both chambers in January.", "washington"),
    ("ASIA-PACIFIC", "DHAKA", "80 FACTORIES",
     "Garment workers clash with police as 80 factories shut over pay",
     "Workers in the Savar-Ashulia belt stopped work demanding a higher minimum wage, and "
     "police fired tear gas and sound grenades in Ashulia. Most plants declared general "
     "holidays. Police have arrested 96 people since unrest began on 4 November, including "
     "five federation leaders.", "dhaka"),
    ("ASIA-PACIFIC", "LADAKH", "70% TURNOUT",
     "Ladakh votes in its first local elections since becoming a territory",
     "Turnout was 70.03% in the panchayat polls and 52.40% in the municipal ones, the "
     "administration said, in the first local-body elections since Ladakh was separated from "
     "Jammu and Kashmir in 2019. Polling covered 137 Sarpanch and 242 Panch seats; 55 "
     "Sarpanches and 1,186 Panches were elected unopposed. Some parties alleged voter-roll "
     "manipulation.", "ladakh"),
    ("AFRICA", "ITURI", "76,000 DISPLACED",
     "The UN warns of killings and a water crisis at a Congo displacement camp",
     "OCHA said families at the Plaine Savo site in Djugu territory face killings, "
     "abductions, sexual violence and child recruitment, and that water has been cut since "
     "6 November after threats at the main collection point. Residents are surviving on about "
     "five litres a person a day, against a minimum of 15.", "congo"),
    ("MIDDLE EAST", "RIYADH", "3 INTERCEPTED",
     "Air defences shoot down three missiles aimed at the Saudi capital",
     "The coalition\u2019s spokesman, Major General Turki al-Maliki, said the missiles were "
     "destroyed before dawn on a third consecutive night of alerts. Two more were "
     "intercepted over Jizan, with debris at al-Shuqaiq, and a drone was brought down. The "
     "Houthis said they hit the al-Shuqaiq power station and Jizan port. It followed a "
     "coalition raid on Hodeidah.", "missiles"),
    ("OCEANIA", "MELBOURNE", "AUS WIN",
     "Australia chase a record 188 to beat England by three wickets",
     "Nikhil Chaudhary made 66 off 38 balls and Jack Edwards finished 25 not out as "
     "Australia chased a record 188 to win the first T20 with a ball to spare at the MCG. "
     "England made 187-9, Harry Brook top-scoring with 65 off 28 after being dropped three "
     "times. Australia lead the five-match series 1-0.", "cricket"),
]

# ------------------------------------------------------- one-line stories
# region, headline, source
BRIEFS = [
    ("EUROPE", "A drone attack sets the Russian cargo ship Sparta II ablaze in the Gulf of Finland; Finland alerts NATO", "Yle"),
    ("EUROPE", "NATO calls Russia\u2019s missile incursion into Poland a grave violation, after three objects came down on Friday", "AP"),
    ("EUROPE", "Zelensky marks the Day of Dignity and calls NATO membership the best security guarantee", "Kyiv Post"),
    ("EUROPE", "A drone hits flats in the Kharkiv region, injuring 11", "Kyiv Post"),
    ("MIDDLE EAST", "Qatari mediators hold two hours of talks in Tehran; Iran says contacts are not negotiations", "Iran Intl"),
    ("MIDDLE EAST", "A fire at a Basra power plant kills two and injures 28", "Al Jazeera"),
    ("MIDDLE EAST", "A 13-year-old boy is shot dead on his way to school in East Jerusalem", "Times of Israel"),
    ("MIDDLE EAST", "Iranian schools close in the UAE and Kuwait", "Iran Intl"),
    ("AMERICAS", "Vance declines to endorse Trump\u2019s claim that Iran was close to a nuclear weapon", "Guardian"),
    ("GLOBAL", "Bitcoin falls to about $55,300, its lowest since September 2024, before recovering above $60,000", "Reuters"),
    ("GLOBAL", "The S&P 500 and the Dow close in correction, 10% or more below their records", "TNFX"),
    ("GLOBAL", "About $2.4bn of crypto positions are liquidated in 24 hours, more than $1bn of them Bitcoin", "CoinGlass"),
    ("AMERICAS", "Congress leaves Washington after a lame-duck week, with House races still uncalled", "The Hill"),
    ("AMERICAS", "Trump says he would work with Democrats to cap credit-card interest and fees", "Axios"),
    ("OCEANIA", "Rahul makes 136 as India reach 486-4, a lead of 118 over New Zealand in Wellington", "AFP"),
    ("ASIA-PACIFIC", "Kim Jong Un inspects school-equipment factories, KCNA reports, after an apparent Trump snub", "CNA"),
    ("ASIA-PACIFIC", "Delhi\u2019s air is rated poor, with the index at 321 at one monitoring station", "IITM"),
    ("ASIA-PACIFIC", "An Air Niugini 767 with 146 aboard lands at Davao after an engine-fire alert; all safe", "AeroCorner"),
    ("ASIA-PACIFIC", "Seoul offers 100m won for a tip on exam cheating", "Korea Times"),
    ("AFRICA", "Congo-Brazzaville convenes Tshisekedi, Ruto and Gnassingb\u00e9 on Sunday to end the Kinshasa-Nairobi rift", "Actualite.cd"),
    ("AFRICA", "A matatu and a lorry collide in western Kenya, killing one and injuring more than ten", "Kenyans.co.ke"),
    ("AFRICA", "Uganda cancels a Ksh385bn contract with a Turkish firm for the Kampala-Malaba railway", "Kenyans.co.ke"),
    ("AFRICA", "Kenya\u2019s judiciary reviews 1,725 cases and releases 1,329 prisoners in a single day", "Kenyans.co.ke"),
    ("AFRICA", "Two Kenyan projects win 2026 WAFA environmental awards in Denmark", "Kenyans.co.ke"),
    ("AFRICA", "Gunmen fire on a school bus in Samburu; two students are slightly hurt", "Kenyans.co.ke"),
    ("OCEANIA", "Hobart Hurricanes beat Sydney Thunder by eight wickets for their first WBBL win of the season", "ESPNcricinfo"),
    ("OCEANIA", "Sydney Sixers beat Perth Scorchers by four wickets under the DLS method", "ESPNcricinfo"),
    ("OCEANIA", "Trenaman makes a maiden WBBL fifty as Hurricanes chase 151 with 29 balls to spare", "ESPNcricinfo"),
]

# ----------------------------------------------------------------- numbers
NUMBERS = [
    ("DAY 13", "COP31, past deadline"),
    ("4TH", "Iranian attack in a week"),
    ("M6.7", "Peru quake, 108km deep"),
    ("3", "missiles downed over Riyadh"),
    ("148", "drones over Ukraine"),
    ("82,500", "marched across France"),
    ("128", "nations on killer robots"),
    ("80", "garment factories shut"),
    ("$5m", "reward for Chapo Isidro"),
]

REGIONS = ["EUROPE", "MIDDLE EAST", "AMERICAS", "ASIA-PACIFIC", "AFRICA", "OCEANIA", "GLOBAL"]

# One pin per story in page order. (lon, lat), or None for the global market
# stories, which have no place on a map.
MAP = [
    (30.7, 36.9),    # 1  COP31, Antalya
    (50.6, 26.1),    # 2  Bahrain
    (-75.8, -11.2),  # 3  Junin, Peru
    (30.5, 50.4),    # 4  Kyiv
    (6.1, 46.2),     # 5  Geneva
    (2.3, 48.9),     # 6  Paris
    (56.3, 26.1),    # 7  Khasab, Oman
    (93.9, 24.8),    # 8  Manipur
    (-108.5, 25.5),  # 9  Guasave, Sinaloa
    (-77.0, 38.9),   # 10 Washington
    (90.4, 23.8),    # 11 Dhaka
    (77.6, 34.2),    # 12 Ladakh
    (29.7, 1.7),     # 13 Ituri
    (46.7, 24.7),    # 14 Riyadh
    (144.9, -37.8),  # 15 Melbourne
    (27.5, 60.3),    # 16 Gulf of Finland
    (22.0, 49.0),    # 17 Poland
    (30.5, 50.4),    # 18 Kyiv
    (36.3, 50.0),    # 19 Kharkiv
    (51.4, 35.7),    # 20 Tehran
    (47.8, 30.5),    # 21 Basra
    (35.2, 31.8),    # 22 Jerusalem
    (55.3, 25.3),    # 23 UAE
    (-77.0, 38.9),   # 24 Washington
    None,            # 25 Bitcoin, global
    None,            # 26 S&P 500, global
    None,            # 27 liquidations, global
    (-77.0, 38.9),   # 28 Washington
    (-77.0, 38.9),   # 29 Washington
    (174.8, -41.3),  # 30 Wellington
    (125.8, 39.0),   # 31 Pyongyang
    (77.2, 28.6),    # 32 Delhi
    (125.6, 7.1),    # 33 Davao
    (127.0, 37.6),   # 34 Seoul
    (15.3, -4.3),    # 35 Oyo
    (35.0, 0.5),     # 36 western Kenya
    (32.6, 0.3),     # 37 Kampala
    (36.8, -1.3),    # 38 Nairobi
    (36.8, -1.3),    # 39 Nairobi
    (37.0, 1.5),     # 40 Samburu
    (147.3, -42.9),  # 41 Hobart
    (151.2, -33.9),  # 42 Sydney
    (147.3, -42.9),  # 43 Hobart
]


def cards():
    return CARDS


def briefs():
    return BRIEFS


def stories():
    """Every story on the page, in page order."""
    out = []
    for lead in LEADS:
        out.append((lead["region"], lead["kicker"], lead["head"], lead["body"]))
    for (region, kicker, deck, head, body, art) in CARDS:
        out.append((region, kicker, head, body))
    for (region, head, source) in BRIEFS:
        out.append((region, "", head, ""))
    return out


def counts():
    c = {r: 0 for r in REGIONS}
    for (region, _k, _h, _b) in stories():
        c[region] = c.get(region, 0) + 1
    return c
