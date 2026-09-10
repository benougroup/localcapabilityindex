# Claude To-Do List

**This file is cleared after each task batch. GPT writes new tasks here, Claude executes them.**

Currently empty. Awaiting tasks from GPT.

When GPT adds tasks, they will appear below this line in clear, actionable format.

# Local Capability Index

## SEO\-to\-AEO Controlled Experiment — Business Requirements Document

**Document version:** 1\.0
**Date:** 10 September 2026
**Status:** Approved for implementation planning
**Business owner:** Benou Group / Local Capability Index
**Implementation audience:** Claude Code or equivalent technical implementer
**Repository:** `benougroup/localcapabilityindex`
**Production site:** `https://localcapabilityindex.com/`

---

## Contents

1. Executive decision
2. Background and current state
3. Business problem
4. Purpose
5. Objectives
6. Research questions and hypotheses
7. Scope
8. Definitions and outcome funnel
9. Experimental design
10. Business and content requirements
11. Functional requirements
12. Technical SEO requirements
13. Indexing and submission requirements
14. Measurement plan
15. Non\-functional requirements
16. Repository and implementation requirements
17. Release and change control
18. Acceptance criteria
19. Risks and controls
20. Implementation instructions for Claude Code
21. Traceability summary
22. Reference guidance

## 1\. Executive decision

Local Capability Index shall run a controlled, public SEO experiment to determine which page characteristics cause low\-competition Falkland Islands service\-discovery pages to progress from crawlability to indexing, ranking, search\-assisted AI retrieval, and citation\.

The experiment shall use two topic families selected by the business owner:

1. Chinese Tui Na massage enquiries in the Falkland Islands\.
2. Vietnamese\-style massage enquiries in the Falkland Islands\.

The experiment shall vary three factors independently: semantic HTML richness, contextual depth, and internal\-link strength\. A complete 2×2×2 design produces eight combinations per topic and sixteen experimental pages\. Pages must be useful, distinct, truthful, visibly identified as research pages, and safe for public indexing\. The site shall not present fictional providers, reviews, ratings, addresses, telephone numbers, qualifications, or health outcomes as real\.

This BRD is intentionally solution\-specific\. It defines the required information architecture, page controls, build behavior, measurement protocol, evidence model, and acceptance criteria so implementation does not depend on discretionary interpretation\.

## 2\. Background and current state

The domain itself appears for exact\-name searches, which demonstrates that search engines can identify the site root\. It does not demonstrate that the two intended test pages have been discovered, crawled, indexed, ranked, retrieved by an AI search system, or cited by a model\.

The current repository is a static Python\-generated site hosted through GitHub Pages\. Its maintained inventory includes two active jurisdictions, HKG and FLK, six problem pages, thirteen synthetic business profiles, directory and jurisdiction hubs, and a generated sitemap\. The current sitemap contains approximately twenty\-eight URLs\. Empty jurisdiction hubs are intentionally `noindex,follow`\.

The two existing pages most relevant to the experiment are:

|Historical page                  |Current subject                                         |Known characteristics                                                   |
|---------------------------------|--------------------------------------------------------|------------------------------------------------------------------------|
|`flk/en/problems/99-flk-002.html`|Old ankle sprain discomfort and Chinese Tui Na enquiries|Approximately 506 words; self-canonical; internal links; no page JSON-LD|
|`flk/en/problems/99-flk-003.html`|Stress-related muscle tension and Vietnamese massage    |Approximately 414 words; self-canonical; internal links; no page JSON-LD|

Two relevant long\-form pages also exist under `premium-blogs/`, but are not currently part of the active sitemap/discovery inventory:

- `chinese-kung-fu-ankle-correction.html`
- `vietnamese-massage-back-pain-relief.html`

The homepage currently contains volume and compliance claims that no longer match the maintained site inventory\. These include claims about hundreds of pages, six active jurisdictions, dozens of queries, and universal structured\-data compliance\. Such discrepancies weaken trust and make the experiment harder to interpret\.

The current `robots.txt` permits crawling and references the sitemap\. An IndexNow key file exists, but the repository does not provide auditable evidence that URL submissions occurred\. Sitemap presence, an IndexNow response, and crawl accessibility are signals or notifications; none proves indexing\.

## 3\. Business problem

The experiment cannot currently answer why a page fails to appear because its tracker and site implementation do not consistently separate the stages of search visibility\. A page may be technically accessible but undiscovered, discovered but uncrawled, crawled but unindexed, indexed but unranked, ranked but not retrieved by a model, or retrieved without citation\.

The business also needs to distinguish the effect of page structure from the effect of useful context and link prominence\. Improving all attributes on one page would create a better page but would not reveal which attribute affected the result\. Conversely, mass\-producing near\-duplicate pages could cause canonical consolidation, quality suppression, or reputational harm and would invalidate the research\.

## 4\. Purpose

The purpose is to establish whether conventional SEO visibility is a practical prerequisite or bridge for AEO visibility on this site, and to identify which controlled page attributes most influence the result in a low\-population, low\-competition location\.

The experiment is a research publication, not a directory of verified local providers and not medical advice\. The public presentation must make that distinction obvious\.

## 5\. Objectives

|ID    |Objective                                                                                                     |Business outcome                                                       |
|------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
|OBJ-01|Make every approved experimental URL technically crawlable and deliberately discoverable.                     |Removes access and discovery ambiguity.                                |
|OBJ-02|Determine the individual and combined effects of HTML structure, contextual depth, and internal-link strength.|Identifies the smallest effective page configuration.                  |
|OBJ-03|Measure the complete search-to-answer funnel separately for Google, Bing, and selected AI systems.            |Prevents “not found” from being treated as one undifferentiated result.|
|OBJ-04|Produce repeatable, auditable observations with timestamps and evidence.                                      |Allows results to be compared across time and model versions.          |
|OBJ-05|Improve site-level trust, accuracy, navigation, and research transparency.                                    |Reduces quality and policy risks that could obscure the experiment.    |
|OBJ-06|Preserve a maintainable static-site workflow with deterministic output and automated validation.              |Enables Claude Code to implement and rerun the experiment safely.      |

