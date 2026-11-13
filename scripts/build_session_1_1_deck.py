"""Build the Session 1.1 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_1_1_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "1.1"
TITLE = "The Platform Model Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


# Cover, orientation, and situation
slide("MODULE 1 / FOUNDATIONS OF PLATFORM BUSINESS &amp; NETWORK DYNAMICS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_1_1_campusbikes_platform_hanji.png" '
      'alt="Leo, owner of CampusBikes, asks whether to buy 70 more bikes or connect the bikes students already own.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("COURSE ORIENTATION", "How every session in this course works",
      '<p class="statement" style="font-weight:400;">In this course you are the owner of a growing business. Each week you learn one strategy.</p>'
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>A business situation and one strategy in one paragraph</p></div>'
      '<div class="card"><div class="n">02</div><p>Words, four rules, and real companies that did it well or badly</p></div>'
      '<div class="card"><div class="n">03</div><p>Tools and three exercises: easy, medium, hard (with a memo)</p></div></div>'
      '<div class="takeaway">At the end of the course you use these strategies in your final project.</div>',
      f"SESSION {SESSION} / ORIENTATION")

slide("THE SITUATION", "CampusBikes: too few bikes in busy months",
      '<p class="statement" style="font-weight:400;">CampusBikes is Leo\'s bike rental shop next to campus. Students rent a bike for $5 a day. '
      "In busy months, 70 students a day go home without a bike, while many student bikes sit unused.</p>"
      "<table><tr><th>CAMPUSBIKES</th><th style=\"text-align:right\">VALUE</th></tr>"
      '<tr><td>Bikes CampusBikes owns / rental price</td><td class="num">50 / $5 a day</td></tr>'
      '<tr><td>Busy months each year</td><td class="num">4</td></tr>'
      '<tr><td>Students who want a bike / turned away (busy day)</td><td class="num">120 / 70</td></tr>'
      '<tr><td>Students who own a bike they rarely ride</td><td class="num">800</td></tr>'
      '<tr><td>Cost of one new bike</td><td class="num">$300</td></tr>'
      '<tr><td>Repair and storage, per bike</td><td class="num">$15 a month</td></tr></table>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", "What is the Platform Model Strategy?",
      '<p class="para">A <b>pipeline</b> business makes or buys a product and sells it, so to grow it must buy more. A <b>platform</b> connects '
      "people who already have something (providers) with people who need it (users), and earns a small fee on each match. It grows by adding "
      "providers, not by buying more things, so it grows faster with less money at risk.</p>"
      '<div class="takeaway">In return, the platform must do new jobs well: help strangers trust each other, make the trade easy, '
      "and keep quality high without owning the product.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Pipeline, platform, provider and user",
      term("Pipeline business", "Makes or buys a product and sells it, step by step, like water through a pipe.",
           "a bakery bakes bread and sells it.")
      + term("Platform business", "Connects two groups so they can trade, and earns a fee on each match.",
             "Airbnb connects people who have a spare room with travelers.")
      + term("Provider and user", "The provider has something to offer; the user wants it.",
             "a student who rents out a bike / a student who rents it."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 3")

slide("WORDS YOU NEED FIRST", "Asset, idle resource, take rate",
      term("Asset", "Something a business owns that it uses to earn money.", "CampusBikes' 50 bikes.")
      + term("Idle resource", "Something people already own but rarely use.", "a bike that sits in a dorm most of the week.")
      + term("Take rate", "The fee the platform keeps, as a share of the price. Take rate = fee / price x 100.",
             "$1 of a $5 rental: 20%."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 3")

slide("WORDS YOU NEED FIRST", "Transaction cost and trust tools",
      term("Transaction cost", "The time, money, and worry needed to find a partner, pay, and check the promise is kept.",
           "meeting a stranger to hand over cash for a bike.")
      + term("Trust tools", "Things that help strangers trust each other: ID checks, ratings, deposits, insurance.",
             "a $50 deposit held by the app until the bike comes back."),
      f"SESSION {SESSION} / KEY TERMS 3 OF 3")

# Rules
rules = [
    ("Rule 1", "Connect what others already own",
     "Look for useful things that sit idle. When you connect them, you grow without paying for every new unit.",
     "800 student bikes sit unused. CampusBikes lists them in its app instead of buying 70 new bikes.",
     "Calling yourself a platform but still buying or renting every asset. You carry a pipeline's costs."),
    ("Rule 2", "Help strangers trust each other",
     "A user will not rent a stranger's bike, and an owner will not lend it, unless both feel safe.",
     "ID checks, ratings for owners and riders, a $50 deposit, and repair cover for damaged bikes.",
     "Posting phone numbers and leaving the rest to users. After one stolen bike, everyone leaves."),
    ("Rule 3", "Make finding, paying, and checking easy",
     "The platform wins when it makes the costs of a trade much smaller than doing the trade alone.",
     "A map of nearby bikes, one-tap payment, and a lock code. No meeting is needed.",
     "Users must message owners, agree on a time, and meet to hand over cash. Students give up."),
    ("Rule 4", "Keep quality high with simple rules",
     "You do not own the product, but users blame you when it is bad. Set a few clear rules for providers.",
     "Every bike passes a 3-point check (brakes, tires, lights). Owners with two bad ratings are removed.",
     "Letting anyone list anything. One broken bike hurts trust in every bike on the platform."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_1_1_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "Airbnb", "good",
     "Airbnb owns almost no homes. It connects people who have a spare room or home with travelers. At the end of 2023 it had about "
     "7.7 million active listings, with about 6,900 employees. A hotel company grows differently: Marriott paid about $13 billion in 2016 "
     "to buy Starwood Hotels.",
     ["Hosts already owned the rooms, so Airbnb grew without buying buildings. <b>(Rule 1)</b>",
      "Reviews, ID checks, and in-app payment helped strangers trust each other. <b>(Rule 2)</b>",
      "Searching, booking, and paying happen in one app. <b>(Rule 3)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "YouTube", "good",
     "YouTube does not make most of its videos. People and companies upload them, and YouTube connects them with viewers and shares ad "
     "money with many creators. In 2019, YouTube said that more than 500 hours of video were uploaded every minute.",
     ["Creators bring the videos, so YouTube does not pay for each video up front. <b>(Rule 1)</b>",
      "Uploading and finding videos is fast and free. <b>(Rule 3)</b>",
      "Community rules remove harmful videos, so viewers and advertisers keep trusting it. <b>(Rule 4)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "WeWork", "bad",
     "WeWork rented office space to companies and called itself a technology company. But it signed long leases on its buildings, while "
     "members could leave after a month. When demand for offices fell, it still had to pay rent. In November 2023 it filed for bankruptcy "
     "protection, with more than $13 billion in lease payments owed.",
     ["It rented every building itself, like a pipeline. <b>(Rule 1)</b>",
      "Its income could disappear in a month; its costs lasted for years.",
      "Calling itself a platform did not change how the business worked."], "Why it is bad"),
    ("BAD EXAMPLE 2", "Bird", "bad",
     "Bird put electric scooters on city streets and rented them through an app. Bird paid for the scooters itself, and many were "
     "damaged, stolen, or wore out quickly. Some cities limited scooters left blocking sidewalks. In December 2023, Bird filed for "
     "bankruptcy protection.",
     ["Bird paid for every scooter, so each new area needed more money. <b>(Rule 1)</b>",
      "Scooters lying on sidewalks angered cities and people who walk. <b>(Rule 4)</b>",
      "An easy app could not cover the cost of owning every scooter."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Airbnb</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Connect rooms others own, with trust tools (Rules 1 and 2)</td></tr>'
      '<tr><td>YouTube</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Creators bring videos; easy upload (Rules 1 and 3)</td></tr>'
      '<tr><td>WeWork</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Rented every building itself (Rule 1)</td></tr>'
      '<tr><td>Bird</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Owned every scooter (Rule 1)</td></tr></table>'
      '<div class="takeaway">A platform connects what others own. A business that owns everything is a pipeline, whatever it calls itself.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Take rate",
      two(flexcard("Formula", "<p>Take rate = fee per match / price x 100</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: a parking app", ul([
              "It keeps $2 of each $10 parking booking.",
              "$2 / $10 x 100 = 20%."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Cost to grow: buying or connecting",
      two(flexcard("Formula", "<p>Pipeline: new units x cost per unit</p><p>Platform: one-time cost to set up (app, checks, insurance)</p>",
                   "card", "USED IN EXERCISE 2"),
          flexcard("Example: a tool shop needs 20 more drills", ul([
              "Buying: 20 x $80 = $1,600.",
              "Connecting neighbors' drills: $500 once.",
              "Buying costs $1,600 / $500 = 3.2 times more."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Profit over several periods",
      two(flexcard("Formula", "<p>Profit = revenue per period x periods - one-time cost - running cost per period x periods</p>",
                   "card", "USED IN EXERCISE 3"),
          flexcard("Example: a $1,000 machine", ul([
              "Earns $400 a month; costs $100 a month to run.",
              "After 6 months: 6 x $400 - $1,000 - 6 x $100 = $800."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 30 students list a bike in the first month, we will buy 20 bikes instead."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Pipeline or platform?",
      '<p class="statement">Six businesses:</p><div class="card">' + ul([
          "(a) A bakery bakes bread and sells it in its shop.",
          "(b) An app connects drivers with people who rent out their empty parking spaces.",
          "(c) A TV channel makes its own shows and sells ads.",
          "(d) A website lets students sell used clothes to each other and keeps 10% of each sale.",
          "(e) A car maker builds cars and sells them through dealers.",
          "(f) An app lets home cooks sell meals to their neighbors."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Business [letter]: [pipeline / platform], because it [makes or buys / connects]\n"
               "[what], and earns money from [selling its own product / a fee on each match]."),
          tbox("WORKED EXAMPLE: TWO OTHER BUSINESSES",
               "A hotel company builds hotels and rents rooms.\n"
               "Pipeline, because it builds hotels, and earns money from selling its own rooms.\n"
               "A ride-hailing app connects riders with drivers who use their own cars.\n"
               "Platform, because it connects riders and drivers, and earns a fee on each ride.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Does it make and sell, or connect and take a fee?",
      "<table><tr><th>BUSINESS</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) Bakery</td><td>Pipeline</td><td>Makes and sells its own bread</td></tr>"
      "<tr><td>(b) Parking-space app</td><td>Platform</td><td>Connects drivers and space owners</td></tr>"
      "<tr><td>(c) TV channel</td><td>Pipeline</td><td>Makes its own shows</td></tr>"
      "<tr><td>(d) Used-clothes website</td><td>Platform</td><td>Connects sellers and buyers, 10% fee</td></tr>"
      "<tr><td>(e) Car maker</td><td>Pipeline</td><td>Builds and sells its own cars</td></tr>"
      "<tr><td>(f) Home-cook app</td><td>Platform</td><td>Connects cooks and neighbors</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Buy more, or connect? CamPro",
      two(flexcard("Scenario", ul([
          "CamPro rents cameras to art students for <b>$20</b> a day. It owns 20 and needs <b>30</b> more in project season.",
          "<b>150</b> students own a good camera they use less than once a month.",
          "<b>Buying:</b> 30 cameras at <b>$400</b> each.",
          "<b>Connecting:</b> owner gets $15, CamPro keeps <b>$5</b>; set-up costs <b>$2,000</b> once."])),
          flexcard("Your steps", ul([
              "<b>Step 1:</b> Take rate = $5 / $20 x 100 = ____%. Buying = 30 x $400 = $____. Connecting = $____. "
              "Buying costs ____ times more.",
              "<b>Step 2:</b> Check the four rules with the template.",
              "<b>Step 3:</b> Give a verdict: connect or buy."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Rule 1 (idle resources): [number] people own [what] they rarely use.\n"
               "Rule 2 (trust): we will use [trust tools].\n"
               "Rule 3 (easy trade): it will be easy because [how].\n"
               "Rule 4 (quality): every [item] must [simple rule].\n"
               "Verdict: [connect / buy], because [one sentence with a number]."),
          tbox("WORKED EXAMPLE: TOOLTOWN DRILLS",
               "Rule 1: 200 neighbors own a drill they use a few times a year.\n"
               "Rule 2: ID checks, ratings, and a $30 deposit.\n"
               "Rule 3: book and pay in the app; pick up at our store.\n"
               "Rule 4: every drill is charged and tested at our counter.\n"
               "Verdict: connect, because it costs $500 instead of $1,600.")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Connecting costs 6 times less",
      '<div class="card good">' + ul([
          "Take rate = <b>25%</b>. Buying = <b>$12,000</b>; connecting = <b>$2,000</b>; buying costs <b>6 times</b> more.",
          "Rule 1 is strong: 150 students own a camera they rarely use.",
          "A strong answer names trust tools (ID checks, ratings, a deposit, damage insurance), an easy trade, and one quality rule.",
          "A careful answer also names the risk: students may not want to lend an expensive camera."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Buy bikes or become a platform? CampusBikes, next 2 years",
      '<p class="statement">24 months, 8 busy months / serve 70 more students a day / each extra bike rented about 20 days a busy month</p>'
      + two(flexcard("Option A: Buy 70 bikes", "<p><b>$300</b> per bike, plus <b>$15</b> a month per bike for 24 months.</p>"
                     "<p>CampusBikes keeps the full <b>$5</b> a day.</p>", "card", "PIPELINE"),
            flexcard("Option B: Connect student bikes", "<p>Owner gets $4; CampusBikes keeps <b>$1</b> a day.</p>"
                     "<p><b>$3,000</b> once, plus <b>$100</b> a month for insurance and support.</p>", "card", "PLATFORM")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1 and 3)",
      '<div class="card">' + ul([
          "Take rate in Option B = $1 / $5 x 100 = ______ %",
          "Bike-days in busy months = 70 x 20 x 8 = ______",
          "Option A: revenue = bike-days x $5 = $______; costs = 70 x $300 + 70 x $15 x 24 = $______; profit = $______",
          "Option B: revenue = bike-days x $1 = $______; costs = $3,000 + $100 x 24 = $______; profit = $______",
          "If only half as many students want a bike: Option A profit = $______; Option B profit = $______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Leo (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [owner name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next busy month we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "CamPro: connect students' cameras?",
      tmpl("To: Mia Park, owner, CamPro\n"
           "1. Decision and evidence: We should connect students' cameras, because 150 students own a camera they rarely use (Rule 1) "
           "and connecting costs $2,000 against $12,000 for buying.\n"
           "2. Biggest risk and trade-off: The weakest point is that owners may fear damage to an expensive camera. We give up the full "
           "$20 a day on new cameras to avoid $12,000 of cameras that sit unused outside project season.\n"
           "3. Next step and decision rule: In the next project season we will open listings with damage insurance and measure how many "
           "cameras are listed. We will change this decision if fewer than 15 cameras are listed in the first two weeks."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Buying earns more only if almost all rentals happen",
      '<div class="card">' + ul([
          "Take rate = <b>20%</b>. Bike-days = <b>11,200</b>.",
          "Option A: $56,000 - $46,200 = <b>$9,800</b>. Option B: $11,200 - $5,400 = <b>$5,800</b>.",
          "Half the demand: Option A = $28,000 - $46,200 = <b>-$18,200</b>; Option B = $5,600 - $5,400 = <b>$200</b>.",
          "Option A wins only if demand is at least about <b>91%</b> of the expected level ($40,800 more costs / $44,800 more revenue)."])
      + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Option B earns a little less but cannot lose much, and it can grow beyond 70 bikes at no extra cost (800 student bikes).",
          "A memo for Option B points to idle bikes (Rule 1) and trust tools (Rule 2), and names the risk that few students list bikes.",
          'Decision rule: "If fewer than 70 bikes are listed by the second busy month, we will buy 30 bikes."',
          "A memo for Option A must explain why Leo is sure demand will stay high."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain pipeline and platform with provider, user, asset, and take rate.</p></div>'
      '<div class="card"><div class="n">02</div><p>Compare the cost of growing by buying with growing by connecting.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare the two plans over several periods and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Van Alstyne, M. W., Parker, G. G., &amp; Choudary, S. P. (2016). Pipelines, platforms, and the new rules of strategy. Harvard Business Review.</p>'
      '<p class="ref">Coase, R. H. (1937). The nature of the firm. Economica, 4(16), 386-405.</p>'
      '<p class="ref">Airbnb (2024). Fourth quarter and full-year 2023 financial results.</p>'
      '<p class="ref">Tubefilter (2019, May 7). More than 500 hours of content are uploaded to YouTube every minute.</p>'
      '<p class="ref">GlobeSt (2023, November 7). WeWork files for Chapter 11. CNBC (2023, December 20). Bird files for bankruptcy.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
