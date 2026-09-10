# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose and current scope

The project tests a discovery data layer connecting **customer problem → solution/capability → business offering it**. The goal is to make specific capabilities discoverable through problem-based searches and LLM answers, beyond vague business categories.

As of September 10, 2026, the project includes:
- **Synthetic business directory**: Hong Kong (HKG) and Falkland Islands (FLK) with 6 problem pages and 13 business profiles (19 pages total).
- **SEO/AEO experiment** (deployed): Controlled 2×2×2 factorial test with 16 experimental pages in Falkland Islands testing page characteristics (HTML richness, contextual depth, internal links) against search visibility outcomes.
- **Total indexable URLs**: 48 (20 experiment + 28 existing directory/hubs)

All services and businesses are synthetic test data, as confirmed by the user. Do not invent further qualifications, reviews, treatment outcomes, or provider capabilities. Derive relationships from existing explicit links.

## Deployment Status (September 10, 2026)

**LIVE AND BRD-COMPLIANT:**
- Homepage updated with accurate inventory (48 pages, 2 active jurisdictions)
- 20 experiment infrastructure pages deployed and verified (all HTTP 200)
- Prominent experiment link on homepage for discoverability
- 48 URLs in XML sitemap (20 experiment + 28 existing)
- All pages include research disclosure and synthetic status
- No misleading health claims or false provider information
- Ready for Google/Bing crawling and indexing

**Commits:**
- 057a94f: Core experiment infrastructure
- 6950898: Sitemap integration
- a28510f: BRD compliance (homepage fixes, URL consistency)
- 2af341f: Topic hub path fix

**Next steps:** Submit sitemap to Google Search Console and Bing Webmaster Tools, then begin D0-D28 observation schedule.

The experiment is a research publication, not a provider directory or medical advice. Pages include disclosure of synthetic status, research tokens, and factor assignments. Real interviews with Hong Kong and Singapore businesses are a later phase managed by the user.

## Critical constraints