## 6\. Research questions and hypotheses

### 6\.1 Primary research questions

1. Does stronger internal linking reduce time to discovery, crawl, or indexing?
2. Does richer contextual content improve non\-brand query ranking after indexing?
3. Does richer semantic HTML and truthful structured data improve interpretation, eligibility, or citation after indexing?
4. Do combinations of factors perform differently from each factor in isolation?
5. Does a page need to be indexed by a search engine before a search\-enabled AI system reliably retrieves or cites it?
6. Do Google and Bing respond differently to the same controlled variants?

### 6\.2 Hypotheses

|ID  |Hypothesis                                                                                           |Disconfirming evidence                                                                |
|----|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
|H-01|High internal-link strength will shorten median time to discovery and first crawl.                   |Low-link pages are consistently discovered/crawled as quickly or faster.              |
|H-02|High contextual depth will improve impressions and rank for natural-language queries after indexing. |Context level shows no directional effect across both topic blocks.                   |
|H-03|High semantic HTML will improve machine interpretation but will not guarantee indexing.              |Markup alone consistently changes indexing while other factors remain controlled.     |
|H-04|Pages with both high context and high links will be retrieved or cited more often than low/low pages.|Retrieval/citation rates are equal or lower after controlling for indexing.           |
|H-05|Exact-domain detection will occur earlier than deep-page discovery.                                  |Deep pages are found before the domain or root page.                                  |
|H-06|Bing and Google will show materially different crawl, index, or ranking behavior.                    |Stage timings and outcomes remain materially equivalent across the observation window.|

The result may be inconclusive\. “No observed effect within 28 days” must not be restated as proof that the factor never matters\.

## 7\. Scope

### 7\.1 In scope

- Sixteen new experimental pages arranged as two topic blocks of eight variants\.
- One experiment hub, two topic hubs, and a public methodology page\.
- Site\-level truth and credibility corrections\.
- Inclusion of relevant existing long\-form pages in navigation when they meet quality requirements\.
- Deterministic page generation from a manifest\.
- Sitemap, canonical, robots, metadata, semantic markup, and internal\-link controls\.
- Google Search Console, Bing Webmaster Tools, IndexNow, search\-result, and AI\-answer observation procedures\.
- A structured evidence log and human\-readable results summary\.
- Automated validation, deployment verification, and change\-freeze rules\.

### 7\.2 Out of scope

- Paid search, paid backlinks, link exchanges, purchased reviews, or traffic manipulation\.
- Creating or impersonating real local businesses\.
- Clinical advice, diagnosis, treatment promises, or claims that massage cures an injury or condition\.
- Broad international expansion before this experiment completes\.
- Redesigning the full visual brand\.
- Treating model training\-data inclusion as measurable; the study concerns live retrieval and citation only\.
- Declaring an SEO factor causal from a single page or a single model response\.

## 8\. Definitions and outcome funnel

|Stage       |Operational definition                                                                       |Required evidence                                                              |
|------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|Accessible  |The production URL returns HTTP 200 and usable HTML to a normal unauthenticated request.     |Timestamped status check and rendered-page check.                              |
|Discoverable|The URL is present in the approved sitemap or reachable from an allowed internal entry point.|Sitemap record and link graph.                                                 |
|Submitted   |The URL was submitted through Search Console, Bing Webmaster Tools, or IndexNow.             |Submission timestamp, method, response/status.                                 |
|Crawled     |A search engine reports or logs a crawl/inspection event.                                    |Search-console inspection, Bing report, or verified crawler log.               |
|Indexed     |The engine explicitly reports indexed status or returns the exact URL for a controlled query.|Inspection evidence is preferred; `site:` is secondary evidence only.          |
|Ranked      |The exact experimental URL appears for a predefined non-brand query.                         |Query, engine, location, date, result position/range, evidence link or capture.|
|Retrieved   |A search-enabled model uses page-specific facts or names the page/site in its answer.        |Saved prompt and answer with model/version/settings.                           |
|Cited       |The model presents a clickable citation to the exact experimental URL.                       |Exact citation URL and saved answer evidence.                                  |

The clock for AI retrieval testing starts only after the relevant page is confirmed indexed\. Pre\-index model checks may be logged as exploratory but must not be combined with post\-index results\.

## 9\. Experimental design

### 9\.1 Design structure

The required design is a blocked full\-factorial experiment:

- Block T: Chinese Tui Na topic family\.
- Block V: Vietnamese\-style massage topic family\.
- Factor H: semantic HTML richness, low or high\.
- Factor C: contextual depth, low or high\.
- Factor L: internal\-link strength, low or high\.

Each topic block contains all eight H×C×L combinations\. Topic is treated as a blocking variable, not an experimental factor\. The primary comparison is the direction and size of each factor within each topic and then across both topics\.

### 9\.2 Factor definitions

