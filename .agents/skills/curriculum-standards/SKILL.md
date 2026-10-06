---
name: curriculum-standards
description: >-
  Authoritative standards and procedural runbook for authoring university-level business/MBA courses,
  16-session modular curriculums, 16:9 widescreen presentation slide decks, audited spreadsheet labs,
  and term project guidelines. Activate this skill whenever creating, updating, or reviewing course
  syllabi, lecture presentations, classroom exercises, or academic learning materials.
---

# University Curriculum & Lecture Presentation Standards

This skill provides comprehensive pedagogical specifications, structural templates, slide deck design systems, and quality assurance checklists for developing professional business and management college courses.

---

## 1. Pedagogical Profile & Audience Guidelines

* **Target Audience:**
  * Undergraduate and graduate (MBA) business college students.
  * Non-native English speakers.
  * Assumed to have zero prior academic or professional background in the subject matter.
* **Tone & Register:**
  * Authoritative, direct, clear, and business-focused.
  * Avoid convoluted academic jargon, empty platitudes, or abstract filler.

### 1.1 Core Concept Instruction Requirement

* **Teach Before Applying:** Every session must give students sufficient conceptual content to understand a framework before asking them to analyze a case, calculate a metric, or make a recommendation. Vocabulary lists and isolated calculations do not count as conceptual instruction.
* **Minimum Concept Package:** For each central framework, provide:
  * A plain-language definition and a contrast with the most likely misconception.
  * The causal mechanism: explain why the framework changes a business outcome, not only what it is called.
  * A stage model when the topic concerns a process, lifecycle, maturity path, or implementation journey. Each stage must name observable evidence that students can recognize.
  * An evaluation rubric or decision scorecard that names the criteria, interpretable evidence, and limits of the assessment. Scores may organize judgment but must not be presented as a substitute for judgment.
  * A worked visual, micro-example, or case that makes the mechanism concrete before independent practice.
* **Application Alignment:** Exercises and presentation assignments must require students to use the same definitions, stages, and evaluation criteria introduced in the concept section. State the explicit connection so an activity is not experienced as a separate task.
* **Business-First Explanation:** Define any financial, technical, or operational term in plain language on first use, including what it means for customers, employees, operations, or the balance sheet.
* **Conceptual Illustration Prompts:** When an illustration is used to teach a framework rather than decorate a page, it must include a small number of readable in-image prompts that direct student attention to the decision or causal mechanism. Use short speech bubbles, thought bubbles, question cards, or callouts such as "What must improve as demand grows?" or "Why would users stay here?". The prompt must be tied to the session's central question, visually adjacent to the relevant person or mechanism, and legible at the intended presentation size. Do not add text merely as decoration.
* **Mandatory Acronym Expansion (Zero Exception Rule):**
  * Whenever financial, accounting, operational, or technical acronyms (e.g., PP&E, CapEx, OpEx, CAC, LTV, ARR, GMV, EBITDA, AOV, HHI) are introduced in slides, syllabus text, or lab exercises, the full English term must be explicitly defined upon first use (e.g., `Property, Plant, and Equipment (PP&E)`).
  * Every specialized acronym must be paired with an intuitive, plain-language business explanation of its real-world balance-sheet or operational meaning so non-native students with no prior background understand it immediately.
* **Interactive 3-Hour Session Rhythm (1:2 Delivery Ratio):**
  * Maximum Interactivity Principle: Courses must minimize passive lecture delivery and maximize hands-on student execution.
  * Lecture Phase (Approx. 1 Hour / 60 Minutes): Concise instruction covering keywords, foundational frameworks, and intuitive micro-examples.
  * Hands-On Practice & Problem-Solving Phase (Approx. 2 Hours / 120 Minutes):
    * Real-Case Practice: Students analyze concrete historical cases and manipulate audited spreadsheet data to master core mechanics.
    * Real-World Problem Solving: Students resolve complex executive dilemmas and formulate strategic decisions.
* **Mandatory Two-Tier Exercise Architecture:**
  * Every session must include a minimum of two structured exercises with ascending difficulty:
  * Exercise 1 (Foundational / Simple): Guided, step-by-step lab protocol with explicit data coordinates and formulas to ensure baseline operational competency.
  * Exercise 2+ (Advanced / Complex): Unstructured strategic decision challenge requiring students to evaluate tradeoffs, stress-test business models, and deliver a structured 3-bullet decision memo to the Board of Directors or CEO.

