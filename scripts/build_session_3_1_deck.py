"""Build the Session 3.1 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_3_1_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import ROOT, two, flexcard, tbox, term, build  # noqa: E402

SESSION = "3.1"
TITLE = "The Platform Envelopment Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


# Cover and situation
slide("MODULE 3 / COMPETITIVE STRATEGY &amp; INNOVATION FRAMEWORKS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_3_1_unihub_envelopment_hanji.png" '
      'alt="Jae, founder of UniHub, asks whether UniHub should add a textbook market of its own.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "UniHub: most BookSwap users are already here",
      '<p class="statement" style="font-weight:400;">UniHub is a free campus app for timetables and notices, run by Jae. '
      "BookSwap is a separate app for selling used textbooks.</p>"
      "<table><tr><th></th><th>UNIHUB</th><th>BOOKSWAP</th></tr>"
      '<tr><td>Users</td><td class="num">18,000</td><td class="num">6,000</td></tr>'
      '<tr><td>Users who use both apps</td><td class="num">4,200</td><td class="num">4,200</td></tr>'
      "<tr><td>Already has</td><td>Student login, student ID check, payment</td><td>Its own login and payment</td></tr>"
      "<tr><td>Earns money from</td><td>Campus ads</td><td>10% fee on each sale</td></tr>"
      "<tr><td>Cost to win one user</td><td>Almost $0 (in-app banner)</td><td>$8.00 in online ads</td></tr></table>"
      '<div class="takeaway">A textbook market inside UniHub: one developer for 3 months at $4,000 a month = $12,000 once, plus $1,000 per semester to run. Should UniHub build it?</div>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", f"What is the {TITLE[4:]}?",
      '<p class="para">A company that already has many users <b>adds the product of a nearby market to its own platform</b>, often in a '
      "<b>bundle</b>, and so wins that market's customers. It works because the attacker already has the customers and many of the parts "
      "it needs (accounts, payments, data, a sales team), so it can offer the new product at a much lower cost. The new product does not "
      "have to be the best; it must be <b>good enough and easier</b> because it comes in the same app.</p>"
      '<div class="takeaway">Use it when many of your users also use a product in a nearby market and your existing parts can serve that market. '
      "Use it fairly: users must keep a choice.</div>",
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Nearby market and standalone product",
      term("Nearby market<br><span style=\"font-size:24px;color:#526174;\">(adjacent market)</span>",
           "A different market that serves many of the same customers.",
           "textbook trading is next to a campus app; both serve the same students.")
      + term("Standalone product", "A product that does one job and is used on its own.", "BookSwap does only textbook trading."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 4")

slide("WORDS YOU NEED FIRST", "Envelopment and overlap rate",
      term("Envelopment", "A platform enters a nearby market by adding that market's product to its own platform. "
           "The company that enters is the <b>attacker</b>; the company already there is the <b>target</b>.",
           "UniHub (attacker) adds a textbook market and competes with BookSwap (target).")
      + term("Overlap rate", "The share of the target's users who already use the attacker's platform.<br>"
             "Overlap rate = shared users / target's users x 100", "4,200 / 6,000 x 100 = 70%."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 4")

slide("WORDS YOU NEED FIRST", "Shared parts and bundle",
      term("Shared parts", "Things the attacker already has and can use again: accounts, payments, data, sales teams.",
           "UniHub already checks every user's student ID.")
      + term("Bundle", "Two or more products offered together, for one price or free together.",
             "Microsoft 365 gives companies Word, Excel, and Teams in one subscription."),
      f"SESSION {SESSION} / KEY TERMS 3 OF 4")

slide("WORDS YOU NEED FIRST", "Customer acquisition cost and competition law",
      term("Customer acquisition cost<br><span style=\"font-size:24px;color:#526174;\">(CAC)</span>",
           "The money a company spends to win one new customer.<br>CAC = marketing spending / new customers",
           "BookSwap spends $8,000 on ads and wins 1,000 users: $8.00.")
      + term("Competition law<br><span style=\"font-size:24px;color:#526174;\">(antitrust law)</span>",
             "Laws that stop large companies from unfairly blocking competitors, for example by forcing customers to take a bundle.",
             "in 2023, the European Commission investigated Microsoft for bundling Teams with Office."),
      f"SESSION {SESSION} / KEY TERMS 4 OF 4")

# Rules
rules = [
    ('Rule 1',
     'Enter a market where your users already are',
     'Look for a nearby market whose customers already use your app. The more customers you share, the easier and cheaper it is to reach them.',
     "70% of BookSwap's users already open UniHub every day. If UniHub adds a textbook market, these students will see it right away. UniHub does not need to pay for ads.",
     'Entering a market where few of your users are, such as a used-car market for office workers. Then you must pay for ads like any new company, so you have no advantage.'),
    ('Rule 2',
     'Use your shared parts again',
     'You already have user accounts, a payment system, and customer data. Use them again in the new market. Then each new customer costs you very little.',
     'UniHub uses its student login, student ID check, and payment system again. Students do not need a new account, and buyers feel safe because every seller is a real student.',
     'Building the new market as a separate app with a new login and a new payment system. Students must sign up again, and UniHub pays as much as any new company.'),
    ('Rule 3',
     'Make the new product good enough and easier to use',
     'The new product does not need to be the best. But it must do its main job well. Users switch when one app is easier or cheaper than two.',
     "In UniHub Market, a student can list a book in one minute with the login they already have. The fee is 5%, half of BookSwap's 10%.",
     'Adding a weak feature, such as a market where finding a book is slow and hard. Students try it once and go back to BookSwap. Being in the same app does not save a bad product.'),
    ('Rule 4',
     'Let users choose, and play fair',
     'Users must be free to use the new product or not, and you must not block the rival. Forced users get angry, and a big company that blocks rivals can break competition law.',
     'UniHub Market is just one tab. Students who do not want it can ignore it. UniHub also keeps showing BookSwap posts on its notice board.',
     'Making every student use UniHub Market, or deleting BookSwap posts from UniHub. Students complain, and the government may step in.'),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_3_1_rule_{i}_hanji.png" alt="{no}: do and avoid" '
           'style="width:6.6in;height:3.71in;object-fit:contain;flex:none;border:1.2px solid #aeb7c1;">')
    cards = ('<div style="flex:1;">'
             + card("Example", f'<p style="font-size:27px">{ex}</p>', "card good", "DO")
             + card("Common mistake", f'<p style="font-size:27px">{mistake}</p>', "card bad\" style=\"margin-top:.18in", "AVOID") + "</div>")
    if not (ROOT / "assets" / f"session_3_1_rule_{i}_hanji.png").exists():
        slide(f"THE FOUR RULES / {no.upper()}", f"{no}: {title}",
              f'<p class="statement">{rule}</p>'
              + two(flexcard("Example", f"<p>{ex}</p>", "card good", "DO"),
                    flexcard("Common mistake", f"<p>{mistake}</p>", "card bad", "AVOID")),
              f"SESSION {SESSION} / {no.upper()} OF 4")
        continue
    slide(f"THE FOUR RULES / {no.upper()}", f"{no}: {title}",
          f'<p class="statement" style="font-size:34px;margin-bottom:.16in;">{rule}</p>'
          '<div style="display:flex;gap:.26in;align-items:flex-start;">' + pic + cards + "</div>",
          f"SESSION {SESSION} / {no.upper()} OF 4")

# Examples
examples = [
    ("GOOD EXAMPLE 1", "Microsoft Teams and Slack", "good",
     "Slack was a popular standalone chat app for companies. In 2017, Microsoft launched Teams inside Office 365 business subscriptions at no extra cost. "
     "By October 2020, Teams had more than 115 million daily users. Slack spent about half of its revenue on sales and marketing, "
     "and in December 2020 it agreed to be bought by Salesforce for $27.7 billion.",
     ["Millions of companies already paid for Office 365. <b>(Rule 1)</b>",
      "Existing accounts, sales team, and Office files made each Teams user almost free to win. <b>(Rule 2)</b>",
      "Good enough for most companies, at no extra price. <b>(Rule 3)</b>",
      "<i>Lesson:</i> in 2023 the European Commission investigated the bundle, and Microsoft began selling Office without Teams in Europe. <b>(Rule 4)</b>"],
     "Why it is good"),
    ("GOOD EXAMPLE 2", "Uber Eats", "good",
     "Uber added food delivery using the same Uber account and saved card, the same maps, and many of the same drivers. "
     "In the fourth quarter of 2020, when many people stopped taking rides, Uber's delivery orders were worth $10.1 billion, "
     "more than its rides ($6.8 billion).",
     ["People who take Uber rides also order food. <b>(Rule 1)</b>",
      "Drivers, maps, and payments were used again. <b>(Rule 2)</b>",
      "One account and one saved card made ordering easy. <b>(Rule 3)</b>"], "Why it is good"),
    ("BAD EXAMPLE 1", "Google+ and YouTube", "bad",
     "Google launched Google+ in 2011 to compete with Facebook. In 2013, YouTube began requiring a Google+ profile to post comments. "
     "Users complained loudly. Google removed the requirement in 2015 and closed Google+ for consumers in April 2019.",
     ["Users were forced into the new product to keep using YouTube. <b>(Rule 4)</b>",
      "Google had the users, but not their friends; a social network needs your friends (Session 1.2). <b>(Rule 3)</b>",
      "Forcing users damaged trust in YouTube, the product people already liked."], "Why it is bad"),
    ("BAD EXAMPLE 2", "Amazon Fire Phone", "bad",
     "In 2014, Amazon launched the Fire Phone, with a Firefly button that recognized products and let users buy them on Amazon. "
     "Sales were weak, and in October 2014 Amazon reported a charge of about $170 million, mainly for unsold phones.",
     ["Shoppers could already use Amazon on any iPhone or Android phone, so the bundle added little. <b>(Rule 3)</b>",
      "Fewer apps than iPhone and Android: it did not do a phone's main job well enough. <b>(Rule 3)</b>",
      "Shared parts helped Amazon sell more, not make the phone better for users. <b>(Rule 2)</b>"], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Microsoft Teams</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Customers and shared parts already in place (Rules 1 and 2)</td></tr>'
      '<tr><td>Uber Eats</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Drivers, maps, and payments used again (Rule 2)</td></tr>'
      '<tr><td>Google+</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Users forced, product not good enough (Rules 4 and 3)</td></tr>'
      '<tr><td>Amazon Fire Phone</td><td style="color:#991b1b;font-weight:700">Bad</td><td>The bundle gave users little new value (Rule 3)</td></tr></table>'
      '<div class="takeaway">Envelopment wins when the attacker already has the users and the parts, and users choose the bundle because it is easier.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Overlap rate",
      two(flexcard("Formula", "<p>Overlap rate = shared users / target's users x 100</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: music and podcasts", ul([
              "A music app has 40,000 users.",
              "A standalone podcast app has 10,000 users; 3,000 also use the music app.",
              "3,000 / 10,000 x 100 = 30%."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Customer acquisition cost (CAC)",
      two(flexcard("Formula", "<p>CAC = marketing spending / new customers</p><p>Compare the attacker's CAC with the target's CAC.</p>",
                   "card", "USED IN EXERCISE 2"),
          flexcard("Example: music and podcasts", ul([
              "Podcast app: $50,000 on ads, 5,000 users: $10.00.",
              "Music app: $3,000 on banners in its own app, 6,000 podcast listeners: $0.50."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Profit over several periods",
      '<p class="statement">A new product often loses money at first because it costs money to build.</p>'
      + two(flexcard("Formula", "<p>Profit = revenue per period x periods - one-time cost - running cost per period x periods</p>",
                     "card", "USED IN EXERCISE 3"),
            flexcard("Example: a gym app", ul([
                "Meal-plan feature costs $5,000 to build.",
                "Earns $2,000 a month; costs $500 a month to run.",
                "After 4 months: $8,000 - $5,000 - $2,000 = $1,000."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 2.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 10% of our users try the new feature in the first semester, we will stop building it."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Envelopment or not?",
      '<p class="statement">Six companies plan a move:</p><div class="card">' + ul([
          "(a) ChatLine, a messaging app with 30 million users, adds money transfers using the same account and saved bank card.",
          "(b) A bakery opens a second shop in another city.",
          "(c) An email service adds a free calendar inside the same login and competes with standalone calendar apps.",
          "(d) A ride-hailing app cuts its ride prices by 20%.",
          "(e) A phone maker puts a free note-taking app on every new phone and competes with standalone note apps.",
          "(f) A shoe store sells video games on a separate website with separate customer accounts."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Move [letter]: [envelopment / not envelopment], because\n"
               "shared users: [yes / no], shared parts: [what is used again, or none],\n"
               "nearby market: [which market it enters, or none]."),
          tbox("WORKED EXAMPLE: TWO OTHER MOVES",
               "Move: a banking app adds stock trading inside the same app.\n"
               "Envelopment, because shared users: yes, shared parts: the same login and bank account, "
               "nearby market: stock trading apps.\n"
               "Move: a coffee shop adds ten more tables.\n"
               "Not envelopment, because shared users: yes, shared parts: none new, "
               "nearby market: none (it grows in its own market).")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Envelopment needs shared users, shared parts, and a nearby market",
      "<table><tr><th>MOVE</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) ChatLine money transfers</td><td>Envelopment</td><td>Same users, same account and saved card</td></tr>"
      "<tr><td>(b) Second bakery</td><td>Not</td><td>Same product in a new place; no nearby market</td></tr>"
      "<tr><td>(c) Free calendar</td><td>Envelopment</td><td>Same users and login; enters calendar apps</td></tr>"
      "<tr><td>(d) 20% price cut</td><td>Not</td><td>A price cut in its own market</td></tr>"
      "<tr><td>(e) Free note app</td><td>Envelopment</td><td>Every phone buyer gets it; enters note apps</td></tr>"
      "<tr><td>(f) Video games</td><td>Not</td><td>No shared parts; not a market next to shoes</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Check an envelopment opportunity: FitTrack",
      two(flexcard("Scenario", ul([
          "FitTrack: a running app with <b>50,000 users</b>.",
          "MealMate: a standalone meal-planning app with <b>20,000 users</b>; <b>9,000</b> also use FitTrack.",
          "MealMate spent <b>$60,000</b> on ads last year and won <b>10,000</b> new users.",
          "FitTrack plans meal plans in its app: <b>$5,000</b> on in-app banners, <b>8,000</b> users expected in year 1."])),
          flexcard("Your steps", ul([
              "<b>Step 1:</b> Overlap rate = 9,000 / 20,000 x 100 = ____ %. MealMate CAC = $60,000 / 10,000 = $____. "
              "FitTrack CAC = $5,000 / 8,000 = $____.",
              "<b>Step 2:</b> Check the four rules with the template on the next slide."]))),
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Rule 1 (users already there): overlap rate = [number]%. [strong / weak], because [reason].\n"
               "Rule 2 (shared parts): we can use [parts] again. Our CAC is $[number] vs. their $[number].\n"
               "Rule 3 (good enough and easier): users will switch because [one reason]. The risk is [one weakness].\n"
               "Rule 4 (choice and fairness): we will keep [what users can still choose].\n"
               "Verdict: [go / do not go], because [one sentence]."),
          tbox("WORKED EXAMPLE: CITYMAP ADDS PARKING PAYMENT",
               "Rule 1: overlap rate = 6,000 / 10,000 = 60%. Strong: most ParkPay users already open CityMap while driving.\n"
               "Rule 2: maps, accounts, and saved cards used again. Our CAC is $4,000 / 10,000 = $0.40 vs. ParkPay's $40,000 / 5,000 = $8.00.\n"
               "Rule 3: drivers pay in the app they already use to drive there. Risk: some lots work only with ParkPay.\n"
               "Rule 4: we keep showing ParkPay lots on our map.\n"
               "Verdict: go, because overlap is high and our CAC is 20 times lower.")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Overlap 45%; CAC $0.63 vs. $6.00",
      '<div class="card good">' + ul([
          "<b>Overlap rate</b> = 9,000 / 20,000 x 100 = <b>45%</b>: medium; almost half of MealMate users already use FitTrack.",
          "<b>CAC:</b> MealMate $60,000 / 10,000 = <b>$6.00</b>; FitTrack $5,000 / 8,000 = <b>$0.63</b> (about 10 times lower).",
          "<b>Shared parts:</b> accounts, workout data that can suggest meals, payment.",
          "<b>Reason to switch:</b> for example, meal plans that match today's run. <b>Risk:</b> MealMate's recipes may be better.",
          "<b>Choice:</b> for example, users can still connect MealMate.",
          "<b>Verdict:</b> go is reasonable; do not go can also be strong if it argues the meal plans would not be good enough (Rule 3)."]) + "</div>",
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Should UniHub envelop BookSwap?",
      '<p class="statement">18,000 UniHub users / 6,000 BookSwap users, 4,200 shared / each active trader sells about $40 of books per semester</p>'
      + two(flexcard("Option A: Build UniHub Market", "<p>Build cost <b>$12,000</b> once (1 developer x 3 months x $4,000), plus <b>$1,000</b> per semester to run.</p>"
                     "<p>Fee <b>5%</b> (half of BookSwap's). Expect <b>20%</b> of UniHub users to trade each semester.</p>", "card", "ENVELOP"),
            flexcard("Option B: Partner with BookSwap", "<p>A BookSwap tab inside UniHub. BookSwap pays <b>$2</b> for each new user who joins through UniHub.</p>"
                     "<p>Expect <b>1,400</b> new users per semester. No building cost.</p>", "card", "PARTNER")),
      "EXERCISE 3 / SCENARIO: FOUR SEMESTERS")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1 and 3)",
      '<div class="card">' + ul([
          "Overlap rate = 4,200 / 6,000 x 100 = ____ %",
          "Option A: traders per semester = 18,000 x 20% = ____; fee revenue = traders x $40 x 5% = $______",
          "Option A profit over 4 semesters = 4 x fee revenue - $12,000 - 4 x $1,000 = $______",
          "Option A if only 10% trade: traders = ____; revenue per semester = $______; profit over 4 semesters = $______",
          "Option B: revenue per semester = 1,400 x $2 = $______; profit over 4 semesters = $______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to the CEO (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [CEO name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the next semester we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "CityMap: build parking payment, or partner with ParkPay?",
      tmpl("To: Sara Lin, CEO, CityMap\n"
           "1. Decision and evidence: We should build parking payment inside CityMap, because 60% of ParkPay users already use "
           "our app (Rule 1) and our CAC is $0.40 against ParkPay's $8.00 (Rule 2).\n"
           "2. Biggest risk and trade-off: The weakest point is that some parking lots work only with ParkPay. We give up a safe "
           "partnership fee to own a payment business that can grow with our map users.\n"
           "3. Next step and decision rule: In the next semester we will launch in one city and measure how many drivers pay "
           "through CityMap. We will change this decision if fewer than 5% of drivers in that city use it."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Envelopment wins only if about 19% of users trade",
      '<div class="card">' + ul([
          "Overlap rate = 4,200 / 6,000 x 100 = <b>70%</b>.",
          "Option A: 3,600 traders x $40 x 5% = <b>$7,200</b> per semester; profit = $28,800 - $16,000 = <b>$12,800</b>.",
          "Option A if only 10% trade: 1,800 traders, $3,600 per semester; profit = $14,400 - $16,000 = <b style='white-space:nowrap'>-$1,600</b> (a loss).",
          "Option B: 1,400 x $2 = $2,800 per semester; profit = <b>$11,200</b>, no building cost and no risk of a loss."]) + "</div>"
      + '<div class="takeaway">A beats B only above 3,400 traders (about 19% of users), and avoids a loss only above 2,000 traders (about 11%). '
      "The team expects 20%: A earns $1,600 more, just above the line.</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      two(flexcard("If you choose Option A", ul([
          "Points to the 70% overlap and the shared student ID check (Rules 1 and 2).",
          "Names the risk that fewer users trade than the team expects.",
          'Gives a decision rule: "If fewer than 19% of UniHub users trade in the first semester, we will switch to the partnership."']),
          "card good", "ENVELOP"),
          flexcard("If you choose Option B", ul([
              "Explains why safe, certain income ($11,200) is worth more than $1,600 of extra profit at risk.",
              "Names the trade-off: UniHub gives up control of the textbook market.",
              "Gives a decision rule for when to build its own market later."]), "card good", "PARTNER")),
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain envelopment with the words attacker, target, overlap, shared parts, and bundle.</p></div>'
      '<div class="card"><div class="n">02</div><p>Check an opportunity with the overlap rate, the CAC, and the four rules.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare envelopment with a partnership over several periods and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Eisenmann, T., Parker, G., &amp; Van Alstyne, M. (2011). Platform envelopment. Strategic Management Journal, 32(12), 1270-1285.</p>'
      '<p class="ref">Slack Technologies (2021). Form 10-K for the fiscal year ended January 31, 2021. SEC EDGAR.</p>'
      '<p class="ref">European Commission (2023). Commission opens investigation into possible anticompetitive practices by Microsoft regarding Teams.</p>'
      '<p class="ref">Uber Technologies (2021). Uber announces results for fourth quarter and full year 2020.</p>'
      '<p class="ref">YouTube (2015). Official YouTube Blog, July 2015: Google+ no longer required.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