|Factor              |Low level                                                                                                                                         |High level                                                                                                                                                                                                                                 |Held constant                                                                                                         |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
|H — semantic HTML   |Valid static HTML; unique title, meta description, H1, self-canonical, one main content region, ordinary headings and paragraphs; no page JSON-LD.|All low-level controls plus `article`, `header`, `nav`, `section`, `aside`, breadcrumbs, definition/list/table/FAQ structures when content warrants them; valid `WebPage` or `Article` plus `BreadcrumbList` JSON-LD matching visible text.|Same CSS design, hosting, URL depth, response status, viewport behavior, and core text for the assigned context level.|
|C — contextual depth|350–500 original words; answer-first summary, service definition, Falkland Islands relevance, selection cautions, and concise FAQ.                |900–1,300 original words; all low elements plus terminology variants, comparison with alternatives, local constraints, verification checklist, evidence/method notes, limitations, and expanded FAQ.                                       |Same scenario intent, truthful status, author identity, safety boundaries, and factor H/L assignment.                 |
|L — internal links  |Included in XML sitemap and linked once from its topic hub; no homepage or cross-content promotion.                                               |All low links plus descriptive links from experiment hub, FLK jurisdiction hub, one relevant service directory, one relevant editorial page, and one paired related page; reciprocal breadcrumb/topic navigation.                          |Self-canonical, no external backlinks arranged by the project, and no paid promotion.                                 |

“HTML richness” means meaningful semantic structure and machine\-readable metadata\. Decorative elements, hidden text, repeated keywords, excessive DOM nodes, and JavaScript complexity do not qualify\.

### 9\.3 Page matrix

Every page shall have a unique scenario, page title, meta description, H1, opening answer, examples, FAQ questions, and research token\. No paragraph may be copied unchanged between variants except the standardized research disclosure and safety notice\.

#### Chinese Tui Na block

|Page ID  |Topic |Unique service-discovery scenario                 |H   |C   |L   |Controlled query theme                                 |
|---------|------|--------------------------------------------------|----|----|----|-------------------------------------------------------|
|EXP-T-000|Tui Na|Old ankle stiffness; how to enquire safely        |Low |Low |Low |Chinese Tui Na for old ankle stiffness Falkland Islands|
|EXP-T-001|Tui Na|Desk-related wrist and forearm tension            |Low |Low |High|Tui Na wrist tension Stanley Falkland Islands          |
|EXP-T-010|Tui Na|Post-walking calf tightness; service comparison   |Low |High|Low |Chinese massage for calf tightness Falkland Islands    |
|EXP-T-011|Tui Na|Shoulder tension; practitioner verification guide |Low |High|High|find Tui Na shoulder massage Falkland Islands          |
|EXP-T-100|Tui Na|General Tui Na terminology and local availability |High|Low |Low |Tui Na massage Falkland Islands                        |
|EXP-T-101|Tui Na|Questions to ask before booking bodywork          |High|Low |High|Tui Na practitioner questions Falkland Islands         |
|EXP-T-110|Tui Na|Tui Na versus relaxation massage                  |High|High|Low |Tui Na vs massage Falkland Islands                     |
|EXP-T-111|Tui Na|Comprehensive local enquiry and alternatives guide|High|High|High|Chinese Tui Na enquiries Falkland Islands              |

#### Vietnamese\-style massage block

|Page ID  |Topic     |Unique service-discovery scenario                 |H   |C   |L   |Controlled query theme                              |
|---------|----------|--------------------------------------------------|----|----|----|----------------------------------------------------|
|EXP-V-000|Vietnamese|Back tension; understanding the style             |Low |Low |Low |Vietnamese massage back tension Falkland Islands    |
|EXP-V-001|Vietnamese|Neck and shoulder relaxation enquiries            |Low |Low |High|Vietnamese massage neck shoulder Stanley            |
|EXP-V-010|Vietnamese|Stress-relief massage style comparison            |Low |High|Low |Vietnamese style massage for stress Falkland Islands|
|EXP-V-011|Vietnamese|Finding culturally specific massage services      |Low |High|High|find Vietnamese massage Falkland Islands            |
|EXP-V-100|Vietnamese|Technique vocabulary and expectations             |High|Low |Low |Vietnamese massage techniques Falkland Islands      |
|EXP-V-101|Vietnamese|Booking and consent questions                     |High|Low |High|Vietnamese massage booking questions Falklands      |
|EXP-V-110|Vietnamese|Vietnamese style versus other massage styles      |High|High|Low |Vietnamese vs other massage Falkland Islands        |
|EXP-V-111|Vietnamese|Comprehensive local enquiry and alternatives guide|High|High|High|Vietnamese style massage Falkland Islands           |

The last three binary digits in the page ID represent H, C, and L in that order\. `1` means high and `0` means low\. This convention shall be enforced by tests and recorded in the manifest\.

### 9\.4 URL convention

URLs shall be stable, readable, and independent of implementation technology:

`/experiments/falkland-islands/{topic}/{scenario-slug}/index.html`

The public canonical shall omit `index.html` if GitHub Pages resolves both forms\. The generator shall use one canonical form consistently across navigation, sitemap, JSON\-LD, measurement records, and submission payloads\.

Page IDs and factor assignments shall appear in the public methodology panel but not be inserted unnaturally into titles or body copy\. Each page shall also show a unique visible research token such as `LCI-EXP-T-011`; the token is for exact retrieval tests and shall not resemble a business name\.

### 9\.5 Assignment and comparability

- Scenario\-to\-factor assignment is fixed by this document for version 1\.0\.
- Titles shall target comparable intent and shall not add superlatives such as “best,” “top,” or “recommended\.”
- Publication date, deployment time, submission time, and test cadence shall be as simultaneous as operationally possible\.
- All pages shall use the same visual template and production origin\.
- The high\-link variant shall not receive external promotional links arranged by the project\.
- Changes during the observation window are prohibited except critical factual, legal, security, accessibility, or broken\-page corrections\. Any content or link change resets that page’s observation clock and is logged\.
- Search personalization, tester login state, location, language, and safe\-search settings shall be recorded where observable\.