---

## 2. Structural Curriculum Architecture

* **Modular Framework:**
  * Exactly 4 Modules per course.
  * Exactly 4 Sessions per Module (16 Sessions total).
* **Course Promotional Image (16:9 Banner):**
  * Placement: Positioned at the very top of the course syllabus document.
  * Resolution & Format: 16:9 widescreen format (1920x1080 resolution), PNG or WebP.
  * Summarizes the 4 modular overview cards, key milestones, and course standards.
* **Clickable Table of Contents (TOC):**
  * Placement: Preceding Module 1.
  * Bidirectional Anchor Matching: Every TOC link (e.g., `[Session X.Y: Title](#session-X-Y)`) must pair with an exact HTML anchor tag (e.g., `<a id="session-X-Y"></a>`) preceding the session heading.

---

## 3. Standardized Session Content Template

Each of the 16 sessions must follow this standardized template:

```markdown
<a id="session-X-Y"></a>
### Session X.Y: [Descriptive Business Title]

![Session X.Y Summary Slide](assets/session_X-Y_slide.png)

* **Lecture Presentation:** [Download Slides (PDF)](slides/session_X_Y_lecture.pdf)

* **Keywords:** 4 to 5 precise, business-relevant terms (with acronym expansions).
* **Main Theories:**
  * [Theory 1](active-link): Author (Year) and seminal framework description.
  * [Theory 2](active-link): Economic model and market mechanism.
* **Micro-Examples:**
  * 3 concise, intuitive cross-industry examples illustrating the concept in action.
* **Real Business Case:**
  * Longitudinal enterprise case study tied to verifiable multi-year historical numbers from SEC filings.
* **Lab Dataset:**
  * File Link: [data/session_X_Y_dataset.csv](data/session_X_Y_dataset.csv)
  * Columns: Complete list of CSV/TSV column names adhering to standardized unit suffix taxonomy.
* **Primary Filings & External References:**
  * Verified Link 1: Official regulatory filing (e.g., SEC EDGAR Form 10-K / Form 20-F).
  * Verified Link 2: Authoritative academic paper or industry standard.
* **Step-by-Step Lab Protocol (Exercise 1: Foundational Practice):**
  * Step 1: Open the Dataset (Specify software and file path).
  * Step 2: Inspect Primary Sources & Financial Terminology (Define acronyms and cite filing item/note).
  * Step 3: Enter Formulas (Provide exact spreadsheet cell coordinates and capitalized English formulas in backticks).
  * Step 4: Compute Derived Metrics / Chart Construction.
  * Step 5: Compare Results & Interpret Business Meaning.
* **Step-by-Step Strategic Decision Challenge (Exercise 2+: Advanced Problem Solving):**
  * Strategic Problem: Framed executive dilemma based on the lab data.
  * Student Task: 3 structured tasks culminating in a 3-bullet decision brief addressed to the Board of Directors or CEO. (For milestone sessions, cross-reference Project.md).
```

---

## 4. Lecture Slide Presentation Deck (16:9 Multi-Page PDF Specifications)

* **Aspect Ratio & Canvas Media:**
  * Standard 16:9 widescreen format (`@page { size: 16in 9in; margin: 0; }`).
  * Print color fidelity: `-webkit-print-color-adjust: exact; print-color-adjust: exact;`.
  * Page breaks: `page-break-after: always; break-after: page;`.
* **Universal Fixed Coordinate Frame (Zero Vertical Drift Mandate):**
  * Top Harvard Crimson Accent Line: `position: absolute; top: 0; left: 0; right: 0; height: 4px; background: #991B1B;`.
  * Header Area: `position: absolute; top: 0.55in; left: 0.8in; right: 0.8in; height: 1.35in;`.
  * Body Content Area: `position: absolute; top: 2.15in; bottom: 1.1in; left: 0.8in; right: 0.8in;` (Height = `5.75in`).
  * Footer Area: `position: absolute; bottom: 0.45in; left: 0.8in; right: 0.8in; height: 0.5in;`.
  * Sub-Pixel Alignment: Footer border lines, slide numbers (`Slide X / N`), and course metadata must maintain mathematically identical Y coordinates across all pages (`y0 = 595.14 pt` within +/- 0.5pt).
