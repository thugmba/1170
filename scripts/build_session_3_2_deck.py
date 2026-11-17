"""Build the Session 3.2 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_3_2_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import ROOT, two, flexcard, tbox, term, build  # noqa: E402

SESSION = "3.2"
TITLE = "The Cannibalization Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


# Cover and situation
slide("MODULE 3 / COMPETITIVE STRATEGY &amp; INNOVATION FRAMEWORKS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_3_2_cornerburger_cannibalization_hanji.png" '
      'alt="Megan, owner of Corner Burger, asks whether to start her own delivery app that may take her own shop customers.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "Corner Burger: profitable, but shrinking",
      '<p class="statement" style="font-weight:400;">Corner Burger is a burger shop near campus. Customers order at the counter and eat in the shop. '
      "Megan is its owner. FastBite, a delivery-only burger app, takes about 300 of her shop customers every month.</p>"
      "<table><tr><th></th><th style=\"text-align:right\">LAST MONTH</th><th style=\"text-align:right\">THIS MONTH</th></tr>"
      '<tr><td>Customers who eat at the shop</td><td class="num">1,800</td><td class="num">1,500</td></tr>'
      '<tr><td>Money each customer spends (4 meals x $10)</td><td class="num">$40</td><td class="num">$40</td></tr>'
      '<tr><td>Cost of the food for 4 meals</td><td class="num">$16</td><td class="num">$16</td></tr>'
      '<tr><td>Profit per customer</td><td class="num">$24</td><td class="num">$24</td></tr>'
      '<tr><td>Total profit</td><td class="num">$43,200</td><td class="num">$36,000</td></tr></table>'
      "",
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE SITUATION", "Megan's idea: her own app, and its problem",
      two(flexcard("The idea", ul([
          "Corner Burger builds its own app for ordering and delivery: <b>$10,000</b> once.",
          "App customers spend the same <b>$40</b> a month.",
          "But delivery costs <b>$4</b>, so an app customer brings <b>$20</b> profit, not $24.",
          "Some new customers who never ate at Corner Burger may join."]), "card", "THE NEW PRODUCT"),
          flexcard("The problem: cannibalization", ul([
              "Many shop customers would move to the app.",
              "They still buy from Corner Burger, but the new app takes sales from Corner Burger's <b>own shop</b>.",
              "Each of them now brings <b>$4 less</b> ($20 instead of $24).",
              "Should Megan launch it anyway? This session helps you decide."]), "card", "WHY IT IS HARD")),
      f"SESSION {SESSION} / THE IDEA")

slide("THE STRATEGY IN ONE PARAGRAPH", f"What is the {TITLE[4:]}?",
      '<p class="para">A company <b>launches a new product even though it will take sales from its own old product</b>. '
      "Some of its own customers move from the old product to the new one. Companies do this on purpose when a new technology "
      "or a rival is already taking their customers. The choice is not \"old sales or new sales\"; it is "
      "<b>\"lose customers to yourself or lose them to a rival.\"</b></p>"
      '<div class="takeaway">Use it when a new way of serving customers is clearly growing, a rival will win your customers if you wait, '
      "and the new product can earn enough over time to make up for the old sales it replaces.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Cannibalization and profit per customer",
      term("Cannibalization", "When a company's new product takes sales from its own old product.",
           "600 of Corner Burger's shop customers switch to ordering on the app.")
      + term("Profit per customer", "The money a company keeps from one customer after paying the costs of serving that customer.",
             "a shop customer spends $40 a month and the food costs $16: $40 - $16 = $24."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 3")

slide("WORDS YOU NEED FIRST", "Cannibalization rate and net gain",
      term("Cannibalization rate", "The share of the new product's customers (or units sold) that came from your own old product.<br>"
           "= old customers (or units) who switched / customers (or units) of the new product x 100", "50 / 200 x 100 = 25%.")
      + term("Net gain", "What the company really gains after counting the profit it loses on the old product.<br>"
             "= profit from the new product - profit lost on the old product", "$4,000 - $1,200 = $2,800."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 3")

slide("WORDS YOU NEED FIRST", "Baseline and rival",
      term("\"Do nothing\" baseline", "What would happen if the company does not launch anything. "
           "A baseline is the result you compare your plan against.",
           "if Corner Burger does nothing, FastBite keeps taking 300 shop customers a month.")
      + term("Rival", "A company that competes for the same customers.", "FastBite is Corner Burger's rival."),
      f"SESSION {SESSION} / KEY TERMS 3 OF 3")

# Rules
rules = [
    ("Rule 1", "Compare with the future, not with today",
     "Ask what will happen if you do nothing. If a rival is already taking your customers, today's profit will not stay.",
     "Corner Burger earns $36,000 this month. If Megan does nothing, FastBite keeps taking 300 customers each month. "
     "The real choice is between the app and a smaller shop, not between the app and $36,000.",
     'Saying "the new product will hurt our sales" and stopping there. The old sales are already disappearing; '
     "the only question is who gets the customers."),
    ("Rule 2", "Count the net gain, not only the new sales",
     "New sales look good on their own. Always subtract the profit you lose on the old product.",
     "The app earns $20 from each customer, but Corner Burger earns $24 from a shop customer, so each shop customer who moves to the app costs $4. "
     "The app helps mainly because of the new customers and the customers it keeps from FastBite.",
     'Reporting "900 app customers, $18,000 of new profit!" without saying that 600 of them were shop customers who used to bring $14,400.'),
    ("Rule 3", "Give the new product its own team and its own goals",
     "Managers of the old product often slow the new one down, because it takes their sales. A separate team with its own targets moves faster.",
     "Megan asks two staff members to run the app. They are measured by app orders, not by shop sales.",
     "Letting the shop manager decide the app's prices and menu. The manager may make the app weak so that shop sales stay high."),
    ("Rule 4", "Move customers step by step, and keep their trust",
     "Give customers time, help, and a good reason to switch. Do not force everyone overnight.",
     "For six months, Corner Burger keeps its dining room open, gives shop customers a discount on their first app orders, and shows them how to order.",
     'Closing the dining room overnight and telling customers to "order on the app." Customers who are not ready leave for a rival.'),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_3_2_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "Apple's iPhone and iPod", "good",
     "In 2007, Apple launched the iPhone, which could also play music, so people would stop buying a separate music player. "
     "iPod sales peaked at about 54.8 million units in 2008 and fell to about 14.4 million in 2014. "
     "By 2012, the iPhone brought in about half of Apple's revenue ($80.5 billion of $156.5 billion).",
     ["Phone makers were adding music to phones; iPod sales would fall anyway. <b>(Rule 1)</b>",
      "The iPhone earned far more than the iPod sales it replaced. <b>(Rule 2)</b>",
      "Apple kept selling iPods for years while customers moved. <b>(Rule 4)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "Adobe Creative Cloud", "good",
     "In 2013, Adobe stopped making new versions of Creative Suite (bought once for about $1,300 to $2,600) and moved to a monthly "
     "subscription, about $50 a month for all apps. Revenue fell from $4.40 billion (2012) to $4.06 billion (2013), "
     "then grew to $4.80 billion (2015) and $7.30 billion (2017).",
     ["Compared with a future where customers stopped paying for upgrades, not with 2012 sales. <b>(Rule 1)</b>",
      "Monthly payments from millions of subscribers were worth more over time. <b>(Rule 2)</b>",
      "Existing customers got a lower first-year price to help them switch. <b>(Rule 4)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Kodak and digital photography", "bad",
     "In 1975, Kodak engineer Steve Sasson built one of the first digital cameras. But Kodak earned most of its profit from film, "
     "and its leaders were slow to move into digital photos because digital would replace film. "
     "Digital cameras and then phones replaced film anyway. Kodak filed for bankruptcy protection in January 2012.",
     ["Compared digital with today's profitable film, not with a future without film. <b>(Rule 1)</b>",
      "Film managers held the power, so digital never had room to grow. <b>(Rule 3)</b>",
      "Kodak did not want digital cameras to cut its film sales, so rivals such as Canon and Sony sold digital cameras to those customers instead. <b>(Rule 1)</b>"], "Why it is bad"),
    ("BAD EXAMPLE 2", "Netflix's Qwikster", "bad",
     "Netflix wanted customers to move from DVDs by mail to streaming. In September 2011, it announced that the DVD service would become "
     "a separate company, Qwikster, with its own website and account. Customers were angry. In October 2011, only three weeks later, "
     "Netflix cancelled the plan.",
     ["The right idea, but Netflix tried to push customers overnight. <b>(Rule 4)</b>",
      "Customers got no new value, only more work: two websites, two bills.",
      "Two months earlier, Netflix had raised its price by 60% (Session 2.3). Customers were already angry, so the Qwikster plan broke their trust even more. <b>(Rule 4)</b>"], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Apple iPhone</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Replaced its own iPod before rivals did (Rule 1)</td></tr>'
      '<tr><td>Adobe Creative Cloud</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Accepted a short fall for a bigger future (Rules 1 and 2)</td></tr>'
      '<tr><td>Kodak</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Protected film instead of facing the future (Rules 1 and 3)</td></tr>'
      '<tr><td>Netflix Qwikster</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Pushed customers overnight (Rule 4)</td></tr></table>'
      '<div class="takeaway">If someone is going to replace your product, it is better that it is you, done step by step.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Cannibalization rate",
      two(flexcard("Formula", "<p>Cannibalization rate = old customers (or units) who switched / customers (or units) of the new product x 100</p>"
                   "<p style=\"font-size:27px;\">Use customers when each customer buys one unit; use units (for example, loaves) when you count products.</p>",
                   "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: Corner Burger tests the app in one area", ul([
              "Megan offers the app in one neighborhood first; 200 customers use it.",
              "50 of them used to eat at the shop.",
              "50 / 200 x 100 = 25%."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("TOOL PRACTICE / THE CASE", "Practice case: BeanBox café adds a subscription",
      two(flexcard("Before: one way to buy coffee", ul([
          "Customers come into the café and <b>pay at the counter for each cup</b>: <b>$3.00</b> a cup.",
          "<b>900</b> regular customers buy about <b>20</b> cups a month this way.",
          "In the practice, we call them <b>café customers</b>."]), "card", "THE OLD PRODUCT"),
          flexcard("Now: a second way to buy coffee", ul([
              "BeanBox adds a <b>subscription</b> in its app: pay <b>$30</b> once a month and pick up a coffee every day.",
              "Some people who never bought from BeanBox join. That is new business.",
              "But some café customers also move to the subscription. That is <b>cannibalization</b>."]), "card", "THE NEW PRODUCT"))
      + '<div class="takeaway">Each tool slide uses Corner Burger as its example. After each tool, you practice the same tool on BeanBox. Across the four practices, decide whether the subscription is good for BeanBox.</div>',
      f"SESSION {SESSION} / PRACTICE CASE")

slide("TOOL 1 / PRACTICE", "Practice Tool 1: Where do BeanBox's subscribers come from?",
      two(flexcard("The facts", ul(['Before the subscription: <b>900</b> café customers.', '<b>Month 1:</b> <b>400</b> subscribers. BeanBox asks them where they bought coffee before: <b>120</b> were BeanBox café customers, <b>60</b> bought at another café, and <b>220</b> did not buy coffee before.', '<b>Month 2:</b> <b>600</b> subscribers; <b>330</b> of them were BeanBox café customers.']), "card", "BEANBOX CAFÉ"),
          flexcard("Your questions", ul(['<b>(a)</b> Month 1 cannibalization rate. Do you divide by 400 or by 900? Why?', '<b>(b)</b> What share of month 1 subscribers are <b>new to BeanBox</b> (they did not buy from BeanBox before)?', '<b>(c)</b> Month 2 cannibalization rate.', '<b>(d)</b> What changed from month 1 to month 2? Is a higher rate always bad for BeanBox? (Hint: Rule 1)']), "card", "SHOW YOUR CALCULATION")),
      f"SESSION {SESSION} / TOOL 1 PRACTICE")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Net gain",
      two(flexcard("Formula", "<p>Net gain = profit from the new product - profit lost on the old product</p>",
                   "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: Corner Burger, the same area", ul([
              "App: 200 x $20 profit = $4,000.",
              "The 50 customers who moved used to bring $24 profit each at the shop. That profit is lost: 50 x $24 = $1,200.",
              "Net gain = $4,000 - $1,200 = $2,800."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("TOOL 2 / PRACTICE", 'Practice Tool 2: More subscribers, less profit?',
      two(flexcard("The facts", ul(['A subscriber pays <b>$30</b> a month and costs BeanBox <b>$22</b> a month to serve.', "A café customer spends <b>$60</b> a month (20 coffees x $3.00); BeanBox's cost is <b>$45</b>.", 'Use the numbers from Tool 1: month 1 = 400 subscribers, 120 of them from the café; month 2 = 600 subscribers, 330 from the café.']), "card", "BEANBOX CAFÉ"),
          flexcard("Your questions", ul(['<b>(a)</b> Profit per subscriber and profit per café customer.', '<b>(b)</b> Net gain in month 1.', '<b>(c)</b> Net gain in month 2.', '<b>(d)</b> Subscribers grew by 50%, but net gain fell. Explain why in one sentence.']), "card", "SHOW YOUR CALCULATION")),
      f"SESSION {SESSION} / TOOL 2 PRACTICE")

slide("BEFORE THE EXERCISES / TOOL 3", 'Tool 3: Compare with the "do nothing" baseline',
      two(flexcard("Formula", "<p>Gain of the plan = result with the plan - result if we do nothing</p>",
                   "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: Corner Burger, the same area", ul([
              "Without the app, FastBite takes 60 shop customers from this area: 60 x $24 = $1,440 lost.",
              "Compared with doing nothing, the app is worth $2,800 + $1,440 = $4,240, if it keeps those customers."]),
              "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("TOOL 3 / PRACTICE", 'Practice Tool 3: Is the rival a real threat?',
      two(flexcard("The facts", ul(['A rival app, <b>BrewNow</b>, may open next to BeanBox.', 'Without the subscription, BrewNow would take some café customers. With the subscription, BeanBox keeps them.', 'Use the month 2 net gain from Tool 2 and the profit per café customer ($15).']), "card", "BEANBOX CAFÉ"),
          flexcard("Your questions", ul(['<b>(a)</b> Gain compared with doing nothing if BrewNow would take <b>100</b> café customers.', '<b>(b)</b> The same if BrewNow would take only <b>30</b> café customers.', '<b>(c)</b> The same if BrewNow does not open.', '<b>(d)</b> How many café customers must BrewNow take before the subscription is worth keeping?']), "card", "SHOW YOUR CALCULATION")),
      f"SESSION {SESSION} / TOOL 3 PRACTICE")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>"
                   "<p><i>Corner Burger: it gives up <b>$1,200</b> of shop profit to win <b>$4,000</b> of app profit "
                   "and keep 60 customers away from FastBite.</i></p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Corner Burger: "If more than 80% of app customers used to eat at our shop, we will raise the delivery fee." '
                   "(Why about 80%? Each customer who moves brings $20 instead of $24, so the app breaks even at $20 / $24 = 83%.)</i></p>",
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

slide("TOOL 4 / PRACTICE", 'Practice Tool 4: Set a break-even point and a rule',
      two(flexcard("The facts", ul(['Each subscriber brings <b>$8</b>. Each café customer who moves to the subscription takes away <b>$15</b> of café profit.', 'With no rival, the subscription breaks even (net gain = 0) when the cannibalization rate = $8 / $15 x 100.', 'Month 1 rate: 30%. Month 2 rate: 55% (Tool 1).']), "card", "BEANBOX CAFÉ"),
          flexcard("Your questions", ul(['<b>(a)</b> Break-even cannibalization rate. Which month was above it?', '<b>(b)</b> Trade-off in month 2: BeanBox gives up $____ of café profit to win $____ of subscription profit.', '<b>(c)</b> At a 55% rate, what is the lowest monthly price that breaks even? (Hint: profit per subscriber must be 0.55 x $15.)', '<b>(d)</b> Write a decision rule with a number, a time, and an action.']), "card", "SHOW YOUR CALCULATION")),
      f"SESSION {SESSION} / TOOL 4 PRACTICE")

slide("TOOL PRACTICE / CHECK YOUR ANSWERS", "BeanBox, Tools 1 and 2: more subscribers, less profit",
      '<div class="card good">' + ul([
          "<b>Tool 1:</b> (a) 120 / 400 x 100 = <b>30%</b>; divide by 400, the customers of the <i>new</i> product. "
          "(b) (60 + 220) / 400 = <b>70%</b>. (c) 330 / 600 x 100 = <b>55%</b>.",
          "(d) The rate rose from 30% to 55%: more than half of the subscribers now come from BeanBox's own café. "
          "This is <b>not always bad</b>: it is bad only if these customers would have stayed at the café anyway. "
          "If they would have left for another café, the subscription keeps them (Rule 1). Tool 3 checks this.",
          "<b>Tool 2:</b> (a) <b>$8</b> and <b>$15</b>. (b) 400 x $8 - 120 x $15 = $3,200 - $1,800 = <b>$1,400</b>. "
          "(c) 600 x $8 - 330 x $15 = $4,800 - $4,950 = <b>-$150</b>.",
          "(d) Each café customer who moves now brings $8 instead of $15, and many more café customers moved in month 2."]) + "</div>",
      "TOOL PRACTICE / ANSWER KEY 1 OF 2")

slide("TOOL PRACTICE / CHECK YOUR ANSWERS", "BeanBox, Tools 3 and 4: the answer depends on the rival",
      '<div class="card good">' + ul([
          "<b>Tool 3:</b> (a) -$150 + 100 x $15 = <b>$1,350</b>. (b) -$150 + 30 x $15 = <b>$300</b>. (c) <b>-$150</b>.",
          "(d) $150 / $15 = 10, so <b>more than 10</b> café customers.",
          "<b>Tool 4:</b> (a) 8 / 15 x 100 = <b>53.3%</b>; month 2 (55%) was above it. (b) <b>$4,950</b> to win <b>$4,800</b>.",
          "(c) 0.55 x $15 = $8.25, so $22 + $8.25 = <b>$30.25</b>.",
          '(d) Example: "If the rate stays above 53% for two more months and BrewNow has not opened, we will raise the price to $31."']) + "</div>",
      "TOOL PRACTICE / ANSWER KEY 2 OF 2")

# Exercise 1
E1_TD = 'style="font-size:27px;padding:.07in .1in;"'
E1_ROWS = [
    ("<i>Example: a bookstore sells e-books</i>", "<i>Paper books</i>", "<i>Cannibalization</i>", "<i>Cheaper e-book</i>"),
    ("(a) A bakery with a $6 loaf adds a $3 basic loaf", "", "", ""),
    ("(b) A newspaper puts its articles on a free website", "", "", ""),
    ("(c) A gym opens a branch in a city with no members", "", "", ""),
    ("(d) A streaming service adds a cheaper plan with ads", "", "", ""),
    ("(e) A car maker adds an electric version of its top car", "", "", ""),
    ("(f) A cafe starts selling umbrellas on rainy days", "", "", ""),
]
slide("EXERCISE 1 / EASY / 20 MIN", "Cannibalization or not? Fill in the table",
      '<p style="font-size:29px;line-height:1.3;margin:0 0 .2in;color:#172033;"><b>Ask for each new product:</b> '
      "Will some customers stop buying the company's <b>own old product</b> and buy the new one instead? "
      "<b>Yes</b> = cannibalization. <b>No</b> = not.</p>"
      '<table style="table-layout:fixed;"><colgroup><col style="width:50%"><col style="width:16%"><col style="width:16%"><col style="width:18%"></colgroup>'
      "<tr><th>NEW PRODUCT</th><th>OLD PRODUCT</th><th>ANSWER</th><th>WHY</th></tr>"
      + "".join("<tr>" + "".join(f"<td {E1_TD}>{c}</td>" for c in r) + "</tr>" for r in E1_ROWS) + "</table>",
      "EXERCISE 1 / WORKSHEET")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Does an old product of the same company lose customers?",
      "<table><tr><th>NEW PRODUCT</th><th>OLD PRODUCT</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) $3 basic loaf</td><td>$6 premium loaf</td><td>Cannibalization</td><td>Some premium buyers pay $3 instead of $6</td></tr>"
      "<tr><td>(b) Free website</td><td>Printed paper</td><td>Cannibalization</td><td>Some readers stop buying the paper</td></tr>"
      "<tr><td>(c) Gym in a new city</td><td>None</td><td>Not</td><td>No current members there</td></tr>"
      "<tr><td>(d) Cheaper plan with ads</td><td>Full-price plan</td><td>Cannibalization</td><td>Some full-price customers move down</td></tr>"
      "<tr><td>(e) Electric version</td><td>Petrol car</td><td>Cannibalization</td><td>Some petrol-car buyers choose electric</td></tr>"
      "<tr><td>(f) Umbrellas</td><td>None</td><td>Not</td><td>Umbrellas do not replace coffee</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
def task(text):
    return f'<p style="font-size:29px;line-height:1.3;margin:0 0 .18in;color:#172033;"><b>Your task:</b> {text}</p>'


WS_TD = 'style="font-size:30px;padding:.09in .1in;"'


def worksheet(rows):
    head = "<tr><th>#</th><th>WHAT TO CALCULATE</th><th>HOW</th><th>YOUR ANSWER</th></tr>"
    body = "".join("<tr>" + "".join(f"<td {WS_TD}>{c}</td>" for c in (str(i),) + r + ("",)) + "</tr>"
                   for i, r in enumerate(rows, 1))
    return ('<table style="table-layout:fixed;"><colgroup><col style="width:5%"><col style="width:40%">'
            '<col style="width:35%"><col style="width:20%"></colgroup>' + head + body + "</table>")


slide("EXERCISE 2 / MEDIUM / 30 MIN", "Calculate the real gain: GoldCrust bakery",
      task("Was the new basic loaf a good idea? Read the facts, then do the two steps on the right.")
      + two(flexcard("The facts", ul([
          "GoldCrust sells <b>1,000</b> premium loaves a month, <b>$3.00</b> profit each.",
          "It adds a basic loaf: <b>$1.00</b> profit each; <b>800</b> sold in the first month.",
          "Premium sales fall to <b>700</b>.",
          "Without a basic loaf, a new discount bakery would take <b>400</b> premium buyers."]), "card", "SCENARIO"),
          flexcard("What you will do", ul([
              "<b>Step 1:</b> Fill in the calculation table (next slide), row by row.",
              "<b>Step 2:</b> Use your numbers to write three sentences with the template (slide after).",
              "Work alone for 20 minutes, then compare with a partner."]), "card", "30 MINUTES")),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / STEP 1", "Fill in the table: one row at a time",
      task("Calculate each row and write the result in the last column. Later rows use earlier rows.")
      + worksheet([
          ("Premium loaves lost (units that switched)", "1,000 - 700"),
          ("Cannibalization rate (Tool 1)", "row 1 / 800 x 100"),
          ("Net gain vs. last month (Tool 2)", "800 x $1.00 - row 1 x $3.00"),
          ("Profit if GoldCrust does nothing (Tool 3)", "(1,000 - 400) x $3.00"),
          ("Profit with the basic loaf", "700 x $3.00 + 800 x $1.00"),
          ("Gain compared with doing nothing", "row 5 - row 4"),
      ]),
      "EXERCISE 2 / CALCULATION TABLE")

slide("EXERCISE 2 / STEP 2", "Explain your result in three sentences",
      task("Copy the template. Replace every [bracket] with your numbers from Step 1 and your own words. The example shows a finished answer.")
      + two(tbox("TEMPLATE",
               "Compared with last month, the new product [gains / loses] $[amount],\n"
               "because [number] [customers / units] switched from our [old product].\n"
               "Compared with doing nothing, it [gains / loses] $[amount],\n"
               "because [what would happen without it].\n"
               "So we should [keep / stop] the new product, because [Rule 1 or Rule 2]."),
          tbox("WORKED EXAMPLE: CORNER BURGER'S ONE-AREA TEST (TOOLS 1 TO 3)",
               "Compared with last month, the app gains $2,800, because 50 customers switched from eating at our shop.\n"
               "Compared with doing nothing, it gains $4,240, because without it FastBite would take 60 of our customers.\n"
               "So we should keep the app, because the real choice is between it and a smaller Corner Burger (Rule 1).")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "A loss compared with last month, a gain compared with the future",
      '<div class="card good">' + ul([
          "<b>Row 1:</b> 1,000 - 700 = <b>300</b> loaves. <b>Row 2:</b> 300 / 800 x 100 = <b>37.5%</b>.",
          "<b>Row 3:</b> $800 - $900 = <b>-$100</b> (a small loss compared with last month).",
          "<b>Row 4:</b> 600 x $3.00 = <b>$1,800</b>. <b>Row 5:</b> $2,100 + $800 = <b>$2,900</b>. <b>Row 6:</b> $2,900 - $1,800 = <b>$1,100</b>.",
          "<b>Step 2:</b> a strong answer keeps the basic loaf: it looks like a loss compared with last month but is a clear gain compared "
          "with the future (Rule 1), as long as the discount bakery really is a threat."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Should Corner Burger launch its own app?",
      task("Help Megan choose A or B. <b>Step 1:</b> calculate (next slide). <b>Step 2:</b> write a memo. <b>Step 3:</b> present it in 2 minutes.")
      + '<p style="font-size:29px;margin:0 0 .14in;color:#172033;"><b>Today:</b> 1,500 shop customers / $24 profit each / $36,000 profit per month.</p>'
      + two(flexcard("Option A: Keep the shop only", "<p>FastBite keeps taking <b>300</b> shop customers each month.</p>"
                     "<p>Shop customers: <b>1,200</b>, then <b>900</b>, <b>600</b>, <b>300</b>.</p>", "card", "DO NOTHING"),
            flexcard("Option B: Launch the app", "<p>Build cost <b>$10,000</b> once. Each month <b>600</b> shop customers switch "
                     "(<b>900</b> still eat at the shop) and <b>300</b> new customers join: <b>900</b> app customers at <b>$20</b> profit each.</p>"
                     "<p>The team believes the app stops customers leaving for FastBite.</p>", "card", "CANNIBALIZE")),
      "EXERCISE 3 / SCENARIO: FOUR MONTHS")

slide("EXERCISE 3 / STEP 1", "Fill in the table before you decide (Tools 1 to 3)",
      task("Calculate each row and write the result in the last column. Later rows use earlier rows.")
      + worksheet([
          ("Option A: profit over 4 months", "(1,200 + 900 + 600 + 300) x $24"),
          ("Option B: profit per month", "900 x $24 + 900 x $20"),
          ("Option B: profit over 4 months", "4 x row 2 - $10,000"),
          ("Option B: first month only", "row 2 - $10,000"),
          ("Is row 4 more or less than today's $36,000?", "compare"),
          ("Cannibalization rate of the app (Tool 1)", "600 / 900 x 100"),
          ("Option A if FastBite stops growing", "4 x $36,000"),
      ]),
      "EXERCISE 3 / CALCULATION TABLE")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Megan (Tool 4)",
      task("Copy the template. Replace every [bracket] with your choice, your numbers from Step 1, and your own words. "
           "The next slide shows a finished memo for GoldCrust.")
      + '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [owner name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next month we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway"><b>Step 3:</b> give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "GoldCrust: keep the basic loaf?",
      tmpl("To: Tom Reyes, owner, GoldCrust\n"
           "1. Decision and evidence: We should keep the basic loaf, because the real choice is between it and losing 400 buyers "
           "to the discount bakery (Rule 1): it earns $2,900 a month against $1,800 if we do nothing.\n"
           "2. Biggest risk and trade-off: The weakest point is that more premium buyers may switch than the 300 we saw. "
           "We give up $900 of premium profit to keep customers away from the new bakery.\n"
           "3. Next step and decision rule: In the next month we will count premium and basic sales every week. "
           "We will change this decision if premium sales fall below 600 loaves."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Compared with today the app looks worse; compared with the future it wins",
      '<div class="card">' + ul([
          "<b>Row 1:</b> 3,000 x $24 = <b>$72,000</b>. <b>Row 2:</b> $21,600 + $18,000 = <b>$39,600</b>.",
          "<b>Row 3:</b> $158,400 - $10,000 = <b>$148,400</b>. <b>Row 4:</b> $39,600 - $10,000 = <b>$29,600</b>.",
          "<b>Row 5:</b> <b>less</b> than today's $36,000, but more than Option A's first month (1,200 x $24 = $28,800).",
          "<b>Row 6:</b> <b>67%</b>: two of every three app customers were shop customers.",
          "<b>Row 7:</b> <b>$144,000</b>, close to Option B. The choice depends on the FastBite threat."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Usually chooses Option B and explains why today's $36,000 is the wrong comparison (Rule 1).",
          "Names a real risk: more shop customers may switch than expected, or the app may not stop customers leaving for FastBite.",
          "Plans a step-by-step move, such as a discount on first app orders for shop customers (Rule 4).",
          'Gives a decision rule: "If fewer than 300 new customers join the app in the first month, we will rethink the delivery fee."']) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain cannibalization and why a company would cannibalize its own product on purpose.</p></div>'
      '<div class="card"><div class="n">02</div><p>Calculate the cannibalization rate and the net gain.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare a plan with the "do nothing" baseline and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      "<p class=\"ref\">Christensen, C. M. (1997). The Innovator's Dilemma. Harvard Business School Press.</p>"
      '<p class="ref">Apple Inc. (2008, 2012, 2014). Form 10-K annual reports.</p>'
      '<p class="ref">Adobe Inc. (2013-2017). Form 10-K annual reports.</p>'
      '<p class="ref">Eastman Kodak Company (2012). Voluntary Chapter 11 business reorganization announcement.</p>'
      '<p class="ref">Hastings, R. (2011, October 10). DVDs will be staying at Netflix.com. Netflix.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


# Answer keys go to the end of the deck, so students cannot copy them during the exercises
answer_keys = [sl for sl in slides if "CHECK YOUR ANSWER" in sl[0]]
slides = [sl for sl in slides if "CHECK YOUR ANSWER" not in sl[0]]
slide("ANSWER KEY", "Answers to the practice and exercises",
      '<p class="statement" style="font-weight:400;">Open these slides only after you finish. '
      "Compare your numbers and reasons with the answers, and ask about any difference.</p>",
      f"SESSION {SESSION} / ANSWER KEY")
slides += answer_keys

if __name__ == "__main__":
    build(slides, SESSION, TITLE)