## 10\. Business and content requirements

### 10\.1 Site positioning

|ID    |Requirement                                                                                                                                                                  |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|BR-001|The homepage shall describe Local Capability Index as a transparent search and AI-retrieval research project, not as an established business directory unless it becomes one.|
|BR-002|All inventory metrics shown publicly shall be generated from the current manifest or removed. No static claim may contradict the deployable inventory.                       |
|BR-003|The site shall distinguish verified real-world information, editorial guidance, and synthetic research content visually and textually.                                       |
|BR-004|The site shall provide an accessible methodology page explaining page variants, factors, observation dates, limits, and how to interpret results.                            |
|BR-005|The site shall provide an editorial/contact route for corrections and removal requests.                                                                                      |
|BR-006|Existing low-quality or obsolete mass-generated pages shall be reviewed against the same truth and quality standard before remaining indexable.                              |

### 10\.2 Experimental page content

|ID    |Requirement                                                                                                                                                                                                                                          |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|CR-001|Every page shall lead with a direct, useful answer to the page’s service-discovery question.                                                                                                                                                         |
|CR-002|Every page shall state that it is part of a controlled SEO/AEO experiment and is not a listing for a real provider.                                                                                                                                  |
|CR-003|Every page shall state that the unique research token is synthetic and exists only for retrieval measurement.                                                                                                                                        |
|CR-004|No page shall invent a provider, street address, phone number, review, rating, credential, opening hour, price, appointment availability, or testimonial.                                                                                            |
|CR-005|No page shall diagnose a condition, prescribe treatment, promise pain relief or recovery, or imply that massage replaces qualified medical care.                                                                                                     |
|CR-006|Health-related language shall be framed as general information and service-selection guidance. Red-flag symptoms shall direct the reader to an appropriately qualified healthcare professional or emergency service without fabricated local details.|
|CR-007|The named massage style shall be defined carefully, including variation among practitioners and the limits of general descriptions.                                                                                                                  |
|CR-008|The page shall explain that local availability is unverified unless supported by a cited, dated source. Absence of evidence shall be written as “not verified,” not “unavailable.”                                                                   |
|CR-009|Sources shall be linked where factual claims require support. Citations shall be relevant, dated where useful, and not added solely to increase link count.                                                                                          |
|CR-010|Every page shall include author or responsible organization, first-published date, last-materially-reviewed date, research ID, and factor assignment.                                                                                                |
|CR-011|If generative AI assisted drafting, the methodology page shall disclose the role of AI and the human review performed.                                                                                                                               |
|CR-012|Low-context pages shall remain genuinely useful; “low” is a controlled minimum, not thin or nonsensical content.                                                                                                                                     |
|CR-013|High-context pages shall add information density, decision support, and local relevance rather than repetition.                                                                                                                                      |
|CR-014|FAQ answers shall be visible in the page and shall exactly support any FAQ-like structured representation. FAQ rich-result eligibility is not promised.                                                                                              |
|CR-015|Each page shall link to the public methodology and correction/contact pages; these mandatory utility links do not count toward Factor L.                                                                                                             |

### 10\.3 Existing content remediation

|ID    |Requirement                                                                                                                                                                                                                              |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|CR-020|Preserve the pre-change Git commit SHA and a machine-readable inventory as the historical baseline.                                                                                                                                      |
|CR-021|Sanitize FLK-002, FLK-003, and mapped synthetic profiles before using them as navigation sources. Remove or explicitly correct misleading real-world claims.                                                                             |
|CR-022|Existing synthetic business pages that cannot meet BR-003 and CR-004 shall be removed from the indexable sitemap and set to `noindex,follow`, or return 410 when retirement is permanent. The selected status and reason shall be logged.|
|CR-023|The two relevant `premium-blogs` pages may be linked and indexed only after factual, originality, safety, authorship, canonical, and disclosure review.                                                                                  |
|CR-024|A legacy URL shall not redirect to an unrelated experiment page merely to transfer signals. Redirects are permitted only for substantively equivalent content.                                                                           |

## 11\. Functional requirements

### 11\.1 Information architecture

|ID    |Requirement                                                                                                                                                                                                                                                                                                                                                          |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|FR-001|Create `/experiments/` as the experiment hub with purpose, topic links, methodology link, publication date, and current observation status.                                                                                                                                                                                                                          |
|FR-002|Create a Falkland Islands topic hub for Tui Na and one for Vietnamese-style massage.                                                                                                                                                                                                                                                                                 |
|FR-003|The hub shall link to all sixteen pages, but links counted for Factor L shall follow the controlled rules in Section 9.2. To prevent the hub from neutralizing L, low-link URLs shall be exposed in a collapsed research inventory loaded as ordinary HTML only on their topic hub; high-link URLs shall receive the additional prominent contextual links specified.|
|FR-004|Every page shall have breadcrumbs to Home → Experiments → Falkland Islands → Topic → Page. Breadcrumbs are navigation controls and do not count toward L.                                                                                                                                                                                                            |
|FR-005|The production 404 page shall return HTTP 404 and offer links to the homepage, experiment hub, and site search/navigation.                                                                                                                                                                                                                                           |
|FR-006|All indexable content shall be reachable without client-side JavaScript.                                                                                                                                                                                                                                                                                             |

### 11\.2 Manifest and generation