* **Classroom Lecture-Hall Readability Standards (20% Enlarged Typography):**
  * Absolute Universal Minimum Font Floor: No text anywhere on the slide canvas may fall below `15px` (badges: `15px-16px`).
  * Card/Box Body Text & Bullet Lists: Minimum `20px` (line-height: `1.38-1.40`).
  * Key Term Markers: `20.5px` semi-bold italic serif.
  * Quantitative Metric Numbers in Showdowns: `32px-36px` bold.
  * Dimension Labels: `20px-22px` bold.
* **Lecture Summary Slide Density Rule:**
  * Treat the `20px` card-body rule as an absolute floor, not a normal design target. In a classroom summary slide, explanatory text should normally be `28px` or larger, and the two or three primary questions or decisions should normally be `36px` or larger.
  * A session summary slide is a conceptual map, not a compressed lesson plan. Show the small set of core concepts students will encounter and the relationship among them. Do not include their definitions, stage descriptions, evaluation criteria, case evidence, formulas, or full activity instructions.
  * Use a concise title, three to five concept names, and at most one guiding question or visual relationship. Move explanatory detail and all evidence to subsequent concept slides.
  * If the intended content cannot be read at the target size, remove or split content. Do not solve density by shrinking instructional text to the minimum floor.
  * Before approval, render the slide at its final 16:9 resolution and inspect it as a single full slide. Confirm that the primary instructional content is readable without zooming and that no slide depends on small text to carry a central concept.
  * **Two-Column Text Safety Rule:** Treat every column as a bounded text area, including small all-caps labels. Do not estimate width from character count. Long labels, letter spacing, and bold weight can substantially increase rendered width. Before export, either shorten the label or verify its rendered bounding box stays inside its column with at least `48px` clearance from a central divider and the slide edge.
  * **Visual Export Gate:** A source SVG or HTML is not an approved slide. Export the final PNG or PDF, inspect the complete 1920x1080 rendered slide, and check every title, label, rule, card edge, divider, and footer for overlap or clipping. If a visual defect is found, correct the source, re-export, and repeat the inspection before showing it to the user.
* **Academic Default Typography (Times New Roman Standard):**
  * Baseline Font: `font-family: 'Times New Roman', Times, Georgia, serif;`.
  * Restrained Bold: Harsh heavy bold (`font-weight: 900`) is barred from body text; use semi-bold italic serif (`font-style: italic; font-weight: 600;`) for conceptual terms.
  * **Font-Fidelity Gate:** CSS component rules must not override the baseline with a different family. After PDF export, run `pdffonts` and confirm that every embedded text font is Times New Roman before approval.
  * **Renderer-Compatibility Gate:** Treat every HTML-to-PDF renderer warning as a layout defect until investigated. Do not rely on unsupported CSS properties for alignment. Use renderer-supported primitives and visually inspect every slide that uses pseudo-elements, counters, grid alignment, or generated markers after export.
* **Dedicated A vs. B Showdown Slides:**
  * Unified Height Placement: Showdowns must live inside `.slide-body` (`height: 5.75in`) as side-by-side contrasting brand cards, guaranteeing identical slide height across all pages.
  * Prominent Vector Logos: 48px vector brand marks in the card header row.
  * Cool vs. Warm Duo: Side-by-side contrasting corporate brand colors.
  * 3-Pillar MBA Content: Audited SEC 10-K operational and balance-sheet metrics (Capacity, Asset Intensity, Productivity Multiplier).
* **Strict Elimination of AI Box Left Lines:**
  * One-sided accent borders (`border-left: 3px/4px solid ...`) are strictly prohibited across all slides, callout boxes, and cards.
  * All containers must use balanced 4-sided translucent surfaces (`border: 1px solid rgba(255,255,255,0.20)`) or clean background cards.

---

## 5. Lab Datasets, Spreadsheet Formulas & OS Environment

