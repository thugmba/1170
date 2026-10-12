"""Build the Session 2.1 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_2_1_deck.py
Writes slides/session_2_1_lecture.html and renders slides/session_2_1_lecture.pdf with WeasyPrint.
"""
from html import escape
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent.parent
HTML_OUT = ROOT / "slides" / "session_2_1_lecture.html"
PDF_OUT = ROOT / "slides" / "session_2_1_lecture.pdf"

CSS = """
  @page { size: 16in 9in; margin: 0; }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: #f8f5ef; color: #172033; font-family: "Times New Roman", Times, serif; }
  .slide { width: 16in; height: 9in; padding: .48in .8in .38in; position: relative; overflow: hidden; page-break-after: always; break-after: page; display: flex; flex-direction: column; background: #f8f5ef; }
  .slide:last-child { page-break-after: auto; break-after: auto; }
  .top-rule { height: 4px; position: absolute; top: 0; left: 0; right: 0; background: #991b1b; }
  .eyebrow { flex: 0 0 auto; margin: 0 0 .12in; font: 700 17px "Times New Roman", Times, serif; letter-spacing: 2px; color: #991b1b; }
  h1 { margin: 0; font-size: 66px; line-height: 1.04; font-weight: 700; }
  h2 { margin: 0; font-size: 50px; line-height: 1.08; font-weight: 700; }
  .subtitle { margin: .14in 0 0; font: 400 33px/1.3 "Times New Roman", Times, serif; color: #526174; }
  .body { flex: 1; min-height: 0; margin-top: .24in; display: flex; flex-direction: column; }
  .footer { flex: 0 0 .35in; margin-top: .2in; border-top: 1px solid #c9c2b6; padding-top: .1in; display: flex; justify-content: space-between; font: 700 16px "Times New Roman", Times, serif; letter-spacing: 1.2px; color: #526174; }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: .26in; }
  .grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: .2in; }
  .wide-left { display: grid; grid-template-columns: 1.15fr .85fr; gap: .26in; }
  .card { border: 1.2px solid #aeb7c1; padding: .2in .24in; background: rgba(255,255,255,.55); }
  .card h3 { margin: 0 0 .12in; font: 700 36px/1.15 "Times New Roman", Times, serif; color: #172033; }
  .card p, .card li { margin: 0; font: 400 33px/1.36 "Times New Roman", Times, serif; color: #354052; }
  .card p + p { margin-top: .1in; }
  .card ul { margin: .04in 0 0; padding-left: .26in; }
  .card li + li { margin-top: .12in; }
  .good { border: 1.6px solid #2f6b47; background: #f1f7f2; }
  .bad { border: 1.6px solid #991b1b; background: #fbf1f0; }
  .small-label { margin: 0 0 .1in; font: 700 20px "Times New Roman", Times, serif; letter-spacing: 1.6px; color: #991b1b; }
  .good .small-label { color: #2f6b47; }
  .statement { margin: 0 0 .22in; font: 700 40px/1.25 "Times New Roman", Times, serif; color: #172033; }
  .para { margin: 0; font: 400 37px/1.45 "Times New Roman", Times, serif; color: #263245; }
  .takeaway { margin-top: .24in; padding: .16in .24in; border: 1.2px solid #991b1b; font: 700 32px/1.3 "Times New Roman", Times, serif; color: #991b1b; }
  .hero { width: 100%; height: 100%; object-fit: contain; object-position: center; }
  .flow { display: grid; grid-template-columns: repeat(5, 1fr); gap: .14in; }
  .flow .card { padding: .18in .16in; }
  .flow .n { margin-bottom: .1in; font: 700 36px "Times New Roman", Times, serif; color: #991b1b; }
  table { border-collapse: collapse; width: 100%; }
  th, td { border-bottom: 1px solid #c9c2b6; padding: .09in .14in; text-align: left; font: 400 34px/1.25 "Times New Roman", Times, serif; color: #263245; }
  th { font-weight: 700; color: #991b1b; font-size: 22px; letter-spacing: 1px; }
  td.num { text-align: right; font-weight: 700; }
  .tmpl { margin: 0; padding: .16in .2in; border: 1.2px solid #aeb7c1; background: #ffffff; white-space: pre-wrap; font: 400 29px/1.38 "Times New Roman", Times, serif; color: #172033; }
  .tmpl b { color: #991b1b; }
  .tag { display: inline-block; padding: .02in .1in; margin-left: .06in; border: 1px solid currentColor; font: 700 16px "Times New Roman", Times, serif; letter-spacing: 1px; vertical-align: middle; }
  .term { display: grid; grid-template-columns: 3.2in 1fr; gap: .24in; padding: .18in 0; border-bottom: 1px solid #d5cec2; }
  .term:last-child { border-bottom: 0; }
  .term strong { font: 700 36px/1.25 "Times New Roman", Times, serif; color: #991b1b; }
  .term span { font: 400 33px/1.38 "Times New Roman", Times, serif; color: #354052; }
  .term em { font-style: italic; color: #526174; }
  .ref { margin: 0 0 .12in; font: 400 25px/1.3 "Times New Roman", Times, serif; color: #354052; }
"""