|ID    |Requirement                                                                                                                                                                                                                                                                                    |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|FR-010|Create a single authoritative experiment manifest in JSON or YAML and a generated CSV view.                                                                                                                                                                                                    |
|FR-011|Each manifest record shall contain page ID, topic, scenario, H/C/L levels, target query family, research token, slug, canonical URL, title, description, publication date, last-material-change date, expected word range, expected inbound-link sources, indexability, and observation status.|
|FR-012|Create a new safe generator dedicated to experiment pages. It shall not call or import legacy mass-page generators.                                                                                                                                                                            |
|FR-013|Generation shall be deterministic and idempotent: two runs from unchanged inputs shall produce byte-equivalent content except explicitly documented build metadata, which should be avoided.                                                                                                   |
|FR-014|`fix_links.py` shall read or safely incorporate the manifest, regenerate experiment navigation and sitemap entries, and preserve manually authored content.                                                                                                                                    |
|FR-015|The generator shall fail closed when a required field, unique token, unique canonical, or factor assignment is missing or duplicated.                                                                                                                                                          |
|FR-016|The generator shall calculate word count from visible primary content and validate it against the assigned context range. Disclosures, navigation, footer, and JSON-LD do not count.                                                                                                           |

### 11\.3 Evidence and observation records

|ID    |Requirement                                                                                                                                                                                                                                                                                                      |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|FR-020|Create an append-oriented observation dataset in CSV plus JSON, with one row/object per URL, engine/model, query, and observation time.                                                                                                                                                                          |
|FR-021|Required fields are page ID, canonical URL, factor levels, topic, event timestamp UTC, tester timezone, platform, engine/model name, model version if shown, browsing/search setting, query ID, exact query, stage result, result position or range, cited URL, response evidence reference, notes, and observer.|
|FR-022|Empty, not tested, not found, not indexed, and technically failed shall be distinct values.                                                                                                                                                                                                                      |
|FR-023|A “cited” result is valid only when the answer includes a clickable link resolving to the exact canonical URL or an equivalent normalized URL. A domain mention alone is not a citation.                                                                                                                         |
|FR-024|A “retrieved” result without citation requires page-specific evidence, such as the unique research token or distinctive factual content. Generic massage advice is not retrieval.                                                                                                                                |
|FR-025|Evidence filenames shall include page ID, platform, query ID, and UTC timestamp. Sensitive account details shall be redacted.                                                                                                                                                                                    |
|FR-026|Generate a human-readable status report from the dataset; do not manually maintain duplicate totals.                                                                                                                                                                                                             |

## 12\. Technical SEO requirements

|ID     |Requirement                                                                                                                                                                                                                                |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|SEO-001|Every indexable page shall return HTTP 200 at its canonical production URL and shall not use soft-404 language or empty templates.                                                                                                         |
|SEO-002|Every indexable page shall have one unique `<title>`, one visible H1, a useful unique meta description, `lang="en"`, UTF-8, viewport metadata, and a self-referencing absolute canonical.                                                  |
|SEO-003|Titles shall normally remain within 45–65 characters and descriptions within 120–165 characters, but clarity takes precedence over truncation targets. Automated tests shall warn rather than fail when a justified page exceeds the range.|
|SEO-004|Indexable pages shall use `index,follow` or omit the directive. Non-indexable pages shall be excluded from the sitemap.                                                                                                                    |
|SEO-005|`robots.txt` shall not block the experimental path and shall reference the absolute production sitemap.                                                                                                                                    |
|SEO-006|The XML sitemap shall include every and only approved canonical indexable page, use accurate `lastmod` values tied to material changes, and contain no redirects, 4xx/5xx URLs, alternate canonical forms, or `noindex` URLs.              |
|SEO-007|No experimental page shall canonicalize to another variant. Near-duplicate detection shall run before release.                                                                                                                             |
|SEO-008|Global structured data may describe the real site organization and website. Page-level high-H variants may use `WebPage` or `Article` and `BreadcrumbList` only when fields match visible content.                                         |
|SEO-009|Experimental pages shall not use `LocalBusiness`, `Product`, `Review`, `AggregateRating`, `MedicalBusiness`, or provider/person markup for synthetic entities.                                                                             |
|SEO-010|JSON-LD shall parse without errors, use absolute canonical URLs, and remain consistent with title, dates, author, breadcrumbs, and visible page content.                                                                                   |
|SEO-011|Open Graph and social-card metadata shall be complete and consistent across all variants so it is not an uncontrolled factor.                                                                                                              |
|SEO-012|Internal anchors shall be descriptive and natural. Sitewide exact-match keyword stuffing is prohibited.                                                                                                                                    |
|SEO-013|All first-party internal links shall resolve without redirect chains or fragment errors. External citation links shall use HTTPS when available and be checked before publication.                                                         |
|SEO-014|Pages shall render their meaningful primary content in the initial HTML response. JavaScript shall not be required for discovery, body text, navigation, canonical, or structured data.                                                    |
|SEO-015|The site shall provide a real favicon and consistent site name; default template assets and broken social images shall be removed.                                                                                                         |

## 13\. Indexing and submission requirements

|ID     |Requirement                                                                                                                                                                                                                           |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|IDX-001|Verify domain properties in Google Search Console and Bing Webmaster Tools before observation begins.                                                                                                                                 |
|IDX-002|Submit the canonical XML sitemap to both services and record the submission timestamp and reported status.                                                                                                                            |
|IDX-003|Inspect every experimental URL after deployment. Record live-test accessibility and current index status separately.                                                                                                                  |
|IDX-004|Implement an IndexNow submission utility that submits changed canonical URLs only after successful deployment.                                                                                                                        |
|IDX-005|IndexNow logs shall record URL, UTC timestamp, endpoint, payload hash, HTTP status, response excerpt, and retry outcome. HTTP 200 means received, not indexed.                                                                        |
|IDX-006|The IndexNow key and key-location URL shall comply with the protocol. No secret credential shall be committed. The public IndexNow key may be stored only as required by the protocol.                                                |
|IDX-007|Submission utilities shall retry only transient failures with bounded exponential backoff and shall not continuously resubmit unchanged URLs.                                                                                         |
|IDX-008|The GitHub repository README shall link to the live experiment hub and explain the public methodology. README links are site-discovery support, not a controlled L-factor link and shall be applied consistently to both topic blocks.|

