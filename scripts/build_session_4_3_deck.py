"""Build the Session 4.3 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_4_3_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "4.3"
TITLE = "The Super-App Strategy (Case Study: Grab)"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


# Cover and situation
slide("MODULE 4 / REAL-WORLD CASE STUDIES &amp; STRATEGIC SYNTHESIS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_4_3_campusgo_superapp_hanji.png" '
      'alt="Ama, founder of CampusGo, asks whether to add every service at once or one at a time.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "CampusGo: an app students open almost every day",
      '<p class="statement" style="font-weight:400;">CampusGo is Ama\'s app for booking seats on campus shuttles. She wants it to become '
      'the one app for daily campus life. An investor says: "Launch food, laundry, printing, tickets, and a wallet at once, with big discounts."</p>'
      "<table><tr><th>CAMPUSGO (ONE MONTH)</th><th style=\"text-align:right\">VALUE</th></tr>"
      '<tr><td>Students who use the app</td><td class="num">12,000</td></tr>'
      '<tr><td>Shuttle rides per student per month</td><td class="num">10</td></tr>'
      '<tr><td>Profit per ride</td><td class="num">$0.20</td></tr>'
      '<tr><td>Monthly profit (12,000 x 10 x $0.20)</td><td class="num">$24,000</td></tr>'
      '<tr><td>Other services</td><td class="num">None</td></tr></table>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", "What is the Super-App Strategy?",
      '<p class="para">One app that people use very often becomes <b>a single app for many daily services</b>. It starts with a '
      "<b>front door</b>, a service people open many times a week, then adds services for the same users, such as food delivery, payments, "
      "and loans, under <b>one account and one wallet</b>. Each new service is cheaper to launch because the users are already there "
      "(Session 3.1). Grab and WeChat are the best-known examples.</p>"
      '<div class="takeaway">Use it when your app is used very often, your users need other services that fit next to it, '
      "and you can make each service pay for itself in time.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Super-app, front door, usage frequency",
      term("Super-app", "One app that offers many everyday services under one account and one wallet.",
           "an app for rides, food delivery, and payments.")
      + term("Front door", "The service that brings people into the app many times a week.",
             "CampusGo's shuttle booking, used 10 times a month.")
      + term("Usage frequency", "How often a person uses a service in a period.",
             "10 rides a month is high; buying a laptop once in three years is low."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "E-wallet, subsidy, contribution",
      term("E-wallet", "Money stored in an app that can pay for any service in it.",
           "a student adds $20 and pays for rides and food.")
      + term("Subsidy<br><span style=\"font-size:24px;color:#526174;\">(incentive)</span>",
             "Money a company spends to make a service cheaper for users or more attractive for drivers or shops.",
             "CampusGo pays $1 of every food order.")
      + term("Contribution", "What a service earns after its own direct costs and subsidies.<br>= revenue - direct costs - subsidies",
             "$10,000 - $7,000 - $1,000 = $2,000."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 2")

# Rules
rules = [
    ("Rule 1", "Start with a service people use very often",
     "The front door must bring users back many times a week. Rarely used services cannot hold up a super-app.",
     "CampusGo is opened 10 times a month by 12,000 students, so a new service inside it is seen by many students right away.",
     "Building a super-app around something people use once a year, such as booking graduation photos. Users forget the app."),
    ("Rule 2", "Add services the same users already need, one at a time",
     "Each new service should fit naturally next to the front door, and should be good before the next one is added.",
     "Students take the shuttle to class, and many order lunch on the way. Food comes first; laundry only after food works well.",
     "Launching many services at once. Each one is weak, users have bad experiences, and the whole app gets a bad name."),
    ("Rule 3", "Connect services with one safe wallet",
     "A wallet makes every service easier to use, but money and personal data need strong protection and must follow the law.",
     "The CampusGo wallet works with a licensed bank partner, checks each user's identity, and pays for rides and food with one tap.",
     "Holding users' money without the right licence or checks. Regulators can stop the service, and users stop trusting the app."),
    ("Rule 4", "Make each service pay for itself in time",
     "Subsidies can start a service, but every service should reach a positive contribution on its own. Stop paying people to use it.",
     "CampusGo pays $1 of each food order for the first two months only, then checks whether food earns money without it.",
     "Using discounts forever to keep users in every service. The app grows in users but loses more money each month."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_4_3_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "Grab", "good",
     "Grab started in 2012 as a taxi-booking app in Malaysia and became a super-app across Southeast Asia, adding food delivery, package "
     "delivery, payments, and loans. For years it spent heavily on incentives and lost money. As it cut incentives, it improved: in 2024, "
     "revenue grew 19% to $2.8 billion and adjusted EBITDA (a measure of operating profit) turned positive at $313 million, though it still "
     "had a net loss of $158 million.",
     ["Rides were a front door used many times a week. <b>(Rule 1)</b>",
      "Food, delivery, and payments were added for the same users. <b>(Rule 2)</b>",
      "GrabPay connected the services. <b>(Rule 3)</b>",
      "<i>Lesson:</i> years of losses show how costly subsidies are. <b>(Rule 4)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "WeChat", "good",
     "WeChat started in 2011 as a messaging app in China. In 2013 it added WeChat Pay. In 2014, at Chinese New Year, users could send digital "
     "red envelopes (gifts of money), and many linked their bank cards for the first time. In 2017 it added mini programs from other "
     "companies. In early 2025, WeChat had about 1.4 billion monthly users.",
     ["Messaging is used many times a day: the strongest front door. <b>(Rule 1)</b>",
      "Each new service fitted what users already did with friends. <b>(Rule 2)</b>",
      "Red envelopes gave a fun reason to link a bank card. <b>(Rule 3)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Paytm Payments Bank", "bad",
     "Paytm, a large Indian payments app, offered wallets, bank accounts, and many other services through Paytm Payments Bank. In January 2024, "
     "the Reserve Bank of India ordered the bank to stop taking new deposits and top-ups after February 29, 2024, because audits found "
     "\"persistent non-compliances.\" Millions of users had to move their money elsewhere.",
     ["The wallet and bank did not follow the regulator's rules. <b>(Rule 3)</b>",
      "When the money service stopped, users lost trust in the other services too.",
      "In a super-app, a problem in one service hurts all the others."], "Why it is bad"),
    ("BAD EXAMPLE 2", "Facebook's Libra (Diem)", "bad",
     "In 2019, Facebook announced Libra, a new digital currency for its apps, such as Messenger and WhatsApp. Governments and central banks "
     "worried about risks to money and privacy. After years of pushback, the project (renamed Diem) was shut down, and its technology was sold "
     "to Silvergate Bank in 2022 for about $182 million.",
     ["Tried to add a very large money service before regulators trusted it. <b>(Rule 3)</b>",
      "Started with a whole new currency, not a small service users already needed. <b>(Rule 2)</b>",
      "Years of work ended without a launched product."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Grab</td><td style="color:#2f6b47;font-weight:700">Good</td><td>A busy front door, then services for the same users (Rules 1 and 2)</td></tr>'
      '<tr><td>WeChat</td><td style="color:#2f6b47;font-weight:700">Good</td><td>A daily habit, then a wallet people wanted (Rules 1 and 3)</td></tr>'
      '<tr><td>Paytm Payments Bank</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Money service broke the rules (Rule 3)</td></tr>'
      '<tr><td>Libra (Diem)</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Too big a money service, too early (Rules 2 and 3)</td></tr></table>'
      '<div class="takeaway">One busy front door, one good service at a time, one safe wallet, and every service paying its own way.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: The front-door test",
      two(flexcard("Formula", "<p>Uses per month = users x times each user opens the service per month</p>",
                   "card", "USED IN EXERCISE 1"),
          flexcard("Example", ul([
              "Bus-ticket app: 5,000 users x 20 trips = 100,000 uses a month.",
              "Car-buying app: 5,000 users x 0.03 purchases = 150 uses a month.",
              "Only the bus app can be a front door."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Users who try a new service",
      two(flexcard("Formula", "<p>New service users = app users x share who try it</p>", "card", "USED IN EXERCISE 3"),
          flexcard("Example", ul([
              "12,000 users; 20% order food.",
              "12,000 x 20% = 2,400 food users."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Contribution of each service",
      two(flexcard("Formula", "<p>Contribution = revenue - direct costs - subsidies</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: food delivery", ul([
              "Revenue $10,000; restaurants and riders $7,000; discounts $1,000.",
              "$10,000 - $7,000 - $1,000 = $2,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If food delivery does not reach a positive contribution by month 3 without discounts, we will not add laundry."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Can it be a front door?",
      '<p class="statement">Six apps want to become super-apps:</p><div class="card">' + ul([
          "(a) A messaging app people use every day.",
          "(b) A wedding-planning app.",
          "(c) A bus-ticket app that commuters use twice a day.",
          "(d) A car-buying website.",
          "(e) A mobile payment app used for coffee and lunch.",
          "(f) A tax-filing app used once a year."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "App [letter]: [good front door / weak front door], because people use it\n"
               "[how often], so [what this means for other services in the app]."),
          tbox("WORKED EXAMPLE: TWO OTHER APPS",
               "App: food delivery used three times a week.\n"
               "Good front door, because people use it three times a week, so a grocery service inside it would be seen often.\n"
               "App: booking house movers.\n"
               "Weak front door, because people use it once every few years, so they would forget any other service in it.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "How often do people open it?",
      "<table><tr><th>APP</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) Messaging</td><td>Good</td><td>Every day</td></tr>"
      "<tr><td>(b) Wedding planning</td><td>Weak</td><td>Once or twice in a lifetime</td></tr>"
      "<tr><td>(c) Bus tickets</td><td>Good</td><td>Twice a day</td></tr>"
      "<tr><td>(d) Car buying</td><td>Weak</td><td>Once in several years</td></tr>"
      "<tr><td>(e) Mobile payments</td><td>Good</td><td>Several times a week</td></tr>"
      "<tr><td>(f) Tax filing</td><td>Weak</td><td>Once a year</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Which services pay for themselves? CityDay",
      "<table><tr><th>SERVICE (ONE MONTH)</th><th style=\"text-align:right\">REVENUE</th><th style=\"text-align:right\">DIRECT COSTS</th>"
      "<th style=\"text-align:right\">SUBSIDIES</th></tr>"
      '<tr><td>Rides</td><td class="num">$50,000</td><td class="num">$30,000</td><td class="num">$5,000</td></tr>'
      '<tr><td>Food delivery</td><td class="num">$40,000</td><td class="num">$30,000</td><td class="num">$15,000</td></tr>'
      '<tr><td>Groceries</td><td class="num">$20,000</td><td class="num">$16,000</td><td class="num">$2,000</td></tr>'
      '<tr><td>Movie tickets</td><td class="num">$5,000</td><td class="num">$2,000</td><td class="num">$6,000</td></tr></table>'
      '<div class="card" style="margin-top:.2in">' + ul([
          "<b>Step 1:</b> Contribution of each service (Tool 3), and the total.",
          "<b>Step 2:</b> For each service: keep, fix (cut subsidies), or stop. Use the template on the next slide."]) + "</div>",
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "[Service]: contribution $[amount]. Without subsidies it would be $[amount].\n"
               "We should [keep / fix / stop] it, because [Rule 4 reason, or how it helps the front door]."),
          tbox("WORKED EXAMPLE: LAUNDRY IN ANOTHER APP",
               "Laundry earns $8,000, costs $6,000, subsidies $3,000.\n"
               "Laundry: contribution -$1,000. Without subsidies it would be $2,000.\n"
               "We should fix it by cutting the subsidy step by step, because the service itself earns money "
               "and only the discounts make it lose (Rule 4).")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Two services pay their way; two need fixing",
      '<div class="card good">' + ul([
          "Rides = <b>$15,000</b>; food = <b>-$5,000</b>; groceries = <b>$2,000</b>; movie tickets = <b>-$3,000</b>; total = <b>$9,000</b>.",
          "Without subsidies: food would earn $10,000; movie tickets $3,000.",
          "Keep rides (the front door) and groceries.",
          "Fix food by cutting its $15,000 subsidy step by step (Rule 4).",
          "Fix or stop movie tickets: used rarely (Rule 1), and the subsidy is larger than the revenue."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "All at once, or one at a time? CampusGo's next 6 months",
      '<p class="statement">12,000 students / $24,000 monthly profit from rides</p>'
      + two(flexcard("Option A: Five services at once", "<p>Food, laundry, printing, tickets, and a wallet: <b>$80,000</b> to build, "
                     "plus <b>$10,000</b> a month of discounts.</p><p>Expect <b>30%</b> of students to use them, <b>$3</b> profit each a month.</p>",
                     "card", "ALL AT ONCE"),
            flexcard("Option B: One service at a time", "<p>Food delivery and a simple wallet: <b>$25,000</b>, discounts only in the first two months "
                     "(<b>$2,000</b> a month).</p><p>Expect <b>25%</b> to order food, <b>$2</b> profit each a month. Laundry only if food works.</p>",
                     "card", "ONE AT A TIME")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 2 and 3)",
      '<div class="card">' + ul([
          "Option A: users = 12,000 x 30% = ____; extra profit = users x $3 x 6 = $______; costs = $80,000 + 6 x $10,000 = $______; result = $______",
          "Option B: food users = 12,000 x 25% = ____; extra profit = users x $2 x 6 = $______; costs = $25,000 + 2 x $2,000 = $______; result = $______",
          "Option B if only 10% order food: result = $______",
          "Option A if only 15% use the new services: result = $______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Ama (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [founder name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next three months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "CityDay: fix food delivery",
      tmpl("To: Victor Lam, CEO, CityDay\n"
           "1. Decision and evidence: We should cut the food subsidy from $15,000 to $5,000 a month over three months, because food "
           "earns $10,000 before subsidies and should pay for itself (Rule 4).\n"
           "2. Biggest risk and trade-off: The weakest point is that some users may order less food. We give up some food orders to stop "
           "losing $5,000 a month.\n"
           "3. Next step and decision rule: In the next three months we will lower discounts step by step and measure weekly food orders. "
           "We will change this decision if orders fall by more than 30%."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "All at once loses even in its good case",
      '<div class="card">' + ul([
          "Option A: 3,600 users; $64,800 extra profit; costs $140,000; result = <b>-$75,200</b>.",
          "Option B: 3,000 food users; $36,000 extra profit; costs $29,000; result = <b>$7,000</b>.",
          "Option B with 10%: $14,400 - $29,000 = <b>-$14,600</b>.",
          "Option A with 15%: $32,400 - $140,000 = <b>-$107,600</b>.",
          "Option A loses money mostly because of discounts. Option B risks much less and shows whether students want food first."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Usually chooses Option B (Rules 2 and 4).",
          "Names a real risk: fewer students may order food than expected.",
          "Builds the wallet with a licensed partner (Rule 3).",
          'Gives a decision rule: "If fewer than 15% of students order food by month 3, we will not add laundry."']) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain a super-app and test whether a service can be its front door.</p></div>'
      '<div class="card"><div class="n">02</div><p>Calculate the contribution of each service with and without subsidies.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare adding services all at once with one at a time, and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Grab Holdings (2025, February 20). Grab reports fourth quarter and full year 2024 results.</p>'
      "<p class=\"ref\">South China Morning Post (2018). Tencent's WeChat hits 1 billion monthly active users.</p>"
      '<p class="ref">Reserve Bank of India (2024, January 31). Action against Paytm Payments Bank Ltd.</p>'
      '<p class="ref">Banking Dive (2022, February 1). Diem to end crypto project, sell its assets to Silvergate Bank for $182M.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
