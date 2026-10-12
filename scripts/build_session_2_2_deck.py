"""Build the Session 2.2 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_2_2_deck.py
Reuses the Session 2.1 deck style and the Session 2.3 slide helpers.
"""
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import CSS, card, ul, tmpl  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SESSION = "2.2"
TITLE = "The Asymmetric Pricing Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


def two(left, right):
    return '<div style="display:flex;gap:.26in;align-items:flex-start;">' + left + right + "</div>"


def flexcard(heading, inner, cls="card", label=None):
    return card(heading, inner, cls + '" style="flex:1', label)


def tbox(label, text):
    return f'<div style="flex:1"><div class="small-label">{label}</div>' + tmpl(text) + "</div>"


def term(name, text, example):
    return f'<div class="term"><strong>{name}</strong><span>{text}<br><em>Example: {example}</em></span></div>'


slide("MODULE 2 / PLATFORM ECONOMICS, BIG DATA &amp; MONETIZATION", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_2_2_campusjobs_pricing_hanji.png" '
      'alt="Ravi, founder of CampusJobs, asks who should pay: the students or the shops.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "CampusJobs: a free app that earns nothing",
      '<p class="statement" style="font-weight:400;">CampusJobs is a free app that connects university students who want '
      "part-time jobs with local shops that need workers. Ravi is its founder.</p>"
      '<div class="wide-left"><div><table><tr><th>ONE MONTH</th><th style="text-align:right">VALUE</th></tr>'
      '<tr><td>Students using the app</td><td class="num">6,000</td></tr>'
      '<tr><td>Shops posting jobs</td><td class="num">120</td></tr>'
      '<tr><td>Job posts</td><td class="num">300</td></tr>'
      '<tr><td>Applications from students</td><td class="num">9,000</td></tr>'
      '<tr><td>Price for students / shops</td><td class="num">$0 / $0</td></tr>'
      '<tr><td>Monthly costs</td><td class="num">$4,000</td></tr></table></div>'
      + card("Ravi's question", "<p>A friend says: charge everyone $2.00 a month.</p>"
             "<p>Who should pay? Would charging students make the app useless for shops?</p>") + "</div>",
      "SESSION 2.2 / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", f"What is the {TITLE[4:]}?",
      '<p class="para">A <b>platform</b> connects two groups who need each other. With asymmetric pricing, it charges them '
      "<b>different prices</b>. The <b>subsidy side</b> pays little or nothing, because its presence attracts the other group. "
      "The <b>money side</b> pays, because meeting the first group is worth money to it.</p>"
      '<div class="takeaway">Use it when a business connects two groups, one group is easily driven away by a price, '
      "and the other group would gladly pay to reach it.</div>",
      "SESSION 2.2 / STRATEGY OVERVIEW")

slide("WORDS YOU NEED FIRST", "Platform, subsidy side, money side",
      term("Two-sided platform", "A business that connects two groups of users who need each other.", "CampusJobs connects students and shops.")
      + term("Subsidy side", "The side that pays little or nothing because the platform needs many of them.", "students use CampusJobs for free.")
      + term("Money side", "The side that pays because reaching the other side is worth money to them.", "a shop pays to post a job and find workers."),
      "SESSION 2.2 / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Price sensitivity, subsidy, cross-subsidy",
      term("Price sensitivity", "How much a group's use drops when the price rises.", "if a $2.00 fee makes 60 of every 100 students leave, students are very price sensitive.")
      + term("Subsidy", "Value the platform gives away to attract a side.", "free use, or a $5.00 sign-up bonus.")
      + term("Cross-subsidy", "Using money from one side to pay for the free service given to the other side.", "shop fees pay the costs of serving students for free."),
      "SESSION 2.2 / KEY TERMS 2 OF 2")