## 14\. Measurement plan

### 14\.1 Observation schedule

Required checkpoints are publication day &#40;D0&#41;, D1, D3, D7, D14, and D28\. If a page first becomes indexed after D28, record the event and begin a separate 14\-day post\-index AI observation window; do not rewrite the original D28 outcome\.

At each checkpoint:

1. Confirm HTTP status, canonical, robots directive, and sitemap presence\.
2. Record Google URL Inspection status where available\.
3. Record Bing URL Inspection/index status where available\.
4. Run the predefined exact\-token, exact\-title, and natural\-language search queries\.
5. Run AI tests only for confirmed indexed pages, except clearly labelled exploratory checks\.
6. Store evidence and append observations without overwriting prior records\.

### 14\.2 Query set

Each page shall have stable query IDs in four classes:

|Query class|Purpose                                               |Example                                                       |
|-----------|------------------------------------------------------|--------------------------------------------------------------|
|Q-TOKEN    |Detect exact page retrieval with minimal ambiguity.   |`"LCI-EXP-T-011"`                                             |
|Q-TITLE    |Detect exact-title indexing and retrieval.            |Quoted page title.                                            |
|Q-NEAR     |Test close topical wording without the research token.|`Tui Na practitioner verification Falkland Islands`           |
|Q-NATURAL  |Test realistic conversational service discovery.      |`How could I look for Chinese Tui Na in the Falkland Islands?`|

Queries shall be defined before deployment and versioned\. New queries may be added but shall not replace original queries or be included retroactively in earlier denominators\.

### 14\.3 Search\-engine protocol

- Test Google and Bing separately\.
- Record desktop/mobile mode where applicable\.
- Record signed\-in/incognito state and approximate tester location\.
- For rank, record the exact experimental URL and position; if position cannot be reliably determined, use fixed ranges: 1–10, 11–20, 21–50, 51–100, not found\.
- `site:` and quoted\-title queries are diagnostic and shall not be described as normal ranking success\.
- Search snippets shall be saved when they demonstrate correct or incorrect page interpretation\.

### 14\.4 AI protocol

- Test the selected versions of ChatGPT, Gemini, and DeepSeek, plus any Bing/Copilot experience chosen by the business owner\.
- Use a new conversation for every trial\.
- Record whether live web search/browsing is enabled and whether the interface confirms it was used\.
- Run three independent trials per page/query/model/checkpoint when practical\.
- Do not tell the model the target URL in natural retrieval trials\.
- Run a separate exact\-token trial to distinguish index discovery from recommendation behavior\.
- Save the complete prompt, relevant answer, citations, model label, date, and settings\.
- Score each trial as 0 = absent, 1 = domain mentioned only, 2 = page\-specific retrieval without exact citation, 3 = exact canonical citation\. Incorrect attribution is separately flagged\.

### 14\.5 Primary metrics

|Metric                  |Definition                                                                  |
|------------------------|----------------------------------------------------------------------------|
|Time to first crawl     |Hours from deployment completion to first verified crawl evidence.          |
|Time to index           |Hours from deployment completion to first verified indexed state.           |
|Index rate D7/D14/D28   |Indexed pages divided by eligible published pages at each checkpoint.       |
|Natural-query visibility|Share of page/query/engine observations appearing in top 100.               |
|Median rank band        |Median fixed rank range among visible observations.                         |
|AI retrieval rate       |Trials scored 2 or 3 divided by eligible post-index trials.                 |
|AI citation rate        |Trials scored 3 divided by eligible post-index trials.                      |
|Citation accuracy       |Exact valid citations divided by all citations attributed to the experiment.|

With only two topic blocks, results are directional evidence rather than statistically robust population estimates\. Report raw counts and per\-page outcomes; avoid unsupported significance claims\.

## 15\. Non\-functional requirements

|ID     |Requirement                                                                                                                                                                                                                      |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|NFR-001|Builds shall be deterministic, idempotent, and runnable on the repository’s documented Python version.                                                                                                                           |
|NFR-002|No secret, account cookie, Search Console export containing personal data, or private token shall be committed.                                                                                                                  |
|NFR-003|Pages shall meet WCAG 2.2 AA fundamentals: keyboard access, visible focus, landmarks, heading order, sufficient contrast, text resizing, and meaningful link text.                                                               |
|NFR-004|Mobile layout shall have no horizontal scrolling at 320 CSS pixels except necessary data tables, which shall have an accessible scroll container.                                                                                |
|NFR-005|Performance budgets on a representative mobile run are LCP ≤2.5 s, CLS ≤0.1, INP ≤200 ms where measurable, total transferred page weight ≤500 KB excluding intentionally downloaded evidence, and no blocking third-party script.|
|NFR-006|The system shall not depend on analytics for page functionality. If analytics is added, it shall respect applicable privacy requirements and be documented as a potential experimental influence.                                |
|NFR-007|All dates stored in datasets shall use ISO 8601 UTC; public pages may additionally display a readable local date.                                                                                                                |
|NFR-008|Generated files shall use UTF-8 and stable ordering to keep diffs reviewable.                                                                                                                                                    |

## 16\. Repository and implementation requirements

The implementer shall add or adapt the following logical components\. Exact filenames may change only if the same responsibilities remain obvious and documented\.

