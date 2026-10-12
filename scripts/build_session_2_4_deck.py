"""Build the Session 2.4 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_2_4_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "2.4"
TITLE = "Module 2 Review: Choosing the Right Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


slide("MODULE 2 / PLATFORM ECONOMICS, BIG DATA &amp; MONETIZATION", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_2_4_freshbox_strategy_hanji.png" '
      'alt="Sora, founder of FreshBox, asks which strategy to use first.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "FreshBox: three strategies, one monthly loss",
      '<p class="statement" style="font-weight:400;">FreshBox sends university students weekly meal-kit boxes with fresh vegetables '
      "from local farms. It keeps $3.00 from each box. Sora is its founder.</p>"
      '<div style="display:flex;gap:.26in;align-items:flex-start;"><div style="flex:1.3"><table><tr><th>ONE MONTH</th><th style="text-align:right">VALUE</th></tr>'
      '<tr><td>Students who signed up</td><td class="num">3,000</td></tr>'
      '<tr><td>Local farms that supply vegetables</td><td class="num">25</td></tr>'
      '<tr><td>Boxes ordered per week</td><td class="num">900</td></tr>'
      '<tr><td>Revenue (900 x $3.00 x 4 weeks)</td><td class="num">$10,800</td></tr>'
      '<tr><td>Monthly costs</td><td class="num">$12,000</td></tr>'
      '<tr><td>Monthly loss</td><td class="num">$1,200</td></tr></table></div>'
      + card("Sora's question", "<p>Each Module 2 strategy suggests a different plan.</p><p>Which strategy should FreshBox use first?</p>", 'card" style="flex:1') + "</div>",
      "SESSION 2.4 / FICTIONAL CLASS DATA")

slide("THE SKILL IN ONE PARAGRAPH", "How do you choose the right strategy?",
      '<p class="para">Diagnose the business problem first, then use the Module 2 strategy that fits it. '
      "Check the evidence for that strategy's key condition, compare the options with the same numbers, "
      "and start with one strategy while planning the next.</p>"
      '<div class="takeaway">Use this skill whenever a business has several possible plans and limited time and money.</div>',
      "SESSION 2.4 / OVERVIEW")

slide("MODULE 2 AT A GLANCE", "Three strategies, three different problems",
      "<table><tr><th>STRATEGY</th><th>PROBLEM IT SOLVES</th><th>KEY CONDITION</th><th>NUMBER TO WATCH</th></tr>"
      "<tr><td>Data Feedback Loop (2.1)</td><td>We do not know what customers really want</td><td>Strong signals and permission</td><td>Churn or repeat rate</td></tr>"
      "<tr><td>Asymmetric Pricing (2.2)</td><td>Two groups need each other: who pays?</td><td>One side price sensitive; the other gains money</td><td>Money-side revenue vs. subsidy cost</td></tr>"
      "<tr><td>Up-Sell and Cross-Sell (2.3)</td><td>Many users, but they spend too little</td><td>A higher tier or related product customers value</td><td>Conversion and attach rate</td></tr></table>",
      "SESSION 2.4 / STRATEGY MAP")

slide("WORDS YOU NEED FIRST", "Diagnosis and condition",
      term("Diagnosis", "Naming the real problem before choosing a solution.", '"Students stop ordering after two weeks" is a diagnosis; "we need more ads" is a solution.')
      + term("Condition", "Something that must be true for a strategy to work.", "up-selling needs a higher tier that customers value."),
      "SESSION 2.4 / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Time to result and sequence",
      term("Time to result", "How long a plan takes before it changes the numbers.", "a data feedback loop may need three months of signals.")
      + term("Sequence", "The order in which a business uses strategies.", "first up-sell to cover costs, then a data loop to learn which premium items students want."),
      "SESSION 2.4 / KEY TERMS 2 OF 2")

rules = [
    ("Rule 1", "Name the problem before you choose a strategy",
     "Write the problem in one sentence that does not include a solution.",
     '"Students order a box for two weeks and then stop" points to a customer-knowledge problem (Session 2.1), not a pricing problem.',
     'Starting with a favorite strategy ("let\'s add a premium box") before knowing what is wrong.'),
    ("Rule 2", "Check the strategy's conditions with evidence",
     "Each strategy works only when its key condition is true.",
     "Asymmetric pricing needs a side that is not price sensitive. If most farms would leave over a $200 fee, the condition is weak.",
     'Using a strategy\'s words without its conditions, such as calling a business a "platform" when it does not connect two groups.'),
    ("Rule 3", "Compare the options with the same numbers",
     "For each option: the change in the monthly result, the time to result, and the main risk.",
     "One plan adds $1,800 a month but needs three months; another adds $3,240 a month and can start next week.",
     "Comparing one option's best case with another option's worst case."),
    ("Rule 4", "Start with one strategy and plan the next",
     "Fix the most urgent problem first, then plan which strategy comes next and why.",
     "First up-sell and cross-sell to stop the monthly loss, then use a data feedback loop to learn which premium items students want.",
     "Trying all three strategies at once, so the team cannot tell which one worked."),
]
for no, title, rule, ex, mistake in rules:
    slide(f"THE FOUR RULES / {no.upper()}", f"{no}: {title}",
          f'<p class="statement">{rule}</p>'
          + two(flexcard("Example", f"<p>{ex}</p>", "card good", "WHAT IT LOOKS LIKE"),
                flexcard("Common mistake", f"<p>{mistake}</p>", "card bad", "WHAT TO AVOID")),
          f"SESSION 2.4 / {no.upper()} OF 4")

examples = [
    ("GOOD EXAMPLE 1", "Spotify: three strategies that fit together", "good",
     "Spotify keeps a free tier paid for by advertisers, uses listening signals to build personal playlists, and up-sells free listeners to Premium, Duo, and Family plans.",
     ["Each strategy fits a clear problem: who pays, what listeners want, and how to earn more per listener. <b>(Rule 1)</b>",
      "The free tier creates the audience and data the other strategies need. <b>(Rule 4)</b>",
      "Premium gives clear extra value: no ads and offline listening. <b>(Rule 2)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "LinkedIn", "good",
     "Members create profiles for free. Recruiters and companies pay to search and contact members, and some members pay for Premium features.",
     ["Members are the subsidy side recruiters come for, so they stay free. <b>(Rule 2)</b>",
      "Recruiters gain the most from the match, so they are the main money side.",
      "Premium up-sells members who need more, such as job seekers, without charging all members. <b>(Rule 1)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "WeWork's 2019 IPO", "bad",
     "WeWork rented office space on long leases and rented desks to members on short contracts. Before its planned 2019 stock listing (IPO), "
     "it called itself a technology platform and was valued at about $47 billion by private investors. When its filings were published, "
     "investors questioned that description, and WeWork withdrew the IPO in September 2019.",
     ["It used platform words but did not mainly connect two groups who need each other. <b>(Rule 2)</b>",
      "The numbers showed a property-rental business with large losses. <b>(Rule 3)</b>",
      "Investors who checked the evidence lost trust, and its value fell sharply."], "Why it is bad"),
    ("BAD EXAMPLE 2", "MoviePass", "bad",
     "In 2017, MoviePass cut its price to $9.95 a month for up to one movie a day, while paying theaters close to the full ticket price for each movie. "
     "Its managers hoped to earn money later from subscriber data. Losses grew with every movie watched, and the service shut down in 2019.",
     ["A huge subsidy with no money side to cover it (Session 2.2, Rule 4).",
      "The data plan was only a hope, not a proven feedback loop. <b>(Rule 2)</b>",
      "One ticket could cost more than a whole month's fee. <b>(Rule 3)</b>"], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name, two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION 2.4 / {label}")

slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Three diagnosis questions",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">1</div><p>Do we know what customers want?</p><p><b>If not: Data Feedback Loop</b></p></div>'
      '<div class="card"><div class="n">2</div><p>Do we connect two groups and need to decide who pays?</p><p><b>If yes: Asymmetric Pricing</b></p></div>'
      '<div class="card"><div class="n">3</div><p>Do many customers use the product but spend too little?</p><p><b>If yes: Up-Sell and Cross-Sell</b></p></div></div>',
      "SESSION 2.4 / TOOL 1 OF 3")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Option comparison table",
      "<table><tr><th>BAKERY APP OPTION</th><th>MONTHLY CHANGE</th><th>TIME TO RESULT</th><th>MAIN RISK</th></tr>"
      "<tr><td>Cake up-sell</td><td>+$600</td><td>2 weeks</td><td>Customers may not want cake</td></tr>"
      "<tr><td>Data loop on favorite breads</td><td>+$900</td><td>3 months</td><td>Customers may refuse permission</td></tr></table>"
      '<div class="takeaway">Write the same three things for every option before you choose.</div>',
      "SESSION 2.4 / TOOL 2 OF 3")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>", "card", "MEMO BULLET 3")),
      "SESSION 2.4 / TOOL 3 OF 3")

slide("EXERCISE 1 / EASY / 20 MIN", "Match the problem to the strategy",
      '<div class="card">' + ul([
          "(a) A fitness app has 8,000 free users, but only 200 pay.",
          "(b) A campus marketplace connects buyers and sellers and does not know which side to charge.",
          "(c) A news app gets many clicks but does not know which articles make readers come back.",
          "(d) A bakery app wants each customer to spend more on each order."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE", "Business [letter]: The problem is [problem in one sentence, with no solution].\n"
                           "The best strategy is [strategy], because [the key condition is true]."),
          tbox("WORKED EXAMPLE: MUSIC SCHOOL APP", "The problem is that students quit after one month and the school does not know why.\n"
               "The best strategy is the Data Feedback Loop, because the school can collect strong signals, such as missed lessons and practice time, with students' permission.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Each problem points to one strategy",
      "<table><tr><th>BUSINESS</th><th>STRATEGY</th><th>WHY</th></tr>"
      "<tr><td>(a) Fitness app</td><td>Up-Sell and Cross-Sell</td><td>Many users, few paying</td></tr>"
      "<tr><td>(b) Marketplace</td><td>Asymmetric Pricing</td><td>Two groups; the question is who pays</td></tr>"
      "<tr><td>(c) News app</td><td>Data Feedback Loop</td><td>Does not know which signals show a real need</td></tr>"
      "<tr><td>(d) Bakery app</td><td>Up-Sell and Cross-Sell</td><td>More spending per order: a drink or a larger size</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Diagnose and plan one strategy: PetPal",
      two(flexcard("Scenario", "<p>PetPal connects pet owners with student pet sitters. It has <b>1,000 pet owners</b>; only <b>300</b> book a second time.</p>"
                   "<p>PetPal does not know why owners do not come back. Sitters are happy and many are waiting for bookings.</p>"),
          flexcard("Your steps", ul(["<b>Step 1:</b> Repeat booking rate = 300 / 1,000 x 100 = ____ %.",
                                     "<b>Step 2:</b> Use Tool 1 to choose a strategy, then fill in the template on the next slide."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE", "Problem: [one sentence, no solution]\nStrategy: [one Module 2 strategy]\n"
                           "Evidence the condition is met: [what we know or can collect]\n"
                           "First action: [one action, tested on a test group]\nMeasure: [one number and a target]"),
          tbox("WORKED EXAMPLE: LAUNDRY PICKUP APP", "Problem: many students use the free pickup, but few pay for ironing.\n"
               "Strategy: Up-Sell and Cross-Sell.\n"
               "Evidence the condition is met: 40% of students say ironed shirts would save them time before interviews.\n"
               "First action: offer ironing for $1.00 per shirt at checkout to half of the students.\n"
               "Measure: attach rate of the ironing offer; target 15%.")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Repeat rate is 30%: use the Data Feedback Loop",
      '<div class="card good">' + ul([
          "Repeat booking rate = 300 / 1,000 x 100 = <b>30%</b>.",
          "PetPal does not know why owners leave (Tool 1, question 1). Pricing is not the main problem: sitters are happy and waiting.",
          "Collect strong signals with permission: owner ratings, photos the sitter sent, whether the owner booked again.",
          "Test one change on a test group, such as a photo update during each visit.",
          "Measure the repeat booking rate, with a target such as 30% to 40%."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

slide("EXERCISE 3 / HARD / 50 MIN", "Choose FreshBox's first strategy",
      '<div class="grid3">'
      + card("Option A: Data Feedback Loop", "<p>Collect which recipes students cook and rate, with permission. Expect orders to rise from 900 to <b>1,050 boxes a week</b>, after about <b>3 months</b>.</p>", "card", "OPTION A")
      + card("Option B: Asymmetric Pricing", "<p>Charge each farm <b>$200 a month</b>. In a survey, <b>40% of farms</b> said they would leave if charged.</p>", "card", "OPTION B")
      + card("Option C: Up-Sell and Cross-Sell", "<p>Premium box: FreshBox keeps <b>$5.00</b> instead of $3.00; <b>20%</b> of boxes. Spice kit: keeps <b>$2.00</b>; <b>25%</b> of boxes. Starts next week.</p>", "card", "OPTION C")
      + "</div>",
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tool 2; 4 weeks per month)",
      '<div class="card">' + ul([
          "Option A: extra boxes per week = 1,050 - 900 = ____; extra revenue = extra boxes x $3.00 x 4 = $______",
          "Option B: farms that stay = 25 x 60% = ____; revenue = farms x $200 = $______",
          "Option C up-sell: Premium boxes per week = 900 x 20% = ____; extra = Premium boxes x $2.00 x 4 = $______",
          "Option C cross-sell: spice kits per week = 900 x 25% = ____; extra = kits x $2.00 x 4 = $______",
          "Then fill in a comparison table: monthly change, time to result, and main risk for each option."]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to the CEO (Tool 3)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [CEO name], [company]\n"
          "1. Decision and evidence: We should start with [option] because [the rule it follows] and [one number from your calculation]. "
          "Next, we will use [second strategy] because [reason].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next 60 days we will [one action] and measure [one number]. We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "CampusPrint: data loop or binding cross-sell?",
      tmpl("To: Ben Cho, CEO, CampusPrint\n"
           "1. Decision and evidence: We should start with the binding cross-sell because it fits a clear need before exams (Rule 1) "
           "and 30% of 2,000 orders x $1.00 = $600 a month covers our $500 loss. Next, we will use a data feedback loop to learn which students print most.\n"
           "2. Biggest risk and trade-off: The weakest point is that binding sales may drop after exams. "
           "We give up a slower, deeper data plan for now to stop the monthly loss quickly.\n"
           "3. Next step and decision rule: In the next 60 days we will offer binding at checkout to half of our users and measure the attach rate. "
           "We will change this decision if it is below 20%."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Start with C, plan A next, avoid B",
      "<table><tr><th>OPTION</th><th>MONTHLY CHANGE</th><th>TIME</th><th>MAIN RISK</th></tr>"
      "<tr><td>A: Data loop</td><td>+$1,800 (150 x $3.00 x 4)</td><td>About 3 months</td><td>Slow; students may refuse permission</td></tr>"
      "<tr><td>B: Charge farms</td><td>$3,000 (15 x $200)</td><td>Next month</td><td>10 farms leave; fewer vegetables, fewer boxes</td></tr>"
      "<tr><td>C: Up-sell + cross-sell</td><td>+$3,240 ($1,440 + $1,800)</td><td>Next week</td><td>Fewer students may choose Premium</td></tr></table>"
      '<div class="takeaway">A strong memo starts with C to cover the $1,200 loss quickly, plans A next (Rule 4), '
      "and explains that farms supply the food students come for, so they are a poor money side.</div>",
      "EXERCISE 3 / ANSWER KEY")

slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Match a business problem to the Module 2 strategy that fits it.</p></div>'
      '<div class="card"><div class="n">02</div><p>Check a strategy\'s key condition with evidence.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare options with the same numbers and choose which strategy to use first.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Hagiu, A., and Wright, J. (2020). When Data Creates Competitive Advantage. Harvard Business Review.</p>'
      '<p class="ref">Eisenmann, T., Parker, G., and Van Alstyne, M. W. (2006). Strategies for Two-Sided Markets. Harvard Business Review.</p>'
      '<p class="ref">The We Company (2019). Form S-1 Registration Statement. U.S. Securities and Exchange Commission.</p></div>',
      "SESSION 2.4 / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
