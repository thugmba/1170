"""Build the Session 4.4 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_4_4_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "4.4"
TITLE = "Final Review: Choosing the Right Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


def strategy_table(rows):
    return ("<table><tr><th>STRATEGY (SESSION)</th><th>USE IT WHEN</th><th>KEY CONDITION</th><th>MAIN NUMBER</th></tr>"
            + "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows) + "</table>")


# Cover and situation
slide("MODULE 4 / REAL-WORLD CASE STUDIES &amp; STRATEGIC SYNTHESIS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_4_4_studyspace_review_hanji.png" '
      'alt="Riya, founder of StudySpace, asks which strategy to use first before UniLife arrives.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "StudySpace: a small loss, and a big rival on the way",
      '<p class="statement" style="font-weight:400;">StudySpace is Riya\'s app for booking study rooms in libraries and cafes. '
      "UniLife, a campus super-app that 15,000 students open every day, will add room booking within six months (envelopment, Session 3.1).</p>"
      "<table><tr><th>STUDYSPACE (ONE MONTH)</th><th style=\"text-align:right\">VALUE</th></tr>"
      '<tr><td>Students who use the app</td><td class="num">6,000</td></tr>'
      '<tr><td>Study rooms (40 in libraries, 40 in cafes)</td><td class="num">80</td></tr>'
      '<tr><td>Cafe room bookings / fee per booking</td><td class="num">6,000 / $2</td></tr>'
      '<tr><td>Revenue (cafe fees $12,000 + library contract $8,000)</td><td class="num">$20,000</td></tr>'
      '<tr><td>Monthly costs / monthly loss</td><td class="num">$22,000 / $2,000</td></tr></table>'
      '<div class="takeaway">Three plans from three strategies. Which one first?</div>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", "How do we choose among fourteen strategies?",
      '<p class="para">Understand your <b>position and problem first</b>, then use the strategy that fits. Some strategies help a company '
      "<b>build a platform and win its first users</b> (1.1, 1.2, 1.3), or decide <b>when to race</b> (1.4). Some help a company "
      "<b>find out what customers want</b> (2.1). Some decide <b>who pays and how much</b> (2.2, 2.3). Some help a company <b>attack or "
      "defend</b> (3.1, 3.2, 3.3). Some help a company <b>grow and keep customers</b> (3.4, 4.1, 4.2, 4.3). No strategy is good everywhere.</p>"
      '<div class="takeaway">Check the key condition with evidence, compare options with the same numbers, use one strategy first, and plan the next. '
      "This is also the method for Part C of your final project.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Position, diagnosis, key condition",
      term("Position", "Where a company stands against its rivals: leader or newcomer, attacker or target.",
           "StudySpace is the leader in room booking and the target of UniLife.")
      + term("Diagnosis", "Naming the real problem before choosing a solution (Session 2.4).",
             '"We have too few cafe rooms to stay better than a rival," not "we need ads."')
      + term("Key condition", "Something that must be true for a strategy to work.",
             "a flywheel needs each arrow of the loop to be real."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Time to result and defense",
      term("Time to result", "How long a plan takes before it changes the numbers.",
           "new cafe rooms bring more bookings only after about three months.")
      + term("Defense", "A plan that makes it harder for a rival to take your customers.",
             "having many more rooms than UniLife can add quickly."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 2")

# Strategy map
slide("THE COURSE STRATEGIES AT A GLANCE", "Module 1 strategies",
      strategy_table([
          ("Platform Model (1.1)", "Many people own something useful that sits idle", "Strangers can trust each other; easy match", "Take rate, cost to grow"),
          ("Network Effect (1.2)", "Users get value from other users", "One small group can reach critical mass", "Density, weekly active rate"),
          ("Two-Sided Market (1.3)", "You connect two groups who need each other", "You can win the harder side first", "Balance, match rate"),
          ("Winner-Takes-All (1.4)", "A rival races you for the same market", "The market can tip", "Market share, multi-homing")]),
      f"SESSION {SESSION} / STRATEGY MAP 1 OF 3")

slide("THE COURSE STRATEGIES AT A GLANCE", "Module 2 and Module 3 strategies",
      strategy_table([
          ("Data Feedback Loop (2.1)", "You do not know what customers really want", "Strong signals and permission", "Churn or repeat rate"),
          ("Asymmetric Pricing (2.2)", "You connect two groups; who pays?", "One side comes for the other", "Money side vs. subsidy"),
          ("Up-Sell and Cross-Sell (2.3)", "Many customers spend too little", "Higher tier or related product with value", "Conversion, attach rate"),
          ("Platform Envelopment (3.1)", "Many users next to another market", "High overlap, shared parts", "Overlap rate, CAC"),
          ("Cannibalization (3.2)", "A new technology or rival takes customers", "New product earns enough over time", "Net gain vs. baseline")]),
      f"SESSION {SESSION} / STRATEGY MAP 2 OF 3")

slide("THE COURSE STRATEGIES AT A GLANCE", "Module 3 and Module 4 strategies",
      strategy_table([
          ("Disruption (3.3)", "A newcomer; the leader ignores some customers", "Simple is good enough; leader will not copy", "Non-consumers, profit test"),
          ("Open Ecosystem (3.4)", "Customers want more than you can build", "Partners can earn; you keep the core", "Partner earnings vs. cost"),
          ("Flywheel (4.1)", "Growth in one part improves another", "Each arrow of the loop is real", "Loop check, retention"),
          ("Ecosystem Lock-In (4.2)", "Several products better together", "Customers stay for value, not traps", "Customer lifetime value"),
          ("Super-App (4.3)", "Your app is used very often", "Busy front door; each service pays", "Contribution per service")]),
      f"SESSION {SESSION} / STRATEGY MAP 3 OF 3")

# Rules
rules = [
    ("Rule 1", "Know your position first",
     "Are you the leader or a newcomer? Are you attacking or being attacked? The same strategy can be right for one position and wrong for another.",
     "StudySpace is the leader in room booking and the target of UniLife. Its first need is a defense UniLife cannot copy quickly.",
     "A newcomer using a leader's strategy, such as fighting a strong leader head-on with discounts (Uber in China)."),
    ("Rule 2", "Check the key condition of the strategy with evidence",
     "Every strategy works only when its key condition in the strategy map is true.",
     "The flywheel plan needs cafes to join when they see more students. Twelve cafes have already asked to be listed.",
     "Choosing a strategy because a famous company used it. Copying Apple's lock-in without products that are truly better together fails."),
    ("Rule 3", "Compare options with the same numbers over the same time",
     "For each option, write the result over the same period, the time to result, the main risk, and whether it helps against the rival.",
     "Riya compares all three plans over the same six months, including what each costs at the start.",
     "Comparing one option's best case with another's worst case, or one option's first month with another's sixth month."),
    ("Rule 4", "Choose one strategy now, plan the next, and watch your rivals",
     "Start with the strategy that fixes the most urgent problem. Write which strategy comes next and what rival move would change your plan.",
     "First add cafe rooms (flywheel) to stay far better than UniLife; next, launch StudySpace Plus (lock-in) once there are enough rooms.",
     "Starting all three plans at once with a small team, so none is done well and nobody can tell which one worked."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_4_4_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "Amazon used strategies in order", "good",
     "Amazon first built a flywheel of low prices and choice in its own store (4.1). In 2000 it opened its store to outside sellers, an open "
     "ecosystem that added choice without buying stock (3.4). In 2005 it launched Prime, so customers bought more often from Amazon (lock-in, 4.2). "
     "In 2006 it launched Amazon Web Services, selling its computing skills to other companies (envelopment of a nearby market, 3.1).",
     ["Each strategy built on what the last one created. <b>(Rule 4)</b>",
      "Each key condition was true when Amazon used it. <b>(Rule 2)</b>",
      "Amazon knew its position: a leader that keeps customers by being better. <b>(Rule 1)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "Netflix changed strategy when its position changed", "good",
     "As a newcomer, Netflix used disruption: DVDs by mail with no late fees, which Blockbuster did not want to copy (3.3). Once it led DVD "
     "rentals, it cannibalized its own DVD business with streaming, starting in 2007 (3.2), even though its 2011 move (Qwikster) was badly handled.",
     ["Disruption as a newcomer, cannibalization as a leader. <b>(Rule 1)</b>",
      "One main strategy at a time, with the next one planned. <b>(Rule 4)</b>",
      "Compared streaming with a future without DVDs. <b>(Rule 3)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Uber in China", "bad",
     "Uber entered China and fought the local leader, Didi, head-on with large discounts for riders and bonuses for drivers. In 2016, Uber's CEO "
     "said it was losing more than $1 billion a year in China. In August 2016, Uber sold its China business to Didi in exchange for a share of Didi.",
     ["A newcomer used a leader's head-on attack. <b>(Rule 1)</b>",
      "Growth did not lower costs while Didi matched every discount. <b>(Rule 2)</b>",
      "Comparing yearly losses with any realistic gain shows the problem. <b>(Rule 3)</b>"], "Why it is bad"),
    ("BAD EXAMPLE 2", "Microsoft's Windows Phone", "bad",
     "Microsoft tried to build a third smartphone ecosystem against Apple and Google, and in 2014 bought Nokia's phone business for about "
     "$7.2 billion. App makers did not build enough apps, because most customers were already on iPhone or Android. In July 2015, Microsoft wrote "
     "down $7.6 billion on the Nokia business and cut 7,800 jobs.",
     ["Chose an ecosystem strategy without willing partners (app makers). <b>(Rule 2)</b>",
      "Customers were locked in elsewhere: high switching costs (4.2).",
      "A newcomer in phones acted as if its computer position carried over. <b>(Rule 1)</b>"], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Amazon</td><td style="color:#2f6b47;font-weight:700">Good</td><td>One strategy at a time, each built on the last (Rule 4)</td></tr>'
      '<tr><td>Netflix</td><td style="color:#2f6b47;font-weight:700">Good</td><td>The right strategy for each position (Rule 1)</td></tr>'
      '<tr><td>Uber in China</td><td style="color:#991b1b;font-weight:700">Bad</td><td>A newcomer fought head-on (Rule 1)</td></tr>'
      '<tr><td>Windows Phone</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Ecosystem without willing partners (Rule 2)</td></tr></table>'
      '<div class="takeaway">Position first, condition second, numbers third, order last.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Position and problem questions",
      '<div class="flow" style="grid-template-columns:repeat(4,1fr);">'
      '<div class="card"><div class="n">1</div><p>Are we the leader or a newcomer?</p></div>'
      '<div class="card"><div class="n">2</div><p>Is a rival attacking us, or are we attacking?</p></div>'
      '<div class="card"><div class="n">3</div><p>What is our most urgent problem, in one sentence with no solution?</p></div>'
      '<div class="card"><div class="n">4</div><p>Which strategy fits, and is its key condition true?</p></div></div>',
      f"SESSION {SESSION} / TOOL 1 OF 3")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Option comparison table",
      '<p class="statement">For each option: result over the same period ($), time to result, main risk, and help against the rival.</p>'
      "<table><tr><th>EXAMPLE: A BIKE-RENTAL APP</th><th>6-MONTH RESULT</th><th>TIME</th><th>MAIN RISK</th><th>AGAINST RIVALS</th></tr>"
      "<tr><td>Lock-in membership</td><td>+$4,000</td><td>1 month</td><td>Few may join</td><td>Helps a little</td></tr>"
      "<tr><td>Flywheel: more bike stations</td><td>+$9,000</td><td>3 months</td><td>Stations cost money</td><td>Helps a lot</td></tr></table>",
      f"SESSION {SESSION} / TOOL 2 OF 3")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>",
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 3 OF 3")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Match the situation to the strategy",
      '<p class="statement">Six businesses describe their situation:</p><div class="card">' + ul([
          "(a) A messaging app with 2 million daily users sees that most of its users also pay bills in a separate app.",
          "(b) A print shop sees students moving to digital notes from a rival app.",
          "(c) A new language-learning startup sees that private tutors cost too much for most students.",
          "(d) A booking platform for salons gets 40 feature requests, and outside developers want to help.",
          "(e) A campus marketplace finds that more sellers bring more buyers, and more buyers bring more sellers.",
          "(f) A smartwatch maker also sells a phone and a scale, but they do not share data."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Business [letter]: Our position is [leader / newcomer; attacker / target / neither].\n"
               "The best strategy is [strategy (session)], because [its key condition is true: evidence]."),
          tbox("WORKED EXAMPLE: A CAMPUS BUS APP",
               "The app is opened 10 times a month and wants to add food delivery.\n"
               "Our position is leader in campus transport; we are not under attack.\n"
               "The best strategy is the Super-App Strategy (4.3), because our app is a busy front door.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Which key condition is true?",
      "<table><tr><th>BUSINESS</th><th>STRATEGY</th><th>WHY</th></tr>"
      "<tr><td>(a) Messaging app</td><td>Envelopment (3.1)</td><td>High user overlap with bill paying</td></tr>"
      "<tr><td>(b) Print shop</td><td>Cannibalization (3.2)</td><td>A rival is already taking customers</td></tr>"
      "<tr><td>(c) Language startup</td><td>Disruption (3.3)</td><td>A newcomer serving people the leaders price out</td></tr>"
      "<tr><td>(d) Salon platform</td><td>Open Ecosystem (3.4)</td><td>Too many requests, willing partners</td></tr>"
      "<tr><td>(e) Campus marketplace</td><td>Flywheel (4.1)</td><td>Each arrow of the loop is real</td></tr>"
      "<tr><td>(f) Smartwatch maker</td><td>Ecosystem Lock-In (4.2)</td><td>Products could be better together</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Diagnose and plan one strategy: FitHub",
      two(flexcard("Scenario", ul([
          "FitHub: a gym-booking app with <b>9,000</b> members at <b>30</b> partner gyms.",
          "A food-delivery super-app with <b>25,000</b> daily users has just added gym booking with a <b>20%</b> discount.",
          "Members like FitHub's class reviews and personal workout history.",
          "<b>300</b> members use FitHub's $5-a-month coaching plan."])),
          flexcard("Your steps", ul([
              "<b>Step 1:</b> Answer the four position and problem questions (Tool 1).",
              "<b>Step 2:</b> Plan with the template on the next slide."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Position: [leader / newcomer; attacker / target]\n"
               "Problem: [one sentence, no solution]\n"
               "Strategy: [one strategy (session)]\n"
               "Evidence the key condition is met: [what we know]\n"
               "First action: [one action, tested on a test group]\n"
               "Measure: [one number and a target]\n"
               "Next strategy: [which one, and why]"),
          tbox("WORKED EXAMPLE: A CAMPUS BOOKSHOP",
               "Position: leader in textbooks; target of a digital rival.\n"
               "Problem: students move to a rival's e-books; paper sales fall each term.\n"
               "Strategy: Cannibalization (3.2).\n"
               "Evidence: 300 students left last term; e-books earn $8 per student.\n"
               "First action: our own e-book pass for half of our customers.\n"
               "Measure: share who stay with us; target 70%.\n"
               "Next strategy: Lock-In (4.2), linking e-books with our note app.")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "A target of envelopment: defend with value, not a price war",
      '<div class="card good">' + ul([
          "<b>Position:</b> leader in gym booking; target of an envelopment attack (Session 3.1).",
          "<b>Strategy:</b> Ecosystem Lock-In (4.2): members value reviews and history, and 300 already use coaching.",
          "<b>First action:</b> a monthly progress report linking bookings and coaching, tested on half of the members.",
          "<b>Measure:</b> bookings through FitHub next month; target: fewer than 5% move to the super-app.",
          "<b>Next:</b> Flywheel (4.1): more gyms bring more members, and more members bring more gyms.",
          "Matching the 20% discount is weak: the super-app can pay for discounts longer (Rule 1)."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Choose StudySpace's first strategy (next 6 months)",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      + card("Option A: Flywheel (4.1)", "<p>New cafes list free for three months; <b>$3,000</b> to help them join. Expect <b>30</b> new cafe rooms.</p>"
             "<p>From month 4: <b>+3,000</b> bookings a month at <b>$2</b>.</p>", "card", "MORE ROOMS")
      + card("Option B: Lock-In (4.2)", "<p>StudySpace Plus, <b>$3</b> a month, for priority booking and statistics. <b>$4,000</b> to build.</p>"
             "<p>From month 2: <b>10%</b> of 6,000 students subscribe.</p>", "card", "SUBSCRIPTION")
      + card("Option C: Open Ecosystem (3.4)", "<p>An API for tutoring and printing partners. <b>$10,000</b> to build.</p>"
             "<p>From month 5: <b>$2,500</b> a month from revenue share.</p>", "card", "PARTNERS")
      + "</div>",
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tool 2)",
      '<div class="card">' + ul([
          "Option A: months 4 to 6 = 3 x 3,000 x $2 = $______; result = extra revenue - $3,000 = $______",
          "Option B: subscribers = 6,000 x 10% = ____; months 2 to 6 = 5 x subscribers x $3 = $______; result = extra revenue - $4,000 = $______",
          "Option C: months 5 and 6 = 2 x $2,500 = $______; result = extra revenue - $10,000 = $______",
          "From month 4, which options cover the $2,000 monthly loss on their own? ____",
          "Comparison table: 6-month result, time to result, main risk, help against UniLife."]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Riya (Tool 3)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [founder name], [company]\n"
          "1. Decision and evidence: We should start with [option] because [the rule it follows] and [one number from your calculation]. "
          "Next, we will use [second strategy] because [reason].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next three months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "FitHub: defend with lock-in by value",
      tmpl("To: Lena Wu, CEO, FitHub\n"
           "1. Decision and evidence: We should start with lock-in by value (4.2), because members already value our reviews and history, "
           "and 300 coaching members show the services fit together. Next, we will push our flywheel by adding gyms (4.1).\n"
           "2. Biggest risk and trade-off: The weakest point is that the super-app's 20% discount may win price-sensitive members. "
           "We give up those members rather than start a price war we cannot afford.\n"
           "3. Next step and decision rule: In the next three months we will send monthly progress reports to half of our members and "
           "measure bookings. We will change this decision if more than 10% of them move to the super-app."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "The flywheel covers the loss and builds a defense",
      '<div class="card">' + ul([
          "Option A: $18,000 - $3,000 = <b>$15,000</b>; from month 4 it adds $6,000 a month, three times the loss.",
          "Option B: 600 subscribers; $9,000 - $4,000 = <b>$5,000</b>; adds $1,800 a month from month 2, almost covering the loss.",
          "Option C: $5,000 - $10,000 = <b>-$5,000</b> over the first 6 months.",
          "Only Option A covers the loss on its own from month 4, and it helps most against UniLife: with 110 rooms, StudySpace stays far "
          "better than any booking tab UniLife can add quickly (Session 3.1, Rule 3)."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Usually starts with Option A (Rules 1 and 4), and plans Option B next, when more rooms make priority booking more valuable.",
          "Names a real risk: cafes may not join, or UniLife may arrive sooner.",
          "States a clear decision rule.",
          "Starting with Option B can also be strong if it explains why fast, certain income comes first and when the flywheel will follow."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      "<div class=\"card\"><div class=\"n\">01</div><p>Name a company's position and problem before choosing a strategy.</p></div>"
      '<div class="card"><div class="n">02</div><p>Match a situation to the course strategy whose key condition is true.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare options with the same numbers and choose which strategy comes first and next.</p></div></div>'
      '<div class="takeaway">Use the same method in Part C of your final project ("If I Ran This Company").</div>'
      '<div style="margin-top:.2in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Porter, M. E. (1996). What is strategy? Harvard Business Review, 74(6), 61-78.</p>'
      '<p class="ref">Amazon.com, Inc. (1997-2006). Annual letters to shareholders.</p>'
      '<p class="ref">TechCrunch (2015, July 8). Microsoft writes down $7.6B of its Nokia acquisition, announces 7,800 layoffs.</p>'
      "<p class=\"ref\">Reuters (2016, August 1). China's Didi Chuxing to buy Uber's China business.</p></div>",
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