```text
data/experiments/seo_aeo_flk_v1.yaml
data/experiments/seo_aeo_flk_v1.csv              # generated view
experiments/index.html
experiments/methodology/index.html
experiments/falkland-islands/tuina/index.html
experiments/falkland-islands/vietnamese-massage/index.html
experiments/falkland-islands/<topic>/<scenario>/index.html
scripts/generate_experiment_pages.py
scripts/submit_indexnow.py
observations/seo_aeo_flk_v1_observations.csv
observations/seo_aeo_flk_v1_observations.json
tests/test_experiment_manifest.py
tests/test_experiment_pages.py
tests/test_experiment_links.py
tests/test_experiment_structured_data.py
tests/test_experiment_sitemap.py
```

### 16\.1 Mandatory automated tests

|ID     |Test                                                                                                                                                             |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|TST-001|Exactly sixteen experiment page records exist: eight Tui Na and eight Vietnamese-style massage.                                                                  |
|TST-002|Each topic contains every binary H/C/L combination exactly once.                                                                                                 |
|TST-003|Page ID digits match manifest factor values.                                                                                                                     |
|TST-004|Canonicals, slugs, research tokens, titles, descriptions, and H1 values are unique.                                                                              |
|TST-005|Every page meets its assigned visible-word range.                                                                                                                |
|TST-006|High-H pages contain required semantic elements and valid allowed JSON-LD; low-H pages contain no page JSON-LD.                                                  |
|TST-007|No experiment JSON-LD contains prohibited synthetic business, review, rating, medical, or provider types/properties.                                             |
|TST-008|High-L pages receive every specified controlled inbound link; low-L pages receive only permitted baseline/navigation links.                                      |
|TST-009|All internal links resolve to an existing build output and no indexable page is orphaned.                                                                        |
|TST-010|Sitemap membership exactly matches approved indexable canonical URLs.                                                                                            |
|TST-011|No indexable sitemap URL has `noindex`, a non-self canonical, or a non-200 local build target.                                                                   |
|TST-012|Normalized text similarity and repeated-paragraph checks flag likely duplicate variants for human review.                                                        |
|TST-013|Standardized disclosure, research token, authorship, dates, methodology link, and safety language are visible on every page.                                     |
|TST-014|Prohibited claim patterns such as fabricated star ratings, phone numbers, credentials, and cure/treatment promises cause test failure or explicit review failure.|
|TST-015|Running generation twice produces no Git diff.                                                                                                                   |
|TST-016|The current existing unit-test suite remains green.                                                                                                              |

### 16\.2 Required pre\-release commands

The repository’s established maintenance and verification commands shall remain successful:

```bash
python3 fix_links.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
git diff --check
```

The implementer shall also inspect the homepage, sitemap, robots file, experiment hub, one low/low/low page, and one high/high/high page in the final diff and deployed output\. Legacy generators identified in repository documentation shall not be executed\.

## 17\. Release and change control

1. Record the baseline commit SHA, production sitemap, robots file, URL inventory, and screenshots before changes\.
2. Implement in a dedicated branch and produce a reviewable pull request\.
3. Run generation and all automated tests locally\.
4. Review public truthfulness and health\-safety language manually\.
5. Deploy all sixteen pages and hubs in one release window where practical\.
6. Verify production status, canonical, structured data, links, and sitemap\.
7. Submit the sitemap and changed URLs; store submission evidence\.
8. Record `deployment_complete_at` only after production verification; D0 begins at that timestamp\.
9. Freeze content and controlled links through D28\.
10. Log every emergency correction with before/after commit SHA, reason, affected pages, and clock\-reset decision\.

Rollback shall be used for systemic technical faults, accidental sensitive data, materially misleading content, broken canonicalization, or widespread 4xx/5xx responses\. A poor ranking result is not a rollback reason\.

## 18\. Acceptance criteria

### 18\.1 Release acceptance

The implementation is accepted for publication when all of the following are true:

- Sixteen distinct experiment pages, three required hubs, and the methodology page build successfully\.
- Every factor combination occurs once per topic and matches the manifest\.
- Every page returns or is expected to return HTTP 200 at one stable self\-canonical URL\.
- All pages are present in the sitemap, unblocked by robots, and free from `noindex`\.
- Low\-H and high\-H outputs differ only according to the defined structural controls; high\-H structured data validates and matches visible content\.
- Low\-C and high\-C outputs meet their content ranges and required information elements\.
- Low\-L and high\-L inbound link sets match the defined graph, with no accidental extra controlled links\.
- No page presents a fictional entity or health claim as real\.
- Homepage inventory and project claims match generated reality\.
- Existing relevant pages have been remediated, excluded, or retired according to a documented decision\.
- The complete automated test suite and `git diff --check` pass\.
- Representative mobile and desktop pages pass visual, navigation, accessibility, and performance review\.
- Production verification and submission records are created\.

### 18\.2 Experiment completion acceptance

The v1 experiment is complete when:

- D0, D1, D3, D7, D14, and D28 technical/search observations exist for all sixteen pages, or a documented platform\-access reason explains a missing observation\.
- AI trials are separated into pre\-index exploratory and post\-index eligible datasets\.
- Every claimed retrieval or citation has saved page\-specific evidence\.
- Results report raw page outcomes by H/C/L combination and by topic\.
- The report distinguishes accessibility, discovery, crawl, index, rank, retrieval, and citation\.
- Limitations and confounders are stated, including sample size, page uniqueness, model variability, tester location, and any clock\-resetting changes\.
- A conclusion identifies which configuration to keep, expand, revise, or reject without claiming more certainty than the evidence supports\.

### 18\.3 Business success thresholds

These are decision thresholds, not guarantees:

