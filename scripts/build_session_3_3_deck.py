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


# Cover and situation
slide("MODULE 3 / COMPETITIVE STRATEGY &amp; INNOVATION FRAMEWORKS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_3_3_tutorbite_disruption_hanji.png" '
      'alt="Linh, founder of TutorBite, asks whether to chase Apex Academy\'s best students or serve the students nobody serves.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "TutorBite: a small app next to a strong leader",
      '<p class="statement" style="font-weight:400;">TutorBite is Linh\'s tutoring app: 15-minute video calls with senior students '
      "who explain one homework problem. The campus leader is Apex Academy.</p>"
      "<table><tr><th></th><th>APEX ACADEMY (LEADER)</th><th>TUTORBITE</th></tr>"
      "<tr><td>What it offers</td><td>Weekly 2-hour classes, expert teachers</td><td>15-minute video help from senior students</td></tr>"
      "<tr><td>Price</td><td>$160 a month</td><td>$5 a session</td></tr>"
      "<tr><td>Customers today</td><td>2,000 students</td><td>300 students</td></tr>"
      "<tr><td>Profit per customer</td><td>$60 a month</td><td>$2 a session</td></tr></table>"
      '<div class="takeaway">8,000 more students use no tutoring because Apex costs too much. '
      "An investor says: hire expert teachers and go after Apex's students.</div>",
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
           "The strong company that already serves most customers in a market.", "Apex Academy.")
      + term("Disruption", "A simpler, cheaper product that starts with customers the leader ignores and later takes the leader's customers.",
             "TutorBite's $5 sessions.")
      + term("Sustaining innovation", "Making a product better for the leader's best customers, often at a higher price.",
             "Apex adds a second weekly class for $240 a month."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Non-consumers, over-served, good enough",
      term("Non-consumers", "People who need a job done but buy nothing today, often because it costs too much or is too hard.",
           "the 8,000 students who use no tutoring.")
      + term("Over-served customers", "Customers who get more than they need and would happily pay less for less.",
             "a student who needs help with one problem but pays for a month of classes.")
      + term("Good enough", "A product that does the main job the customer needs, even if it is not the best.",
             "a 15-minute explanation for one homework problem."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 2")

# Rules
rules = [
    ("Rule 1", "Start where the leader is not looking",
     "Begin with non-consumers or with the leader's least profitable customers. They are easy to win, and the leader will not miss them.",
     "TutorBite starts with the 8,000 students who use no tutoring. Apex does not serve them, so it will not fight for them.",
     "Going straight after the leader's best customers. The leader is strongest exactly there, and it will fight hard to keep them."),
    ("Rule 2", "Make it simpler and cheaper, and good enough for the job",
     "Do not try to be better than the leader at everything. Be good enough at the main job, and much easier and cheaper.",
     "A $5, 15-minute call answers one homework question. Students do not need a 2-hour class for that.",
     "Adding expert teachers, long classes, and a high price to look like the leader. Then the product is neither cheap nor better."),
    ("Rule 3", "Choose a model the leader does not want to copy",
     "If copying you would earn the leader much less profit than its own product, the leader will ignore you, often until it is too late.",
     "Apex earns $60 a month from each student. Copying TutorBite would earn it about $2 a session, so Apex protects its $160 classes.",
     "Choosing a model the leader can copy easily and profitably, such as the same classes at a slightly lower price. The leader cuts its price and wins."),
    ("Rule 4", "Improve step by step, then move up to better customers",
     "Use what you learn from your first customers to improve. When you are good enough for the leader's customers, they come to you at a lower price.",
     "After one year, TutorBite adds $40-a-month exam-prep plans with its best senior tutors. Some of Apex's students start to switch.",
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
          flexcard("Example: websites", ul([
              "5,000 small shops in a city need a website.",
              "1,000 pay a design agency.",
              "Non-consumers = 5,000 - 1,000 = 4,000 shops."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: The leader's profit test",
      two(flexcard("Will the leader copy you?", "<p>Compare the leader's profit per customer today with the profit it would earn by copying you. "
                   "If copying earns much less, the leader will probably not fight back.</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: websites", ul([
              "A design agency earns $1,500 profit per website.",
              "A simple website builder earns $10 a month per shop.",
              "The agency will not want to copy it."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Profit over several periods (from Session 3.1)",
      two(flexcard("Formula", "<p>Profit = profit per period x number of periods - one-time cost</p>", "card", "USED IN EXERCISE 3"),
          flexcard("Example: a website builder", ul([
              "$6,000 on launch ads; $2,000 profit a month.",
              "After 12 months: 12 x $2,000 - $6,000 = $18,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 500 students use TutorBite in the first three months, we will change the price."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Disruption or not?",
      '<p class="statement">Six companies plan a new product:</p><div class="card">' + ul([
          "(a) A startup sells a $300 basic 3D printer to schools that cannot afford $3,000 printers.",
          "(b) A car maker builds a faster, more expensive sports car to beat a rival's top model.",
          "(c) A startup offers a free, simple video-call app for families; companies pay for expensive meeting systems.",
          "(d) A bank adds a metal credit card with airport lounge access for its richest customers.",
          "(e) A website offers $10 online courses in skills that colleges teach for $3,000.",
          "(f) A phone maker adds a fourth camera to its most expensive phone."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Product [letter]: [disruption / not disruption], because\n"
               "its first customers are [non-consumers / over-served customers / the leader's best customers],\n"
               "and it is [simpler and cheaper / better and more expensive] than what the leader sells."),
          tbox("WORKED EXAMPLE: SCANNERS",
               "Product: a $2 app that turns a phone into a simple scanner.\n"
               "Disruption, because its first customers are non-consumers who never bought a scanner, "
               "and it is simpler and cheaper than a $200 office scanner.\n"
               "Product: faster scanning on a $900 office model.\n"
               "Not disruption, because it serves the leader's best customers and is better and more expensive (sustaining).")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Who are the first customers, and is it simpler and cheaper?",
      "<table><tr><th>PRODUCT</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) $300 3D printer</td><td>Disruption</td><td>Schools that bought no printer; much cheaper</td></tr>"
      "<tr><td>(b) Faster sports car</td><td>Not</td><td>Better and pricier for the best customers</td></tr>"
      "<tr><td>(c) Free family video calls</td><td>Disruption</td><td>Families who would never buy a meeting system</td></tr>"
      "<tr><td>(d) Metal credit card</td><td>Not</td><td>A better product for the richest customers</td></tr>"
      "<tr><td>(e) $10 online courses</td><td>Disruption</td><td>People who could not pay for college courses</td></tr>"
      "<tr><td>(f) Fourth camera</td><td>Not</td><td>More features for top customers</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Check a disruption plan: QuickCut",
      two(flexcard("Scenario", ul([
          "QuickCut: <b>$8</b>, 10-minute haircut kiosks in train stations; <b>$3</b> profit per haircut.",
          "Salons: <b>$40</b> for 45 minutes with washing and styling; <b>$15</b> profit per haircut.",
          "<b>50,000</b> men need a haircut every month; <b>20,000</b> go to salons; the rest cut their hair at home."])),
          flexcard("Your steps", ul([
              "<b>Step 1:</b> Non-consumers = 50,000 - 20,000 = ____. Salon profit = $____; QuickCut profit = $____. "
              "Copying QuickCut earns a salon ____ times less per haircut.",
              "<b>Step 2:</b> Check the four rules with the template on the next slide."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Rule 1: our first customers are [who], [number] people.\n"
               "Rule 2: we do [the main job] for $[price] instead of $[leader's price]; we leave out [what we do not offer].\n"
               "Rule 3: the leader earns $[number] per customer; copying us earns $[number].\n"
               "Rule 4: first we [first step]; later we [how we move up].\n"
               "Verdict: [go / do not go], because [one sentence]."),
          tbox("WORKED EXAMPLE: SITEEASY WEBSITE BUILDER",
               "Rule 1: our first customers are the 4,000 small shops with no website.\n"
               "Rule 2: a simple one-page shop website for $10 a month instead of $2,000; we leave out custom design and meetings.\n"
               "Rule 3: the agency earns $1,500 per website; copying us earns $10 a month.\n"
               "Rule 4: first one-page sites; later online ordering for bigger shops.\n"
               "Verdict: go, because 4,000 shops are not served and agencies will not fight for them.")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "30,000 non-consumers; salons earn 5 times more per haircut",
      '<div class="card good">' + ul([
          "Non-consumers = <b>30,000</b> men who cut their hair at home. Salon profit <b>$15</b>; QuickCut <b>$3</b>: copying earns <b>5 times</b> less.",
          "<b>Rule 1:</b> the 30,000 men at home, plus salon customers who only want a quick cut.",
          "<b>Rule 2:</b> a clean haircut for $8, leaving out washing, styling, and booking.",
          "<b>Rule 3:</b> salons will not copy a $3-profit model.",
          "<b>Rule 4:</b> start in a few stations, then add more stations or simple extras such as beard trims.",
          "<b>Verdict:</b> go."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Head-on or disruption? TutorBite's next 12 months",
      two(flexcard("Option A: Go after Apex's students", "<p>Expert teachers, weekly classes for <b>$120</b> a month, <b>$20</b> profit per student a month. "
                   "Marketing and hiring <b>$20,000</b> once.</p><p>Expect <b>300</b> of Apex's 2,000 students; only <b>100</b> if Apex cuts its price.</p>",
                   "card", "HEAD-ON"),
          flexcard("Option B: Serve non-consumers first", "<p>Keep <b>$5</b> sessions, <b>$2</b> profit each. Marketing <b>$5,000</b> once.</p>"
                   "<p>Expect <b>10%</b> of the 8,000 non-consumers to join, each using <b>3</b> sessions a month.</p>", "card", "DISRUPTION")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1 to 3)",
      '<div class="card">' + ul([
          "Option A, 300 students: per month = 300 x $20 = $______; over 12 months = 12 x monthly - $20,000 = $______",
          "Option A if Apex cuts its price (100 students): per month = $______; over 12 months = $______",
          "Option B: students = 8,000 x 10% = ____; sessions = students x 3 = ____; per month = sessions x $2 = $______; "
          "over 12 months = 12 x monthly - $5,000 = $______",
          "Leader's profit test: Apex earns $60 a month per student. Would copying Option B earn more or less? ____ Option A? ____"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to the investor (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [name], [role]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next three months we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "QuickCut: open kiosks for men who cut their own hair?",
      tmpl("To: Omar Haddad, investor, QuickCut\n"
           "1. Decision and evidence: We should open $8 kiosks for the 30,000 men who cut their hair at home (Rule 1), because salons "
           "earn $15 a haircut and will not copy a $3-profit model (Rule 3).\n"
           "2. Biggest risk and trade-off: The weakest point is that men may keep cutting their hair at home. We give up the higher price "
           "of a salon service to win customers nobody serves.\n"
           "3. Next step and decision rule: In the next three months we will open two kiosks and count haircuts per day. "
           "We will change this decision if a kiosk does fewer than 40 haircuts a day."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Same profit if all goes well; only one plan depends on the leader",
      '<div class="card">' + ul([
          "Option A, 300 students: <b>$6,000</b> a month; over 12 months = $72,000 - $20,000 = <b>$52,000</b>.",
          "Option A if Apex cuts its price: <b>$2,000</b> a month; over 12 months = $24,000 - $20,000 = <b>$4,000</b>.",
          "Option B: 800 students, 2,400 sessions, <b>$4,800</b> a month; over 12 months = $57,600 - $5,000 = <b>$52,600</b>.",
          "Leader's profit test: copying B earns Apex far less than $60 a month per student, so Apex will probably ignore it. "
          "A is the same kind of class as Apex's, so Apex can fight back."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Usually chooses Option B: it does not depend on Apex staying quiet (Rules 1 and 3).",
          "Names a real risk: fewer than 10% of non-consumers may join, or students may use fewer than 3 sessions.",
          "Plans how to move up later, such as exam-prep plans (Rule 4).",
          'Gives a decision rule: "If fewer than 500 students use TutorBite in the first three months, we will change the price or the offer."']) + "</div>",
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


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
