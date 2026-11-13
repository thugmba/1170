"""Build the Session 1.3 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_1_3_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "1.3"
TITLE = "The Two-Sided Market Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


# Cover and situation
slide("MODULE 1 / FOUNDATIONS OF PLATFORM BUSINESS &amp; NETWORK DYNAMICS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_1_3_roomlink_twosided_hanji.png" '
      'alt="Kenji, founder of RoomLink, asks whether to bring more students or more rooms first.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "RoomLink: 2,000 students, only 40 rooms",
      '<p class="statement" style="font-weight:400;">RoomLink is Kenji\'s app that connects students who need a room near campus with local '
      "landlords. Students use it for free; the landlord pays $150 when a room is rented. Most students found nothing and left.</p>"
      "<table><tr><th>ROOMLINK (THIS SEMESTER)</th><th style=\"text-align:right\">VALUE</th></tr>"
      '<tr><td>Students searching for a room</td><td class="num">2,000</td></tr>'
      '<tr><td>Rooms listed / rented through RoomLink</td><td class="num">40 / 24 (60%)</td></tr>'
      '<tr><td>Students who found nothing and left</td><td class="num">1,200</td></tr>'
      '<tr><td>Landlords within 2 km of campus</td><td class="num">300</td></tr>'
      '<tr><td>Fee per room rented / money for two semesters</td><td class="num">$150 / $10,000</td></tr></table>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", "What is the Two-Sided Market Strategy?",
      '<p class="para">A platform that serves <b>two different groups who need each other</b>: students come for rooms, and landlords list '
      "rooms only where students look. Each side waits for the other: the <b>chicken-and-egg problem</b>. Solve it in order: win the side "
      "that is harder to get, give that side value even before the other side arrives, do the hard work yourself in one small area, and give "
      "both sides a reason to finish the deal on your platform.</p>"
      '<div class="takeaway">Who should pay, and how much, is the topic of Session 2.2.</div>',
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Two sides, cross-side effect, chicken and egg",
      term("Two-sided market", "A platform serves two different groups who need each other.",
           "students (one side) and landlords (the other side).")
      + term("Cross-side network effect", "More users on one side make the platform more useful for the other side.",
             "more rooms make RoomLink more useful for students.")
      + term("Chicken-and-egg problem", "Each side waits for the other side to come first.",
             "no rooms, no students; no students, no rooms."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 3")

slide("WORDS YOU NEED FIRST", "Harder side, seeding, match rate",
      term("Harder side", "The side that is harder to win and that the other side comes for.",
           "rooms are scarce, students are many: landlords.")
      + term("Seeding", "Doing the work of one side yourself at the start.",
             "Kenji photographs rooms and writes the listings.")
      + term("Match rate", "Deals / listings (or searches) x 100.", "24 rented / 40 listed = 60%."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 3")

slide("WORDS YOU NEED FIRST", "Multi-homing and going around the platform",
      term("Multi-homing", "Using several platforms at the same time.",
           "a landlord lists on RoomLink and with an agent.")
      + term("Going around the platform", "The two sides meet on the platform but finish the deal directly.",
             "they swap phone numbers and skip RoomLink."),
      f"SESSION {SESSION} / KEY TERMS 3 OF 3")

# Rules
rules = [
    ("Rule 1", "Win the harder side first",
     "Ask which side the other side comes for, and which is harder to get. More of the easy side does not help.",
     "Kenji spends on landlords, because 2,000 students already search but only 40 rooms are listed.",
     "Buying ads for more students when there are almost no rooms. They find nothing and leave."),
    ("Rule 2", "Give the first side value before the other arrives",
     "The harder side will join if the platform helps them today, even with few users on the other side.",
     "A free tool for leases, rent reminders, and repairs that landlords use for their current tenants.",
     "Asking landlords to list a room and wait. If no student calls soon, they forget the app."),
    ("Rule 3", "Do the hard work yourself, in one small area",
     "At the start, do what users will later do alone, in one small area so both sides meet quickly.",
     "Kenji visits landlords within 1 km of campus, takes the photos, and writes the listings himself.",
     "Launching in the whole city at once. Rooms and students are spread so thin that few ever meet."),
    ("Rule 4", "Give both sides a reason to finish the deal with you",
     "If the platform only introduces people, they go around it. Add value that works only on the platform.",
     "Leases signed on RoomLink protect the deposit, are checked, and get repair help in the app.",
     "Offering nothing after the introduction. Both sides swap phone numbers and skip the fee."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_1_3_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "OpenTable", "good",
     "OpenTable started in San Francisco in 1998 to let diners book restaurant tables online. It first gave restaurants software to manage "
     "their own reservations and tables, which helped them even when few diners booked online. Diners book for free; restaurants pay. In 2014, "
     "Priceline bought OpenTable for about $2.6 billion.",
     ["It won restaurants first, because diners come where restaurants are. <b>(Rule 1)</b>",
      "Its table software helped restaurants even with few online diners. <b>(Rule 2)</b>",
      "It started in one city before moving to others. <b>(Rule 3)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "DoorDash", "good",
     "In January 2013, four Stanford students started a food-delivery website for Palo Alto, called PaloAltoDelivery.com. They put local "
     "restaurant menus online and delivered the first orders themselves. By 2023, DoorDash had become the largest food-delivery company in "
     "the United States.",
     ["The founders did the drivers' work themselves at the start. <b>(Rule 3)</b>",
      "One small town, so restaurants, eaters, and drivers met quickly. <b>(Rule 3)</b>",
      "Restaurants got new orders without doing anything new. <b>(Rule 2)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Homejoy", "bad",
     "Homejoy connected people who wanted their home cleaned with cleaners. It attracted customers with very cheap first cleanings, but many "
     "did not book again at the normal price. Former employees said good cleaners and regular customers often made private arrangements. "
     "Homejoy also faced lawsuits about its workers, and it closed in July 2015.",
     ["After the first match, both sides had little reason to stay, so they went around it. <b>(Rule 4)</b>",
      "Cheap first offers brought customers who did not stay (Session 1.4).",
      "It expanded to many cities before each city worked well. <b>(Rule 3)</b>"], "Why it is bad"),
    ("BAD EXAMPLE 2", "Google Helpouts", "bad",
     "In November 2013, Google launched Helpouts, where experts gave live video help (cooking, guitar, computer help) for a fee. It covered "
     "many topics at once. In February 2015, Google said Helpouts had not grown as fast as expected, and it closed in April 2015.",
     ["Experts waited for customers and got little value while they waited. <b>(Rule 2)</b>",
      "Many topics at once: few experts and few users in each. <b>(Rule 3)</b>",
      "It did not first win the harder side in each topic. <b>(Rule 1)</b>"], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>OpenTable</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Useful to restaurants first (Rules 1 and 2)</td></tr>'
      '<tr><td>DoorDash</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Founders did the work in one town (Rule 3)</td></tr>'
      '<tr><td>Homejoy</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Both sides went around it (Rule 4)</td></tr>'
      '<tr><td>Google Helpouts</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Experts waited with no value (Rule 2)</td></tr></table>'
      '<div class="takeaway">Bring the harder side first, and keep both sides on the platform after the match.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Balance between the sides",
      two(flexcard("Formula", "<p>Balance = users on the demand side / providers on the supply side</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: a pet-sitting app", ul([
              "300 pet owners searching; 60 sitters.",
              "300 / 60 = 5 owners per sitter."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Match rate",
      two(flexcard("Formula", "<p>Match rate = deals / searches (or listings) x 100</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example", ul([
              "120 bookings from 300 pet owners searching.",
              "120 / 300 x 100 = 40%."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Profit over several periods (from Session 1.1)",
      two(flexcard("Formula", "<p>Profit = extra revenue per period x number of periods - cost</p>", "card", "USED IN EXERCISE 3"),
          flexcard("Example", ul([
              "A plan costs $3,000 and adds $1,000 a month.",
              "After 6 months: 6 x $1,000 - $3,000 = $3,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 1.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 30 new rooms are listed in the first two months, we will change the plan."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Name the two sides",
      '<p class="statement">Six platforms:</p><div class="card">' + ul([
          "(a) A ride-hailing app.",
          "(b) A video game console.",
          "(c) A phone app store.",
          "(d) An online market for handmade goods.",
          "(e) A free newspaper.",
          "(f) A credit card."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Platform [letter]: side 1 = [group], side 2 = [group].\n"
               "More [side 1] attracts more [side 2] because [reason].\n"
               "Harder side to win first: [group], because [reason]."),
          tbox("WORKED EXAMPLE: A HOTEL BOOKING WEBSITE",
               "Side 1 = travelers, side 2 = hotels.\n"
               "More hotels attract more travelers because travelers want many choices.\n"
               "Harder side to win first: hotels, because travelers come only where many hotels are listed.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Which side does the other side come for?",
      "<table><tr><th>PLATFORM</th><th>TWO SIDES</th><th>HARDER SIDE FIRST</th></tr>"
      "<tr><td>(a) Ride-hailing</td><td>Riders, drivers</td><td>Drivers</td></tr>"
      "<tr><td>(b) Game console</td><td>Players, game makers</td><td>Game makers</td></tr>"
      "<tr><td>(c) App store</td><td>Phone users, developers</td><td>Developers</td></tr>"
      "<tr><td>(d) Handmade market</td><td>Buyers, makers</td><td>Makers</td></tr>"
      "<tr><td>(e) Free newspaper</td><td>Readers, advertisers</td><td>Readers</td></tr>"
      "<tr><td>(f) Credit card</td><td>Shoppers, stores</td><td>Stores</td></tr></table>"
      '<div class="takeaway">Other answers can be strong if the reason is clear.</div>',
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Which side is missing? PetSit",
      "<table><tr><th>AREA</th><th style=\"text-align:right\">PET OWNERS SEARCHING</th><th style=\"text-align:right\">SITTERS LISTED</th>"
      "<th style=\"text-align:right\">BOOKINGS</th></tr>"
      '<tr><td>North</td><td class="num">600</td><td class="num">10</td><td class="num">6</td></tr>'
      '<tr><td>Center</td><td class="num">300</td><td class="num">60</td><td class="num">120</td></tr>'
      '<tr><td>South</td><td class="num">100</td><td class="num">80</td><td class="num">20</td></tr></table>'
      '<div class="card" style="margin-top:.2in;">' + ul([
          "<b>Step 1:</b> For each area, balance = owners / sitters, and match rate = bookings / owners x 100.",
          "<b>Step 2:</b> Which side is missing in each area?",
          "<b>Step 3:</b> Choose one action for each area, and the rule it follows."]) + "</div>",
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "[Area]: [number] owners per sitter, match rate [number]%.\n"
               "The missing side is [owners / sitters / none].\n"
               "Action: [one action] (Rule [number])."),
          tbox("WORKED EXAMPLE: BOOKSWAP, CAMPUS 1",
               "500 buyers searching, 20 sellers, 10 sales.\n"
               "Campus 1: 25 buyers per seller, match rate 2%.\n"
               "The missing side is sellers.\n"
               "Action: ask final-year students to list the books they no longer need,\n"
               "and write the listings for them (Rule 3).")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Each area is missing a different side",
      "<table><tr><th>AREA</th><th style=\"text-align:right\">OWNERS PER SITTER</th><th style=\"text-align:right\">MATCH RATE</th>"
      "<th>MISSING SIDE</th><th>ONE ACTION</th></tr>"
      '<tr><td>North</td><td class="num">60</td><td class="num">1%</td><td>Sitters</td><td>Help dorm students make sitter profiles (Rule 3)</td></tr>'
      '<tr><td>Center</td><td class="num">5</td><td class="num">40%</td><td>None</td><td>Payment protection (Rule 4)</td></tr>'
      '<tr><td>South</td><td class="num">1.25</td><td class="num">20%</td><td>Owners</td><td>Reach owners at pet shops and vets (Rule 1)</td></tr></table>'
      '<div class="takeaway">The same platform can be missing a different side in each area. Look at each area separately.</div>',
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Students or landlords first? RoomLink, next 2 semesters",
      '<p class="statement">2,000 students / 40 rooms listed, 24 rented / $150 fee per room rented / $10,000 to spend</p>'
      + two(flexcard("Option A: More students", "<p><b>$10,000</b> on student ads: 2,000 more students search.</p>"
                     "<p>Rooms do not change, but <b>70%</b> of them rent instead of 60%.</p>", "card", "EASY SIDE"),
            flexcard("Option B: More landlords", "<p><b>$4,000</b> for a free lease-and-rent tool, plus <b>$3,000</b> per semester for a "
                     "helper who visits landlords and writes listings.</p><p>Expect <b>100</b> more rooms each semester; 60% rent.</p>",
                     "card", "HARDER SIDE")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1, 2, and 3)",
      '<div class="card">' + ul([
          "Balance now = 2,000 / 40 = ______ students per room",
          "Option A: rooms rented = 40 x 70% = ______; extra = ______; extra fees over 2 semesters = extra x $150 x 2 = $______; "
          "profit = $______",
          "Option B: rooms rented = 140 x 60% = ______; extra = ______; extra fees = $______; profit = $______",
          "Option B with only 50 new rooms each semester: profit = $______",
          "New rooms per semester Option B needs to pay back $10,000: new rooms x 60% x $150 x 2 = $10,000, so ______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Kenji (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [founder name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next two months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "PetSit: sitters first in North?",
      tmpl("To: Lina Haddad, founder, PetSit\n"
           "1. Decision and evidence: We should spend this month's budget on sitters in North, not on owners, because North has 60 owners "
           "per sitter and a match rate of only 1% (Rule 1).\n"
           "2. Biggest risk and trade-off: The weakest point is that students may not want to pet-sit during exams. We give up growth in "
           "owner numbers to make the owners we already have find a sitter.\n"
           "3. Next step and decision rule: In the next two months we will help students in three dorms create sitter profiles and measure "
           "the match rate in North. We will change this decision if the match rate is still below 10% after two months."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "More students cannot rent rooms that do not exist",
      '<div class="card">' + ul([
          "Balance now = <b>50</b> students per room: rooms are the harder side.",
          "Option A: 28 rooms rented; extra 4; $1,200 - $10,000 = <b>-$8,800</b>.",
          "Option B: 84 rooms rented; extra 60; $18,000 - $10,000 = <b>$8,000</b>.",
          "Option B with only 50 new rooms: 54 rented; extra 30; $9,000 - $10,000 = <b>-$1,000</b>.",
          "Payback line: $10,000 / $180 = about <b>56</b> new rooms per semester."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Chooses Option B (Rules 1, 2, and 3), but only if the helper adds at least about 56 rooms per semester.",
          'Decision rule: "If fewer than 30 new rooms are listed in the first two months, we will change the plan."',
          "Adds a reason to sign the lease on RoomLink, such as deposit protection (Rule 4), so new landlords do not go around the app."])
      + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain a two-sided market, the chicken-and-egg problem, and the harder side.</p></div>'
      '<div class="card"><div class="n">02</div><p>Measure balance and match rate to find the missing side.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare growing one side with the other and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Rochet, J.-C., &amp; Tirole, J. (2003). Platform competition in two-sided markets. JEEA, 1(4), 990-1029.</p>'
      '<p class="ref">Caillaud, B., &amp; Jullien, B. (2003). Chicken &amp; egg. RAND Journal of Economics, 34(2), 309-328.</p>'
      '<p class="ref">OpenTable, Inc. (2014). Schedule 14D-9: The Priceline Group to acquire OpenTable. SEC EDGAR.</p>'
      '<p class="ref">The Stanford Daily (2013, September 23). Alumni-founded startup delivers local eatery goods to campus.</p>'
      '<p class="ref">Fortune (2015, July 17). Homejoy is closing. 9to5Google (2015, February 13). Google Helpouts is shutting down.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