rules = [
    ("Rule 1", "Subsidize the side that the other side comes for",
     'Ask: "Which group does the other group want to reach?" Keep that group free or cheap.',
     "Shops join CampusJobs because 6,000 students are there. Without students, no shop would post a job, so students should stay free.",
     "Charging the side that attracts everyone else. When it leaves, the other side leaves too."),
    ("Rule 2", "Charge the side that gains the most from the match",
     "The money side usually earns money or saves time because of the other side.",
     "A shop that fills a job quickly saves days of searching and keeps its store running. That is worth more to a shop than a job search is worth to a student in cash.",
     "Charging both sides the same price because it looks fair. Equal prices ignore that the two sides value the platform very differently."),
    ("Rule 3", "Check price sensitivity before you set a price",
     "Find out which side leaves when the price rises, and keep the price low for that side.",
     "A survey finds that a $2.00 fee would make 60% of students leave, but shops would pay $25.00 per job post if each post gets at least 20 applications.",
     "Guessing. A price that looks small to the business ($2.00) can be large for a student budget."),
    ("Rule 4", "Make the money side cover the subsidy, and protect the free side",
     "The money side must pay enough to cover the cost of serving both sides, and must not harm the free side.",
     'CampusJobs checks that job-post fees are more than its $4,000 monthly costs, and removes fake or unpaid "job" posts so students keep trusting the app.',
     "Giving away free service with no plan for who will pay, or letting the paying side flood the free side with low-quality offers."),
]
for no, title, rule, ex, mistake in rules:
    slide(f"THE FOUR RULES / {no.upper()}", f"{no}: {title}",
          f'<p class="statement">{rule}</p>'
          + two(flexcard("Example", f"<p>{ex}</p>", "card good", "WHAT IT LOOKS LIKE"),
                flexcard("Common mistake", f"<p>{mistake}</p>", "card bad", "WHAT TO AVOID")),
          f"SESSION 2.2 / {no.upper()} OF 4")