* **English MS Windows & US English Excel Baseline:**
  * Operating System: Microsoft Windows (US English Edition).
  * Decimal Separator: Standard period (`.`, e.g., `0.08` or `125.50`).
  * Formula Argument Separator: Standard comma (`,`, e.g., `=IF(D2>0, D2/C2*100, 0)`).
  * Capitalized English Functions: Use official English Excel function names exclusively (e.g., `=SUM(...)`, `=AVERAGE(...)`, `=IF(...)`).
  * Mandatory Inline Code Formatting: Every cell coordinate, column header, and mathematical formula must be enclosed in standard Markdown backticks (e.g., "In cell `H2`, enter formula: `=(D2/C2)*100`").
* **Standardized Column Naming & Unit Suffix Taxonomy:**
  * Scale & Currency: `_USD_M` (millions of USD), `_USD` (exact dollars), `_JPY_B` (billions of JPY), `_EUR_M` (millions of EUR).
  * Ratios & Percentages: `_Pct` (e.g., `Operating_Margin_Pct`).
  * Counts & Quantities: `_Count` or `_Units`.
  * Audit Trail: Mandatory `Filing_Source` column identifying the exact regulatory item/note.

---

## 6. Strict Editorial Invariants & Style Constraints

* **Internal Scope Isolation:** Developer rules and prompt instructions must NEVER appear within student-facing syllabus text.
* **Zero Emojis:** Strictly prohibited across all documentation, markdown files, HTML templates, slide decks, and script outputs.
* **Zero Em/En Dashes:** Em dashes (`—`) and en dashes (`–`) are barred. All textual separators use standard hyphens (`-`) or colons (`:`).
* **Audit-First Methodology:** Every factual claim and financial figure requires verification against primary source documents (SEC Form 10-K, Form 20-F).

---

## 7. Pre-Flight 7-Point Quality Assurance Checklist

Before approving or deploying any curriculum deliverable, verify compliance against this checklist:

1. **Visual Asset & Slide Deck Integrity:**
   - 16:9 Course Promotional Banner positioned at top.
   - 16:9 Summary slide image at the start of every session (`assets/session_X-Y_slide.png`).
   - 16:9 Lecture presentation PDF available for download (`slides/session_X_Y_lecture.pdf`).
   - Slide decks enforce Universal Slide Frame (4px Crimson bar, Header 1.35in, Body 5.75in, Footer 0.5in) with sub-pixel footer coordinates locked at `y0 = 595.14 pt` (+/- 0.5pt).
   - Times New Roman typography enforced; 20% font floor (minimum 20px card body, 15px universal canvas floor); zero `border-left` AI lines.
   - For every two-column or multi-column slide, rendered text remains inside its assigned column with no overlap at dividers, card boundaries, or slide edges. Final exported PNG/PDF has been visually inspected, not only source code reviewed.
2. **Mandatory Acronym Expansion:**
   - All accounting, financial, and technical acronyms (PP&E, CapEx, OpEx, CAC, LTV, ARR, GMV, EBITDA, etc.) expanded on first use with plain-language real-world business definitions.
3. **Table of Contents & Anchor Integrity:**
   - TOC immediately precedes Module 1.
   - Bidirectional match between TOC links (`#session-X-Y`) and HTML anchor tags (`<a id="session-X-Y"></a>`).
4. **Interactive 1:2 Delivery Ratio & Two-Tier Exercises:**
   - Exercise 1: Step-by-step Excel protocol with explicit cell coordinates and US English formulas.
   - Exercise 2+: Executive dilemma with structured 3-bullet decision brief deliverable. Milestone sessions cross-reference Project.md.
5. **Dataset Integrity & Taxonomy:**
   - Dedicated CSV file in `data/` for every session.
   - Columns follow unit suffix taxonomy (`_USD_M`, `_Pct`, `_Count`).
   - `Filing_Source` column traces every number to audited primary filings.
6. **100% Free Accessibility & Literature Hyperlinks:**
   - Every cited theory and author has an active markdown link (open-access paper priority, Wikipedia fallback).
   - No paywalls or gated logins. All URLs return HTTP 200.
7. **Strict Editorial Invariants:**
   - 100% zero emojis.
   - 100% zero em dashes and en dashes (hyphens and colons only).
   - Authoritative, professional academic tone throughout.
