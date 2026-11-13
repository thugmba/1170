"""Build the Session 1.2 lecture deck (HTML + PDF) for course 1170.

Usage: python3 scripts/build_session_1_2_deck.py
Reuses the Session 2.1 deck style and the Session 2.2 slide helpers.
"""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_session_2_1_deck import card, ul, tmpl  # noqa: E402
from build_session_2_2_deck import two, flexcard, tbox, term, build  # noqa: E402

SESSION = "1.2"
TITLE = "The Network Effect Strategy"
slides = []


def slide(eyebrow, title, body, footer):
    slides.append((eyebrow, title, body, footer))


# Cover and situation
slide("MODULE 1 / FOUNDATIONS OF PLATFORM BUSINESS &amp; NETWORK DYNAMICS", f"Session {SESSION}: {TITLE}",
      '<img class="hero" src="../assets/session_1_2_classchat_network_hanji.png" '
      'alt="Tomás, founder of ClassChat, asks whether to advertise to the whole campus or fill a few classes first.">',
      "COURSE 1170 / DIGITAL TRANSFORMATION &amp; PLATFORM STRATEGY")

slide("THE SITUATION", "ClassChat: 3,000 users, but every class feels empty",
      '<p class="statement" style="font-weight:400;">ClassChat is Tomás\'s free app where students in the same class chat, share notes, '
      "and ask questions before exams. Users are spread over 300 classes, so most students open an almost empty class and leave.</p>"
      "<table><tr><th>CLASSCHAT (THIS SEMESTER)</th><th style=\"text-align:right\">VALUE</th></tr>"
      '<tr><td>Users / classes with at least one user</td><td class="num">3,000 / 300</td></tr>'
      '<tr><td>Students in a typical class / users in it</td><td class="num">60 / 10</td></tr>'
      '<tr><td>Weekly active rate, classes with 30 or more users</td><td class="num">80%</td></tr>'
      '<tr><td>Weekly active rate, classes with fewer than 30 users</td><td class="num">15%</td></tr>'
      '<tr><td>Money to spend on growth</td><td class="num">$6,000</td></tr></table>',
      f"SESSION {SESSION} / FICTIONAL CLASS DATA")

slide("THE STRATEGY IN ONE PARAGRAPH", "What is the Network Effect Strategy?",
      '<p class="para">Some products become <b>more useful for each user when more people use them</b>: a chat app is useless if none of '
      "your friends use it. Nobody wants to join first, and an almost empty product loses its first users. So you <b>fill one small group "
      "first</b> until it is clearly useful there, give early users a reason to stay, help people join together, and check with data that "
      "each new user really makes the product better. Then you move to the next group.</p>"
      '<div class="takeaway">Use it when users get value from each other, not only from the product itself.</div>',
      f"SESSION {SESSION} / STRATEGY OVERVIEW")

# Words
slide("WORDS YOU NEED FIRST", "Network effect, critical mass, penguin problem",
      term("Network effect", "A product becomes more useful for each user as more people use it.",
           "a chat app is more useful when more classmates use it.")
      + term("Direct network effect", "Users gain from users of the same group. (Session 1.3: two different groups.)",
             "chat app users want other chat app users.")
      + term("Critical mass", "The number of users at which a product is useful enough that people stay and invite others.",
             "about 30 of the 60 students in a class."),
      f"SESSION {SESSION} / KEY TERMS 1 OF 3")

slide("WORDS YOU NEED FIRST", "Penguin problem and density",
      term("Penguin problem", "Everyone waits for someone else to join first, so nobody joins.",
           "penguins on the ice wait for one to jump into the water first.")
      + term("Density", "How full a group is. Density = users in the group / people in the group x 100.",
             "12 users in a class of 60: 20%."),
      f"SESSION {SESSION} / KEY TERMS 2 OF 3")

slide("WORDS YOU NEED FIRST", "Standalone value and weekly active rate",
      term("Standalone value", "The value a user gets even when no one else uses the product.",
           "a note app that organizes your own notes.")
      + term("Weekly active rate", "Weekly active users / all users x 100.", "45 of 300 users: 15%."),
      f"SESSION {SESSION} / KEY TERMS 3 OF 3")

