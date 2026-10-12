"""Build the Session 2.3 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_2_3_deck.py
Reuses the Session 2.1 deck style. Writes slides/session_2_3_lecture.html and
renders slides/session_2_3_lecture.pdf with WeasyPrint.
"""
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import CSS, card, ul, tmpl  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
HTML_OUT = ROOT / "slides" / "session_2_3_lecture.html"
PDF_OUT = ROOT / "slides" / "session_2_3_lecture.pdf"

slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


def two(left, right):
    return '<div style="display:flex;gap:.26in;align-items:flex-start;">' + left + right + "</div>"


def flexcard(heading, inner, cls="card", label=None):
    return card(heading, inner, cls + '" style="flex:1', label)


# 1. Cover
slide("MODULE 2 / PLATFORM ECONOMICS, BIG DATA &amp; MONETIZATION",
      "Session 2.3: The Up-Sell and Cross-Sell Strategy",
      '<img class="hero" src="../assets/session_2_3_studynest_pricing_hanji.png" '
      'alt="Hana, founder of StudyNest, looks at her pricing table and asks how to earn more without losing students.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

# 2. Situation
slide("THE SITUATION", "StudyNest: many users, but costs are higher than revenue",
      '<p class="statement" style="font-weight:400;">StudyNest is a note-taking and study app for university students. '
      'Students can use it for free or pay for more storage and study tools. Hana is its founder.</p>'
      "<table><tr><th>PLAN</th><th>WHAT IT GIVES</th><th style=\"text-align:right\">PRICE / MONTH</th><th style=\"text-align:right\">USERS</th></tr>"
      '<tr><td>Free</td><td>500 MB of notes storage</td><td class="num">$0</td><td class="num">20,000</td></tr>'
      '<tr><td>Plus</td><td>10 GB storage, exam planner</td><td class="num">$4.00</td><td class="num">1,000</td></tr>'
      '<tr><td>Pro</td><td>Unlimited storage, exam planner, group study rooms</td><td class="num">$9.00</td><td class="num">200</td></tr></table>'
      '<div class="takeaway">Revenue = 1,000 x $4.00 + 200 x $9.00 = $5,800 a month. Costs = $9,000. StudyNest loses $3,200 a month. '
      'A teammate says: "Raise all prices 30%." Hana worries that students will leave.</div>',
      "SESSION 2.3 / FICTIONAL CLASS DATA")

# 3. Strategy paragraph
slide("THE STRATEGY IN ONE PARAGRAPH", "What is the Up-Sell and Cross-Sell Strategy?",
      '<p class="para">Earn more from customers who already use a product by offering them <b>more value</b>, '
      "not by charging everyone more for the same thing. <b>Up-selling</b> offers a higher, better version of what the customer "
      "already uses. <b>Cross-selling</b> offers a related product that helps the customer finish the same goal. Both work only "
      "when the price matches the value the customer sees and the offer comes at the right moment.</p>"
      '<div class="takeaway">Use it when many customers use a product but few pay, or when a company wants more revenue '
      "without simply raising prices for everyone.</div>",
      "SESSION 2.3 / STRATEGY OVERVIEW")

# 4-5. Words
slide("WORDS YOU NEED FIRST", "Price tier and willingness to pay",
      '<div class="term"><strong>Price tier</strong><span>One level of a product at one price.<br><em>Example: StudyNest has Free, Plus, and Pro.</em></span></div>'
      '<div class="term"><strong>Willingness to pay</strong><span>The highest price a customer would accept for something they value.<br>'
      "<em>Example: a student who saves 3 hours a week may pay $4.00 a month, but not $15.00.</em></span></div>",
      "SESSION 2.3 / KEY TERMS 1 OF 3")

slide("WORDS YOU NEED FIRST", "Up-sell and cross-sell",
      '<div class="term"><strong>Up-sell</strong><span>Offering a higher tier or bigger version of the same product.<br>'
      "<em>Example: a free user who runs out of storage is offered Plus.</em></span></div>"
      '<div class="term"><strong>Cross-sell</strong><span>Offering a different but related product.<br>'
      "<em>Example: a Plus user is offered an exam note pack for $6.00.</em></span></div>",
      "SESSION 2.3 / KEY TERMS 2 OF 3")

slide("WORDS YOU NEED FIRST", "Two rates that measure the strategy",
      '<div class="term"><strong>Conversion rate<br><span style="font-size:24px;color:#526174;">(upgrade rate)</span></strong>'
      "<span>The percentage of users who move to a paid tier.<br>Conversion rate = users who upgraded / users who could upgrade x 100<br>"
      "<em>Example: 1,000 / 20,000 x 100 = 5%.</em></span></div>"
      '<div class="term"><strong>Attach rate</strong><span>The percentage of customers who also buy the cross-sold product.<br>'
      "Attach rate = buyers of the add-on / customers who saw the offer x 100<br>"
      "<em>Example: 30 of 200 Pro users buy the exam pack: 30 / 200 x 100 = 15%.</em></span></div>",
      "SESSION 2.3 / KEY TERMS 3 OF 3")

# 6-9. Rules
rules = [
    ("Rule 1", "Price by the value the customer sees",
     "Ask what problem each tier solves and how much that is worth to the customer, not only what it costs you.",
     "The exam planner saves a student about 3 hours a week before exams. That value explains why students pay $4.00 for Plus, even though storage costs StudyNest very little.",
     "Raising every price by the same amount because costs went up. Customers do not see more value, so many leave."),
    ("Rule 2", "Build tiers for different customer groups",
     "Good, better, best: a free tier to try, a middle tier for most paying customers, a top tier for heavy users.",
     "Free for students who take a few notes, Plus for students preparing for exams, Pro for study groups. The middle tier often sells best because it looks like good value next to the top tier.",
     "Tiers that are too similar, so customers cannot see why to pay more, or so many tiers that customers get confused."),
    ("Rule 3", "Up-sell at the moment of need, and show the extra value",
     "The best time to offer a higher tier is when the customer feels the limit of the current tier.",
     'When a free user\'s storage is full: "Your notes are full. Plus gives you 20 times more space and an exam planner for $4.00 a month."',
     "Showing upgrade pop-ups to every new user on the first day, before they know whether the app is useful."),
    ("Rule 4", "Cross-sell what helps the customer finish the same goal",
     "A good cross-sell feels like help, not like an extra sales push.",
     "In the two weeks before exams, StudyNest offers Plus and Pro users an exam note pack for $6.00. It fits what they are already trying to do.",
     "Offering unrelated products, such as phone cases in a study app, or pushing products customers do not need just to hit a sales target."),
]
for no, title, rule, ex, mistake in rules:
    slide(f"THE FOUR RULES / {no.upper()}", f"{no}: {title}",
          f'<p class="statement">{rule}</p>'
          + two(flexcard("Example", f"<p>{ex}</p>", "card good", "WHAT IT LOOKS LIKE"),
                flexcard("Common mistake", f"<p>{mistake}</p>", "card bad", "WHAT TO AVOID")),
          f"SESSION 2.3 / {no.upper()} OF 4")

# 10-13. Examples
examples = [
    ("GOOD EXAMPLE 1", "Dropbox storage plans", "good",
     "Dropbox gives a free Basic plan with 2 GB of storage. When users fill their space, Dropbox shows them how much more space the paid Plus plan gives.",
     ["The free tier lets people learn the product's value before paying. <b>(Rule 2)</b>",
      "The offer appears exactly when the user feels the limit: the storage is full. <b>(Rule 3)</b>",
      "The paid plan gives clearly more of what the user already values. <b>(Rule 1)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", 'Amazon "Frequently bought together"', "good",
     "On a product page, Amazon shows items that customers often buy with that product, such as a memory card with a camera, and lets the shopper add them in one click.",
     ["The items help the customer use the main product, so the offer feels like help. <b>(Rule 4)</b>",
      "The offer appears while the customer is already deciding to buy. <b>(Rule 3)</b>",
      "The customer can easily ignore it, so it does not damage trust."], "Why it is good"),
    ("BAD EXAMPLE 1", "Netflix's 2011 price change", "bad",
     "In July 2011, Netflix split its streaming plus DVD-by-mail plan into two plans. A customer who wanted both now paid $15.98 a month instead of $9.99, a 60% increase. "
     "Netflix lost about 800,000 U.S. subscribers in the next quarter, and its CEO later apologized.",
     ["Customers paid much more for the same service, with no new value. <b>(Rule 1)</b>",
      "It was a price increase for everyone, not an up-sell customers could choose.",
      "It hit all customers at once, so many left instead of paying more."], "Why it is bad"),
    ("BAD EXAMPLE 2", "Wells Fargo's cross-selling targets", "bad",
     "In 2016, U.S. regulators found that Wells Fargo employees had opened about 2 million bank and credit card accounts without customers' permission, "
     "under pressure to meet high cross-selling targets. The bank paid $185 million in fines.",
     ["The products helped employees reach targets, not customers reach their goals. <b>(Rule 4)</b>",
      "Customers did not choose the products, so it was not a real cross-sell.",
      "Lost trust, fines, and lost customers cost far more than the extra sales."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION 2.3 / {label}")

# 14. Summary
slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Dropbox</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Up-sell at the moment of need (Rule 3)</td></tr>'
      '<tr><td>Amazon</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Related items that help the purchase (Rule 4)</td></tr>'
      '<tr><td>Netflix 2011</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Higher price, no new value (Rule 1)</td></tr>'
      '<tr><td>Wells Fargo</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Products for sales targets, not customers (Rule 4)</td></tr></table>'
      '<div class="takeaway">Customers pay more when they get more value they chose, at the moment they need it.</div>',
      "SESSION 2.3 / EXAMPLE SUMMARY")

# 15-17. Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Revenue after a price change",
      '<p class="statement">When prices rise, some customers may leave. Count only the customers who stay.</p>'
      + two(flexcard("Formula", "<p>Revenue = customers who stay x new price</p>", "card", "USED IN EXERCISE 3"),
            flexcard("Example: a gym", ul([
                "100 members x $20.00 = $2,000 a month.",
                "Price rises to $25.00 and 20 members leave.",
                "80 x $25.00 = $2,000: no extra money, and fewer members."]), "card good", "WHAT IT LOOKS LIKE")),
      "SESSION 2.3 / TOOL 1 OF 3")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Revenue from up-selling and cross-selling",
      two(flexcard("Two formulas", ul([
          "Up-sell: users who upgrade x price of the new tier",
          "Cross-sell: customers who see the offer x attach rate x price of the add-on"]), "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: a music app", ul([
              "5,000 free users; 3% upgrade to a $6.00 plan: 150 x $6.00 = $900 a month.",
              "1,000 paying users; 10% buy a $3.00 playlist pack: 100 x $3.00 = $300."]), "card good", "WHAT IT LOOKS LIKE")),
      "SESSION 2.3 / TOOL 2 OF 3")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 2% of free users upgrade in 60 days, we will change the offer."</i></p>', "card", "MEMO BULLET 3")),
      "SESSION 2.3 / TOOL 3 OF 3")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Up-sell, cross-sell, or neither? BrewBox",
      '<p class="statement">BrewBox is a campus coffee kiosk with an ordering app. Six possible actions:</p>'
      '<div class="card">' + ul([
          "(a) Offer a large size for $0.80 more when a student orders a medium coffee.",
          "(b) Suggest a muffin with a morning coffee.",
          "(c) Raise the price of every drink by $0.50.",
          "(d) Offer a monthly coffee pass instead of single cups.",
          "(e) Sell phone cases at the counter.",
          "(f) Sell a reusable cup that gives $0.30 off every refill."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two('<div style="flex:1"><div class="small-label">TEMPLATE</div>' + tmpl(
          "Action [letter]: [up-sell / cross-sell / neither], because [what the customer gets, and whether it is a "
          "higher version of the same product, a related product, or neither].") + "</div>",
          '<div style="flex:1"><div class="small-label">WORKED EXAMPLE: CAMPUS BOOKSTORE</div>' + tmpl(
          "Action: offer a hardcover edition for $8 more to a student buying the paperback.\n"
          "Up-sell, because it is a better version of the same book.\n"
          "Action: suggest a highlighter set to a student buying a textbook.\n"
          "Cross-sell, because it is a related product that helps the student study the book.") + "</div>"),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Up-sell, cross-sell, or neither",
      "<table><tr><th>ACTION</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) Large size</td><td>Up-sell</td><td>A bigger version of the same drink</td></tr>"
      "<tr><td>(b) Muffin</td><td>Cross-sell</td><td>A related product for the same moment</td></tr>"
      "<tr><td>(c) +$0.50 on all drinks</td><td>Neither</td><td>A price increase: no extra value or choice</td></tr>"
      "<tr><td>(d) Monthly pass</td><td>Up-sell</td><td>A higher plan that gives more coffee</td></tr>"
      "<tr><td>(e) Phone cases</td><td>Neither</td><td>Does not help the coffee customer's goal (Rule 4)</td></tr>"
      "<tr><td>(f) Reusable cup</td><td>Cross-sell</td><td>Related, and gives value back on every refill</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Design an up-sell offer: LingoLeap",
      two(flexcard("Scenario", "<p>A language-learning app: <b>10,000 free users</b> and <b>400 Premium users</b> at <b>$8.00 a month</b>.</p>"
                   "<p>Free users can take 5 lessons per day. Each week, <b>2,000 free users</b> reach the 5-lesson limit.</p>"),
          flexcard("Your steps", ul([
              "<b>Step 1:</b> Conversion rate = 400 / 10,000 x 100 = ____ %. Premium revenue = 400 x $8.00 = $____.",
              "<b>Step 2:</b> Design the offer with Rules 1 and 3, using the template on the next slide."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two('<div style="flex:1"><div class="small-label">TEMPLATE</div>' + tmpl(
          "Who: [which users see the offer]\n"
          "When: [the moment of need that triggers the offer]\n"
          "Message: [the extra value, in one sentence, and the price]\n"
          "Measure: [one number we compare between a test group and a comparison group, and our target]\n"
          "Money: If [number] users upgrade, extra revenue = [number] x $[price] = $[amount] per month.") + "</div>",
          '<div style="flex:1"><div class="small-label">WORKED EXAMPLE: PHOTO APP ($3.00 PREMIUM)</div>' + tmpl(
          "Who: free users who have stored 100 photos.\n"
          "When: the moment they try to save photo number 101.\n"
          'Message: "Keep every memory: Premium stores unlimited photos for $3.00 a month."\n'
          "Measure: upgrade rate of users who see this message vs. users who see the old message; target 6%.\n"
          "Money: If 300 users upgrade, extra revenue = 300 x $3.00 = $900 per month.") + "</div>"),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Conversion is 4%; Premium earns $3,200 a month",
      '<div class="card good">' + ul([
          "<b>Who:</b> the 2,000 free users who hit the 5-lesson limit each week.",
          "<b>When:</b> right after they finish lesson 5.",
          "<b>Message:</b> names the extra value (for example, unlimited lessons) and the price, $8.00 a month.",
          "<b>Measure:</b> one number with a target, compared with a comparison group.",
          "<b>Money:</b> if 10% of the 2,000 upgrade, 200 x $8.00 = $1,600 more per month."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Choose a revenue plan for StudyNest",
      '<p class="statement">Revenue $5,800 / costs $9,000 / 20,000 Free, 1,000 Plus ($4.00), 200 Pro ($9.00)</p>'
      + two(flexcard("Option A: Raise all prices by 30%", "<p>Plus becomes <b>$5.20</b>; Pro becomes <b>$11.70</b>.</p>"
                     "<p>In a survey, <b>25% of paying users</b> said they would cancel if prices rose.</p>", "card", "OPTION A"),
            flexcard("Option B: Up-sell and cross-sell", "<p>Show the Plus offer when a free user's storage is full; expect <b>2%</b> of free users to upgrade.</p>"
                     "<p>In exam season, offer all paying users an exam pack for <b>$6.00</b>; expect an attach rate of <b>20%</b>.</p>", "card", "OPTION B")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1 and 2)",
      '<div class="card">' + ul([
          "Option A, nobody leaves: 1,000 x $5.20 + 200 x $11.70 = $______",
          "Option A, 25% leave: Plus users = 1,000 x 75% = ____; Pro users = 200 x 75% = ____; revenue = Plus x $5.20 + Pro x $11.70 = $______",
          "Option B up-sell: new Plus users = 20,000 x 2% = ____; extra revenue = new Plus users x $4.00 = $______",
          "Option B cross-sell: paying users = 1,000 + 200 + new Plus users = ____; buyers = paying users x 20% = ____; extra = buyers x $6.00 = $______",
          "Option B total in exam season = $5,800 + up-sell + cross-sell = $______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to the CEO (Tool 3)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [CEO name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next 60 days we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "FitClub: raise the fee, or sell a training add-on?",
      tmpl("To: Leo Kim, CEO, FitClub\n"
           "1. Decision and evidence: We should sell a $15 personal-training add-on instead of raising every fee, because it matches "
           "what members want (Rule 4) and 10% of 1,500 members buying it adds 150 x $15 = $2,250 a month.\n"
           "2. Biggest risk and trade-off: The weakest point is that members may not buy the add-on after the first month. "
           "We give up a fast, certain fee increase to keep members who would leave over a higher price.\n"
           "3. Next step and decision rule: In the next 60 days we will offer the add-on to half of our members and measure the "
           "attach rate. We will change this decision if fewer than 5% of them buy it."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Raising all prices earns less; up-sell and cross-sell covers costs",
      two(flexcard("The numbers", ul([
          "Option A: $7,540 if nobody leaves. If 25% leave: 750 x $5.20 + 150 x $11.70 = <b>$5,655</b>, less than today's $5,800.",
          "Option B: 400 new Plus users x $4.00 = $1,600. 1,600 paying users x 20% = 320 buyers x $6.00 = $1,920.",
          "Option B total: $5,800 + $1,600 + $1,920 = <b>$9,320</b>, above the $9,000 costs in exam season."])),
          flexcard("A strong memo", ul([
              "Usually chooses Option B.",
              "Uses at least one number from Step 1.",
              "Names a real risk: 2% is only an estimate, and pack sales come mainly in exam season.",
              "States a clear decision rule."]), "card good")),
      "EXERCISE 3 / ANSWER KEY")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain the difference between an up-sell, a cross-sell, and a simple price increase.</p></div>'
      '<div class="card"><div class="n">02</div><p>Design an up-sell offer with a moment of need and a measurable target.</p></div>'
      '<div class="card"><div class="n">03</div><p>Calculate whether up-selling and cross-selling earn more than raising all prices.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Dropbox. Dropbox plans (dropbox.com/plans).</p>'
      '<p class="ref">Netflix (2011). Letter to shareholders, third quarter 2011. Netflix Investor Relations.</p>'
      '<p class="ref">Consumer Financial Protection Bureau (2016). CFPB fines Wells Fargo $100 million for widespread illegal practice of secretly opening unauthorized accounts.</p></div>',
      "SESSION 2.3 / WRAP-UP")


def build():
    n = len(slides)
    parts = []
    for i, (eyebrow, title, body, footer) in enumerate(slides, 1):
        parts.append(
            f'<section class="slide"><div class="top-rule"></div>\n'
            f'  <div class="eyebrow">{eyebrow}</div><h2>{title}</h2>\n'
            f'  <div class="body">{body}</div>\n'
            f'  <div class="footer"><span>{footer}</span><span>SLIDE {i} / {n}</span></div>\n</section>\n')
    html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            "<title>Session 2.3 Lecture Presentation: The Up-Sell and Cross-Sell Strategy</title>\n"
            f"<style>{CSS}</style>\n</head>\n<body>\n\n" + "\n".join(parts) + "\n</body>\n</html>\n")
    HTML_OUT.write_text(html, encoding="utf-8")
    subprocess.run(["weasyprint", str(HTML_OUT), str(PDF_OUT)], check=True)
    print(f"{n} slides -> {PDF_OUT}")


if __name__ == "__main__":
    build()
