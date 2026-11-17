"""Build the Session 3.3 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_3_3_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "3.3"
TITLE = "The Disruption Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))




def task(text):
    return f'<p style="font-size:29px;line-height:1.3;margin:0 0 .18in;color:#172033;"><b>Your task:</b> {text}</p>'


WS_TD = 'style="font-size:30px;padding:.09in .1in;"'


def worksheet(rows, td=WS_TD):
    head = "<tr><th>#</th><th>WHAT TO CALCULATE</th><th>HOW</th><th>YOUR ANSWER</th></tr>"
    body = "".join("<tr>" + "".join(f"<td {td}>{c}</td>" for c in (str(i),) + r + ("",)) + "</tr>"
                   for i, r in enumerate(rows, 1))
    return ('<table style="table-layout:fixed;"><colgroup><col style="width:5%"><col style="width:40%">'
            '<col style="width:35%"><col style="width:20%"></colgroup>' + head + body + "</table>")


def practice(title, facts, questions, footer):
    slide(f"{footer} / PRACTICE", title,
          two(flexcard("The facts", ul(facts), "card", "SNAPBOX PHOTO BOOTHS"),
              flexcard("Your questions", ul(questions), "card", "SHOW YOUR CALCULATION")),
          f"SESSION {SESSION} / {footer} PRACTICE")


# Cover and situation
slide("MODULE 3 / COMPETITIVE STRATEGY &amp; INNOVATION FRAMEWORKS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_3_3_sweetslice_disruption_hanji.png" '
      'alt="Lily, owner of the Sweet Slice cake shop, asks whether to make fancy cakes like Royal Cakes or serve the people who buy no cake.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "Sweet Slice: a tiny cake shop across from a strong leader",
      '<p class="statement" style="font-weight:400;font-size:30px;">Sweet Slice is Lily\'s tiny cake shop near campus: single slices and cupcakes, '
      "ready to eat. Across the street is Royal Cakes, the leader in town.</p>"
      "<table><tr><th></th><th>ROYAL CAKES (LEADER)</th><th>SWEET SLICE (LILY)</th></tr>"
      "<tr><td>What it sells</td><td>Decorated whole cakes for 10 people, ordered 2 days ahead</td><td>Single slices and cupcakes, ready now</td></tr>"
      "<tr><td>Price</td><td>$40 a cake</td><td>$5 a slice</td></tr>"
      "<tr><td>Sales a month</td><td>2,000 cakes</td><td>1,500 slices</td></tr>"
      "<tr><td>Profit</td><td>$15 a cake</td><td>$2 a slice</td></tr></table>"
      '<div class="takeaway">10,000 people a month want a cake for a small celebration; only 2,000 buy from Royal. '
      "An investor says: hire a top pastry chef, make fancy cakes, and take Royal's customers.</div>",
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE SITUATION", "Why do 8,000 people buy no cake?",
      two(flexcard("What they want", ul([
          "A cake for a <b>small</b> celebration: a birthday with two or three friends, or passing an exam.",
          "Something sweet, with a candle, <b>today</b>."]), "card", "THE JOB TO BE DONE"),
          flexcard("What Royal Cakes offers", ul([
              "A cake for <b>10 people</b>, ordered <b>two days ahead</b>.",
              "<b>$40</b>: too much for three friends.",
              "So they buy <b>no cake at all</b>."]), "card bad", "TOO BIG, TOO EXPENSIVE"))
      + '<div class="takeaway">Lily\'s question: fight Royal for its 2,000 customers, or serve the 8,000 people nobody serves?</div>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", f"What is the {TITLE[4:]}?",
      '<p class="para">A small company beats a strong leader <b>without fighting it head-on</b>. It starts with customers the leader '
      "ignores: people who buy nothing because the leader is too expensive or too hard to use, or customers who get more than they need. "
      "It offers a <b>simpler, cheaper product that is good enough</b>. The leader does not fight back, because these customers earn it "
      "little profit. Then the newcomer <b>improves step by step</b> until it is good enough for the leader's own customers.</p>"
      '<div class="takeaway">Use it when the leader\'s product is expensive or complex, many people are not served, '
      "and a simpler product can do the main job.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Leader, disruption, sustaining innovation",
      term("Leader<br><span style=\"font-size:24px;color:#526174;\">(incumbent)</span>",
           "The strong company that already serves most customers in a market.", "Royal Cakes.")
      + term("Disruption", "A simpler, cheaper product that starts with customers the leader ignores and later takes the leader's customers.",
             "Sweet Slice's $5 slices.")
      + term("Sustaining innovation", "Making a product better for the leader's best customers, often at a higher price.",
             "Royal Cakes adds a three-layer cake for $60."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Non-consumers, over-served, good enough",
      term("Non-consumers", "People who need a job done but buy nothing today, often because it costs too much or is too hard.",
           "the 8,000 people who want a cake but buy none.")
      + term("Over-served customers", "Customers who get more than they need and would happily pay less for less.",
             "a student who wants cake for three people but must buy a cake for 10.")
      + term("Good enough", "A product that does the main job the customer needs, even if it is not the best.",
             "a slice with one candle for a birthday with two friends."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 2")

# Rules
rules = [
    ("Rule 1", "Start where the leader is not looking",
     "Begin with non-consumers or with the leader's least profitable customers. They are easy to win, and the leader will not miss them.",
     "Sweet Slice starts with the 8,000 people who want a cake but buy none. Royal Cakes does not serve them, so it will not fight for them.",
     "Going straight after the leader's best customers. The leader is strongest exactly there, and it will fight hard to keep them."),
    ("Rule 2", "Make it simpler and cheaper, and good enough for the job",
     "Do not try to be better than the leader at everything. Be good enough at the main job, and much easier and cheaper.",
     "A $5 slice with a candle, ready now, is enough for a birthday with two friends. They do not need a 10-person cake.",
     "Adding a famous chef, fancy decorations, and a high price to look like the leader. Then the product is neither cheap nor better."),
    ("Rule 3", "Choose a model the leader does not want to copy",
     "If copying you would earn the leader much less profit than its own product, the leader will ignore you, often until it is too late.",
     "Royal earns $15 on each cake. Copying Sweet Slice would earn it about $2 a slice, so Royal protects its $40 cakes.",
     "Choosing a model the leader can copy easily and profitably, such as the same cakes at a slightly lower price. The leader cuts its price and wins."),
    ("Rule 4", "Improve step by step, then move up to better customers",
     "Use what you learn from your first customers to improve. When you are good enough for the leader's customers, they come to you at a lower price.",
     "After a year of slices, Sweet Slice adds $12 mini cakes, then $25 whole cakes. Some of Royal's customers start to switch.",
     "Spending a lot of money to grow very fast before the product works. A newcomer has little money and cannot survive big mistakes."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_3_3_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "Netflix and Blockbuster", "good",
     "Netflix started in 1998 by renting DVDs by mail, with no late fees: slower than a Blockbuster store, but good enough for people who "
     "planned ahead. Blockbuster earned a large part of its profit from stores and late fees. In 2000, Netflix offered to sell itself to "
     "Blockbuster for $50 million; Blockbuster said no. Netflix started streaming in 2007. Blockbuster filed for bankruptcy in September 2010.",
     ["Started with people who did not mind waiting for a DVD. <b>(Rule 1)</b>",
      "No late fees: a model Blockbuster did not want to copy. <b>(Rule 3)</b>",
      "Improved step by step, from mail to streaming. <b>(Rule 4)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "M-Pesa in Kenya", "good",
     "In March 2007, the phone company Safaricom launched M-Pesa: people send money with a simple text message on a basic phone and put in "
     "or take out cash at local shops. Fewer than 20% of Kenyans had access to a bank. Safaricom hoped for 350,000 users in the first year; "
     "by November 2007 it had more than 1 million active users. Later it added savings, loans, and bill payments.",
     ["Served millions of people that banks did not serve. <b>(Rule 1)</b>",
      "Basic phones and local shops: simpler and cheaper than a bank account. <b>(Rule 2)</b>",
      "Started with sending money, then added more step by step. <b>(Rule 4)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Quibi", "bad",
     "Quibi launched in April 2020 with expensive short shows from Hollywood stars, made for phones. It raised $1.75 billion and charged "
     "$4.99 to $7.99 a month. But people already watched free short videos on YouTube and TikTok. Quibi announced it would close in "
     "October 2020, about six months after launch.",
     ["Went after viewers that strong leaders already served well. <b>(Rule 1)</b>",
      "More expensive than free short videos, not simpler or cheaper. <b>(Rule 2)</b>",
      "Spent heavily before learning what viewers wanted. <b>(Rule 4)</b>"], "Why it is bad"),
    ("BAD EXAMPLE 2", "Webvan", "bad",
     "Webvan was a U.S. online grocery delivery company. Before it had many customers, it built large high-tech warehouses (about "
     "$35 million each) and planned to enter many cities quickly. It lost more than $800 million and went bankrupt in July 2001.",
     ["Tried to grow very fast before the service worked and made money. <b>(Rule 4)</b>",
      "Expensive warehouses made its costs high, not low. <b>(Rule 2)</b>",
      "Later online grocers grew slowly, city by city, and survived."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Netflix</td><td style="color:#2f6b47;font-weight:700">Good</td><td>A model the leader did not want to copy (Rule 3)</td></tr>'
      '<tr><td>M-Pesa</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Served people banks ignored (Rule 1)</td></tr>'
      '<tr><td>Quibi</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Attacked strong leaders with a pricier product (Rules 1 and 2)</td></tr>'
      '<tr><td>Webvan</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Grew too fast before the model worked (Rule 4)</td></tr></table>'
      '<div class="takeaway">Start small where the leader is not looking, then climb step by step.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Size of the non-consumer market",
      two(flexcard("Formula", "<p>Non-consumers = people who need the job done - people who buy from the leader</p>",
                   "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: Sweet Slice", ul([
              "10,000 people a month want a cake for a small celebration.",
              "2,000 buy a Royal cake.",
              "Non-consumers = 10,000 - 2,000 = 8,000 people."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("TOOL PRACTICE / THE CASE", "Practice case: SnapBox photo booths",
      two(flexcard("Until now: the photo studio", ul([
          "Students who want nice photos with friends go to a <b>photo studio</b>.",
          "A photographer takes photos for <b>one hour</b>; the studio charges <b>$80</b>.",
          "Most students <b>never go</b>."]), "card", "THE LEADER"),
          flexcard("SnapBox's idea", ul([
              "<b>Self-service photo booths</b> on shopping streets.",
              "Four photos for <b>$6</b>, printed in one minute.",
              "<b>No photographer.</b>"]), "card", "THE NEWCOMER"))
      + '<div class="takeaway">Each tool slide uses Sweet Slice as its example. After each tool, you practice the same tool on SnapBox. '
      "Across the four practices, decide whether SnapBox is a real disruption and how fast it should grow.</div>",
      f"SESSION {SESSION} / PRACTICE CASE")

practice("Practice Tool 1: Who are SnapBox's first customers?",
         ["The city has <b>60,000</b> students.",
          "<b>30%</b> say they want photos with friends at least once a month.",
          "Photo studios serve <b>3,000</b> of these students a month.",
          "Of these studio customers, <b>40%</b> only want quick, fun photos, not a photographer."],
         ["<b>(a)</b> How many students need the job done?",
          "<b>(b)</b> How many are non-consumers?",
          "<b>(c)</b> How many studio customers are over-served?",
          "<b>(d)</b> Which group should SnapBox start with, and which group should it leave alone? Explain with Rule 1."],
         "TOOL 1")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: The leader's profit test",
      two(flexcard("Will the leader copy you?", "<p>Compare the leader's profit per customer today with the profit it would earn by copying you. "
                   "If copying earns much less, the leader will probably not fight back.</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: Sweet Slice", ul([
              "Royal Cakes earns <b>$15</b> on each cake. Copying Sweet Slice earns <b>$2</b> a slice.",
              "To earn one cake's profit, Royal must sell $15 / $2 = 7.5 slices: 7 or 8 customers instead of one.",
              "Royal will not want to copy Sweet Slice."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

practice("Practice Tool 2: Will photo studios copy SnapBox?",
         ["Studio session: the customer pays <b>$80</b>; the studio's cost (photographer, room, printing) is <b>$40</b>.",
          "SnapBox use: the customer pays <b>$6</b>; SnapBox's cost is <b>$3</b>.",
          "A photographer can do <b>8</b> sessions a day."],
         ["<b>(a)</b> Profit per customer for the studio and for SnapBox.",
          "<b>(b)</b> How many booth uses earn the same profit as one studio session? (Round up.)",
          "<b>(c)</b> A studio puts one booth in its lobby and gets <b>40</b> uses a day. Compare the booth's daily profit with one photographer's day.",
          "<b>(d)</b> Will studios copy SnapBox? What are they more likely to do instead?"],
         "TOOL 2")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Profit over several periods (from Session 3.1)",
      two(flexcard("Formula", "<p>Profit = profit per period x number of periods - one-time cost</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: Sweet Slice", ul([
              "Lily spends $3,000 on a second display fridge and earns $1,000 more profit a month.",
              "After 12 months: 12 x $1,000 - $3,000 = $9,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

practice("Practice Tool 3: When does one booth pay off?",
         ["One booth costs <b>$4,000</b> to buy and set up.",
          "Rent for its space: <b>$700</b> a month.",
          "Each use brings <b>$3</b> profit before rent.",
          "Use <b>30</b> days a month."],
         ["<b>(a)</b> At <b>30</b> uses a day: profit a month after rent, and profit over 12 months.",
          "<b>(b)</b> How many months to earn back the $4,000?",
          "<b>(c)</b> At only <b>15</b> uses a day: profit over 12 months.",
          "<b>(d)</b> The smallest number of uses a day that gives a profit of $0 or more over 12 months. (Round up.)"],
         "TOOL 3")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>"
                   "<p><i>Sweet Slice: Lily gives up the higher price of fancy whole cakes to win the 8,000 people nobody serves "
                   "and to stay out of Royal's way.</i></p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Sweet Slice: "If we sell fewer than 400 slices a week by the end of month 3, we will change the price or the menu."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

practice("Practice Tool 4: Five booths now, or one booth first?",
         ["<b>Plan 1:</b> open <b>5</b> booths at once (5 x $4,000 = $20,000).",
          "<b>Plan 2:</b> open <b>1</b> booth first and add more later.",
          "Nobody knows yet how many uses a day a booth will get.",
          "Use your Tool 3 numbers."],
         ["<b>(a)</b> With 5 booths: 12-month profit if each booth gets <b>30</b>, <b>15</b>, or <b>8</b> uses a day.",
          "<b>(b)</b> Trade-off: what does SnapBox give up by opening only 1 booth first, and what does it protect?",
          "<b>(c)</b> Which rule supports starting with one booth?",
          "<b>(d)</b> Write a decision rule with a number, a time, and an action. (Hint: Tool 3 (d).)"],
         "TOOL 4")

slide("TOOL PRACTICE / CHECK YOUR ANSWERS", "SnapBox, Tools 1 and 2: a real disruption",
      '<div class="card good">' + ul([
          "<b>Tool 1:</b> (a) 60,000 x 30% = <b>18,000</b>. (b) 18,000 - 3,000 = <b>15,000</b> non-consumers. "
          "(c) 3,000 x 40% = <b>1,200</b> over-served.",
          "(d) Start with the 15,000 (and the 1,200). Leave alone the other 1,800 studio customers who want a photographer: "
          "they are the studio's best customers, and it will fight for them (Rule 1).",
          "<b>Tool 2:</b> (a) studio <b>$40</b>; SnapBox <b>$3</b>. (b) $40 / $3 = 13.3, so <b>14</b> uses. "
          "(c) booth 40 x $3 = <b>$120</b> a day; photographer 8 x $40 = <b>$320</b> a day.",
          "(d) Probably not. Studios will more likely improve sessions for their best customers, such as a $120 premium session "
          "(sustaining innovation, Rule 3)."]) + "</div>",
      "TOOL PRACTICE / ANSWER KEY 1 OF 2")

slide("TOOL PRACTICE / CHECK YOUR ANSWERS", "SnapBox, Tools 3 and 4: test one booth before five",
      '<div class="card good">' + ul([
          "<b>Tool 3:</b> (a) 900 uses x $3 = $2,700 - $700 = <b>$2,000</b> a month; 12 x $2,000 - $4,000 = <b>$20,000</b>. "
          "(b) <b>2 months</b>. (c) 450 x $3 - $700 = $650; 12 x $650 - $4,000 = <b>$3,800</b>.",
          "(d) $4,000 / 12 = $333 after rent = $1,033 before rent; $1,033 / $3 = 344 uses a month; 344 / 30 = 11.5, so <b>12 a day</b>.",
          "<b>Tool 4:</b> (a) <b>$100,000</b> / <b>$19,000</b> / <b>-$18,800</b> (at 8 uses, each booth earns $20 a month: 12 x $20 - $4,000 = -$3,760).",
          "(b) It gives up up to $80,000 of extra profit in the best case to avoid an $18,800 loss. (c) <b>Rule 4</b> (remember Webvan).",
          '(d) Example: "If the first booth averages at least 12 uses a day for two months, we will open four more; if not, we will move it."']) + "</div>",
      "TOOL PRACTICE / ANSWER KEY 2 OF 2")

# Exercise 1
E1_TD = 'style="font-size:24px;padding:.06in .09in;"'
E1_ROWS = [
    ("<i>Example: a $2 phone app that works as a scanner; office scanners cost $200</i>", "<i>Non-consumers</i>",
     "<i>Simpler, cheaper</i>", "<i>Disruption</i>", "<i>Rules 1, 2</i>"),
    ("(a) A $3 rice-box stand for students who skip lunch because restaurants charge $12", "", "", "", ""),
    ("(b) A famous steak house adds a $120 dinner for its best customers", "", "", "", ""),
    ("(c) A free app that fixes the light in photos; studios charge $50 to edit", "", "", "", ""),
    ("(d) A coffee chain adds a gold card with free drinks for its biggest spenders", "", "", "", ""),
    ("(e) $10 online cooking videos; cooking schools charge $500 a course", "", "", "", ""),
    ("(f) A phone maker adds a fourth camera to its most expensive phone", "", "", "", ""),
]
slide("EXERCISE 1 / EASY / 20 MIN", "Disruption or not? Fill in the table",
      task("For each new product, ask: <b>Who are the first customers?</b> Is it <b>simpler and cheaper</b> than the leader's, "
           "or <b>better and more expensive</b>? Non-consumers or over-served + simpler and cheaper = disruption.")
      + '<table style="table-layout:fixed;"><colgroup><col style="width:40%"><col style="width:17%"><col style="width:15%">'
      '<col style="width:14%"><col style="width:14%"></colgroup>'
      "<tr><th>NEW PRODUCT</th><th>FIRST CUSTOMERS</th><th>SIMPLER OR BETTER?</th><th>ANSWER</th><th>WHY (RULE)</th></tr>"
      + "".join("<tr>" + "".join(f"<td {E1_TD}>{c}</td>" for c in r) + "</tr>" for r in E1_ROWS) + "</table>",
      "EXERCISE 1 / WORKSHEET")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Who are the first customers, and is it simpler and cheaper?",
      '<table style="table-layout:fixed;"><colgroup><col style="width:24%"><col style="width:24%"><col style="width:20%"><col style="width:32%"></colgroup>'
      "<tr><th>PRODUCT</th><th>FIRST CUSTOMERS</th><th>ANSWER</th><th>WHY (RULE)</th></tr>"
      "<tr><td>(a) $3 rice box</td><td>Non-consumers</td><td>Disruption</td><td>Simpler, cheaper (Rules 1, 2)</td></tr>"
      "<tr><td>(b) $120 steak dinner</td><td>Leader's best</td><td>Sustaining</td><td>Leader is strong here (Rule 1)</td></tr>"
      "<tr><td>(c) Free photo app</td><td>Non-consumers</td><td>Disruption</td><td>Simpler, cheaper (Rules 1, 2)</td></tr>"
      "<tr><td>(d) Gold card</td><td>Leader's best</td><td>Sustaining</td><td>For top spenders (Rule 1)</td></tr>"
      "<tr><td>(e) $10 videos</td><td>Non-consumers</td><td>Disruption</td><td>Simpler, cheaper (Rules 1, 2)</td></tr>"
      "<tr><td>(f) Fourth camera</td><td>Leader's best</td><td>Sustaining</td><td>Better and pricier (Rule 1)</td></tr></table>"
      "",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Check a disruption plan: QuickCut",
      task("Is QuickCut a real disruption, and should it open? <b>Step 1:</b> fill in the calculation table (next slide). "
           "<b>Step 2:</b> check the four rules and give a verdict (slide after).")
      + two(flexcard("QuickCut (the newcomer)", ul([
          "<b>$8</b>, 10-minute haircut shops in train stations.",
          "No washing, styling, or booking.",
          "Cost per haircut: <b>$5</b>.",
          "Each shop costs <b>$6,000</b> to open; QuickCut plans <b>3</b> shops."]), "card", "SCENARIO"),
          flexcard("Salons and customers", ul([
              "Salons: <b>$40</b> for 45 minutes with washing and styling. Cost per haircut: <b>$25</b>.",
              "<b>50,000</b> men need a haircut every month; <b>20,000</b> go to salons; the rest cut their hair at home.",
              "QuickCut expects <b>1 in 10</b> men who cut their hair at home to come once a month."]), "card", "THE MARKET")),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / STEP 1", "Fill in the table: one row at a time",
      task("Calculate each row and write the result in the last column. Later rows use earlier rows.")
      + worksheet([
          ("Non-consumers (Tool 1)", "50,000 - 20,000"),
          ("Salon profit per haircut", "$40 - $25"),
          ("QuickCut profit per haircut", "$8 - $5"),
          ("How many times more a salon earns (Tool 2)", "row 2 / row 3"),
          ("QuickCut haircuts a month", "row 1 x 10%"),
          ("QuickCut profit a month", "row 5 x row 3"),
          ("Profit over 12 months (Tool 3)", "12 x row 6 - 3 x $6,000"),
      ]),
      "EXERCISE 2 / CALCULATION TABLE")

slide("EXERCISE 2 / STEP 2", "Check the four rules and give a verdict",
      task("Copy the template. Replace every [bracket] with your numbers from Step 1 and your own words. The example shows a finished answer.")
      + two(tbox("TEMPLATE",
                 "Rule 1: our first customers are [who], [number] people.\n"
                 "Rule 2: we do [the main job] for $[price] instead of $[leader's price]; we leave out [what we do not offer].\n"
                 "Rule 3: the leader earns $[number] per customer; copying us earns $[number].\n"
                 "Rule 4: first we [first step]; later we [how we move up].\n"
                 "Verdict: [go / do not go], because [one sentence]."),
            tbox("WORKED EXAMPLE: WASHGO ($3 DORM WASHING MACHINES; LAUNDRY SHOPS CHARGE $15 A BAG)",
                 "Rule 1: our first customers are the 6,000 dorm students who wash clothes by hand.\n"
                 "Rule 2: one load of clothes for $3 instead of $15; we leave out ironing and folding.\n"
                 "Rule 3: the laundry shop earns $7 a bag; copying us earns $1 a load.\n"
                 "Rule 4: first machines in two dorms; later dryers and an app that shows free machines.\n"
                 "Verdict: go, because 6,000 students are not served and laundry shops will not fight for them.")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "30,000 non-consumers; salons earn 5 times more per haircut",
      '<div class="card good">' + ul([
          "<b>Row 1:</b> <b>30,000</b>. <b>Row 2:</b> <b>$15</b>. <b>Row 3:</b> <b>$3</b>. <b>Row 4:</b> <b>5 times</b>.",
          "<b>Row 5:</b> <b>3,000</b> haircuts. <b>Row 6:</b> <b>$9,000</b>. <b>Row 7:</b> $108,000 - $18,000 = <b>$90,000</b>.",
          "<b>Rule 1:</b> the 30,000 men at home, plus salon customers who only want a quick cut. "
          "<b>Rule 2:</b> a clean haircut for $8, without washing, styling, or booking.",
          "<b>Rule 3:</b> salons earn 5 times more per haircut and will not copy a $3-profit model. "
          "<b>Rule 4:</b> start with one shop, then add stations or simple extras such as beard trims.",
          "<b>Verdict:</b> go."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Should Sweet Slice fight Royal Cakes head-on?",
      task("Help Lily choose A or B for the next 12 months. <b>Step 1:</b> calculate (next slide). <b>Step 2:</b> write a memo to the investor. "
           "<b>Step 3:</b> present it in 2 minutes.")
      + two(flexcard("Option A: Go after Royal's customers", "<p>Hire a top pastry chef; decorated whole cakes for <b>$30</b>, "
                     "<b>$10</b> profit each. Chef and ads: <b>$20,000</b> once.</p>"
                     "<p>Expect <b>600</b> of Royal's 2,000 cakes a month; only <b>200</b> if Royal cuts its price.</p>",
                     "card", "HEAD-ON"),
            flexcard("Option B: Serve non-consumers first", "<p>Keep <b>$5</b> slices, <b>$2</b> profit each. Ads on campus: <b>$5,000</b> once.</p>"
                     "<p>Expect <b>10%</b> of the 8,000 non-consumers to become regular customers, each buying <b>3</b> slices a month.</p>",
                     "card", "DISRUPTION")),
      "EXERCISE 3 / SCENARIO: 12 MONTHS")

slide("EXERCISE 3 / STEP 1", "Fill in the table before you decide (Tools 1 to 3)",
      task("Calculate each row and write the result in the last column. Later rows use earlier rows.")
      + worksheet([
          ("A: profit a month (600 cakes)", "600 x $10"),
          ("A: profit over 12 months", "12 x row 1 - $20,000"),
          ("A: profit a month if Royal cuts its price", "200 x $10"),
          ("A: 12 months if Royal cuts its price", "12 x row 3 - $20,000"),
          ("B: regular customers", "8,000 x 10%"),
          ("B: slices a month", "row 5 x 3"),
          ("B: profit a month", "row 6 x $2"),
          ("B: profit over 12 months", "12 x row 7 - $5,000"),
          ("Royal earns $15 a cake. Would copying B earn it more or less? Copying A? (Tool 2)", "compare"),
      ], td='style="font-size:25px;padding:.05in .1in;"'),
      "EXERCISE 3 / CALCULATION TABLE")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to the investor (Tool 4)",
      task("Copy the template. Replace every [bracket] with your choice, your numbers from Step 1, and your own words. "
           "The next slide shows a finished memo for QuickCut.")
      + '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [name], [role]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next three months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway"><b>Step 3:</b> give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "QuickCut: open shops for men who cut their own hair?",
      tmpl("To: Oliver Hayes, investor, QuickCut\n"
           "1. Decision and evidence: We should open $8 haircut shops for the 30,000 men who cut their hair at home (Rule 1), because salons "
           "earn $15 a haircut and will not copy a $3-profit model (Rule 3).\n"
           "2. Biggest risk and trade-off: The weakest point is that men may keep cutting their hair at home. We give up the higher price "
           "of a salon service to win customers nobody serves.\n"
           "3. Next step and decision rule: In the next three months we will open one shop and count haircuts per day. "
           "We will open the other two shops only if the first shop does at least 30 haircuts a day."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Same profit if all goes well; only one plan depends on the leader",
      '<div class="card">' + ul([
          "<b>Row 1:</b> <b>$6,000</b>. <b>Row 2:</b> $72,000 - $20,000 = <b>$52,000</b>.",
          "<b>Row 3:</b> <b>$2,000</b>. <b>Row 4:</b> $24,000 - $20,000 = <b>$4,000</b>.",
          "<b>Row 5:</b> <b>800</b>. <b>Row 6:</b> <b>2,400</b> slices. <b>Row 7:</b> <b>$4,800</b>. <b>Row 8:</b> $57,600 - $5,000 = <b>$52,600</b>.",
          "<b>Row 9:</b> copying B earns Royal <b>less</b> ($2 a slice against $15 a cake), so Royal will probably ignore it. "
          "A is the same kind of cake as Royal's, so Royal can easily fight back by cutting its price."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Both options earn about $52,000 if all goes well, but A falls to $4,000 if Royal fights back. B does not depend on Royal.",
          "Usually chooses Option B (Rules 1 and 3).",
          "Names a real risk: fewer than 10% of non-consumers may come, or each may buy fewer than 3 slices a month.",
          "Plans how to move up later: mini cakes, then whole cakes (Rule 4).",
          'Gives a decision rule: "If we sell fewer than 450 slices a week by the end of month 3, we will change the price or the menu."']) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain disruption and how it differs from sustaining innovation.</p></div>'
      "<div class=\"card\"><div class=\"n\">02</div><p>Find non-consumers and use the leader's profit test.</p></div>"
      '<div class="card"><div class="n">03</div><p>Compare a head-on attack with a disruption plan and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Christensen, C. M., Raynor, M. E., &amp; McDonald, R. (2015). What is disruptive innovation? Harvard Business Review, 93(12), 44-53.</p>'
      '<p class="ref">Newsweek (2021). Fact check: Did Blockbuster turn down the chance to buy Netflix for $50 million?</p>'
      '<p class="ref">Safaricom (2017). The M-PESA wonder: how it all began.</p>'
      '<p class="ref">NBC News (2020, October 21). Quibi is shutting down just months after launching.</p>'
      '<p class="ref">TidBITS (2001, July 16). Where Webvan went wrong.</p></div>',
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
