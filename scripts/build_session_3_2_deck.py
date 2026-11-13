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
      '<img class="hero" src="../assets/session_3_2_studyprint_cannibalization_hanji.png" '
      'alt="Mei, owner of StudyPrint, asks whether to sell a digital pass that may replace her own paper packs.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "StudyPrint: profitable, but shrinking",
      '<p class="statement" style="font-weight:400;">StudyPrint is a campus print shop that sells printed course packs to students. '
      "Mei is its owner. NoteCloud, a $6-a-month digital notes app, takes about 300 of her buyers every semester.</p>"
      "<table><tr><th></th><th style=\"text-align:right\">LAST SEMESTER</th><th style=\"text-align:right\">THIS SEMESTER</th></tr>"
      '<tr><td>Students who buy paper course packs</td><td class="num">1,800</td><td class="num">1,500</td></tr>'
      '<tr><td>Money each buyer spends (2 packs x $20)</td><td class="num">$40</td><td class="num">$40</td></tr>'
      '<tr><td>Cost to print 2 packs</td><td class="num">$16</td><td class="num">$16</td></tr>'
      '<tr><td>Profit per buyer</td><td class="num">$24</td><td class="num">$24</td></tr>'
      '<tr><td>Total profit</td><td class="num">$43,200</td><td class="num">$36,000</td></tr></table>'
      '<div class="takeaway">Idea: a Digital Pass with every course pack for $24 per semester; $20 profit per student; $10,000 to build. '
      "But many paper buyers would switch to it.</div>",
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

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
           "600 of StudyPrint's paper buyers switch to the Digital Pass.")
      + term("Profit per customer", "The money a company keeps from one customer after paying the costs of serving that customer.",
             "a paper buyer pays $40 and costs $16: $40 - $16 = $24."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 3")

slide("WORDS YOU NEED FIRST", "Cannibalization rate and net gain",
      term("Cannibalization rate", "The share of the new product's customers who came from your own old product.<br>"
           "= old customers who switched / customers of the new product x 100", "600 / 900 x 100 = 67%.")
      + term("Net gain", "What the company really gains after counting the profit it loses on the old product.<br>"
             "= profit from the new product - profit lost on the old product", "$9,000 - $5,000 = $4,000."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 3")

slide("WORDS YOU NEED FIRST", "Baseline and rival",
      term("\"Do nothing\" baseline", "What would happen if the company does not launch anything. "
           "A baseline is the result you compare your plan against.",
           "if StudyPrint does nothing, NoteCloud keeps taking 300 buyers a semester.")
      + term("Rival", "A company that competes for the same customers.", "NoteCloud is StudyPrint's rival."),
      f"SESSION {SESSION} / KEY TERMS 3 OF 3")

# Rules
rules = [
    ("Rule 1", "Compare with the future, not with today",
     "Ask what will happen if you do nothing. If a rival is already taking your customers, today's profit will not stay.",
     "StudyPrint earns $36,000 this semester. If Mei does nothing, NoteCloud keeps taking 300 buyers each semester. "
     "The real choice is between the Digital Pass and a smaller business, not between the pass and $36,000.",
     'Saying "the new product will hurt our sales" and stopping there. The old sales are already disappearing; '
     "the only question is who gets the customers."),
    ("Rule 2", "Count the net gain, not only the new sales",
     "New sales look good on their own. Always subtract the profit you lose on the old product.",
     "The Digital Pass earns $20 from each student, but a paper buyer who switches earned $24, so each switcher costs $4. "
     "The pass helps mainly because of the new students and the buyers it keeps from NoteCloud.",
     'Reporting "900 Digital Pass users, $18,000 of new profit!" without saying that 600 of them were paper buyers who used to bring $14,400.'),
    ("Rule 3", "Give the new product its own team and its own goals",
     "Managers of the old product often slow the new one down, because it takes their sales. A separate team with its own targets moves faster.",
     "Mei asks two staff members to run the Digital Pass. They are measured by digital users, not by paper sales.",
     "Letting the paper team decide the price and features of the Digital Pass. They may make it weak so that paper sales stay high."),
    ("Rule 4", "Move customers step by step, and keep their trust",
     "Give customers time, help, and a good reason to switch. Do not force everyone overnight.",
     "For one year, StudyPrint keeps selling paper packs, offers the Digital Pass at a discount to paper buyers, and shows them how to use it in class.",
     'Stopping paper sales overnight and telling students to "go digital." Students who are not ready leave for a rival.'),
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
      "Rivals took the customers Kodak did not want to cannibalize."], "Why it is bad"),
    ("BAD EXAMPLE 2", "Netflix's Qwikster", "bad",
     "Netflix wanted customers to move from DVDs by mail to streaming. In September 2011, it announced that the DVD service would become "
     "a separate company, Qwikster, with its own website and account. Customers were angry. In October 2011, only three weeks later, "
     "Netflix cancelled the plan.",
     ["The right idea, but Netflix tried to push customers overnight. <b>(Rule 4)</b>",
      "Customers got no new value, only more work: two websites, two bills.",
      "It came just after a large price increase (Session 2.3), so trust was already low."], "Why it is bad"),
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
      two(flexcard("Formula", "<p>Cannibalization rate = old customers who switched / customers of the new product x 100</p>",
                   "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: a music school", ul([
              "It starts online lessons; 200 students take them.",
              "50 of them used to take lessons at the school.",
              "50 / 200 x 100 = 25%."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Net gain",
      two(flexcard("Formula", "<p>Net gain = profit from the new product - profit lost on the old product</p>",
                   "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: a music school", ul([
              "Online lessons: 200 x $10 profit = $2,000.",
              "Each switcher earned $30 at the school: 50 x $30 = $1,500 lost.",
              "Net gain = $2,000 - $1,500 = $500."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", 'Tool 3: Compare with the "do nothing" baseline',
      two(flexcard("Formula", "<p>Gain of the plan = result with the plan - result if we do nothing</p>",
                   "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: a music school", ul([
              "Without online lessons, an online rival takes 60 school students: 60 x $30 = $1,800 lost.",
              "Compared with doing nothing, the plan is worth $500 + $1,800 = $2,300, if it keeps those students."]),
              "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 300 students use the Digital Pass in the first semester, we will stop it."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Cannibalization or not?",
      '<p class="statement">Six companies plan a new product:</p><div class="card">' + ul([
          "(a) A bakery that sells a $6 premium loaf adds a $3 basic loaf.",
          "(b) A newspaper puts all its articles on a free website.",
          "(c) A gym opens a branch in a city where it has no members.",
          "(d) A streaming service adds a cheaper plan with ads.",
          "(e) A car maker launches an electric version of its best-selling car.",
          "(f) A cafe starts selling umbrellas on rainy days."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Product [letter]: [cannibalization / not cannibalization], because\n"
               "[which old product of the same company could lose customers, or none]\n"
               "and [why customers might switch, or why they would not]."),
          tbox("WORKED EXAMPLE: A BOOKSTORE",
               "Product: e-books of the same titles.\n"
               "Cannibalization, because its paper books could lose customers, and some readers will choose "
               "the cheaper, lighter e-book instead.\n"
               "Product: coffee.\n"
               "Not cannibalization, because no old product loses customers; coffee is bought in addition to books.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Does an old product of the same company lose customers?",
      "<table><tr><th>PRODUCT</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) $3 basic loaf</td><td>Cannibalization</td><td>Some premium buyers pay $3 instead of $6</td></tr>"
      "<tr><td>(b) Free website</td><td>Cannibalization</td><td>Some readers stop buying the paper</td></tr>"
      "<tr><td>(c) Gym in a new city</td><td>Not</td><td>No current members there</td></tr>"
      "<tr><td>(d) Cheaper plan with ads</td><td>Cannibalization</td><td>Some full-price customers move down</td></tr>"
      "<tr><td>(e) Electric version</td><td>Cannibalization</td><td>Some petrol-car buyers choose electric</td></tr>"
      "<tr><td>(f) Umbrellas</td><td>Not</td><td>Umbrellas do not replace coffee</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Calculate the real gain: GoldCrust bakery",
      two(flexcard("Scenario", ul([
          "1,000 premium loaves a month, <b>$3.00</b> profit each.",
          "New basic loaf: <b>$1.00</b> profit each; <b>800</b> sold in the first month.",
          "Premium sales fall to <b>700</b>.",
          "Without a basic loaf, a new discount bakery would take <b>400</b> premium buyers."])),
          flexcard("Your steps", ul([
              "<b>Step 1:</b> Switched = 1,000 - 700 = ____. Rate = switched / 800 x 100 = ____ %. "
              "Net gain vs. last month = 800 x $1.00 - switched x $3.00 = $____.",
              "<b>Step 2:</b> Do nothing = 600 x $3.00 = $____. With basic loaf = 700 x $3.00 + 800 x $1.00 = $____. Gain vs. doing nothing = $____.",
              "<b>Step 3:</b> Explain with the template."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Compared with last month, the new product [gains / loses] $[amount],\n"
               "because [number] customers switched from our [old product].\n"
               "Compared with doing nothing, it [gains / loses] $[amount],\n"
               "because [what would happen without it].\n"
               "So we should [keep / stop] the new product, because [Rule 1 or Rule 2]."),
          tbox("WORKED EXAMPLE: THE MUSIC SCHOOL",
               "Compared with last month, online lessons gain $500, because 50 students switched from our school lessons.\n"
               "Compared with doing nothing, they gain $2,300, because without them a rival would take 60 of our students.\n"
               "So we should keep online lessons, because the real choice is between them and a smaller school (Rule 1).")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "A loss compared with last month, a gain compared with the future",
      '<div class="card good">' + ul([
          "Switched = <b>300</b>. Cannibalization rate = 300 / 800 x 100 = <b>37.5%</b>.",
          "Net gain vs. last month = $800 - $900 = <b>-$100</b> (a small loss).",
          "Do nothing = 600 x $3.00 = <b>$1,800</b>. With the basic loaf = $2,100 + $800 = <b>$2,900</b>.",
          "Gain compared with doing nothing = <b>$1,100</b>.",
          "A strong answer keeps the basic loaf: it looks like a loss compared with last month but is a clear gain compared "
          "with the future (Rule 1), as long as the discount bakery really is a threat."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Should StudyPrint launch the Digital Pass?",
      '<p class="statement">Today: 1,500 paper buyers / $24 profit each / $36,000 profit per semester. Next four semesters:</p>'
      + two(flexcard("Option A: Keep paper only", "<p>NoteCloud keeps taking <b>300</b> buyers each semester.</p>"
                     "<p>Paper buyers: <b>1,200</b>, then <b>900</b>, <b>600</b>, <b>300</b>.</p>", "card", "DO NOTHING"),
            flexcard("Option B: Launch the Digital Pass", "<p>Build cost <b>$10,000</b> once. Each semester <b>600</b> paper buyers switch "
                     "(<b>900</b> still buy paper) and <b>300</b> new students join: <b>900</b> pass users at <b>$20</b> profit each.</p>"
                     "<p>The team believes the pass stops students leaving for NoteCloud.</p>", "card", "CANNIBALIZE")),
      "EXERCISE 3 / SCENARIO: FOUR SEMESTERS")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1 to 3)",
      '<div class="card">' + ul([
          "Option A over 4 semesters = (1,200 + 900 + 600 + 300) x $24 = $______",
          "Option B per semester = 900 x $24 + 900 x $20 = $______",
          "Option B over 4 semesters = 4 x per semester - $10,000 = $______",
          "Option B in the first semester = per semester - $10,000 = $______. More or less than today's $36,000? ____",
          "Cannibalization rate = 600 / 900 x 100 = ____ %",
          "If NoteCloud stops growing (paper stays at 1,500): Option A = 4 x $36,000 = $______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Mei (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [owner name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next semester we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
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

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Compared with today the pass looks worse; compared with the future it wins",
      '<div class="card">' + ul([
          "Option A = 3,000 x $24 = <b>$72,000</b>.",
          "Option B per semester = $21,600 + $18,000 = <b>$39,600</b>; over 4 semesters = $158,400 - $10,000 = <b>$148,400</b>.",
          "Option B first semester = <b>$29,600</b>: less than today's $36,000, but more than Option A's first semester (1,200 x $24 = $28,800).",
          "Cannibalization rate = <b>67%</b>: two of every three pass users were paper buyers.",
          "If NoteCloud stops growing, Option A = <b>$144,000</b>, close to Option B. The choice depends on the NoteCloud threat."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Usually chooses Option B and explains why today's $36,000 is the wrong comparison (Rule 1).",
          "Names a real risk: more paper buyers may switch than expected, or the pass may not stop students leaving for NoteCloud.",
          "Plans a step-by-step move, such as a discount for paper buyers (Rule 4).",
          'Gives a decision rule: "If fewer than 300 new students join the pass in the first semester, we will rethink the price."']) + "</div>",
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


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
