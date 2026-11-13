"""Build the Session 1.4 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_1_4_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "1.4"
TITLE = "The Winner-Takes-All Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


# Cover and situation
slide("MODULE 1 / FOUNDATIONS OF PLATFORM BUSINESS &amp; NETWORK DYNAMICS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_1_4_latebite_winner_hanji.png" '
      'alt="Omar, founder of LateBite, asks whether to race QuickEats with discounts or own the late night.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "LateBite: race a rich rival, or be different?",
      '<p class="statement" style="font-weight:400;">LateBite is Omar\'s food-delivery app for students, the only one open after 11 pm. '
      "QuickEats, a much bigger rival, now gives $3 off every order. 60% of LateBite users also have QuickEats.</p>"
      "<table><tr><th>ONE MONTH</th><th style=\"text-align:right\">LATEBITE</th><th style=\"text-align:right\">QUICKEATS</th></tr>"
      '<tr><td>Orders</td><td class="num">6,000</td><td class="num">9,000</td></tr>'
      '<tr><td>Hours open</td><td class="num">6 pm - 3 am</td><td class="num">10 am - 11 pm</td></tr>'
      '<tr><td>Restaurants</td><td class="num">25</td><td class="num">60</td></tr>'
      '<tr><td>Orders after 11 pm</td><td class="num">2,500</td><td class="num">0</td></tr>'
      '<tr><td>Money left from each order</td><td class="num">$2</td><td class="num">Not known</td></tr>'
      '<tr><td>Money in the bank</td><td class="num">$40,000</td><td class="num">Large funding</td></tr></table>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", "What is the Winner-Takes-All Strategy?",
      '<p class="para">Some markets <b>tip</b>: one platform ends up with almost all customers. This happens when a bigger network is clearly '
      "better, using two platforms is hard, and most users want the same thing. There, racing to lead, one local market at a time, can make "
      "sense. But many markets do not tip, and racing with discounts only burns money. There, <b>choose a niche and be clearly different</b>.</p>"
      '<div class="takeaway">First test: will this market tip? Then decide: race, or be different.</div>',
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Winner-takes-all, tipping, multi-homing, switching cost",
      term("Winner-takes-all market", "One company ends up with almost all the customers.",
           "most people in a country use one main search engine.")
      + term("Tipping", "Users move to one leader faster and faster, because the bigger network keeps getting better.",
             "once most friends are on one network, the rest join too.")
      + term("Multi-homing (Session 1.3)", "Using several platforms at the same time.",
             "a student has both LateBite and QuickEats."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 3")

slide("WORDS YOU NEED FIRST", "Switching cost and market share",
      term("Switching cost", "What a user loses by moving to a rival: money, time, data, or friends.",
           "leaving your photos and friends behind.")
      + term("Market share", "Our sales / all sales in the market x 100.", "6,000 / 15,000 x 100 = 40%."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 3")

slide("WORDS YOU NEED FIRST", "Niche and months of cash",
      term("Niche", "A smaller part of a market with special needs that you can serve better than anyone.",
           "late-night delivery for students.")
      + term("Burn rate and months of cash", "Money lost each month / money in the bank divided by that loss.",
             "$40,000 / $10,000 = 4 months."),
      f"SESSION {SESSION} / KEY TERMS 3 OF 3")

# Rules
rules = [
    ("Rule 1", "Check whether the market can tip before you race",
     "Three conditions: a bigger network is clearly better, using two platforms is hard, users want the same thing.",
     "60% of LateBite users already have both apps, and a second app is free. This market is unlikely to tip.",
     'Believing "the biggest always wins everything." Many markets have two or three winners for years.'),
    ("Rule 2", "If it can tip, win one local market first, and fast",
     "Tipping happens place by place. Be clearly the biggest in one city or campus before you spread out.",
     "LateBite is the clear leader at night on its home campus before it opens on a second campus.",
     "Opening on ten campuses with a few users each. A rival that leads each campus wins them one by one."),
    ("Rule 3", "Do not buy users with discounts alone",
     "Users who come only for a discount leave when it ends. Spend on things that stay: speed, choice, quality.",
     "Instead of $3 off, LateBite signs 10 more late-night restaurants and promises delivery in 20 minutes.",
     "Matching a rich rival's discount. Your cash runs out first, and users switch back."),
    ("Rule 4", "If it will not tip, choose a niche and be different",
     "Find the customers the leader serves badly, and become the best choice for them.",
     "LateBite focuses on 11 pm to 3 am, when QuickEats is closed, and delivers to the dorm room door.",
     "Copying the leader's product at a lower price. Users have no reason to choose the smaller copy."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_1_4_rule_{i}_hanji.png" alt="{no}: do and avoid" '
           'style="width:6.6in;height:3.71in;object-fit:contain;flex:none;border:1.2px solid #aeb7c1;">')
    cards = ('<div style="flex:1;">'
             + card("Example", f'<p style="font-size:27px">{ex}</p>', "card good", "DO")
             + card("Common mistake", f'<p style="font-size:27px">{mistake}</p>', "card bad\" style=\"margin-top:.18in", "AVOID") + "</div>")
    slide(f"THE FOUR RULES / {no.upper()}", f"{no}: {title}",
          f'<p class="statement" style="font-size:34px;margin-bottom:.16in;">{rule}</p>'
          '<div style="display:flex;gap:.26in;align-items:flex-start;">' + pic + cards + "</div>",
          f"SESSION {SESSION} / {no.upper()} OF 4")

# Examples
examples = [
    ("GOOD EXAMPLE 1", "Yahoo! Auctions in Japan", "good",
     "Online auctions can tip: buyers go where most sellers are, and sellers go where most buyers are. Yahoo! Japan opened its auction site "
     "in 1999, a few months before eBay entered Japan, and grew quickly. By 2002 eBay had only about 3% of the Japanese online auction market, "
     "and it closed its Japanese site in March 2002.",
     ["Auctions can tip, so being first and biggest mattered. <b>(Rule 1)</b>",
      "Yahoo! Japan became the clear leader in one country, fast. <b>(Rule 2)</b>",
      "More sellers made the site more useful for every buyer, and the gap grew."], "Why it is good"),
    ("GOOD EXAMPLE 2", "Bumble", "good",
     "Dating apps do not tip to one winner: many people use two or three apps, and people want different things. Bumble, started in 2014, "
     "chose to be different: women send the first message. In February 2021 Bumble became a public company, and its Bumble app had about "
     "1.1 million paying users.",
     ["It saw the market would not tip: people use several dating apps. <b>(Rule 1)</b>",
      "It did not copy the leader; it served women who wanted more control. <b>(Rule 4)</b>",
      "Users chose it for this difference, not for a discount. <b>(Rule 3)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Groupon", "bad",
     "Groupon sold daily discount deals from local shops and grew very fast; in December 2010 it reportedly turned down about $6 billion "
     "from Google. But hundreds of similar deal sites appeared, and shoppers and shops used several of them. It went public in November 2011 "
     "at $20 a share; a year later its shares had lost more than three-quarters of their value.",
     ["Shoppers and shops easily used many deal sites: the market could not tip. <b>(Rule 1)</b>",
      "It spent heavily on marketing and discounts to keep growing. <b>(Rule 3)</b>",
      "It acted like a future sole winner in a market with many winners."], "Why it is bad"),
    ("BAD EXAMPLE 2", "MoviePass", "bad",
     "In August 2017, MoviePass let members see one movie a day for $9.95 a month, and paid theaters the full ticket price itself. Members "
     "rose to more than 3 million. It hoped size would make theaters share their money. Instead AMC started its own subscription in June "
     "2018. MoviePass ran out of money and closed in September 2019.",
     ["It lost money on almost every member: a price it could not keep. <b>(Rule 3)</b>",
      "More members did not help other members: no network effect, no tipping. <b>(Rule 1)</b>",
      "When the low price ended, members left."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Yahoo! Auctions Japan</td><td style="color:#2f6b47;font-weight:700">Good</td><td>A market that tips; led one country fast (Rules 1 and 2)</td></tr>'
      '<tr><td>Bumble</td><td style="color:#2f6b47;font-weight:700">Good</td><td>A market that does not tip; chose to be different (Rule 4)</td></tr>'
      '<tr><td>Groupon</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Raced in a market that could not tip (Rule 1)</td></tr>'
      '<tr><td>MoviePass</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Bought members with a price it could not keep (Rule 3)</td></tr></table>'
      '<div class="takeaway">Race only where the market can tip. Everywhere else, be different.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Market share",
      two(flexcard("Formula", "<p>Market share = our sales / all sales in the market x 100</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: two scooter apps", ul([
              "40,000 rides and 60,000 rides.",
              "Smaller app: 40,000 / 100,000 x 100 = 40%."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Multi-homing rate",
      two(flexcard("Formula", "<p>Multi-homing rate = our users who also use a rival / our users x 100</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example", ul([
              "14,000 of 20,000 users also use a rival app.",
              "14,000 / 20,000 x 100 = 70%.",
              "Above about 50%, using two apps is clearly easy."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Months of cash",
      two(flexcard("Formula", "<p>Months of cash = money in the bank / monthly loss</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example", ul([
              "$100,000 in the bank, losing $20,000 a month.",
              "$100,000 / $20,000 = 5 months."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Profit over several periods, with a decision rule",
      two(flexcard("Formula", "<p>Profit = monthly profit x number of months - one-time cost</p>"
                   "<p>A <b>decision rule</b> says which result would make you change the plan (Session 1.1).</p>",
                   "card", "USED IN EXERCISE 3"),
          flexcard("Example", ul([
              "A plan costs $5,000; the business earns $3,000 a month.",
              "After 6 months: 6 x $3,000 - $5,000 = $13,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Will the market tip?",
      '<p class="statement">Six markets:</p><div class="card">' + ul([
          "(a) A social network where friends share photos.",
          "(b) Taxi apps in a city where riders and drivers use several apps.",
          "(c) Operating systems for office computers, where files and software must work together.",
          "(d) Food-delivery apps.",
          "(e) An online auction site for rare collectibles.",
          "(f) Coffee shops in a city."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Market [letter]: network effects [strong / weak / none];\n"
               "using two at once is [easy / hard];\n"
               "users want [the same thing / different things].\n"
               "So the market is [likely / unlikely] to tip."),
          tbox("WORKED EXAMPLE: TWO OTHER MARKETS",
               "Video-call apps for a company's staff: strong; hard;\n"
               "the same thing. Likely to tip (inside each company).\n"
               "Online clothing stores: weak; easy; different things.\n"
               "Unlikely to tip.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Are all three conditions true?",
      "<table><tr><th>MARKET</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) Photo social network</td><td>Likely</td><td>Leaving means leaving your friends</td></tr>"
      "<tr><td>(b) Taxi apps</td><td>Unlikely</td><td>Riders and drivers use several apps</td></tr>"
      "<tr><td>(c) Office operating systems</td><td>Likely</td><td>Files and software must work together</td></tr>"
      "<tr><td>(d) Food delivery</td><td>Unlikely</td><td>A second app is free</td></tr>"
      "<tr><td>(e) Rare-item auctions</td><td>Likely</td><td>Everyone wants the one place with everyone else</td></tr>"
      "<tr><td>(f) Coffee shops</td><td>Unlikely</td><td>No network effect</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Race or niche? SeatSwap",
      two(flexcard("Scenario", ul([
          "You run SeatSwap, a ticket-resale app for students: <b>8,000</b> users; <b>5,000</b> also use TicketGo.",
          "This month: TicketGo <b>3,000</b> trades, SeatSwap <b>2,000</b>.",
          "SeatSwap loses <b>$5,000</b> a month and has <b>$30,000</b> in the bank.",
          "Students complain about fake tickets on both apps."])),
          flexcard("Your steps", ul([
              "<b>Step 1:</b> Market share = ____%. Multi-homing = 5,000 / 8,000 x 100 = ____%. Months of cash = ____.",
              "<b>Step 2:</b> Check the three tipping conditions (Rule 1).",
              "<b>Step 3:</b> Choose: race or niche?"]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Market share [number]%, multi-homing [number]%, [number] months of cash.\n"
               "Tipping test: network effects [strong / weak]; using two apps is\n"
               "[easy / hard]; users want [the same / different things].\n"
               "The market is [likely / unlikely] to tip.\n"
               "Decision: [race / niche]. Our plan: [one sentence] (Rule [number])."),
          tbox("WORKED EXAMPLE: RIDEON SCOOTERS",
               "Market share 40%, multi-homing 70%, 5 months of cash.\n"
               "Tipping test: weak; easy; different things\n"
               "(short trips vs. daily commuting).\n"
               "The market is unlikely to tip.\n"
               "Decision: niche. Monthly passes and reserved scooters\n"
               "for commuters near the train station (Rule 4).")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Unlikely to tip: choose a niche",
      '<div class="card good">' + ul([
          "Market share = <b>40%</b>. Multi-homing = <b>62.5%</b>. Months of cash = <b>6</b>.",
          "Network effects are moderate, using two apps is easy (62.5% already do), and students have a special need: no fake tickets.",
          "The market is <b>unlikely to tip</b>, so a race with 6 months of cash is risky.",
          'Strong answer: a niche such as "only tickets from verified students, with money back if a ticket is fake" (Rule 4), '
          "with no discounts (Rule 3)."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Should LateBite race QuickEats? Next 6 months",
      '<p class="statement">6,000 orders a month / $2 left from each order / $40,000 in the bank / 60% of users also use QuickEats</p>'
      + two(flexcard("Option A: Race", "<p><b>$3</b> off every order. Orders rise to <b>10,000</b> a month while the discount lasts.</p>"
                     "<p>When it ends, orders fall back to about <b>6,500</b>.</p>", "card", "DISCOUNT"),
            flexcard("Option B: Own the late night", "<p><b>$12,000</b> once: 10 more late-night restaurants and door delivery in 20 minutes.</p>"
                     "<p>Late-night orders rise by <b>1,500</b> a month (2,500 to 4,000). No discount.</p>", "card", "NICHE")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1, 3, and 4)",
      '<div class="card">' + ul([
          "Market share now = 6,000 / (6,000 + 9,000) x 100 = ______%",
          "No change: 6,000 x $2 x 6 = $______",
          "Option A: money left per order = $2 - $3 = $______; monthly result = 10,000 x ______ = $______; "
          "months of cash = $40,000 / ______ = ______",
          "Option B: orders a month = ______; profit over 6 months = ______ x $2 x 6 - $12,000 = $______",
          "Option B if late-night orders rise by only 600: $______",
          "Extra orders a month Option B needs to beat no change: extra x $2 x 6 = $12,000, so ______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Omar (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [founder name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next two months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "RideOn: race BikeGo or serve commuters?",
      tmpl("To: Daniel Kim, CEO, RideOn\n"
           "1. Decision and evidence: We should not race BikeGo with free rides. We should offer monthly passes for commuters near the "
           "train station, because 70% of our users already use both apps (Rule 1) and we have only 5 months of cash.\n"
           "2. Biggest risk and trade-off: The weakest point is that commuters may want more scooters than we have at 8 am. We give up the "
           "hope of becoming the biggest app in the city to become the best app for one group that stays.\n"
           "3. Next step and decision rule: In the next two months we will sell passes at one station and measure how many pass holders ride "
           "at least 15 days a month. We will change this decision if fewer than 300 passes are sold by the end of month two."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "The race runs out of cash in month 4",
      '<div class="card">' + ul([
          "Market share = <b>40%</b>. No change: <b>$72,000</b>.",
          "Option A: <b>-$1</b> per order; <b>-$10,000</b> a month; <b>4 months</b> of cash, before the race ends. "
          "Afterward, orders fall back to about 6,500.",
          "Option B: 7,500 x $2 x 6 - $12,000 = <b>$78,000</b>, $6,000 more than no change.",
          "Option B with only 600 extra: <b>$67,200</b>, $4,800 less than no change.",
          "Option B needs at least <b>1,000</b> extra orders a month."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Rejects Option A: the market is unlikely to tip (Rule 1), and the discount buys users who leave (Rule 3).",
          "Chooses Option B (Rule 4): it builds on LateBite's strength, the only app after 11 pm.",
          'Decision rule: "If late-night orders are below 3,000 a month after two months, we will stop adding restaurants and review the plan."',
          "May say when Omar would race: only if students started deleting one of the two apps."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain winner-takes-all markets, tipping, and multi-homing.</p></div>'
      '<div class="card"><div class="n">02</div><p>Test whether a market can tip; measure share, multi-homing, and months of cash.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare a race with a niche plan and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Eisenmann, T., Parker, G., &amp; Van Alstyne, M. W. (2006). Strategies for two-sided markets. Harvard Business Review.</p>'
      '<p class="ref">Arthur, W. B. (1989). Competing technologies, increasing returns, and lock-in by historical events. The Economic Journal.</p>'
      '<p class="ref">Internet News (2002, February). eBay enters Taiwan market, exits Japan.</p>'
      '<p class="ref">Fortune (2021, February 11). Bumble IPO. CNN Money (2010, December 3). Groupon turns down Google.</p>'
      '<p class="ref">NPR (2019, September 14). MoviePass has officially shut down.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