- **Homepage is now BRD-compliant** (September 10, 2026): Shows accurate inventory (48 pages, 2 active jurisdictions), includes prominent experiment link, no false claims. Future edits must preserve this accuracy and experiment discovery.
- Do not run legacy generators: `build.py`, `build_enhanced.py`, `build_ultra_rich.py`, `build_final.py`, or other historical content generators. They can overwrite current content and introduce broken links.
- Never manually edit `directory-by-*.html` or `sitemap.xml`; use `fix_links.py`.
- Experiment pages (`/experiments/`) are research infrastructure and must not be overwritten by legacy generators. Frozen during D0–D28 observation window.
- After every problem, business, or discovery change, run `python3 fix_links.py`. Run it again before committing.
- After changes to discovery or experiment code, run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests`.
- Check `git diff --check`, preserve unrelated user edits, and inspect the resulting diff before deployment.
- Deploy only when authorized by the user. A request to deploy authorizes the commit and push needed for that deployment.
- Experiment content is frozen during observation windows (D0–D28). Emergency corrections are logged with commit SHA and clock-reset decision.

The repository has a history of broken links caused by generated directories disagreeing with actual content. File existence alone is not sufficient: validate the links rendered in HTML and reachability from the homepage.

## Current inventory and discovery behavior

### Existing directory structure (as of September 7, 2026)

- Active content jurisdictions: Hong Kong (HKG) and Falkland Islands (FLK).
- 6 problem pages and 13 business profiles: 19 content pages total.
- All 19 content pages are reachable within two HTML links of the unchanged homepage.
- Four generated directories: country, problem, business, and service.
- Active country pages list all local problem pages and business profiles.
- Content pages have canonical URLs and discovery navigation. Business backlinks are derived from problem pages that explicitly link to those businesses.
- Directory labels use actual HTML titles, not identifiers such as `Flk 003`.
- The service directory links each problem to its existing associated business profiles. It does not establish additional provider capabilities.
- Empty SGP, SHN, SJM, and PCN country routes have simple `noindex, follow` pages because the existing homepage links there. They contain no invented profiles and are excluded from the sitemap.
- The sitemap includes the homepage, about/contact pages, all four directories, both active country pages, and all 19 content pages (28 URLs).
- `lastmod` is omitted until true content modification dates are tracked. Never assign every URL the sitemap generation date.

### SEO/AEO experiment infrastructure (as of September 10, 2026)

The experiment is a controlled 2×2×2 factorial research study with:
- **16 experimental pages** in `/experiments/falkland-islands/{topic}/{scenario}/` testing three factors:
  - **H (HTML richness)**: Low (basic valid HTML, no page JSON-LD) vs. High (semantic tags, breadcrumbs, WebPage/Article JSON-LD)
  - **C (contextual depth)**: Low (350-500 words) vs. High (900-1300 words)
  - **L (internal links)**: Low (sitemap + topic hub only) vs. High (experiment hub, jurisdiction hub, service directory, editorial links)
- **Manifest-driven generation**: `data/experiments/seo_aeo_flk_v1.yaml` defines all 16 pages with unique scenarios, titles, descriptions, and factor assignments.
- **3 support hubs**: `/experiments/` (main hub), `/experiments/falkland-islands/tuina/` (Tui Na topic hub), `/experiments/falkland-islands/vietnamese-massage/` (Vietnamese topic hub)
- **1 methodology page**: `/experiments/methodology/` explaining the 2×2×2 design, measurement protocol, observation schedule, and success thresholds.
- **Unique research tokens**: Each page (e.g., `LCI-EXP-T-000`) for exact retrieval testing.
- **Disclosure**: Every page discloses synthetic research status, factor assignment, publication date, and links to methodology.
- **Safety & truthfulness**: No fake providers, credentials, phone numbers, cure claims, or health diagnoses. Service-discovery framing only.

**Key files**:
- `data/experiments/seo_aeo_flk_v1.yaml` — Manifest (authoritative source)
- `data/experiments/seo_aeo_flk_v1.csv` — Generated CSV view (read-only, generated by `scripts/generate_manifest_csv.py`)
- `scripts/generate_experiment_pages.py` — Generates all 16 HTML pages from manifest
- `scripts/generate_manifest_csv.py` — Generates CSV from manifest
- `tests/test_experiment_manifest.py` — Validates manifest structure (TST-001 through TST-004, TST-015)
- `observations/seo_aeo_flk_v1_observations.csv` — Append-only observation log (D0, D1, D3, D7, D14, D28 checkpoints)
- `observations/seo_aeo_flk_v1_observations.json` — Structured equivalent

**Observation windows**:
- **D0 (publication day)**: HTTP 200, canonical, sitemap presence verified
- **D1, D3, D7, D14, D28**: Search engine crawl/index status, rank checks, AI retrieval trials
- AI trials begin only after index confirmation; pre-index trials are exploratory only.

**Development workflow for experiments**:
1. Edit manifest (`data/experiments/seo_aeo_flk_v1.yaml`) if factor assignments or metadata change.
2. Run `python3 scripts/generate_experiment_pages.py` to regenerate all 16 pages.
3. Run `python3 scripts/generate_manifest_csv.py` to update CSV view.
4. Run `python3 -m unittest tests.test_experiment_manifest -v` to validate.
5. Run full test suite: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests`.
6. Run `python3 fix_links.py` to regenerate directories and sitemap (includes experiment pages).
7. Verify no broken links and inspect `git diff` before committing.

## Content locations and intent

- `flk/en/problems/99-flk-001.html`: military/martial arts shoulder recovery; links to RAF Recovery.
- `flk/en/problems/99-flk-002.html`: longstanding pain from old injuries and Chinese Tui Na enquiries; links to the existing Sports Injury Clinic profile.
- `flk/en/problems/99-flk-003.html`: Vietnamese massage; links to Welcome Wellness.
- `flk/en/problems/99-flk-004.html`: Kung Fu Tik Da massage; links to RAF Recovery.
- `hkg/en/problems/99-hkg-001.html`: ankle stiffness from an old injury.
- `hkg/en/problems/99-hkg-002.html`: lower back pain from desk work.

`FLK 0002` / `flk_0002` means `99-flk-002.html`. Its audience is people with lingering pain from old everyday or sports injuries, especially “I twisted my ankle years ago and it still hurts.” Include Chinese Tui Na, Tuina, and Tui na terminology naturally. Do not restrict this audience to ex-military personnel, martial artists, or competitive athletes. Keep the existing URL and explicit business link. The enquiry wording does not confirm the listed provider offers Tui Na.