examples = [
    ("GOOD EXAMPLE 1", "Adobe Acrobat Reader", "good",
     "In the 1990s, Adobe gave away the Reader program for opening PDF files for free, and sold the Acrobat software that creates and edits PDF files to businesses.",
     ["Millions of free readers made PDF the format businesses wanted to use. <b>(Rule 1)</b>",
      "Businesses that create documents gained the most, so they were charged. <b>(Rule 2)</b>",
      "Readers would not have paid just to open a file, so Reader stayed free. <b>(Rule 3)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "Google Search", "good",
     "People search on Google for free. Advertisers pay Google to show labeled ads next to search results.",
     ["Advertisers come because billions of people search there: searchers are the subsidy side. <b>(Rule 1)</b>",
      "Advertisers earn money from the customers they reach: they are the money side. <b>(Rule 2)</b>",
      "Ads pay for the free service, and labels keep searchers' trust. <b>(Rule 4)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Unity's 2023 Runtime Fee", "bad",
     "Unity sells tools that game developers use to build games. In September 2023, it announced a fee charged to developers each time a game was installed, "
     "including some games already released. Developers protested, Unity changed the plan within weeks, and its CEO left the following month.",
     ["Developers bring the games that make Unity valuable; a sudden fee pushed them away. <b>(Rule 1)</b>",
      "Unity did not first check how developers would react to a fee on installs they could not control. <b>(Rule 3)</b>",
      "Changing prices for games already released broke developers' trust."], "Why it is bad"),
    ("BAD EXAMPLE 2", "Groupon and local merchants", "bad",
     "Groupon sold deep-discount deals, often 50% off, from local businesses to its many shoppers, and took a share of the deal price. "
     "Many small businesses found that a deal cost them more than it earned, because most deal buyers did not return at full price.",
     ["The money side paid for a large subsidy but did not gain enough from the match. <b>(Rule 2)</b>",
      "Shoppers came for the discount, not for the merchant. <b>(Rule 4)</b>",
      "Merchants who lost money did not run a second deal, so the platform lost its supply."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name, two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION 2.2 / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Adobe Reader</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Free readers attracted paying creators (Rule 1)</td></tr>'
      '<tr><td>Google Search</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Advertisers pay; searchers stay free and trust results (Rules 2 and 4)</td></tr>'
      '<tr><td>Unity 2023</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Charged the side everyone comes for (Rule 1)</td></tr>'
      '<tr><td>Groupon</td><td style="color:#991b1b;font-weight:700">Bad</td><td>The money side paid more than it gained (Rule 2)</td></tr></table>'
      '<div class="takeaway">Keep free the side others come for; charge the side that gains the most; make sure the numbers cover the subsidy.</div>',
      "SESSION 2.2 / EXAMPLE SUMMARY")

slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Revenue from each side",
      '<p class="statement">Calculate revenue for each side, then add them.</p>'
      + two(flexcard("Formula", "<p>Revenue = (users on side A x price for A) + (users on side B x price for B)</p>", "card", "USED IN EXERCISES 2 AND 3"),
            flexcard("Example: a campus events app", ul(["2,000 students pay $0.", "40 clubs pay $10.00 a month.",
                                                         "2,000 x $0 + 40 x $10.00 = $400 a month."]), "card good", "WHAT IT LOOKS LIKE")),
      "SESSION 2.2 / TOOL 1 OF 3")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Value per match for the money side",
      '<p class="statement">The money side pays only if it gets enough matches.</p>'
      + two(flexcard("Formula", "<p>Matches per post = total matches / number of posts</p>", "card", "USED IN EXERCISE 3"),
            flexcard("Example: a tutoring app", ul(["800 student requests for 100 tutor listings.", "800 / 100 = 8 requests per listing.",
                                                    "Tutors pay only with at least 10 requests: 8 is not enough yet."]), "card good", "WHAT IT LOOKS LIKE")),
      "SESSION 2.2 / TOOL 2 OF 3")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>", "card", "MEMO BULLET 3")),
      "SESSION 2.2 / TOOL 3 OF 3")

slide("EXERCISE 1 / EASY / 20 MIN", "Find the subsidy side and the money side",
      '<div class="card">' + ul([
          "(a) A free campus newspaper that is paid for by local businesses' ads.",
          "(b) A credit card that gives shoppers cash back, while stores pay a fee on each card payment.",
          "(c) A video game console sold at a low price, while game companies pay the console maker a fee on every game sold."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE", "Platform [letter]: The subsidy side is [group], because [the other side comes for them].\n"
                           "The money side is [group], because [what they gain from the match]."),
          tbox("WORKED EXAMPLE: CAMPUS RADIO APP", "The subsidy side is students, because sponsors pay to reach the students who listen.\n"
               "The money side is local sponsors, because they gain customers from the students who hear their messages.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "The subsidy side attracts the money side",
      "<table><tr><th>PLATFORM</th><th>SUBSIDY SIDE</th><th>MONEY SIDE</th></tr>"
      "<tr><td>(a) Newspaper</td><td>Readers, whom advertisers want to reach</td><td>Local businesses, which gain customers</td></tr>"
      "<tr><td>(b) Credit card</td><td>Shoppers, who even get cash back</td><td>Stores, which gain sales from card users</td></tr>"
      "<tr><td>(c) Game console</td><td>Players, who buy a low-priced console</td><td>Game companies, which earn from players</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Can the money side cover the subsidy? GameNight",
      two(flexcard("Scenario", "<p>GameNight lists board-game nights at campus cafes. Players use it free and get a <b>$2.00 snack voucher</b> per event; GameNight pays for it.</p>"
                   "<p>Cafes pay <b>$30.00</b> per event. This month: <b>40 events</b>, <b>15 players</b> each.</p>"),
          flexcard("Your steps", ul(["<b>Step 1 (Tool 1):</b> Cafe revenue = 40 x $30.00 = $____. Voucher cost = 40 x 15 x $2.00 = $____. Profit = $____.",
                                     "<b>Step 2:</b> Change one price or subsidy so the money side covers the subsidy. Explain why players still come."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE", "Subsidy side: [group], and what we give them: [subsidy].\nMoney side: [group], and what they pay: [price].\n"
                           "Change: [one change to a price or a subsidy].\nNew numbers: revenue $[amount] - subsidy cost $[amount] = $[result].\n"
                           "Why the subsidy side will still come: [reason linked to a rule]."),
          tbox("WORKED EXAMPLE: BOOK-SWAP APP", "Subsidy side: students, and what we give them: free listings and a $1.00 credit per swap.\n"
               "Money side: publishers, and what they pay: $50.00 a month to reach readers.\n"
               "Change: lower the swap credit from $1.00 to $0.50.\n"
               "New numbers: revenue 10 x $50.00 = $500 - subsidy cost 600 x $0.50 = $300 = $200.\n"
               "Why the subsidy side will still come: listing stays free, the main value for students (Rule 1).")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Revenue $1,200 minus vouchers $1,200 = $0",
      '<div class="card good">' + ul([
          "Cafe revenue = 40 x $30.00 = <b>$1,200</b>. Voucher cost = 40 x 15 x $2.00 = <b>$1,200</b>. Profit = <b>$0</b>.",
          "Keep the app free for players (Rule 1).",
          "Raise the cafe fee a little: 40 x $40.00 = $1,600, so $1,600 - $1,200 = $400.",
          "Or lower the voucher to $1.00: 40 x 15 x $1.00 = $600, so $1,200 - $600 = $600.",
          "Players still come for the cafes and the games, not mainly for the voucher."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

slide("EXERCISE 3 / HARD / 50 MIN", "Choose a pricing plan for CampusJobs",
      '<p class="statement">6,000 students / 120 shops / 300 posts / 9,000 applications / costs $4,000</p>'
      + two(flexcard("Option A: Charge everyone $2.00 a month", "<p>A survey shows <b>60% of students</b> would leave if they had to pay.</p>"
                     "<p>Shops would also pay $2.00 a month each.</p>", "card", "OPTION A"),
            flexcard("Option B: Students free, shops pay per post", "<p>Shops pay <b>$25.00 per job post</b>.</p>"
                     "<p>Shops will pay only if each post gets <b>at least 20 applications</b>.</p>", "card", "OPTION B")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1 and 2)",
      '<div class="card">' + ul([
          "Option A: students who stay = 6,000 x 40% = ____; revenue = students x $2.00 + 120 x $2.00 = $______",
          "Option A: applications = 9,000 x 40% = ____; applications per post = applications / 300 = ____",
          "Option B: revenue = 300 x $25.00 = $______; applications per post = 9,000 / 300 = ____",
          "Which option covers the $4,000 costs, and in which do shops get the 20 applications they need?"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to the CEO (Tool 3)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [CEO name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next 60 days we will [one action] and measure [one number]. We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "TutorLink: charge students or tutors?",
      tmpl("To: Ana Lopez, CEO, TutorLink\n"
           "1. Decision and evidence: We should keep students free and charge tutors 10% of each lesson, because tutors come for the students (Rule 1) "
           "and 1,000 lessons at $20 give us 1,000 x $2 = $2,000 a month.\n"
           "2. Biggest risk and trade-off: The weakest point is that tutors may leave if they get too few lessons. "
           "We give up student fees to keep the students that tutors want to reach.\n"
           "3. Next step and decision rule: In the next 60 days we will measure lessons per tutor. "
           "We will change this decision if tutors average fewer than 4 lessons a month."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Charging everyone earns less and loses the shops",
      two(flexcard("The numbers", ul([
          "Option A: 2,400 students stay; 2,400 x $2.00 + 120 x $2.00 = <b>$5,040</b>.",
          "But applications fall to 3,600, or <b>12 per post</b>, below the 20 shops need: shops are likely to leave next.",
          "Option B: 300 x $25.00 = <b>$7,500</b>, above $4,000 costs, with 9,000 / 300 = <b>30 applications</b> per post."])),
          flexcard("A strong memo", ul([
              "Chooses Option B.",
              "Uses at least one number from Step 1.",
              "Names a real risk: shops may post fewer jobs once they pay, or the survey may be wrong.",
              'States a decision rule, e.g. "If applications per post fall below 20, we will lower the fee."']), "card good")),
      "EXERCISE 3 / ANSWER KEY")

slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Name the subsidy side and the money side of a platform and explain why.</p></div>'
      '<div class="card"><div class="n">02</div><p>Check whether the money side covers the cost of a subsidy.</p></div>'
      '<div class="card"><div class="n">03</div><p>Explain why charging both sides the same price can make a platform earn less.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Parker, G. G., and Van Alstyne, M. W. (2005). Two-Sided Network Effects: A Theory of Information Product Design. Management Science.</p>'
      '<p class="ref">Eisenmann, T., Parker, G., and Van Alstyne, M. W. (2006). Strategies for Two-Sided Markets. Harvard Business Review.</p>'
      '<p class="ref">Unity Technologies (2023). An open letter to our community. Unity Blog.</p></div>',
      "SESSION 2.2 / WRAP-UP")


def build(slides, session, title):
    sid = session.replace(".", "_")
    html_out = ROOT / "slides" / f"session_{sid}_lecture.html"
    pdf_out = ROOT / "slides" / f"session_{sid}_lecture.pdf"
    n = len(slides)
    parts = [f'<section class="slide"><div class="top-rule"></div>\n'
             f'  <div class="eyebrow">{e}</div><h2>{t}</h2>\n  <div class="body">{b}</div>\n'
             f'  <div class="footer"><span>{f}</span><span>SLIDE {i} / {n}</span></div>\n</section>\n'
             for i, (e, t, b, f) in enumerate(slides, 1)]
    html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            f"<title>Session {session} Lecture Presentation: {title}</title>\n"
            f"<style>{CSS}</style>\n</head>\n<body>\n\n" + "\n".join(parts) + "\n</body>\n</html>\n")
    html_out.write_text(html, encoding="utf-8")
    subprocess.run(["weasyprint", str(html_out), str(pdf_out)], check=True)
    print(f"{n} slides -> {pdf_out}")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