# Rules
rules = [
    ("Rule 1", "Fill one small group first",
     "A product feels alive when a group is full, not when many groups each have a few users.",
     "ClassChat spends its budget on 40 first-year business classes, so most students there join at once.",
     "Advertising to the whole campus. Users are spread thin, no class feels alive, and new users leave."),
    ("Rule 2", "Give the first user value even when alone",
     "Early users join an almost empty product. Give them a reason to stay until their friends arrive.",
     "ClassChat organizes each student's own timetable and notes, so it is useful from the first day.",
     "A product that is useless until friends arrive. The first users delete it before friends come."),
    ("Rule 3", "Help the first penguins jump together",
     "People join when they see others join. Bring a whole group in at the same moment.",
     "A class ambassador asks everyone to join in the first lecture, so 40 students join on the same day.",
     "Letting people join one by one, or limiting invitations so friends cannot get in."),
    ("Rule 4", "Check that new users make it better for others",
     "Do not count downloads only. Measure whether fuller groups are more active.",
     "80% weekly active where 30 or more students joined; 15% where fewer joined. The effect is real.",
     "Celebrating downloads. Many people install the app once and never come back."),
]
for i, (no, title, rule, ex, mistake) in enumerate(rules, 1):
    pic = (f'<img src="../assets/session_1_2_rule_{i}_hanji.png" alt="{no}: do and avoid" '
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
    ("GOOD EXAMPLE 1", "Facebook", "good",
     "Facebook started on February 4, 2004, open only to Harvard students. A month later it opened to just three more universities "
     "(Columbia, Stanford, and Yale), then to other universities one by one, before opening to everyone in 2006.",
     ["It filled one university at a time, so each campus was full of real friends. <b>(Rule 1)</b>",
      "Students at a campus joined together, because their friends had just joined. <b>(Rule 3)</b>",
      "It opened a new campus only when earlier ones were active. <b>(Rule 4)</b>"], "Why it is good"),
    ("GOOD EXAMPLE 2", "Sony PlayStation 3 and Blu-ray", "good",
     "Around 2006, two movie-disc formats competed: Blu-ray (Sony) and HD DVD (Toshiba). Buyers and film studios waited to see which would "
     "win. Sony put a Blu-ray player inside every PS3. About 10.5 million PS3s were sold by early 2008, Warner Bros. chose Blu-ray only, "
     "and in February 2008 Toshiba stopped making HD DVD.",
     ["Every PS3 buyer became a Blu-ray owner at once: millions jumped together. <b>(Rule 3)</b>",
      "The PS3 was useful as a game console even without movies. <b>(Rule 2)</b>",
      "More owners made studios choose Blu-ray, which helped every owner."], "Why it is good"),
    ("BAD EXAMPLE 1", "Google Wave", "bad",
     "Google Wave was a tool for writing and chatting together online. In September 2009, Google opened it to about 100,000 invited users. "
     "Most could not invite their friends or coworkers, and many did not understand what to use it for. In August 2010, Google stopped "
     "developing it.",
     ["Limited invitations: users could not bring the people they worked with. <b>(Rule 3)</b>",
      "A tool for working together is useless alone. <b>(Rule 2)</b>",
      "Users were spread over the world instead of whole teams joining. <b>(Rule 1)</b>"], "Why it is bad"),
    ("BAD EXAMPLE 2", "Clubhouse", "bad",
     "Clubhouse is an app for live audio conversations. It grew very fast in early 2021 and had about 14 million downloads by mid-April "
     "2021. But many users found few good live rooms, other apps added live audio, and use fell sharply. In April 2023, Clubhouse cut more "
     "than half of its staff.",
     ["Growth was measured by downloads, not by users who came back. <b>(Rule 4)</b>",
      "With no interesting room live, the app gave a user nothing to do. <b>(Rule 2)</b>",
      "Users could easily listen on other apps too (Session 1.4)."], "Why it is bad"),
]
for label, name, kind, story, reasons, why in examples:
    slide(label, name,
          two(flexcard("What happened", f"<p>{story}</p>"), flexcard(why, ul(reasons), f"card {kind}")),
          f"SESSION {SESSION} / {label}")

slide("GOOD AND BAD AT A GLANCE", "Which rule made the difference?",
      "<table><tr><th>EXAMPLE</th><th>RESULT</th><th>THE RULE THAT DECIDED IT</th></tr>"
      '<tr><td>Facebook</td><td style="color:#2f6b47;font-weight:700">Good</td><td>One campus at a time (Rule 1)</td></tr>'
      '<tr><td>PS3 and Blu-ray</td><td style="color:#2f6b47;font-weight:700">Good</td><td>Millions joined together (Rule 3)</td></tr>'
      '<tr><td>Google Wave</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Friends could not get in (Rule 3)</td></tr>'
      '<tr><td>Clubhouse</td><td style="color:#991b1b;font-weight:700">Bad</td><td>Counted downloads, not return visits (Rule 4)</td></tr></table>'
      '<div class="takeaway">A full small group beats a large empty network.</div>',
      f"SESSION {SESSION} / EXAMPLE SUMMARY")