slides = []


def slide(eyebrow, title, body, footer, title_tag="h2", subtitle=None):
    sub = f'<p class="subtitle">{subtitle}</p>' if subtitle else ""
    slides.append((eyebrow, title, body, footer, title_tag, sub))


def card(heading, inner, cls="card", label=None):
    lab = f'<div class="small-label">{label}</div>' if label else ""
    head = f"<h3>{heading}</h3>" if heading else ""
    return f'<div class="{cls}">{lab}{head}{inner}</div>'


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def tmpl(text):
    return f'<div class="tmpl">{escape(text)}</div>'


# 1. Cover: the situation first, to spark curiosity
slide("MODULE 2 / PLATFORM ECONOMICS, BIG DATA &amp; MONETIZATION",
      "Session 2.1: The Data Feedback Loop Strategy",
      '<img class="hero" src="../assets/session_2_1_streamwise_signals_hanji.png" '
      'alt="Jun, founder of StreamWise, looks at a dashboard and asks which signals should change the next decision.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

# 2. Situation data
slide("THE SITUATION", "StreamWise: members cancel, and Jun does not know why",
      '<div class="wide-left">'
      '<div><table><tr><th>MEASURE (ONE MONTH)</th><th style="text-align:right">VALUE</th></tr>'
      '<tr><td>Members at the start of the month</td><td class="num">12,000</td></tr>'
      '<tr><td>Plays started</td><td class="num">48,000</td></tr>'
      '<tr><td>Plays finished</td><td class="num">9,600</td></tr>'
      '<tr><td>Titles saved to "My List"</td><td class="num">3,100</td></tr>'
      '<tr><td>Members who cancelled</td><td class="num">420</td></tr>'
      '<tr><td>Monthly price per member</td><td class="num">$5.00</td></tr></table></div>'
      + card("Jun's three questions", ul([
          "Which signals should he use?",
          "What should he change because of them?",
          "Should he sell viewer profiles to an advertiser, or would that hurt students' trust?"]))
      + "</div>",
      "SESSION 2.1 / FICTIONAL CLASS DATA")

# 3. Strategy in one paragraph
slide("THE STRATEGY IN ONE PARAGRAPH", "What is the Data Feedback Loop Strategy?",
      '<p class="para">A company decides <b>which customer signals to collect</b>, <b>which business decision each signal will improve</b>, '
      "and <b>how to keep customers' trust</b>. Collecting more data does not make a company stronger by itself. "
      "A company gains an advantage when a small set of useful signals changes a decision, the company measures the result, "
      "and the next decision becomes better. This repeating cycle is the <b>data feedback loop</b>.</p>"
      '<div class="takeaway">Use it when a business can see many customer actions but does not know which ones show a real need, '
      'or when it is tempted to collect everything "just in case."</div>',
      "SESSION 2.1 / STRATEGY OVERVIEW")

# 5-6. Words
slide("WORDS YOU NEED FIRST", "Signals",
      '<div class="term"><strong>Signal</strong><span>One recorded customer action.<br><em>Example: a viewer presses "Save" on a show.</em></span></div>'
      '<div class="term"><strong>Strong signal</strong><span>Shows a clear preference because the customer spent time or effort.<br>'
      "<em>Example: finishing a 40-minute episode.</em></span></div>"
      '<div class="term"><strong>Weak signal</strong><span>Can have many meanings.<br>'
      "<em>Example: opening a title for 3 seconds. The viewer may have clicked by mistake.</em></span></div>",
      "SESSION 2.1 / KEY TERMS 1 OF 2")

slide("WORDS YOU NEED FIRST", "Churn rate, ARPU, and consent",
      '<div class="term"><strong>Churn rate</strong><span>The percentage of members who cancel in a period.<br>'
      "Churn rate = members who cancelled / members at the start x 100<br><em>Example: 420 / 12,000 x 100 = 3.5% per month.</em></span></div>"
      '<div class="term"><strong>ARPU<br><span style="font-size:22px;color:#526174;">Average Revenue Per User</span></strong>'
      "<span>The average money earned from one member in a period.<br><em>Example: StreamWise charges $5.00 per month, so ARPU is $5.00 per member per month.</em></span></div>"
      '<div class="term"><strong>Consent</strong><span>A customer\'s clear permission to collect and use their data for a stated purpose.<br>'
      '<em>Example: "We use what you finish and save to recommend shows."</em></span></div>',
      "SESSION 2.1 / KEY TERMS 2 OF 2")

# 7. Loop
steps = [("Collect", "Record a signal."), ("Interpret", "Ask what it may mean."),
         ("Act", "Change one action."), ("Measure", "Compare one number."), ("Learn", "Keep or change the action.")]
slide("THE DATA FEEDBACK LOOP", "Five steps that repeat",
      '<div class="flow">' + "".join(
          f'<div class="card"><div class="n">0{i}</div><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(steps, 1))
      + '</div><div class="takeaway">The loop is complete only when the result of one decision makes the next decision better.</div>'
      '<p class="subtitle" style="margin-top:.24in;">The strategy has four rules. Each rule protects one part of this loop.</p>',
      "SESSION 2.1 / FEEDBACK LOOP")

# 8-11. Rules
rules = [
    ("Rule 1", "Start with the decision, not the data",
     "First name the decision you want to improve. Then collect only the signals that can change it.",
     'A campus cafe app wants to decide "which drink to promote on rainy days." It needs two signals: the weather and the drinks ordered that day. It does not need contact lists or browsing history.',
     '"Let\'s collect everything and find something later." Data with no decision costs money to store and adds privacy risk, but improves nothing.'),
    ("Rule 2", "Use strong signals; check weak signals before you act",
     "Prefer actions that show effort or repeat behavior: finishing, saving, buying again, searching for a specific item.",
     "At StreamWise, 48,000 plays were started but only 9,600 were finished: 9,600 / 48,000 x 100 = 20%. A play started is a weak signal of interest; a play finished is stronger.",
     "Treating a weak signal as proof. A viewer who stops after 10 seconds may dislike the show, or may have received a phone call."),
    ("Rule 3", "Close the loop and measure one result",
     "Collect, interpret, change one action, measure the result, and learn for the next decision.",
     'Students who finish a cooking show often save other cooking shows. StreamWise adds a "More easy cooking" row for them and measures their churn for one month. If churn falls from 3.5% to 2.5%, the row is kept; if not, it is changed.',
     "Changing something but never measuring the result. Without the measure step, the company cannot learn whether the data helped."),
    ("Rule 4", "Earn trust: ask permission, collect only what you need, give value back",
     "Customers share data more willingly when they understand the purpose and receive something useful in return.",
     'A sign-up screen says: "We use what you finish and save to recommend shows. We never sell your viewing history." Members can turn this off at any time.',
     "Collecting or selling data in ways customers would not expect. Even accurate data can damage the brand if customers feel watched."),
]
for no, title, rule, ex, mistake in rules:
    slide(f"THE FOUR RULES / {no.upper()}", f"{no}: {title}",
          f'<p class="statement">{rule}</p><div class="grid2" style="flex:1;">'
          + card("Example", f"<p>{ex}</p>", "card good", "WHAT IT LOOKS LIKE")
          + card("Common mistake", f"<p>{mistake}</p>", "card bad", "WHAT TO AVOID")
          + "</div>",
          f"SESSION 2.1 / {no.upper()} OF 4")

# 12-15. Examples
examples = [
    ("GOOD EXAMPLE 1", "Netflix recommendations", "good",
     "Netflix uses what members watch, finish, and search for to decide which titles and which artwork to show each member. "
     "It tests a change on a group of members and keeps it only if viewing improves. Netflix researchers reported that "
     "recommendations influence about 80% of the hours members stream (Gomez-Uribe and Hunt, 2015).",
     ["It starts with a clear decision: which titles to show on each home screen. <b>(Rule 1)</b>",
      "It relies on strong signals such as finished titles, not only clicks. <b>(Rule 2)</b>",
      "It tests each change and measures the result before keeping it. <b>(Rule 3)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "Spotify Discover Weekly", "good",
     "Since 2015, Spotify has given each listener a new personalized playlist every Monday. "
     "It is built from songs the listener plays, saves, adds to playlists, and skips.",
     ["Saves and repeated plays are strong signals; quick skips show what to avoid. <b>(Rule 2)</b>",
      "The listener receives clear value from the data: new music chosen for them. <b>(Rule 4)</b>",
      "Each week, the listener's reaction becomes new data for the next playlist. <b>(Rule 3)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Google Flu Trends", "bad",
     "From 2008, Google estimated how many people had the flu by counting flu-related searches. In February 2013, it estimated "
     "more than twice the share of flu doctor visits that the U.S. Centers for Disease Control and Prevention (CDC) later reported "
     "(Lazer and others, 2014). Google stopped publishing the estimates in 2015.",
     ["A search is a weak signal: people search because of news or curiosity, not only because they are sick. <b>(Rule 2)</b>",
      "The model was not regularly checked against real doctor-visit data and corrected. <b>(Rule 3)</b>",
      "Big data volume created confidence without accuracy. Many signals are not the same as useful signals."], "Why it is bad"),
    ("BAD EXAMPLE 2", "Target's pregnancy prediction", "bad",
     "The New York Times reported in 2012 that Target used shopping signals, such as unscented lotion and certain vitamins, "
     "to predict which customers were pregnant and mailed them baby-product coupons. A father complained after his teenage "
     "daughter received these coupons.",
     ["The signals were strong and the prediction was often accurate, but customers did not expect a store to know this. <b>(Rule 4)</b>",
      "Customers had not agreed to have sensitive facts guessed from their purchases: no clear consent.",
      "Lesson: accurate data can still damage trust and the brand."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          '<div class="grid2" style="flex:1;">'
          + card("What happened", f"<p>{story}</p>")
          + card(why, ul(reasons), f"card {kind}")
          + "</div>",
          f"SESSION 2.1 / {label}")

# 16. Summary matrix
slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      "<tr><td>Netflix</td><td style=\"color:#2f6b47;font-weight:700\">Good</td><td>Tests each change and measures it (Rule 3)</td></tr>"
      "<tr><td>Spotify</td><td style=\"color:#2f6b47;font-weight:700\">Good</td><td>Strong signals, and value back to the listener (Rules 2 and 4)</td></tr>"
      "<tr><td>Google Flu Trends</td><td style=\"color:#991b1b;font-weight:700\">Bad</td><td>Weak signal, never corrected (Rules 2 and 3)</td></tr>"
      "<tr><td>Target</td><td style=\"color:#991b1b;font-weight:700\">Bad</td><td>Accurate, but no consent or trust (Rule 4)</td></tr></table>"
      '<div class="takeaway">Good data use is not about the amount of data. It is about the right signal, a measured result, and trust.</div>',
      "SESSION 2.1 / EXAMPLE SUMMARY")

# Tools needed for the exercises
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Test group and comparison group",
      '<p class="statement">Try a change on one group, not on a similar group, and compare the same number.</p>'
      '<div class="grid2" style="flex:1;">'
      + card("Example: a cafe coupon", ul([
          "500 members get a coupon (test group). 500 members get none (comparison group).",
          "Coupon group: 75 order this week, or 15 of every 100.",
          "Other group: 50 order, or 10 of every 100.",
          "The coupon added about 5 orders for every 100 members."]), "card good", "WHAT IT LOOKS LIKE")
      + card("Why it matters", "<p>Without the comparison group, you cannot tell whether orders rose because of the coupon or because of something else, such as rainy weather.</p>", "card", "USED IN EXERCISE 2")
      + "</div>",
      "SESSION 2.1 / TOOL 1 OF 3")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: From churn to money",
      '<p class="statement">Lower churn means more members stay and keep paying.</p>'
      '<div style="display:flex;gap:.26in;align-items:flex-start;">'
      + card("Two formulas", ul([
          "Members kept per month = members x (old churn rate - new churn rate)",
          "Revenue kept per month = members kept x monthly price"]), "card\" style=\"flex:1", "USED IN EXERCISE 3")
      + card("Example: a cafe subscription", ul([
          "1,000 members pay $10.00 a month.",
          "Churn falls from 6% to 4%: 1,000 x 2% = 20 more members stay.",
          "Revenue kept: 20 x $10.00 = $200.00 that month.",
          "The gain grows every month, because those members keep paying."]), "card good\" style=\"flex:1", "WHAT IT LOOKS LIKE")
      + "</div>",
      "SESSION 2.1 / TOOL 2 OF 3")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Trade-off and decision rule",
      '<div class="grid2" style="flex:1;">'
      + card("Trade-off", "<p>What you give up to get something you value more.</p>"
             "<p><i>Example: a fitness app refuses $2.00 per user from an advertiser (gives up money) to protect users' trust and its subscriptions (gains).</i></p>", "card", "MEMO BULLET 2")
      + card("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
             '<p><i>Example: "If churn does not fall below 4% in 90 days, we will try a different plan."</i></p>'
             "<p>The result, not opinion, decides.</p>", "card", "MEMO BULLET 3")
      + "</div>",
      "SESSION 2.1 / TOOL 3 OF 3")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Choose the strongest signal: CampusEats",
      '<p class="statement">Decision: which restaurants to show at the top of the app at lunchtime.</p>'
      '<div class="card" style="flex:1;"><h3>Signals the app records</h3>' + ul([
          "(a) A student opens a restaurant page for 2 seconds.",
          "(b) A student orders from the same restaurant three times in one month.",
          "(c) A student gives a restaurant 5 stars after an order.",
          "(d) A student scrolls past a restaurant.",
          '(e) A student adds a restaurant to "Favorites."']) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      '<div class="grid2" style="flex:1;">'
      '<div><div class="small-label">TEMPLATE</div>' + tmpl(
          "Decision: [the decision the business wants to improve]\n"
          "Strongest signal: [letter and action], because [what effort or repeat behavior it shows].\n"
          "Weakest signal: [letter and action], because [two different things it could mean].") + "</div>"
      '<div><div class="small-label">WORKED EXAMPLE: MUSIC APP</div>' + tmpl(
          'Decision: Which songs to put in the "Study Focus" playlist.\n'
          "Strongest signal: a student plays the same song five times during study hours, because repeating a song takes effort and shows a clear preference.\n"
          "Weakest signal: a student opens a song for 2 seconds, because it could mean the student disliked it or simply clicked by mistake.") + "</div>"
      "</div>",
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Repeat orders are the strongest signal",
      '<div class="grid2" style="flex:1;">'
      + card("Strongest", "<p><b>(b) Three orders in one month.</b> The student paid money again and again.</p>"
             '<p>(e) "Favorites" and (c) 5 stars are also useful, but show less effort than repeat orders.</p>', "card good", "STRONG SIGNALS")
      + card("Weakest", "<p><b>(a) a 2-second view</b> and <b>(d) a scroll</b>.</p>"
             "<p>They can mean dislike, a mistake, or simply that the student was not hungry.</p>", "card bad", "WEAK SIGNALS")
      + "</div>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Build a feedback loop: FitU gym app",
      '<div class="wide-left" style="flex:1;">'
      + card("Scenario", "<p>FitU is a campus gym app with <b>2,000 members</b>. Last month <b>160 members cancelled</b>.</p>"
             "<p>Many members <b>book</b> a fitness class but do <b>not attend</b> it.</p>")
      + card("Your steps", ul(["<b>Step 1:</b> Churn rate = 160 / 2,000 x 100 = ____ %",
                               "<b>Step 2:</b> Complete the five-step loop (Rule 3). Use a test group and a comparison group (Tool 1)."]))
      + "</div>",
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      '<div class="grid2" style="flex:1;">'
      '<div><div class="small-label">TEMPLATE</div>' + tmpl(
          "1. Collect: [the signal we record]\n"
          "2. Interpret: [what the signal may mean, and one other possible meaning]\n"
          "3. Act: [one change we will test on a test group, and who is the comparison group]\n"
          "4. Measure: [one number we will compare before and after, and our target]\n"
          "5. Learn: If [the result], we will [keep / change] the action.") + "</div>"
      '<div><div class="small-label">WORKED EXAMPLE: CAMPUS EVENTS APP</div>' + tmpl(
          "1. Collect: students who save an event but do not check in at the door.\n"
          "2. Interpret: they may forget the event, or they may save events they never planned to attend.\n"
          "3. Act: send a reminder 2 hours before saved events to half of these students; the other half gets no reminder (comparison group).\n"
          "4. Measure: attendance rate of saved events; target: from 20% to 30%.\n"
          "5. Learn: If attendance rises to 30% only in the reminded group, we will keep reminders for everyone.") + "</div>"
      "</div>",
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Churn is 8%. Does your loop have all five steps?",
      '<p class="statement">Churn rate = 160 / 2,000 x 100 = 8%</p>'
      '<div class="card good" style="flex:1;"><div class="small-label">A GOOD LOOP</div>' + ul([
          '<b>Collect:</b> records "booked but did not attend."',
          "<b>Interpret:</b> gives two meanings, for example the class time is inconvenient, or the member forgot.",
          "<b>Act:</b> tests one change on a test group and compares it with a comparison group, for example a reminder for half of these members.",
          "<b>Measure:</b> one number with a target, for example churn from 8% to 6%.",
          "<b>Learn:</b> says what happens if the target is or is not reached."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Choose a data strategy for StreamWise",
      '<p class="statement">12,000 members / $5.00 per month / churn 3.5%</p>'
      '<div class="grid2" style="flex:1;">'
      + card("Option A: Sell viewer profiles", "<p>An advertiser will pay <b>$1.00 per member per month</b> for detailed viewing histories.</p>"
             "<p>In a StreamWise survey, <b>30% of members</b> said they would cancel if their viewing history were sold.</p>", "card", "OPTION A")
      + card("Option B: Permission-based recommendations", "<p>Ask permission to use three signals (finished titles, saved titles, searches) only to improve recommendations. Never sell them.</p>"
             "<p>Goal: lower monthly churn from <b>3.5% to 2.5%</b>.</p>", "card", "OPTION B")
      + "</div>",
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tool 2)",
      '<div class="card" style="flex:1;">' + ul([
          "Option A extra revenue per month = 12,000 x $1.00 = $______",
          "If 30% of members cancel: members lost = 12,000 x 30% = ______",
          "Revenue lost per month = members lost x $6.00 ($5.00 subscription + $1.00 advertiser payment) = $______",
          "Option B members kept per month = 12,000 x (3.5% - 2.5%) = ______",
          "Option B revenue kept per month = members kept x $5.00 = $______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to the CEO (Tool 3)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [CEO name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next 90 days we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "FitTrack: an insurer wants users' location history",
      '<p class="subtitle" style="margin:0 0 .14in;">FitTrack is a running app. An insurance company offers $2.00 per user per month for location history.</p>'
      + tmpl(
          "To: Mia Park, CEO, FitTrack\n"
          "1. Decision and evidence: We should refuse to sell location history and instead ask permission to use running data "
          "only for training plans, because users expect privacy (Rule 4) and 25% of surveyed users said they would leave if we sold it.\n"
          "2. Biggest risk and trade-off: The weakest point is that we do not yet know whether better training plans will keep users. "
          "We give up $2.00 per user per month in insurance revenue to protect our users' trust and our subscription revenue.\n"
          "3. Next step and decision rule: In the next 90 days we will offer personalized plans to users who give permission and "
          "measure their monthly churn. We will change this decision if churn does not fall below 4%."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Selling the data costs more than it earns",
      '<div class="grid2" style="flex:1;">'
      + card("The numbers", ul([
          "Option A brings <b>$12,000</b> per month.",
          "If 3,600 members (30%) cancel, StreamWise loses 3,600 x $6.00 = <b>$21,600</b> per month.",
          "Option B keeps 12,000 x 1% = <b>120 members</b>, or <b>$600</b> per month, and this grows every month churn stays lower."]))
      + card("A strong memo", ul([
          "Usually chooses Option B, or a version of it.",
          "Uses at least one number from Step 1.",
          "Names a real risk: members may refuse permission, or recommendations may not lower churn.",
          "States a clear rule for changing the decision.",
          "Option A can still be strong if it explains real consent and gives a decision rule."]), "card good")
      + "</div>",
      "EXERCISE 3 / ANSWER KEY")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Name one strong and one weak signal for a business decision and explain the difference.</p></div>'
      '<div class="card"><div class="n">02</div><p>Complete all five steps of a feedback loop with one measurable result.</p></div>'
      '<div class="card"><div class="n">03</div><p>Explain why selling customer data can cost more than it earns.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Gomez-Uribe, C. A., and Hunt, N. (2015). The Netflix Recommender System: Algorithms, Business Value, and Innovation. ACM Transactions on Management Information Systems.</p>'
      '<p class="ref">Lazer, D., Kennedy, R., King, G., and Vespignani, A. (2014). The Parable of Google Flu: Traps in Big Data Analysis. Science.</p>'
      '<p class="ref">Duhigg, C. (2012). How Companies Learn Your Secrets. The New York Times Magazine.</p>'
      '<p class="ref">Hagiu, A., and Wright, J. (2020). When Data Creates Competitive Advantage. Harvard Business Review.</p></div>',
      "SESSION 2.1 / WRAP-UP")


def build():
    n = len(slides)
    parts = []
    for i, (eyebrow, title, body, footer, tag, sub) in enumerate(slides, 1):
        parts.append(
            f'<section class="slide"><div class="top-rule"></div>\n'
            f'  <div class="eyebrow">{eyebrow}</div><{tag}>{title}</{tag}>{sub}\n'
            f'  <div class="body">{body}</div>\n'
            f'  <div class="footer"><span>{footer}</span><span>SLIDE {i} / {n}</span></div>\n</section>\n')
    html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            "<title>Session 2.1 Lecture Presentation: The Data Feedback Loop Strategy</title>\n"
            f"<style>{CSS}</style>\n</head>\n<body>\n\n" + "\n".join(parts) + "\n</body>\n</html>\n")
    HTML_OUT.write_text(html, encoding="utf-8")
    subprocess.run(["weasyprint", str(HTML_OUT), str(PDF_OUT)], check=True)
    print(f"{n} slides -> {PDF_OUT}")


if __name__ == "__main__":
    build()
