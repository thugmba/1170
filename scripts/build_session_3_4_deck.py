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


# Cover and situation
slide("MODULE 3 / COMPETITIVE STRATEGY &amp; INNOVATION FRAMEWORKS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_3_4_shopnest_ecosystem_hanji.png" '
      'alt="Arjun, founder of ShopNest, asks whether to let outside developers build apps for his shops.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "ShopNest: more requests than one team can build",
      '<p class="statement" style="font-weight:400;">ShopNest lets small shops build their own online store. Arjun is its founder. '
      "Shops keep asking for new features, and some leave for bigger store builders.</p>"
      "<table><tr><th>SHOPNEST</th><th style=\"text-align:right\">VALUE</th></tr>"
      '<tr><td>Shops using ShopNest</td><td class="num">400</td></tr>'
      '<tr><td>Price per shop</td><td class="num">$50 a month ($600 a year)</td></tr>'
      '<tr><td>Features shops have asked for</td><td class="num">30</td></tr>'
      '<tr><td>Features the team can build in a year</td><td class="num">3</td></tr>'
      '<tr><td>Shops that left last year, mostly for missing features</td><td class="num">60</td></tr>'
      '<tr><td>Small software companies asking to build add-ons</td><td class="num">12</td></tr></table>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", f"What is the {TITLE[4:]}?",
      '<p class="para">A company <b>opens its product so that outside companies, called partners, can build on it</b>. '
      "It becomes a <b>platform</b>: it keeps the core of the product and sets the rules, and many partners add features, apps, "
      "or ideas that the company could never build alone. Customers get more choice, partners get customers, and the platform "
      "becomes harder to leave.</p>"
      '<div class="takeaway">Use it when customers want more features than your team can build, outside companies are able and willing '
      "to build them, and you can protect the core and the customers.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Ecosystem, partner, API",
      term("Ecosystem", "A group of companies that work around one platform and help each other's customers.",
           "ShopNest plus the companies that build add-ons for ShopNest shops.")
      + term("Partner<br><span style=\"font-size:24px;color:#526174;\">(outside developer)</span>",
             "An outside company that builds something on your platform.", "a small company that builds a loyalty-points app.")
      + term("API", "Application programming interface: rules that let one program safely use parts of another program.",
             "through ShopNest's API, a delivery app can read a shop's orders."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Core, revenue share, open innovation",
      term("Core", "The central parts the platform keeps for itself, because they hold its value and customers' trust.",
           "ShopNest keeps payments and customer data.")
      + term("Revenue share", "The part of a partner's sales that the platform keeps.",
             "an app earns $1,000; the platform keeps 20%: $200 for the platform, $800 for the partner.")
      + term("Open innovation", "Using ideas and work from people outside the company, such as customers, fans, or partners.",
             "a toy company lets fans send in designs for new sets."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 2")

# Rules
rules = [
    ("Rule 1", "Open the edges, keep the core",
     "Let partners add features around your product, but keep the parts that hold your value and customers' trust.",
     "ShopNest opens an API so partners can add delivery tracking, loyalty points, and gift cards. Payments and customer data stay with ShopNest.",
     "Opening everything, including payments and customer data, with no control. Partners can misuse it, and the platform loses its value."),
    ("Rule 2", "Make it worth it for partners to join",
     "Partners build only if they can earn more than it costs them. Give them customers, tools, and a fair share of the money.",
     "ShopNest keeps 0% of the first $10,000 each partner earns in a year, and 15% after that. Partners also get free test stores.",
     "Taking a large share of every sale, so partners cannot cover their costs. No partners join, and the app market stays empty."),
    ("Rule 3", "Set clear rules and check quality",
     "Customers trust the platform, not each small partner. Review apps before they go live, and protect customers' data.",
     "Every app is tested before it appears in the ShopNest app market, and apps can read only the data that a shop allows.",
     "Letting any app in without checks. One bad app that leaks data or breaks stores damages trust in the whole platform."),
    ("Rule 4", "Do not compete unfairly with your partners",
     "Partners invest time and money because they trust you. Do not copy their apps, change the rules suddenly, or push them out.",
     "When ShopNest plans a new feature, it tells partners six months ahead and does not copy any partner's app.",
     "Copying the most popular partner app, or cutting partners off with no warning. Other partners stop building."),
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
      two(flexcard("Formula", "<p>Years to build alone = features customers want / features your team builds per year</p>",
                   "card", "USED IN EXERCISE 3"),
          flexcard("Example: a booking app", ul([
              "Customers want 20 features.",
              "The team builds 4 a year.",
              "20 / 4 = 5 years."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Value of customers kept and won",
      two(flexcard("Formula", "<p>Value = (customers who stay instead of leaving + new customers) x revenue per customer per year</p>",
                   "card", "USED IN EXERCISE 3"),
          flexcard("Example: a booking app", ul([
              "Keeps 10 customers who would have left; wins 15 new ones.",
              "Each pays $300 a year.",
              "(10 + 15) x $300 = $7,500."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Revenue share for the platform and the partner",
      two(flexcard("Formula", "<p>Platform's share = partner's sales x share %</p><p>Partner keeps = partner's sales - platform's share</p>",
                   "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: an app", ul([
              "The app sells $12,000 a year; the platform keeps 20%.",
              "Platform: $2,400. Partner keeps: $9,600."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 10 partner apps are live after six months, we will lower our revenue share."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Open ecosystem or not?",
      '<p class="statement">Six companies plan a move:</p><div class="card">' + ul([
          "(a) A game console lets outside studios sell games in its online store.",
          "(b) A bank lets budgeting apps read a customer's spending, only with permission, through an API.",
          "(c) A restaurant hires one more cook.",
          "(d) A map company lets taxi apps use its maps for a fee.",
          "(e) A phone maker makes its phones work only with its own chargers.",
          "(f) A toy company invites fans to send in designs for new toys."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Move [letter]: [open ecosystem / not open ecosystem], because\n"
               "[who outside the company builds or adds something, or nobody]\n"
               "and [what the company keeps or controls]."),
          tbox("WORKED EXAMPLE: TWO OTHER MOVES",
               "Move: an e-book store lets small publishers upload and sell their own books.\n"
               "Open ecosystem, because outside publishers add books, and the store keeps payments, pricing rules, and the reading app.\n"
               "Move: a bakery buys a bigger oven.\n"
               "Not open ecosystem, because nobody outside the company builds anything.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Who outside builds something, and what does the company keep?",
      "<table><tr><th>MOVE</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) Outside game studios</td><td>Open</td><td>Studios add games; the console keeps the store</td></tr>"
      "<tr><td>(b) Bank API for budget apps</td><td>Open</td><td>Apps build on data, with the customer's permission</td></tr>"
      "<tr><td>(c) One more cook</td><td>Not</td><td>Only grows its own work</td></tr>"
      "<tr><td>(d) Maps for taxi apps</td><td>Open</td><td>Taxi apps build on the maps</td></tr>"
      "<tr><td>(e) Own chargers only</td><td>Not</td><td>Closes the product to outsiders</td></tr>"
      "<tr><td>(f) Fan toy designs</td><td>Open</td><td>Open innovation: fans add ideas</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Design a deal that partners want: BookIt",
      two(flexcard("Scenario", ul([
          "BookIt: a booking platform used by <b>2,000</b> hair salons.",
          "A partner's reminder app: <b>$8</b> a month per salon; <b>5%</b> of salons expected to buy.",
          "The app costs the partner <b>$8,000</b> a year to build and run.",
          "Share rules: <b>30%</b>, <b>15%</b>, or <b>0% on the first $10,000</b> a year (15% after)."])),
          flexcard("Your steps", ul([
              "<b>Step 1:</b> Salons = 2,000 x 5% = ____. Sales = salons x $8 x 12 = $____. Partner keeps at 30% = $____; "
              "at 15% = $____; with 0% on the first $10,000 = $____.",
              "<b>Step 2:</b> Which rules leave the partner more than $8,000?",
              "<b>Step 3:</b> Recommend with the template."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Under [rule], the partner keeps $[amount], which is [more / less] than its cost of $[cost],\n"
               "so partners [will / will not] want to build for us.\n"
               "We should choose [rule], because [Rule 2 reason],\n"
               "even though we give up $[amount] a year from this app."),
          tbox("WORKED EXAMPLE: A RECIPE PLATFORM",
               "A meal-planner app sells $20,000 a year and costs its maker $15,000.\n"
               "Under 30%, the partner keeps $14,000, less than its cost, so partners will not want to build for us.\n"
               "Under 10%, the partner keeps $18,000, more than its cost.\n"
               "We should choose 10%, because partners must earn more than they spend (Rule 2), "
               "even though we give up $4,000 a year ($6,000 - $2,000).")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Only a low share leaves the partner a profit",
      '<div class="card good">' + ul([
          "Salons that buy = <b>100</b>. App sales = 100 x $8 x 12 = <b>$9,600</b>.",
          "Partner keeps: <b>$6,720</b> at 30%; <b>$8,160</b> at 15%; <b>$9,600</b> with 0% on the first $10,000.",
          "Only the last two are above the $8,000 cost, and 15% leaves very little.",
          "A strong answer chooses 0% on the first $10,000 (Rule 2), and notes that BookIt gives up $2,880 a year compared with 30%, "
          "in return for more apps that keep salons on BookIt."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Build alone or open an app market? ShopNest's next 12 months",
      '<p class="statement">400 shops / $600 a year each / 30 features wanted / 3 built per year / 60 shops left last year</p>'
      + two(flexcard("Option A: Build more yourself", "<p>Hire one more developer for <b>$48,000</b> a year; the team builds 3 more features.</p>"
                     "<p>Expect <b>20</b> fewer shops to leave and <b>20</b> new shops.</p>", "card", "BUILD ALONE"),
            flexcard("Option B: Open an app market", "<p>API and app reviews: <b>$15,000</b> once + <b>$500</b> a month. "
                     "Expect <b>20</b> partners and <b>25</b> apps.</p><p>Expect <b>30</b> fewer shops to leave and <b>40</b> new shops. "
                     "<b>100</b> shops buy apps at <b>$10</b> a month; ShopNest keeps <b>20%</b>.</p>", "card", "OPEN")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1 to 3)",
      '<div class="card">' + ul([
          "Years to build 30 features alone: today = 30 / 3 = ____; with one more developer = 30 / 6 = ____",
          "Option A: value = (20 + 20) x $600 = $______; result = value - $48,000 = $______",
          "Option B costs = $15,000 + 12 x $500 = $______",
          "Option B: value = (30 + 40) x $600 = $______; share = 100 x $10 x 12 x 20% = $______; result = value + share - costs = $______",
          "Option B if only 5 partners join (10 fewer leave, 10 new, 20 shops buy apps): "
          "(10 + 10) x $600 + 20 x $10 x 12 x 20% - costs = $______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Arjun (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [founder name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next six months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "BookIt: which revenue share?",
      tmpl("To: Grace Park, CEO, BookIt\n"
           "1. Decision and evidence: We should keep 0% of the first $10,000 each partner earns, because small partners must earn "
           "more than they spend (Rule 2): the reminder app keeps $9,600, above its $8,000 cost.\n"
           "2. Biggest risk and trade-off: The weakest point is that we earn almost nothing from small apps at first. We give up "
           "$2,880 a year from this app to attract more partners and keep salons on BookIt.\n"
           "3. Next step and decision rule: In the next six months we will invite 20 small developers and count live apps. "
           "We will change this decision if fewer than 8 apps are live by then."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Opening wins if partners come, and loses if they do not",
      '<div class="card">' + ul([
          "Years to build alone: <b>10</b> today; <b>5</b> with one more developer. Too slow for 30 features.",
          "Option A: (20 + 20) x $600 = $24,000; result = <b>-$24,000</b>.",
          "Option B costs = <b>$21,000</b>. Value = $42,000; share = <b>$2,400</b>; result = <b>$23,400</b>.",
          "Option B with only 5 partners: $12,000 + $480 - $21,000 = <b>-$8,520</b>."]) + "</div>"
      + '<div class="takeaway">The key question is Rule 2: will partners want to build?</div>',
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Usually chooses Option B.",
          "Protects the core: payments and data stay with ShopNest (Rule 1).",
          "Plans a partner-friendly share and app reviews (Rules 2 and 3).",
          'Gives a decision rule: "If fewer than 10 apps are live after six months, we will lower our share or help partners build."']) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain an open ecosystem with the words platform, partner, API, core, and revenue share.</p></div>'
      '<div class="card"><div class="n">02</div><p>Design a revenue share that partners want to join.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare building alone with opening an app market and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Chesbrough, H. W. (2003). Open Innovation. Harvard Business School Press.</p>'
      '<p class="ref">Parker, G. G., Van Alstyne, M. W., &amp; Choudary, S. P. (2016). Platform Revolution. W. W. Norton.</p>'
      '<p class="ref">CNBC (2021, June 29). Shopify cuts app store fees for developers on first $1 million in revenue.</p>'
      '<p class="ref">LEGO. What happens to my product idea after I reach 10,000 supporters?</p>'
      '<p class="ref">TechCrunch (2023, January 19). Twitter third-party apps Tweetbot and Twitterrific stop working.</p>'
      '<p class="ref">Federal Trade Commission (2019, July 24). FTC imposes $5 billion penalty on Facebook.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