|Level         |Threshold by D28                                                                                                                                                |Decision meaning                                                                                     |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|Minimum viable|At least 12 of 16 pages indexed by either Google or Bing; all pages technically valid; at least one non-brand impression or visible result in each topic.       |The experiment infrastructure works; continue observation and improve content/linking.               |
|Useful        |At least 12 pages indexed, at least 6 pages visible for a natural or near query, and at least 2 exact page citations in eligible post-index AI trials.          |Compare factor directions and select a preferred template.                                           |
|Strong        |At least 14 pages indexed, high-C or high-L variants show a consistent directional advantage in both topics, and citations occur on at least two model families.|Expand cautiously to a new low-competition location or service topic using the winning configuration.|

Failure to meet a threshold is still a valid result if implementation and observation acceptance criteria are met\.

## 19\. Risks and controls

|Risk                                                                 |Impact                                    |Control                                                                                              |
|---------------------------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------------------------|
|Near-duplicate variants are consolidated.                            |Factor comparison becomes invalid.        |Unique scenarios and text; self-canonicals; similarity test; human review.                           |
|Synthetic content is mistaken for a real provider.                   |User harm, trust loss, search policy risk.|Prominent research disclosure; synthetic tokens only; no actionable fake data or ratings.            |
|Health language overstates benefits.                                 |Safety and credibility risk.              |Service-discovery framing, cautious language, review checklist, prohibited-claim tests.              |
|High-link pages receive more than controlled links through templates.|L factor is contaminated.                 |Manifest-driven link graph and exact inbound-link tests.                                             |
|Search engines ignore new pages for longer than 28 days.             |Insufficient observation window.          |Preserve D28 outcome; continue passive observation; never fabricate or over-submit.                  |
|Model interfaces or versions change.                                 |Results become non-comparable.            |Record model label, date, settings, prompt, and citations for each trial.                            |
|Homepage claims contradict the repository.                           |Sitewide trust signal is weakened.        |Generate current counts or remove claims.                                                            |
|Existing synthetic pages contaminate domain quality.                 |New page results are harder to interpret. |Remediate, noindex, or retire before D0 and document inventory decision.                             |
|Small sample creates false certainty.                                |Bad strategic conclusion.                 |Treat topic as block, report raw data, use directional language, repeat in a later independent block.|
|Submission response is misread as indexing.                          |False success reporting.                  |Separate submitted, crawled, and indexed fields and evidence.                                        |

## 20\. Implementation instructions for Claude Code

Claude Code shall treat this BRD as the authoritative scope and shall not convert it into a story backlog\. It may create a technical implementation plan, but every requirement ID must be mapped to code, data, a manual procedure, or an explicit non\-code control\.

Before editing:

1. Read `CLAUDE.md`, repository contribution instructions, current tests, `fix_links.py`, sitemap generation, homepage, FLK hubs, FLK\-002, FLK\-003, mapped profiles, and both `premium-blogs` pages\.
2. Produce a current inventory and record the baseline commit SHA\.
3. Identify all scripts marked legacy or unsafe and keep them outside the execution path\.
4. Create a requirement traceability table covering BR, CR, FR, SEO, IDX, NFR, and TST IDs\.

During implementation:

1. Build the manifest and validators before generating pages\.
2. Implement the controlled link graph explicitly; do not infer high/low status from page prose\.
3. Author unique useful content for every scenario and run both automated similarity checks and human review\.
4. Keep structured data truthful and limited to allowed types\.
5. Update `fix_links.py` cautiously so it cannot overwrite hand\-authored article content\.
6. Generate sitemap and public inventory from the same canonical source\.
7. Add observation schemas and example blank records, but do not pre\-populate outcomes\.
8. Run the complete verification suite and provide a release report containing command outputs, file inventory, known limitations, and manual actions still required in Google/Bing interfaces\.

Claude Code shall stop and request a business decision if it discovers a real provider the project wants to name, because verification and consent requirements would materially change scope\. It shall also stop if an existing generator would overwrite unrelated user\-authored content\.

## 21\. Traceability summary

|Requirement group|Primary implementation evidence           |Primary acceptance evidence                   |
|-----------------|------------------------------------------|----------------------------------------------|
|BR               |Homepage, methodology, inventory source   |Truth/content review                          |
|CR               |Page source content and remediation log   |Manual review plus prohibited-pattern tests   |
|FR               |Hubs, manifest, generator, datasets       |Unit/integration tests and generated artifacts|
|SEO              |HTML head/body, sitemap, robots, JSON-LD  |Local validators and production inspection    |
|IDX              |Submission utility and operating procedure|Timestamped platform/submission records       |
|NFR              |Build configuration, CSS, templates       |Rebuild diff, accessibility/performance review|
|TST              |Test modules and CI output                |Passing release report                        |

## 22\. Reference guidance

Implementation and content review shall follow current primary\-source guidance, including:

- [Google Search Central: creating helpful, reliable, people\-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google Search Central: crawling and indexing documentation](https://developers.google.com/search/docs/crawling-indexing)
- [Google Search Central: structured\-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [IndexNow protocol documentation](https://www.indexnow.org/documentation.html)
- [Bing Webmaster Tools introduction and current tool guidance](https://blogs.bing.com/webmaster/June-2025/Start-Using-Bing-Webmaster-Tools-to-Improve-Your-Site-Visibility)

Search\-engine documentation may change\. The implementer shall re\-check current primary documentation before deployment if implementation occurs materially after this document date\.

---

## Approval record

|Role                   |Name|Decision|Date|
|-----------------------|----|--------|----|
|Business owner         |    |        |    |
|Technical implementer  |    |        |    |
|Content/safety reviewer|    |        |    |