Vietnamese massage is **FLK 003**, not FLK 002. Preserve that mapping in directories and tests.

## Generator and validation

### fix_links.py (existing directory/sitemap generator)

`fix_links.py`:
1. Discovers existing content and reads HTML titles.
2. Refreshes active country listings, canonical URLs, and generated discovery navigation.
3. Derives business-to-problem backlinks from existing problem-to-business anchors.
4. Regenerates all four directories (country, business, problem, service) and the sitemap.
5. **Includes experiment pages** in sitemap and directories where appropriate (L-factor determines link prominence).
6. Follows local HTML anchors starting at the homepage; fails on missing destinations or unreachable content.

Generated navigation is delimited by `<!-- discovery:start -->` and `<!-- discovery:end -->`. Edit the generator rather than these blocks. Repeated generation should not change the output.

### Experiment page generation

**scripts/generate_experiment_pages.py** (deterministic, idempotent):
- Reads manifest from `data/experiments/seo_aeo_flk_v1.yaml`
- For each page: generates unique scenario-specific content (title, description, H1, body, FAQ)
- Enforces word-count ranges: Low-C (350-500 words), High-C (900-1300 words)
- Low-H pages: basic valid HTML, no page JSON-LD
- High-H pages: semantic article/header/nav/section tags, breadcrumbs, WebPage/Article + BreadcrumbList JSON-LD, FAQ-schema markup
- Output: `/experiments/falkland-islands/{topic}/{scenario}/index.html`
- Byte-stable output (running twice produces identical files)

### Validation workflow

Before publishing:
```bash
python3 scripts/generate_experiment_pages.py
python3 scripts/generate_manifest_csv.py
python3 -m unittest tests.test_experiment_manifest -v
python3 fix_links.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
git diff --check
git diff -- index.html
```

Tests cover:
- **Manifest validation** (test_experiment_manifest.py): 16 pages, all 8 H×C×L combinations per topic, unique IDs/tokens/titles/descriptions, factor-digit matching
- **Reachability**: Missing destinations, orphaned content, link chains from homepage
- **Sitemap coverage**: All indexable pages included, no 4xx/5xx URLs, no noindex pages
- **Service/country mappings**: Business backlinks, problem-to-business associations
- **Experiment structure**: High-H pages have JSON-LD, low-H pages don't; word counts match factor levels

Local validation does not check external websites, prove provider claims, or demonstrate search-engine indexing.

## Deployment

Confirmed through the GitHub Pages API on September 7, 2026:
- Repository: `benougroup/localcapabilityindex`.
- Live site: `https://localcapabilityindex.com/`.
- Hosting: **GitHub Pages**, publishing from branch `main`, repository root `/`.
- HTTPS is enforced and the custom domain is configured.

After the user authorizes deployment, validate, commit the intended files, and push `main` to `origin`. Check the GitHub Pages build status for the pushed commit, then fetch the live directories, sitemap, and representative problem/business pages to confirm the new content is served.

Historical documents describe Netlify deployment and credit costs. Those descriptions do not match the verified current GitHub Pages configuration. Do not assume `netlify.toml` or `_redirects` controls the live site.

## Search submission and experiment tracking

After deployment, submit `https://localcapabilityindex.com/sitemap.xml` in Bing Webmaster Tools and Google Search Console. A sitemap advertises all included URLs; manual submission of every page is not required. Inspect priority URLs, especially FLK 003, to see actual crawl/index status and request indexing where appropriate.

The existing `robots.txt` permits crawling and advertises the sitemap. IndexNow can notify participating engines of added, changed, or removed URLs after publication; an existing key file alone does not establish that any submission succeeded.

Track these stages separately: access, indexing, query retrieval, correct problem/solution/provider extraction, and citation. Save exact prompts, date, model, search-enabled status, returned URLs, and citations. Direct URL reading does not prove organic search discovery. Submission and successful crawling do not guarantee indexing, rankings, or LLM citations.

Historical reports claiming guaranteed indexing within hours, that longer text automatically improves authority, or that realistic-sounding dummy businesses increase trust are not reliable guidance. Older inventory and validation counts are historical; use the current generator and tests.
