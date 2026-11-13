"""Build the Session 4.1 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_4_1_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "4.1"
TITLE = "The Flywheel Strategy (Case Study: Amazon)"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


# Cover and situation
slide("MODULE 4 / REAL-WORLD CASE STUDIES &amp; STRATEGIC SYNTHESIS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_4_1_campusmart_flywheel_hanji.png" '
      'alt="Sofia, founder of CampusMart, asks which part of her flywheel to push first.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "CampusMart: loyal buyers, slow growth",
      '<p class="statement" style="font-weight:400;">CampusMart is Sofia\'s online store for student goods. It buys and stocks every '
      "product itself, so it adds only a few products a month. Her marketing manager wants to spend $20,000 on ads; small campus "
      "shops ask to sell on CampusMart.</p>"
      "<table><tr><th>CAMPUSMART (ONE MONTH)</th><th style=\"text-align:right\">VALUE</th></tr>"
      '<tr><td>Buyers</td><td class="num">4,000</td></tr>'
      '<tr><td>Products for sale (all stocked by CampusMart)</td><td class="num">300</td></tr>'
      '<tr><td>Average order / profit per order (10%)</td><td class="num">$25 / $2.50</td></tr>'
      '<tr><td>Monthly profit (4,000 x $2.50)</td><td class="num">$10,000</td></tr>'
      '<tr><td>Delivery time</td><td class="num">3 days</td></tr>'
      '<tr><td>Money to invest</td><td class="num">$20,000</td></tr></table>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", "What is the Flywheel Strategy?",
      '<p class="para">A business is built as <b>a loop in which each part pushes the next</b>. A flywheel is a heavy wheel: hard to start, '
      "but each push makes it spin faster. Amazon's loop: <b>lower prices and more choice bring more buyers; more buyers attract more "
      "sellers; more sellers add choice; growing sales lower costs, so prices fall again.</b> Instead of paying again and again for "
      "growth, the company invests in the parts of the loop that keep turning on their own.</p>"
      '<div class="takeaway">Use it when growth in one part really makes another part better, and you have enough money to keep '
      "pushing until the wheel turns by itself.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Flywheel, marketplace, seller fee",
      term("Flywheel", "A loop of business steps in which each step makes the next one stronger.",
           "more buyers, then more sellers, then more choice, then more buyers.")
      + term("Marketplace", "An online store where outside sellers sell their own products, and the owner earns a fee.",
             "small campus shops sell their own products on CampusMart.")
      + term("Seller fee<br><span style=\"font-size:24px;color:#526174;\">(commission)</span>",
             "The share of each sale that the marketplace keeps.", "a $20 lamp; CampusMart keeps 10%, or $2."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Economies of scale, cross-subsidy, retention",
      term("Economies of scale", "Lower cost per unit when a business grows.",
           "shipping 100 boxes a day costs less per box than shipping 10.")
      + term("Cross-subsidy", "Using profit from one part of a business to pay for another part that is still losing money or growing.",
             "Amazon used profit from its cloud business to support its online shops.")
      + term("Retention", "The share of customers who keep buying after their first purchase.",
             "600 of 2,000 new buyers order again: 600 / 2,000 x 100 = 30%."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 2")

# Rules
rules = [
    ("Rule 1", "Draw your loop, and check each arrow",
     "Write the loop as arrows. For each arrow, ask: does more of this really lead to more of the next?",
     "More buyers bring more outside sellers, because sellers want customers. More sellers add products. More products bring more buyers.",
     'Drawing a loop with a weak arrow, such as "more buyers lead to lower prices" when the business is too small to get better prices.'),
    ("Rule 2", "Push the step that turns the whole wheel",
     "Usually this is what customers feel: lower prices, more choice, or faster delivery. Spending there helps every other step.",
     "Opening CampusMart to outside sellers adds hundreds of products without CampusMart buying any stock. More choice turns the whole loop.",
     "Spending on ads that bring buyers for one month only. The wheel moves once and stops when the ads stop."),
    ("Rule 3", "Turn growth into lower costs, and give the savings back",
     "As the wheel spins, use the savings to lower prices or speed up delivery. That makes the wheel spin faster.",
     "When CampusMart ships 300 orders a day instead of 130, delivery costs less per order, so Sofia offers next-day delivery.",
     "Keeping all the savings as profit too early. Customers see no improvement, and the wheel slows down."),
    ("Rule 4", "Pay for the wheel with steady profit",
     "A flywheel is slow at first. Fund it from a profitable part of the business, not only with borrowed money or discounts, and know how long you can wait.",
     "CampusMart's own product sales earn $10,000 a month. Sofia uses part of this profit to support the marketplace until seller fees grow.",
     "Paying for growth with huge discounts funded by investors. When the money runs out, buyers who came for discounts leave."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_4_1_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "Amazon", "good",
     "In 2001, Jeff Bezos sketched Amazon's flywheel. Amazon opened its store to outside sellers; by 2023 they sold about 60% of the units "
     "on Amazon. It launched Prime in 2005 ($79 a year for free two-day shipping). In 2022, Amazon's online shops lost about "
     "$10.6 billion, but AWS, its cloud business, earned about $22.8 billion of operating profit and kept Amazon profitable.",
     ["Each step feeds the next: buyers bring sellers, sellers bring choice. <b>(Rule 1)</b>",
      "Invested in what customers feel: choice, price, fast delivery. <b>(Rule 2)</b>",
      "AWS profit paid for the retail wheel in hard years. <b>(Rule 4)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "Costco", "good",
     "Costco charges a yearly membership fee and keeps prices low: it limits how much it adds to the cost of most products (about 14 to 15%). "
     "About 90% of members worldwide renew each year. Membership fees brought in about $5.3 billion in fiscal 2025.",
     ["Low prices bring members; members give buying power; buying power lowers prices. <b>(Rule 1)</b>",
      "Gives savings back to members instead of raising margins. <b>(Rule 3)</b>",
      "Steady membership fees pay for the low prices. <b>(Rule 4)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Jet.com", "bad",
     "Jet.com launched in 2015 as an online store that promised lower prices than Amazon. It spent heavily on discounts and marketing, "
     "funded by investors. Walmart bought it in 2016 for about $3.3 billion. Sales did not keep growing, and Walmart shut Jet.com down in 2020.",
     ["Low prices came from investor money, not from savings the loop created. <b>(Rule 3)</b>",
      "Buyers came for discounts and did not stay. <b>(Rule 4)</b>",
      "Never built its own strong loop of sellers and loyal members. <b>(Rule 1)</b>"], "Why it is bad"),
    ("BAD EXAMPLE 2", "ofo bike sharing", "bad",
     "ofo, a Chinese bike-sharing company, put millions of bikes on city streets and offered very cheap rides, paid for with investors' money. "
     "More bikes did not lower its costs: many were broken or lost. In December 2018, more than 10 million users asked for their deposits "
     "back, and ofo could not pay them all.",
     ["More bikes created more costs, so \"growth lowers costs\" was broken. <b>(Rule 1)</b>",
      "Cheap rides were paid for with investors' money, not steady profit. <b>(Rule 4)</b>",
      "When the money ran out, users lost trust and the wheel stopped."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Amazon</td><td style="color:#2f6b47;font-weight:700">Good</td><td>A real loop, funded by AWS profit (Rules 1 and 4)</td></tr>'
      '<tr><td>Costco</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Savings go back to members (Rule 3)</td></tr>'
      '<tr><td>Jet.com</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Low prices bought with investor money (Rules 3 and 4)</td></tr>'
      '<tr><td>ofo</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Growth raised costs instead of lowering them (Rule 1)</td></tr></table>'
      '<div class="takeaway">A real flywheel keeps turning after you stop paying for it.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: The loop check",
      two(flexcard("How to check", '<p>Write each step of the loop, and for each arrow write "because ..."</p>'
                   "<p>If you cannot finish the sentence, the arrow is weak.</p>", "card", "USED IN EXERCISES 1 AND 2"),
          flexcard("Example: a ride app", ul([
              '"More riders lead to more drivers, because drivers earn more where there are more riders." Strong.',
              '"More drivers lead to lower costs, because ..." If you cannot say why, the arrow is weak.']),
              "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Value of buyers who stay",
      two(flexcard("Formula", "<p>Extra profit = new buyers who stay x profit per buyer per month x number of months</p>",
                   "card", "USED IN EXERCISE 3"),
          flexcard("Example: ads", ul([
              "Ads bring 1,000 new buyers; 20% stay: 200 buyers.",
              "Each brings $3 profit a month.",
              "Over 6 months: 200 x $3 x 6 = $3,600."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Profit over several periods (from Session 3.1)",
      two(flexcard("Formula", "<p>Profit = extra profit per period x number of periods - one-time cost</p>", "card", "USED IN EXERCISE 3"),
          flexcard("Example", ul([
              "A $5,000 investment adds $1,500 profit a month.",
              "After 6 months: 6 x $1,500 - $5,000 = $4,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 50 outside sellers join in the first three months, we will lower the seller fee."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Is the loop real?",
      '<p class="statement">Six companies describe one arrow of their loop:</p><div class="card">' + ul([
          "(a) A food delivery app: more restaurants lead to more customers.",
          "(b) A video site: more viewers lead to more video makers.",
          "(c) A bakery: more customers lead to lower flour prices from its supplier (it buys 20 kg a week).",
          "(d) A language app: more learners lead to more practice data, which makes lessons better.",
          "(e) A clothing shop: more ads lead to more loyal customers.",
          "(f) A marketplace: more sellers lead to lower prices, because sellers compete."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Arrow [letter]: [strong / weak], because [why more of the first step really leads,\n"
               "or does not lead, to more of the next step]."),
          tbox("WORKED EXAMPLE: TWO OTHER ARROWS",
               "Arrow: a ride app: more riders lead to more drivers.\n"
               "Strong, because drivers earn more and wait less where there are more riders.\n"
               "Arrow: a small cafe: more customers lead to faster coffee.\n"
               "Weak, because more customers make the line longer, not faster.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Can you finish the \"because\" sentence?",
      "<table><tr><th>ARROW</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) Restaurants to customers</td><td>Strong</td><td>More choice brings more customers</td></tr>"
      "<tr><td>(b) Viewers to video makers</td><td>Strong</td><td>Makers go where the viewers are</td></tr>"
      "<tr><td>(c) Bakery flour prices</td><td>Weak</td><td>20 kg a week is too little to get better prices</td></tr>"
      "<tr><td>(d) Learners to better lessons</td><td>Strong</td><td>More practice data improves lessons (Session 2.1)</td></tr>"
      "<tr><td>(e) Ads to loyal customers</td><td>Weak</td><td>Loyalty comes from products; ads stop</td></tr>"
      "<tr><td>(f) Sellers to lower prices</td><td>Strong</td><td>Competing sellers lower prices</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Draw a flywheel and find the step to push: StayLocal",
      two(flexcard("Scenario", ul([
          "Students rent rooms from local home owners for short stays: <b>2,000</b> renters, <b>150</b> home owners.",
          "Renters complain that there are too few rooms.",
          "Home owners would list rooms if they could find renters easily.",
          "<b>$6,000</b> for one option: (1) ads to renters, (2) free photos for new home owners' rooms, "
          "(3) a 10% discount for every renter for one month."])),
          flexcard("Your steps", ul([
              '<b>Step 1:</b> Draw four steps of the loop, with a "because" sentence for each arrow (Tool 1).',
              "<b>Step 2:</b> Choose the push with the template on the next slide."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Our loop: [step 1] -> [step 2] -> [step 3] -> [step 4] -> back to [step 1].\n"
               "The weakest step today is [step], because [evidence from the scenario].\n"
               "We should spend on [option], because it [how it pushes the weakest step and then the whole loop] (Rule 2).\n"
               "We should not spend on [option], because [why its effect stops] (Rule 2 or Rule 4)."),
          tbox("WORKED EXAMPLE: A HOMEWORK-HELP APP",
               "Our loop: more students -> more questions -> more paid answers for tutors -> more tutors -> faster answers -> more students.\n"
               "The weakest step today is tutors, because students wait 2 hours for an answer.\n"
               "We should spend on a bonus for tutors' first 10 answers, because faster answers bring more students (Rule 2).\n"
               "We should not spend on student ads, because new students would wait even longer and leave.")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Push the weakest step: rooms",
      '<div class="card good">' + ul([
          "<b>Loop:</b> more rooms -> more renters -> more income for home owners -> more home owners list rooms -> more rooms.",
          "<b>Weakest step:</b> the number of rooms (renters complain there are too few).",
          "<b>Best push:</b> option (2), free photos for new home owners: more and better rooms bring renters, and renters bring home owners (Rule 2).",
          "<b>Not (1):</b> more renters for too few rooms, so they leave.",
          "<b>Not (3):</b> helps for one month and stops when the discount ends (Rule 4)."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Ads or the flywheel? CampusMart's next 6 months",
      '<p class="statement">4,000 buyers / $2.50 profit per order / one order per buyer per month / $20,000 to invest</p>'
      + two(flexcard("Option A: Ads", "<p>Spend <b>$20,000</b> on ads: <b>2,000</b> new buyers in month 1.</p>"
                     "<p><b>30%</b> of them keep ordering every month after that.</p>", "card", "ONE-TIME PUSH"),
            flexcard("Option B: Open a marketplace", "<p>Spend <b>$20,000</b> to build it. <b>100</b> sellers add <b>3,000</b> products; "
                     "their sales are <b>$30,000</b> a month, with a <b>10%</b> fee.</p>"
                     "<p>More choice adds <b>300</b> more buyers every month: 300, 600, ... up to 1,800 in month 6.</p>",
                     "card", "FLYWHEEL")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 2 and 3)",
      '<div class="card">' + ul([
          "Option A: month 1 = 2,000 x $2.50 = $______; buyers who stay = 2,000 x 30% = ____; "
          "months 2 to 6 = stayers x $2.50 x 5 = $______; result = month 1 + months 2 to 6 - $20,000 = $______",
          "Option B: fees = $30,000 x 10% x 6 = $______; buyer-months = 300 + 600 + 900 + 1,200 + 1,500 + 1,800 = ____; "
          "profit = buyer-months x $2.50 = $______; result = fees + profit - $20,000 = $______",
          "Option B if only 20 sellers join: fees = $600 a month; extra buyers 100, 200, ..., 600. Result = $______",
          "In month 7, which plan still brings new buyers? ____"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Sofia (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [founder name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next three months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "StayLocal: where to spend $6,000?",
      tmpl("To: Ben Ortiz, founder, StayLocal\n"
           "1. Decision and evidence: We should spend $6,000 on free photos for new home owners, because rooms are the weakest step "
           "of our loop (Rule 2): renters already complain that there are too few rooms.\n"
           "2. Biggest risk and trade-off: The weakest point is that home owners may not list rooms even with free photos. We give up "
           "a quick rise in renters from ads to fix the step that turns the whole wheel.\n"
           "3. Next step and decision rule: In the next three months we will offer photos to 100 home owners and count new rooms. "
           "We will change this decision if fewer than 40 new rooms are listed."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Ads stop; the flywheel keeps turning, if sellers come",
      '<div class="card">' + ul([
          "Option A: month 1 = <b>$5,000</b>; 600 stay; months 2 to 6 = <b>$7,500</b>; result = <b>-$7,500</b>.",
          "Option B: fees = <b>$18,000</b>; 6,300 buyer-months = <b>$15,750</b>; result = <b>$13,750</b>.",
          "Option B with only 20 sellers: $3,600 + $5,250 - $20,000 = <b>-$11,150</b>.",
          "In month 7, only Option B still brings new buyers. Option A's effect stops when the ads stop."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Usually chooses Option B (Rules 1 and 2).",
          "Names the real risk: too few sellers may join.",
          "Plans to support the marketplace with profit from CampusMart's own sales (Rule 4).",
          'Gives a decision rule: "If fewer than 50 sellers join in the first three months, we will lower the seller fee or help sellers list products."']) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      "<div class=\"card\"><div class=\"n\">01</div><p>Draw a business's flywheel and check each arrow.</p></div>"
      '<div class="card"><div class="n">02</div><p>Find the step that turns the whole wheel.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare a one-time push with an investment in the loop and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Collins, J. (2019). Turning the Flywheel. Harper Business.</p>'
      '<p class="ref">Amazon.com, Inc. (2023). Form 10-K for fiscal year 2022. Segment operating income.</p>'
      '<p class="ref">Marketplace Pulse. Amazon third-party seller share.</p>'
      '<p class="ref">Costco Wholesale Corporation (2025). Form 10-K for fiscal year 2025.</p>'
      '<p class="ref">Axios (2020, May 20). Walmart grounds Jet.com. Caixin Global (2018, December 17). Riders go to ofo in search of refunds.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
