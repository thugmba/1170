"""Build the Session 3.4 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_3_4_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "3.4"
TITLE = "The Open Ecosystem Strategy"
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
          two(flexcard("The facts", ul(facts), "card", "BLOCKWORLD MAP MARKET"),
              flexcard("Your questions", ul(questions), "card", "SHOW YOUR CALCULATION")),
          f"SESSION {SESSION} / {footer} PRACTICE")


# Cover and situation
slide("MODULE 3 / COMPETITIVE STRATEGY &amp; INNOVATION FRAMEWORKS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_3_4_foodsquare_ecosystem_hanji.png" '
      'alt="Adam, owner of the Food Square food court, asks whether to let outside cooks open stalls.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "Food Square: more requests than one kitchen can cook",
      two(flexcard("Until now", ul([
          "Adam owns <b>Food Square</b>, a food court near campus with 200 seats.",
          "His <b>own kitchen</b> cooks all the food: one menu of 12 dishes.",
          "Students ask for ramen, tacos, bubble tea, desserts...",
          "Each new dish needs a new cook and equipment."]), "card", "THE PROBLEM"),
          flexcard("The numbers", '<table style="font-size:26px;">'
                   "<tr><td>Regular customers</td><td><b>400</b></td></tr>"
                   "<tr><td>Profit per regular, per year</td><td><b>$600</b></td></tr>"
                   "<tr><td>Kinds of food students want</td><td><b>30</b></td></tr>"
                   "<tr><td>New dishes a year</td><td><b>3</b></td></tr>"
                   "<tr><td>Regulars who left last year</td><td><b>60</b></td></tr>"
                   "<tr><td>Cooks asking for a stall</td><td><b>12</b></td></tr></table>", "card", "FOOD SQUARE"))
      + '<div class="takeaway">Adam\'s question: keep cooking everything himself, or let outside cooks open stalls?</div>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", f"What is the {TITLE[4:]}?",
      '<p class="para">A company opens its product so that outside companies, called <b>partners</b>, can build on it. '
      "The company becomes a <b>platform</b>: it <b>keeps the core</b> and <b>sets the rules</b>, and many partners add features, apps, "
      "or ideas it could never build alone. Customers get more choice, partners get customers, and the platform becomes harder to leave.</p>"
      '<div class="takeaway">Use it when customers want more than your team can build, outside companies can build it, '
      "and you can protect the core and the customers.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Ecosystem, partner, API",
      term("Ecosystem", "A group of companies that work around one platform and help each other's customers.",
           "Food Square plus the cooks who run stalls inside it.")
      + term("Partner<br><span style=\"font-size:24px;color:#526174;\">(outside developer)</span>",
             "An outside company or person that builds something on your platform.", "a ramen cook who runs a stall in Food Square.")
      + term("API", "Rules that let one program safely use parts of another program.",
             "Food Square's shared ordering screen is similar: each stall adds its own menu."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Core, revenue share, open innovation",
      term("Core", "The central parts the platform keeps for itself, because they hold its value and customers' trust.",
           "Food Square keeps the payment counter, the customer list, and the food-safety rules.")
      + term("Revenue share", "The part of a partner's sales that the platform keeps.",
             "a stall sells $1,000; Food Square keeps 20%: $200 for Food Square, $800 for the cook.")
      + term("Open innovation", "Using ideas and work from people outside the company, such as customers, fans, or partners.",
             "a snack company lets fans vote for a new chip flavor."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 2")

# Rules
rules = [
    ("Rule 1", "Open the edges, keep the core",
     "Let partners add features around your product, but keep the parts that hold your value and customers' trust.",
     "Food Square opens 8 stall spaces to outside cooks. The payment counter, the customer list, and the food-safety rules stay with Food Square.",
     "Opening everything, including payments and the customer list, with no control. Partners can misuse it, and the platform loses its value."),
    ("Rule 2", "Make it worth it for partners to join",
     "Partners build only if they can earn more than it costs them. Give them customers, tools, and a fair share of the money.",
     "Food Square keeps 0% of the first $10,000 each stall sells in a year, and 15% after that. New cooks get free equipment for a month.",
     "Taking a large share of every sale, so cooks cannot cover their costs. No cooks join, and the stalls stay empty."),
    ("Rule 3", "Set clear rules and check quality",
     "Customers trust the platform, not each small partner. Check partners before they start, and protect customers.",
     "Every cook passes a food-safety check and a taste test before opening, and Food Square checks every stall once a month.",
     "Letting anyone in without checks. One stall that makes customers sick damages trust in the whole food court."),
    ("Rule 4", "Do not compete unfairly with your partners",
     "Partners invest time and money because they trust you. Do not copy their products, change the rules suddenly, or push them out.",
     "Before his own kitchen adds a dish, Adam checks that it does not copy a stall's menu. He tells cooks six months before any rule change.",
     "Copying the most popular stall's dish at a lower price, or ending a cook's contract with no warning. Other cooks stop joining."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_3_4_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "The Shopify App Store", "good",
     "Shopify helps millions of businesses run online stores. Instead of building every feature itself, it lets outside developers sell "
     "apps to Shopify stores through its API and app store. In 2021, Shopify announced that developers would keep all of their first "
     "$1 million in app sales each year, and pay only 15% after that, instead of 20% before.",
     ["Shopify keeps checkout and payments; partners add thousands of features. <b>(Rule 1)</b>",
      "A low share lets small developers earn enough to keep building. <b>(Rule 2)</b>",
      "Shopify reviews apps before they are listed. <b>(Rule 3)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "LEGO Ideas", "good",
     "LEGO lets fans post designs for new LEGO sets online. If a design gets 10,000 supporters, LEGO reviews it. "
     "If LEGO makes the set, the fan designer receives a small share (1%) of its sales.",
     ["New ideas from fans; LEGO keeps design checks, production, and the brand. <b>(Rule 1)</b>",
      "Fans get public credit and a share of sales. <b>(Rule 2)</b>",
      "10,000 supporters plus LEGO's review keep quality high. <b>(Rule 3)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Twitter and its developers", "bad",
     "For years, outside apps such as Tweetbot and Twitterrific gave people other ways to read Twitter. In January 2023, Twitter suddenly "
     "cut these apps off with no warning, then changed its rules to ban them. Twitterrific shut down. In 2023, Twitter also stopped free "
     "access to its API and began charging developers (from $100 a month).",
     ["Changed the rules suddenly and pushed out partners who helped it grow. <b>(Rule 4)</b>",
      "Developers lost their business overnight, so others stopped trusting the platform. <b>(Rule 2)</b>",
      "Users who liked these apps lost them too."], "Why it is bad"),
    ("BAD EXAMPLE 2", "Facebook and Cambridge Analytica", "bad",
     "In 2014, a personality-quiz app on Facebook collected data from its users and their friends, up to 87 million people. "
     "The data was passed to Cambridge Analytica, a political consulting company. After this became public in 2018, the U.S. Federal "
     "Trade Commission fined Facebook $5 billion in 2019, partly for failing to control what outside apps did with users' data.",
     ["Outside apps could reach far more data than they needed. <b>(Rule 1)</b>",
      "Facebook did not check well what apps did with the data. <b>(Rule 3)</b>",
      "Users lost trust in the whole platform, not only in one app."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Shopify App Store</td><td style="color:#2f6b47;font-weight:700">Good</td><td>A deal small developers want (Rule 2)</td></tr>'
      '<tr><td>LEGO Ideas</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Open to fans, with clear checks (Rules 1 and 3)</td></tr>'
      '<tr><td>Twitter</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Pushed out its partners overnight (Rule 4)</td></tr>'
      '<tr><td>Facebook</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Opened user data without control (Rules 1 and 3)</td></tr></table>'
      '<div class="takeaway">An ecosystem grows when partners can earn and trust you, and customers stay safe.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Years to build alone",
      two(flexcard("Formula", "<p>Years to build alone = things customers want / things your team can add per year</p>",
                   "card", "USED IN EXERCISE 3"),
          flexcard("Example: Food Square", ul([
              "Students have also asked for 12 kinds of desserts and drinks.",
              "The kitchen can add 2 a year.",
              "12 / 2 = 6 years."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("TOOL PRACTICE / THE CASE", "Practice case: BlockWorld opens a map market",
      two(flexcard("Until now", ul([
          "BlockWorld is a phone game: players build worlds with blocks.",
          "Only BlockWorld's <b>own designers</b> make new maps (game levels).",
          "Players get bored waiting for new maps."]), "card", "CLOSED"),
          flexcard("The plan: a Creator Market", ul([
              "<b>Outside creators</b> (skilled players, small studios) make maps and sell them inside the game.",
              "BlockWorld keeps a <b>share</b> of each sale.",
              "BlockWorld keeps the game, payments, and the rules."]), "card", "OPEN"))
      + '<div class="takeaway">Each tool slide uses Food Square as its example. After each tool, you practice the same tool on BlockWorld. '
      "Across the four practices, decide whether BlockWorld should open the market, and on what terms.</div>",
      f"SESSION {SESSION} / PRACTICE CASE")

practice("Practice Tool 1: Can BlockWorld's team keep up alone?",
         ["Players voted for <b>60</b> new map ideas this year.",
          "BlockWorld has <b>4</b> designers.",
          "Each designer makes <b>one map every 2 months</b>.",
          "Players finish a new map in about <b>one week</b>."],
         ["<b>(a)</b> How many maps does the team make in a year?",
          "<b>(b)</b> How many years to make all 60 maps alone?",
          "<b>(c)</b> BlockWorld wants 52 new maps a year. How many <b>more</b> designers does it need? (Round up.)",
          "<b>(d)</b> Is building alone realistic? Explain in one sentence."],
         "TOOL 1")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Value of customers kept and won",
      two(flexcard("Formula", "<p>Value = (customers who stay instead of leaving + new customers) x profit per customer per year</p>",
                   "card", "USED IN EXERCISE 3"),
          flexcard("Example: Food Square", ul([
              "A new ramen stall keeps 5 regular customers who would have left and brings 10 new ones.",
              "Each brings $600 a year: (5 + 10) x $600 = $9,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

practice("Practice Tool 2: Is the market worth its cost?",
         ["<b>10,000</b> paying players spend <b>$24</b> a year each.",
          "Last year <b>2,000</b> of them quit, mostly because they were bored.",
          "Expected: the market stops <b>25%</b> of these from quitting and brings <b>800</b> new paying players.",
          "Running the market costs <b>$20,000</b> a year."],
         ["<b>(a)</b> How many players does BlockWorld keep?",
          "<b>(b)</b> Value of players kept and won.",
          "<b>(c)</b> The value if the market stops only <b>10%</b> and brings only <b>300</b> new players.",
          "<b>(d)</b> Does each case cover the $20,000 cost?"],
         "TOOL 2")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Revenue share for the platform and the partner",
      two(flexcard("Formula", "<p>Platform's share = partner's sales x share %</p><p>Partner keeps = partner's sales - platform's share</p>",
                   "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: Food Square", ul([
              "The ramen stall sells $30,000 a year; Food Square keeps 15%.",
              "Food Square gets $4,500; the cook keeps $25,500."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

practice("Practice Tool 3: Which share keeps creators building?",
         ["A creator sells maps for <b>$2</b> each and sells <b>6,000</b> a year.",
          "Making the maps costs the creator <b>$9,000</b> a year (time and software).",
          "Three rules: keep <b>30%</b>; keep <b>20%</b>; or keep <b>0% of the first $5,000</b> and 20% after that."],
         ["<b>(a)</b> Under each rule: what BlockWorld gets and what the creator keeps.",
          "<b>(b)</b> Under which rules does the creator earn more than its cost?",
          "<b>(c)</b> At what share would the creator exactly break even?",
          "<b>(d)</b> Which rule should BlockWorld choose? Explain with Rule 2."],
         "TOOL 3")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>"
                   "<p><i>Food Square: Adam gives up the full profit of cooking everything himself (he keeps only a share of stall sales) "
                   "to offer many more kinds of food much faster.</i></p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Food Square: "If a stall sells less than $2,000 a month for three months in a row, we will give its space to another cook."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

practice("Practice Tool 4: Should BlockWorld check every map?",
         ["Creators will publish about <b>4,000</b> maps a year.",
          "Checking costs <b>$1</b> per map.",
          "Without checks, <b>2%</b> of maps are broken or have bad content.",
          "Each bad map makes about <b>15</b> paying players quit ($24 a year each)."],
         ["<b>(a)</b> How many bad maps a year without checks?",
          "<b>(b)</b> What is the value lost from bad maps?",
          "<b>(c)</b> Trade-off: BlockWorld pays $____ to protect $____. Which rule is this?",
          "<b>(d)</b> Write a decision rule with a number, a time, and an action."],
         "TOOL 4")

slide("TOOL PRACTICE / CHECK YOUR ANSWERS", "BlockWorld, Tools 1 and 2: too slow alone; worth it only if players stay",
      '<div class="card good">' + ul([
          "<b>Tool 1:</b> (a) 6 maps per designer a year, so 4 x 6 = <b>24</b>. (b) 60 / 24 = <b>2.5 years</b>. "
          "(c) 52 / 6 = 8.7, so 9 in total: <b>5 more</b>.",
          "(d) No: hiring 5 more designers is slow and expensive, while many outside creators can make maps right away.",
          "<b>Tool 2:</b> (a) 2,000 x 25% = <b>500</b>. (b) (500 + 800) x $24 = <b>$31,200</b>. "
          "(c) (200 + 300) x $24 = <b>$12,000</b>.",
          "(d) The first case covers the cost ($11,200 left); the second does not (<b>-$8,000</b>). "
          "The market works only if it really keeps players and brings new ones."]) + "</div>",
      "TOOL PRACTICE / ANSWER KEY 1 OF 2")

slide("TOOL PRACTICE / CHECK YOUR ANSWERS", "BlockWorld, Tools 3 and 4: a fair share and checks",
      '<div class="card good">' + ul([
          "<b>Tool 3:</b> (a) sales $12,000. 30%: <b>$3,600</b> / creator <b>$8,400</b>. 20%: <b>$2,400</b> / <b>$9,600</b>. "
          "0% of first $5,000: 20% x $7,000 = <b>$1,400</b> / <b>$10,600</b>.",
          "(b) Only 20% and the 0%-first rule. (c) $3,000 / $12,000 = <b>25%</b>. "
          "(d) The 0%-first rule: small creators clearly earn more than they spend, so many join (Rule 2).",
          "<b>Tool 4:</b> (a) 4,000 x 2% = <b>80</b>. (b) 80 x 15 x $24 = <b>$28,800</b>. "
          "(c) pay <b>$4,000</b> to protect <b>$28,800</b>: <b>Rule 3</b>.",
          '(d) Example: "If more than 1% of live maps are reported as broken in the first three months, we will add a second review step."']) + "</div>",
      "TOOL PRACTICE / ANSWER KEY 2 OF 2")

# Exercise 1
E1_TD = 'style="font-size:24px;padding:.06in .09in;"'
E1_ROWS = [
    ("<i>Example: an e-book store lets small publishers sell their own books</i>", "<i>Small publishers</i>",
     "<i>Payments, price rules, reading app</i>", "<i>Open</i>", "<i>Rule 1</i>"),
    ("(a) A game console lets outside studios sell games in its online store", "", "", "", ""),
    ("(b) A bubble tea shop hires one more staff member", "", "", "", ""),
    ("(c) A food delivery app lets restaurants list menus and keeps a share of each order", "", "", "", ""),
    ("(d) A phone maker makes its phones work only with its own chargers", "", "", "", ""),
    ("(e) A music app lets independent musicians upload songs and pays them per play", "", "", "", ""),
    ("(f) A snack company invites fans to send ideas for new chip flavors", "", "", "", ""),
]
slide("EXERCISE 1 / EASY / 20 MIN", "Open ecosystem or not? Fill in the table",
      task("For each move, ask: <b>Does someone outside the company add something?</b> <b>What does the company keep?</b> "
           "Someone outside adds something + the company keeps the core = open ecosystem.")
      + '<table style="table-layout:fixed;"><colgroup><col style="width:40%"><col style="width:16%"><col style="width:18%">'
      '<col style="width:13%"><col style="width:13%"></colgroup>'
      "<tr><th>MOVE</th><th>WHO OUTSIDE ADDS?</th><th>WHAT THE COMPANY KEEPS</th><th>ANSWER</th><th>WHY (RULE)</th></tr>"
      + "".join("<tr>" + "".join(f"<td {E1_TD}>{c}</td>" for c in r) + "</tr>" for r in E1_ROWS) + "</table>",
      "EXERCISE 1 / WORKSHEET")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Who outside adds something, and what does the company keep?",
      '<table style="table-layout:fixed;"><colgroup><col style="width:22%"><col style="width:20%"><col style="width:32%"><col style="width:26%"></colgroup>'
      "<tr><th>MOVE</th><th>WHO OUTSIDE ADDS?</th><th>COMPANY KEEPS</th><th>ANSWER</th></tr>"
      "<tr><td>(a) Game store</td><td>Studios</td><td>The store and its rules</td><td>Open (Rule 1)</td></tr>"
      "<tr><td>(b) One more staff</td><td>Nobody</td><td>-</td><td>Not open</td></tr>"
      "<tr><td>(c) Delivery app</td><td>Restaurants</td><td>Payments, delivery rules, data</td><td>Open (Rules 1, 2)</td></tr>"
      "<tr><td>(d) Own chargers only</td><td>Nobody</td><td>Closed to outsiders</td><td>Not open</td></tr>"
      "<tr><td>(e) Music app</td><td>Musicians</td><td>Player, payments, rules</td><td>Open (Rules 1, 2)</td></tr>"
      "<tr><td>(f) Chip flavors</td><td>Fans (ideas)</td><td>Tests, production, brand</td><td>Open innovation</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Design a deal that partners want: CupCorner",
      task("Which revenue-share rule should CupCorner choose? <b>Step 1:</b> fill in the calculation table (next slide). "
           "<b>Step 2:</b> recommend a rule with the template (slide after).")
      + two(flexcard("The partner", ul([
          "<b>CupCorner</b> is a chain of <b>20</b> cafés.",
          "<b>Rosie's Bakery</b>, a small local bakery, wants to sell its pastries in all 20 cafés.",
          "Each café sells <b>10</b> of Rosie's pastries a month, at <b>$4</b> each.",
          "Baking and delivery cost the bakery <b>$8,000</b> a year."]), "card", "SCENARIO"),
          flexcard("Three rules", ul([
              "Keep <b>30%</b> of the bakery's sales.",
              "Keep <b>15%</b>.",
              "Keep <b>0% of the first $10,000</b> a year (15% after that)."]), "card", "REVENUE SHARE")),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / STEP 1", "Fill in the table: one row at a time",
      task("Calculate each row and write the result in the last column. Later rows use earlier rows.")
      + worksheet([
          ("Pastries sold in a year", "20 x 10 x 12"),
          ("Pastry sales in a year", "row 1 x $4"),
          ("Bakery keeps if CupCorner keeps 30%", "row 2 - row 2 x 30%"),
          ("Bakery keeps if CupCorner keeps 15%", "row 2 - row 2 x 15%"),
          ('Bakery keeps with "0% of the first $10,000"', "is row 2 below $10,000?"),
          ("Which rules leave the bakery more than its $8,000 cost?", "compare rows 3 to 5"),
          ("What CupCorner gives up with the third rule instead of 30%", "row 2 x 30%"),
      ], td='style="font-size:28px;padding:.07in .1in;"'),
      "EXERCISE 2 / CALCULATION TABLE")

slide("EXERCISE 2 / STEP 2", "Recommend a rule",
      task("Copy the template. Replace every [bracket] with your numbers from Step 1 and your own words. The example shows a finished answer.")
      + two(tbox("TEMPLATE",
                 "Under [rule], the partner keeps $[amount], which is [more / less] than its cost of $[cost],\n"
                 "so partners [will / will not] want to join.\n"
                 "We should choose [rule], because [Rule 2 reason],\n"
                 "even though we give up $[amount] a year from this partner."),
            tbox("WORKED EXAMPLE: A BOOKSTORE SELLS AN ARTIST'S POSTCARDS ($20,000 SALES, $15,000 COST; 30% OR 10%)",
                 "Under 30%, the artist keeps $14,000, which is less than the cost of $15,000, so artists will not want to join.\n"
                 "Under 10%, the artist keeps $18,000, which is more than the cost.\n"
                 "We should choose 10%, because partners must earn more than they spend (Rule 2), "
                 "even though we give up $4,000 a year from this artist ($6,000 - $2,000).")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Only a low share leaves the partner a profit",
      '<div class="card good">' + ul([
          "<b>Row 1:</b> <b>2,400</b> pastries. <b>Row 2:</b> <b>$9,600</b>.",
          "<b>Row 3:</b> $9,600 - $2,880 = <b>$6,720</b>. <b>Row 4:</b> $9,600 - $1,440 = <b>$8,160</b>. "
          "<b>Row 5:</b> <b>$9,600</b> (below $10,000, so 0%).",
          "<b>Row 6:</b> only 15% and the 0%-first rule; 15% leaves just $160. <b>Row 7:</b> <b>$2,880</b>.",
          "<b>Step 2:</b> choose \"0% of the first $10,000\": small partners must earn more than they spend (Rule 2). "
          "CupCorner gives up $2,880 a year for more local partners and more choice."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Cook everything yourself, or open stalls?",
      task("Help Adam choose A or B for the next 12 months. <b>Step 1:</b> calculate (next slide). <b>Step 2:</b> write a memo. "
           "<b>Step 3:</b> present it in 2 minutes.")
      + '<p style="font-size:27px;margin:0 0 .12in;color:#172033;"><b>Today:</b> 400 regulars / $600 profit a year each / 30 kinds wanted / 3 new dishes a year.</p>'
      + two(flexcard("Option A: Cook more yourself", "<p>One more cook and new equipment: <b>$48,000</b> a year. The kitchen adds <b>3</b> more dishes a year.</p>"
                     "<p>Expect <b>20</b> fewer regulars to leave and <b>20</b> new regulars.</p>", "card", "BUILD ALONE"),
            flexcard("Option B: Open stalls to outside cooks", "<p>8 stall spaces and a shared ordering screen: <b>$15,000</b> once; "
                     "food-safety inspector <b>$500</b> a month.</p>"
                     "<p>Expect 8 cooks, <b>30</b> fewer leaving, <b>40</b> new regulars. Stall sales <b>$15,000</b> a month; Food Square keeps <b>10%</b>.</p>",
                     "card", "OPEN ECOSYSTEM")),
      "EXERCISE 3 / SCENARIO: 12 MONTHS")

slide("EXERCISE 3 / STEP 1", "Fill in the table before you decide (Tools 1 to 3)",
      task("Calculate each row and write the result in the last column. Later rows use earlier rows.")
      + worksheet([
          ("Years to add all 30 kinds alone, today (Tool 1)", "30 / 3"),
          ("Years with one more cook", "30 / 6"),
          ("A: value of customers kept and won (Tool 2)", "(20 + 20) x $600"),
          ("A: result", "row 3 - $48,000"),
          ("B: costs", "$15,000 + 12 x $500"),
          ("B: value of customers kept and won (Tool 2)", "(30 + 40) x $600"),
          ("B: revenue share (Tool 3)", "12 x $15,000 x 10%"),
          ("B: result", "row 6 + row 7 - row 5"),
          ("B if only 3 cooks come: 10 fewer leave, 10 new, sales $5,000 a month",
           "(10 + 10) x $600 + 12 x $5,000 x 10% - row 5"),
      ], td='style="font-size:25px;padding:.05in .1in;"'),
      "EXERCISE 3 / CALCULATION TABLE")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Adam (Tool 4)",
      task("Copy the template. Replace every [bracket] with your choice, your numbers from Step 1, and your own words. "
           "The next slide shows a finished memo for CupCorner.")
      + '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [owner name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next six months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway"><b>Step 3:</b> give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "CupCorner: which revenue share?",
      tmpl("To: Grace Parker, CEO, CupCorner\n"
           "1. Decision and evidence: We should keep 0% of the first $10,000 each partner sells, because small partners must earn "
           "more than they spend (Rule 2): Rosie's Bakery keeps $9,600, above its $8,000 cost.\n"
           "2. Biggest risk and trade-off: The weakest point is that we earn almost nothing from small partners at first. "
           "We give up $2,880 a year from this bakery to attract more local partners and give customers more choice.\n"
           "3. Next step and decision rule: In the next six months we will invite 10 local bakers and count how many sell in our cafés. "
           "We will change this decision if fewer than 4 bakers are selling by then."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Opening wins if cooks come, and loses if they do not",
      '<div class="card">' + ul([
          "<b>Row 1:</b> <b>10 years</b>. <b>Row 2:</b> <b>5 years</b>: cooking everything alone is too slow.",
          "<b>Row 3:</b> <b>$24,000</b>. <b>Row 4:</b> $24,000 - $48,000 = <b>-$24,000</b>.",
          "<b>Row 5:</b> <b>$21,000</b>. <b>Row 6:</b> <b>$42,000</b>. <b>Row 7:</b> <b>$18,000</b>. "
          "<b>Row 8:</b> $42,000 + $18,000 - $21,000 = <b>$39,000</b>.",
          "<b>Row 9:</b> $12,000 + $6,000 - $21,000 = <b>-$3,000</b>."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Usually chooses Option B, but says the key question is Rule 2: will cooks want to open stalls?",
          "Protects the core: the payment counter and the customer list stay with Food Square (Rule 1).",
          "Plans a cook-friendly share and food-safety checks (Rules 2 and 3).",
          'Gives a decision rule: "If fewer than 5 stalls are open after six months, we will lower our share or give free equipment to new cooks."']) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain an open ecosystem with the words platform, partner, API, core, and revenue share.</p></div>'
      '<div class="card"><div class="n">02</div><p>Design a revenue share that partners want to join.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare building alone with opening to partners and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Chesbrough, H. W. (2003). Open Innovation. Harvard Business School Press.</p>'
      '<p class="ref">Parker, G. G., Van Alstyne, M. W., &amp; Choudary, S. P. (2016). Platform Revolution. W. W. Norton.</p>'
      '<p class="ref">CNBC (2021, June 29). Shopify cuts app store fees for developers on first $1 million in revenue.</p>'
      '<p class="ref">LEGO. What happens to my product idea after I reach 10,000 supporters?</p>'
      '<p class="ref">TechCrunch (2023, January 19). Twitter third-party apps Tweetbot and Twitterrific stop working.</p>'
      '<p class="ref">Federal Trade Commission (2019, July 24). FTC imposes $5 billion penalty on Facebook.</p></div>',
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
