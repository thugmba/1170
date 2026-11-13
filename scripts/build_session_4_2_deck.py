"""Build the Session 4.2 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_4_2_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "4.2"
TITLE = "The Ecosystem Lock-In Strategy (Case Study: Apple)"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


# Cover and situation
slide("MODULE 4 / REAL-WORLD CASE STUDIES &amp; STRATEGIC SYNTHESIS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_4_2_pulsefit_lockin_hanji.png" '
      'alt="Noah, founder of PulseFit, asks how to make customers want to stay.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "PulseFit: customers like the band, then buy a rival's",
      '<p class="statement" style="font-weight:400;">PulseFit is Noah\'s fitness-band company. A teammate suggests a quick fix: '
      'make it impossible to move step and sleep history out of the app, so customers "cannot leave."</p>'
      "<table><tr><th>PULSEFIT</th><th style=\"text-align:right\">VALUE</th></tr>"
      '<tr><td>Customers who own a PulseFit band</td><td class="num">10,000</td></tr>'
      '<tr><td>Price of a band / profit per band</td><td class="num">$60 / $20</td></tr>'
      '<tr><td>Time until a band wears out</td><td class="num">About 2 years</td></tr>'
      '<tr><td>Customers who buy their next band from PulseFit</td><td class="num">40%</td></tr>'
      '<tr><td>Customers who switch to a rival\'s band</td><td class="num">60%</td></tr>'
      '<tr><td>Other PulseFit products or services</td><td class="num">None</td></tr></table>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", "What is the Ecosystem Lock-In Strategy?",
      '<p class="para">A company keeps customers by making its <b>products and services work better together than with anything else</b>. '
      "They share one account, one set of data, and one design, so each extra product makes the others more useful, and leaving would "
      "cost the customer convenience, data, or benefits. The company then earns <b>steady money from services</b> on top of the products. "
      "Apple is the best-known example.</p>"
      '<div class="takeaway">It works only when customers stay because of value. When a company traps customers or treats partners '
      "unfairly, customers and regulators push back.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Ecosystem, lock-in, switching cost",
      term("Ecosystem<br><span style=\"font-size:24px;color:#526174;\">(of products)</span>",
           "A company's products and services that share one account, one set of data, and one design.",
           "a PulseFit band, scale, and app.")
      + term("Lock-in", "When customers keep buying from one company because leaving would cost them something.",
             "two years of sleep history are in the PulseFit app.")
      + term("Switching cost", "What a customer loses by moving to a rival: money, time, data, or benefits.",
             "buying a new scale, learning a new app, losing rewards points."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Services revenue, lifetime value, regulator",
      term("Services revenue", "Money earned again and again from services, such as subscriptions, on top of products.",
           "$5 a month for PulseFit Plus training plans.")
      + term("Customer lifetime value<br><span style=\"font-size:24px;color:#526174;\">(CLV)</span>",
             "The total profit from one customer during all the years the customer stays.", "$20 a year for 3 years = $60.")
      + term("Regulator", "A government body that makes sure companies follow the law and compete fairly.",
             "the European Commission."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 2")

# Rules
rules = [
    ("Rule 1", "Make each product better when it is used with the others",
     "The customer should feel a clear benefit every time two of your products work together.",
     "When a customer steps on a PulseFit scale, the band and the app combine weight, steps, and sleep into one weekly health report.",
     "Selling many products that only share a logo. If they do not work better together, customers buy each from whoever is cheapest."),
    ("Rule 2", "Earn steady service revenue from the customers you already have",
     "Products are sold once; services earn money every month and keep customers using the ecosystem.",
     "PulseFit Plus costs $5 a month for training plans and sleep coaching that use the band's data.",
     "Adding a service customers do not value, just to charge a monthly fee. Customers cancel and feel tricked."),
    ("Rule 3", "Keep customers with value, not with traps",
     "Customers should stay because the ecosystem is better, not because leaving is made painful. Let them take their own data.",
     "PulseFit lets customers download their full history at any time, and most still stay, because the combined report is useful.",
     "Blocking data export or making other brands' accessories stop working. Customers feel trapped and new buyers stay away."),
    ("Rule 4", "Play fair with partners, and expect regulators to watch",
     "When many customers depend on your ecosystem, you have power over other companies. Using it unfairly brings fines and new laws.",
     "PulseFit lets other workout apps read band data with the customer's permission, and charges them a small, clear fee.",
     "Blocking partners from telling customers about cheaper offers, or charging very high fees because partners have no other way in."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_4_2_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "Apple", "good",
     "An iPhone, a Mac, an iPad, an Apple Watch, and AirPods share one Apple account; photos, messages, and files appear on every device "
     "through iCloud. In early 2024, Apple said it had more than 2.2 billion active devices. In fiscal 2024, its services earned "
     "$96.2 billion, with a gross margin of about 74%, far higher than its hardware.",
     ["Each product works better with the others. <b>(Rule 1)</b>",
      "Services earn money every month from billions of devices. <b>(Rule 2)</b>",
      "Many customers stay because it is easy, not because they cannot leave. <b>(Rule 3)</b>",
      "<i>Lesson:</i> its App Store rules have been challenged by regulators (Bad example 2). <b>(Rule 4)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "Starbucks Rewards", "good",
     "The Starbucks app combines ordering ahead, paying, and collecting stars for free drinks. At the end of 2023, Starbucks had "
     "34.3 million active Rewards members in the United States, and payments through the program made up about 59% of sales in its "
     "U.S. company-operated stores.",
     ["Ordering, paying, and rewards work together in one app. <b>(Rule 1)</b>",
      "Money in the app and collected stars bring customers back. <b>(Rule 2)</b>",
      "Customers stay for convenience and free drinks: value, not a trap. <b>(Rule 3)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "HP printer ink", "bad",
     "In September 2016, a software update to some HP printers made other companies' ink cartridges stop working; printers said the "
     "cartridges were \"damaged.\" After many complaints, HP offered an optional update to remove the block. In the United States, a court "
     "approved a $1.5 million settlement in 2019, and later settlements followed in Europe.",
     ["Tried to keep customers with a trap, not with better ink. <b>(Rule 3)</b>",
      "Customers felt tricked and lost trust in the brand.",
      "Courts and consumer groups stepped in. <b>(Rule 4)</b>"], "Why it is bad"),
    ("BAD EXAMPLE 2", "Apple and music streaming apps in Europe", "bad",
     "Apple's App Store rules stopped music streaming apps, such as Spotify, from telling iPhone users inside the app that they could pay "
     "less on the app's own website. In March 2024, the European Commission fined Apple more than €1.8 billion and ordered it to remove "
     "these rules.",
     ["Used its control over the iPhone to limit partners unfairly. <b>(Rule 4)</b>",
      "Kept customers from finding better prices: a trap, not value. <b>(Rule 3)</b>",
      "Even a very successful ecosystem faces fines when it treats partners unfairly."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Apple devices and services</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Better together, plus services (Rules 1 and 2)</td></tr>'
      '<tr><td>Starbucks Rewards</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Customers stay for value (Rule 3)</td></tr>'
      '<tr><td>HP printer ink</td><td style="color:#991b1b;font-weight:700">Bad</td><td>A trap instead of value (Rule 3)</td></tr>'
      '<tr><td>Apple App Store in Europe</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Unfair rules for partners (Rule 4)</td></tr></table>'
      '<div class="takeaway">Lock customers in with value they would miss, never with doors they cannot open.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Customer lifetime value (CLV)",
      two(flexcard("Formula", "<p>CLV = profit per customer per year x years the customer stays</p>", "card", "USED IN EXERCISE 2"),
          flexcard("Example: phone cases", ul([
              "Case only: $10 a year for 2 years = $20.",
              "Case plus a $3-a-month care plan: $40 a year for 4 years = $160."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Value of customers who come back",
      two(flexcard("Formula", "<p>Profit from repeat buyers = customers x repeat rate x profit per purchase</p>",
                   "card", "USED IN EXERCISE 3"),
          flexcard("Example", ul([
              "5,000 customers; 50% buy again; $20 profit each.",
              "5,000 x 50% x $20 = $50,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Profit over several periods (from Session 3.1)",
      two(flexcard("Formula", "<p>Profit = monthly profit x number of months - one-time cost</p>", "card", "USED IN EXERCISE 3"),
          flexcard("Example: an app update", ul([
              "Costs $30,000; adds $2,000 profit a month.",
              "After 24 months: 24 x $2,000 - $30,000 = $18,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 5% of band owners subscribe to PulseFit Plus in six months, we will change the plan."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Value or trap?",
      '<p class="statement">Six companies try to keep customers:</p><div class="card">' + ul([
          "(a) A phone's photos appear on the same company's laptop automatically.",
          "(b) A printer stops working with other brands' ink.",
          "(c) A coffee app gives stars that customers trade for free drinks.",
          "(d) A gym charges $200 to cancel a membership.",
          "(e) A music app lets users export their playlists to other apps.",
          '(f) A cloud storage company hides the "delete account" button behind 12 steps.']) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Move [letter]: [lock-in by value / lock-in by trap], because customers stay\n"
               "[because they get a benefit: which one / because leaving is made hard: how]."),
          tbox("WORKED EXAMPLE: TWO OTHER MOVES",
               "Move: a smartwatch unlocks the same company's laptop when the user sits down.\n"
               "Lock-in by value, because customers save time every day.\n"
               "Move: an airline makes miles expire if a customer flies with another airline once.\n"
               "Lock-in by trap, because customers are punished for trying a rival.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Do customers stay for a benefit, or because leaving is hard?",
      "<table><tr><th>MOVE</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) Photos on the laptop</td><td>Value</td><td>Products work better together</td></tr>"
      "<tr><td>(b) Blocks other ink</td><td>Trap</td><td>Other brands are blocked</td></tr>"
      "<tr><td>(c) Stars for free drinks</td><td>Value</td><td>A real reward</td></tr>"
      "<tr><td>(d) $200 to cancel</td><td>Trap</td><td>Leaving is made expensive</td></tr>"
      "<tr><td>(e) Export playlists</td><td>Value</td><td>Customers who stay do so by choice</td></tr>"
      "<tr><td>(f) Hidden delete button</td><td>Trap</td><td>Leaving is made hard on purpose</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "What is a customer in the ecosystem worth? ChefBox",
      two(flexcard("Scenario", ul([
          "Blender only: <b>$15</b> profit a year, stays <b>2</b> years.",
          "Blender plus a recipe app that controls it ($4 a month): <b>$40</b> profit a year, stays <b>5</b> years.",
          "Idea: a <b>$25</b> coupon for the first year of the app for every blender owner."])),
          flexcard("Your steps", ul([
              "<b>Step 1:</b> CLV blender only = $15 x 2 = $____. CLV blender and app = $40 x 5 = $____. "
              "Gain per customer moved = $____ - $____ - $25 = $____.",
              "<b>Step 2:</b> Value or trap? Which rule does the app follow?",
              "<b>Step 3:</b> Recommend with the template."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "A customer who uses [products] is worth $[CLV], against $[CLV] for [one product only].\n"
               "After the cost of $[cost], each customer we move gains us $[amount].\n"
               "This is lock-in by [value / trap], because [reason] (Rule [number]).\n"
               "We should [offer / not offer] the [plan], and measure [one number]."),
          tbox("WORKED EXAMPLE: PHONE CASES (TOOL 1)",
               "A customer who uses the case and the care plan is worth $160, against $20 for the case only.\n"
               "After the cost of a $15 first-month discount, each customer we move gains us $125.\n"
               "This is lock-in by value, because the plan replaces broken cases quickly (Rule 1).\n"
               "We should offer the discount, and measure how many keep the plan after 3 months.")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Each customer moved into the ecosystem gains $145",
      '<div class="card good">' + ul([
          "CLV blender only = <b>$30</b>; CLV blender and app = <b>$200</b>.",
          "Gain per customer = $200 - $30 - $25 = <b>$145</b>.",
          "Lock-in by value: the app makes the blender more useful (Rules 1 and 2), and the blender still works without it (Rule 3).",
          "A strong answer offers the coupon and measures how many coupon users keep paying after the first year."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Trap or ecosystem? PulseFit's next two years",
      '<p class="statement">10,000 band owners / $20 profit per band / no change: 40% buy their next band from PulseFit</p>'
      + two(flexcard("Option A: Lock the data", "<p>Block customers from moving their history. Expect <b>60%</b> to buy their next band from PulseFit.</p>"
                     "<p>Angry reviews cost <b>2,000</b> new buyers ($20 each). No extra cost.</p>", "card", "TRAP"),
            flexcard("Option B: Build the ecosystem", "<p><b>$50,000</b> for PulseFit Plus ($5 a month, <b>$4</b> profit) and a smart scale "
                     "(<b>$15</b> profit); data export stays open.</p><p>Expect <b>70%</b> to buy the next band, <b>1,000</b> subscribers "
                     "for 24 months, <b>1,000</b> scales.</p>", "card", "VALUE")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 2 and 3)",
      '<div class="card">' + ul([
          "No change: 10,000 x 40% x $20 = $______",
          "Option A: 10,000 x 60% x $20 = $______; minus 2,000 x $20 = $______; result = $______",
          "Option B: bands = 10,000 x 70% x $20 = $______; Plus = 1,000 x $4 x 24 = $______; scales = 1,000 x $15 = $______; "
          "result = bands + Plus + scales - $50,000 = $______",
          "Option B if only 300 subscribe, 300 buy a scale, and 50% buy the next band: result = $______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Noah (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [founder name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next six months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "ChefBox: offer the recipe-app coupon?",
      tmpl("To: Ana Ruiz, CEO, ChefBox\n"
           "1. Decision and evidence: We should give every blender owner a $25 coupon for the recipe app, because a customer who uses "
           "both is worth $200 against $30 for the blender alone (Rules 1 and 2).\n"
           "2. Biggest risk and trade-off: The weakest point is that many coupon users may stop paying after the first year. We give up "
           "$25 per customer now to build customers who stay five years.\n"
           "3. Next step and decision rule: In the next six months we will send the coupon to 1,000 owners and measure how many still "
           "pay after month 12. We will change this decision if fewer than 30% keep paying."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "The trap earns nothing extra; the ecosystem earns more",
      '<div class="card">' + ul([
          "No change: <b>$80,000</b>.",
          "Option A: $120,000 - $40,000 = <b>$80,000</b>: no more than doing nothing, and it damages trust (Rule 3).",
          "Option B: $140,000 + $96,000 + $15,000 - $50,000 = <b>$201,000</b>.",
          "Option B weak case: $100,000 + $28,800 + $4,500 - $50,000 = <b>$83,300</b>, still slightly above doing nothing."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Chooses Option B (Rules 1, 2, and 3).",
          "Names a real risk: few owners may pay for PulseFit Plus.",
          "Keeps data export open.",
          'Gives a decision rule: "If fewer than 5% of owners subscribe in six months, we will improve the training plans or lower the price."']) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain lock-in and switching costs, and tell value lock-in from trap lock-in.</p></div>'
      '<div class="card"><div class="n">02</div><p>Calculate customer lifetime value inside and outside an ecosystem.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare a trap plan with an ecosystem plan and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Shapiro, C., &amp; Varian, H. R. (1999). Information Rules (Chapter 5). Harvard Business School Press.</p>'
      '<p class="ref">Apple Inc. (2024). Apple reports fourth quarter results. Fiscal 2024 services.</p>'
      '<p class="ref">Starbucks Corporation (2024). Q1 fiscal 2024 earnings call.</p>'
      '<p class="ref">The Register (2018, September 21). HP should pay out $1.5m for printer-bricking update.</p>'
      '<p class="ref">European Commission (2024, March 4). Commission fines Apple over €1.8 billion over App Store rules for music streaming.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