# Tools
slide("BEFORE THE EXERCISES / TOOL 1", "Tool 1: Density",
      two(flexcard("Formula", "<p>Density = users in the group / people in the group x 100</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example: a dorm", ul([
              "200 students; 50 use a laundry-sharing app.",
              "50 / 200 x 100 = 25%."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 1 OF 4")

slide("BEFORE THE EXERCISES / TOOL 2", "Tool 2: Weekly active rate",
      two(flexcard("Formula", "<p>Weekly active rate = weekly active users / all users x 100</p>", "card", "USED IN EXERCISES 2 AND 3"),
          flexcard("Example", ul([
              "50 users; 35 use it every week.",
              "35 / 50 x 100 = 70%."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 2 OF 4")

slide("BEFORE THE EXERCISES / TOOL 3", "Tool 3: Cost per new user",
      two(flexcard("Formula", "<p>Cost per new user = money spent / new users</p>", "card", "USED IN EXERCISE 3"),
          flexcard("Example: a game", ul([
              "$2,000 on ads brings 500 new players.",
              "$2,000 / 500 = $4.00."]), "card good", "WHAT IT LOOKS LIKE")),
      f"SESSION {SESSION} / TOOL 3 OF 4")

slide("BEFORE THE EXERCISES / TOOL 4", "Tool 4: Trade-off and decision rule (from Session 1.1)",
      two(flexcard("Trade-off", "<p>What you give up to get something you value more.</p>", "card", "MEMO BULLET 2"),
          flexcard("Decision rule", "<p>A promise, written before you start, about which result would make you change your decision.</p>"
                   '<p><i>Example: "If fewer than 30 students in a class join by week 3, we will stop spending in that class."</i></p>',
                   "card", "MEMO BULLET 3")),
      f"SESSION {SESSION} / TOOL 4 OF 4")

# Exercise 1
slide("EXERCISE 1 / EASY / 20 MIN", "Is there a network effect?",
      '<p class="statement">Six products:</p><div class="card">' + ul([
          "(a) A messaging app.",
          "(b) A calculator app.",
          "(c) An online game where players play against each other.",
          "(d) A flashlight app.",
          "(e) A language-exchange app that matches learners who teach each other.",
          "(f) A paid photo-editing app."]) + "</div>",
      "EXERCISE 1 / SCENARIO")

slide("EXERCISE 1 / EASY / 20 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Product [letter]: [network effect / no network effect],\n"
               "because when one more user joins,\n"
               "[who gains what / nobody else gains anything]."),
          tbox("WORKED EXAMPLE: TWO OTHER PRODUCTS",
               "A video-call app: network effect, because when one more user joins,\n"
               "everyone who knows that person can now call them.\n"
               "An alarm clock app: no network effect, because when one more user joins,\n"
               "nobody else gains anything.")),
      "EXERCISE 1 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 1 / CHECK YOUR ANSWER", "Does one more user help the others?",
      "<table><tr><th>PRODUCT</th><th>ANSWER</th><th>WHY</th></tr>"
      "<tr><td>(a) Messaging app</td><td>Network effect</td><td>More people you can message</td></tr>"
      "<tr><td>(b) Calculator</td><td>No</td><td>Works the same alone</td></tr>"
      "<tr><td>(c) Online game</td><td>Network effect</td><td>More players, faster matches</td></tr>"
      "<tr><td>(d) Flashlight</td><td>No</td><td>Works the same alone</td></tr>"
      "<tr><td>(e) Language exchange</td><td>Network effect</td><td>More partners for each language</td></tr>"
      "<tr><td>(f) Photo editor</td><td>No</td><td>Works the same for each user</td></tr></table>",
      "EXERCISE 1 / ANSWER KEY")

# Exercise 2
slide("EXERCISE 2 / MEDIUM / 30 MIN", "Find critical mass: GymBuddy",
      "<table><tr><th>GYM</th><th style=\"text-align:right\">MEMBERS</th><th style=\"text-align:right\">GYMBUDDY USERS</th>"
      "<th style=\"text-align:right\">WEEKLY ACTIVE</th></tr>"
      '<tr><td>A</td><td class="num">400</td><td class="num">40</td><td class="num">6</td></tr>'
      '<tr><td>B</td><td class="num">500</td><td class="num">200</td><td class="num">150</td></tr>'
      '<tr><td>C</td><td class="num">300</td><td class="num">150</td><td class="num">105</td></tr>'
      '<tr><td>D</td><td class="num">600</td><td class="num">60</td><td class="num">9</td></tr>'
      '<tr><td>E</td><td class="num">200</td><td class="num">30</td><td class="num">6</td></tr></table>'
      '<div class="card" style="margin-top:.2in;">' + ul([
          "<b>Step 1:</b> For each gym, density and weekly active rate (Tools 1 and 2).",
          "<b>Step 2:</b> At what density does the weekly active rate jump?",
          "<b>Step 3:</b> How many more users does each low gym need? Which gym is cheapest to fill?"]) + "</div>",
      "EXERCISE 2 / SCENARIO")

slide("EXERCISE 2 / MEDIUM / 30 MIN", "Use the template",
      two(tbox("TEMPLATE",
               "Critical mass is about [number]% density, because groups above it\n"
               "have [number]% weekly active users and groups below it only [number]%.\n"
               "We should focus on [group] next, because it needs only [number] more users.\n"
               "We will use Rule [number]: [one action]."),
          tbox("WORKED EXAMPLE: STUDYBUDDY IN FOUR DORMS",
               "Critical mass is about 50% density, because dorms above it have\n"
               "75-80% weekly active users and dorms below it only 20%.\n"
               "We should focus on Dorm 3 next, because it needs only 40 more users\n"
               "(Dorm 2 needs 160).\n"
               "We will use Rule 3: invite a whole floor to a study night.")),
      "EXERCISE 2 / TEMPLATE AND WORKED EXAMPLE")

slide("EXERCISE 2 / CHECK YOUR ANSWER", "Critical mass is about 40%; fill Gym E next",
      "<table><tr><th>GYM</th><th style=\"text-align:right\">DENSITY</th><th style=\"text-align:right\">WEEKLY ACTIVE RATE</th>"
      "<th style=\"text-align:right\">USERS NEEDED FOR 40%</th></tr>"
      '<tr><td>A</td><td class="num">10%</td><td class="num">15%</td><td class="num">120</td></tr>'
      '<tr><td>B</td><td class="num">40%</td><td class="num">75%</td><td class="num">-</td></tr>'
      '<tr><td>C</td><td class="num">50%</td><td class="num">70%</td><td class="num">-</td></tr>'
      '<tr><td>D</td><td class="num">10%</td><td class="num">15%</td><td class="num">180</td></tr>'
      '<tr><td>E</td><td class="num">15%</td><td class="num">20%</td><td class="num">50</td></tr></table>'
      '<div class="takeaway">A strong answer names one action, such as a "find a partner" week where a whole class joins together (Rule 3).</div>',
      "EXERCISE 2 / ANSWER KEY")

# Exercise 3
slide("EXERCISE 3 / HARD / 50 MIN", "Where should ClassChat spend $6,000?",
      '<p class="statement">300 classes of 60 / about 10 users each / 80% active at 30+ users, 15% below / both options: $6,000, 1,500 new users</p>'
      + two(flexcard("Option A: Ads for the whole campus", "<p>The 1,500 new users spread evenly over all <b>300</b> classes.</p>",
                     "card", "SPREAD WIDE"),
            flexcard("Option B: Fill 40 classes first", "<p>$100 ambassador in each of <b>40</b> first-year business classes ($4,000) "
                     "and a launch event ($2,000).</p><p>All 1,500 join in those 40 classes, which now have <b>400</b> users.</p>",
                     "card", "FILL ONE GROUP")),
      "EXERCISE 3 / SCENARIO")

slide("EXERCISE 3 / STEP 1", "Calculate before you decide (Tools 1, 2, and 3)",
      '<div class="card">' + ul([
          "Cost per new user in both options = $6,000 / 1,500 = $______",
          "Now: weekly active users = 3,000 x 15% = ______",
          "Option A: users per class = 4,500 / 300 = ______; density = ______%; weekly active = 4,500 x ______% = ______",
          "Option B: users per class in 40 classes = (400 + 1,500) / 40 = ______; weekly active there = 1,900 x ______% = ______; "
          "other 260 classes = 2,600 x 15% = ______; total = ______",
          "New users Option B needs so that the 40 classes reach 30 each: 40 x 30 - 400 = ______"]) + "</div>",
      "EXERCISE 3 / CALCULATIONS")

slide("EXERCISE 3 / STEP 2", "Write a 3-bullet memo to Tomás (Tool 4)",
      '<div class="small-label">TEMPLATE</div>' + tmpl(
          "To: [founder name], [company]\n"
          "1. Decision and evidence: We should choose [option] because [the rule it follows] and [one number from your calculation].\n"
          "2. Biggest risk and trade-off: The weakest point is [risk]. We give up [what we lose] to gain [what we protect or win].\n"
          "3. Next step and decision rule: In the first weeks we will [one action] and measure [one number]. "
          "We will change this decision if [result].")
      + '<div class="takeaway">Then give a 2-minute presentation using your three bullets.</div>',
      "EXERCISE 3 / MEMO TEMPLATE")

slide("EXERCISE 3 / WORKED EXAMPLE", "GymBuddy: focus on Gym E?",
      tmpl("To: Sam Lee, founder, GymBuddy\n"
           "1. Decision and evidence: We should focus next month's budget on Gym E, because gyms at 40% density have 70-75% weekly "
           "active users (Rule 4) and Gym E needs only 50 more users to get there (Rule 1).\n"
           "2. Biggest risk and trade-off: The weakest point is that Gym E is small, so it adds few users. We give up faster growth in "
           "user numbers to make one more gym truly active.\n"
           "3. Next step and decision rule: In the next four weeks we will run a \"find a partner\" week at Gym E and measure density. "
           "We will change this decision if Gym E is still below 30% density after four weeks."),
      "EXERCISE 3 / WORKED EXAMPLE")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "Same cost, almost 3 times more active users",
      '<div class="card">' + ul([
          "Cost per new user = <b>$4.00</b> in both options. Now: <b>450</b> weekly active users.",
          "Option A: <b>15</b> users per class, density <b>25%</b> (below critical mass); 4,500 x 15% = <b>675</b>.",
          "Option B: <b>47.5</b> users per class; 1,900 x 80% = 1,520, plus 2,600 x 15% = 390; total = <b>1,910</b>.",
          "Option B needs at least <b>800</b> new users in the 40 classes. With only 600, each class has 25 users, and the total falls to "
          "3,600 x 15% = 540."]) + "</div>",
      "EXERCISE 3 / ANSWER KEY 1 OF 2")

slide("EXERCISE 3 / CHECK YOUR ANSWER", "What a strong memo looks like",
      '<div class="card good">' + ul([
          "Chooses Option B (Rules 1 and 3): the cost is the same, so the difference is where the users go.",
          "Names the risk: ambassadors may bring fewer than 800 users.",
          'Decision rule: "If fewer than 20 students in a class join by week 3, we will move that ambassador budget to another class."']) + "</div>",
      "EXERCISE 3 / ANSWER KEY 2 OF 2")

# Success check and references
slide("SUCCESS CHECK", "Can you do these three things?",
      '<div class="flow" style="grid-template-columns:repeat(3,1fr);">'
      '<div class="card"><div class="n">01</div><p>Explain network effects, critical mass, and the penguin problem.</p></div>'
      '<div class="card"><div class="n">02</div><p>Measure density and weekly activity to find critical mass.</p></div>'
      '<div class="card"><div class="n">03</div><p>Compare "spread wide" with "fill one group first" and write a decision rule.</p></div></div>'
      '<div style="margin-top:.3in;"><div class="small-label">REFERENCES</div>'
      '<p class="ref">Katz, M. L., &amp; Shapiro, C. (1985). Network externalities, competition, and compatibility. American Economic Review, 75(3).</p>'
      '<p class="ref">Farrell, J., &amp; Saloner, G. (1986). Installed base and compatibility. American Economic Review, 76(5).</p>'
      '<p class="ref">Harvard Magazine (2019). How Facebook escaped Harvard.</p>'
      '<p class="ref">The Japan Times (2008, February 20). It\'s official: Toshiba pulls plug on HD DVD.</p>'
      '<p class="ref">eWeek (2010). Google cancels Wave. CNBC (2023, April 27). Clubhouse layoffs.</p></div>',
      f"SESSION {SESSION} / WRAP-UP")


if __name__ == "__main__":
    build(slides, SESSION, TITLE)
