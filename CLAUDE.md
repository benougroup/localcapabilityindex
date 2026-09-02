# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Local Capability Index is a static site generator for Answer Engine Optimization (AEO) research. It tests how LLMs discover and rank content based on:
- **Content richness** (sparse vs 1,000+ word pages)
- **Structured data signals** (JSON-LD schema vs semantic content)
- **Design complexity** (minimal HTML vs responsive vs premium CSS)
- **Geographic authenticity** (realistic addresses, phone prefixes, district names)
- **Internal linking architecture** (8-10 links per page creating knowledge graphs)
- **Entity density** (companies, locations, market data, regulatory context)

**Current State (Sept 2026):**
- 6 jurisdictions (HKG, SGP, FLK, SHN, SJM, PCN)
- Ultra-rich problem pages (1,000+ words each with market data, regulatory context, company integration)
- 2 custom Falkland Islands massage problems for testing
- 3 build scripts (original, enhanced, ultra-rich)
- Complete internal linking and directory navigation
- IndexNow API integration for instant Bing indexing

## Build & Deploy

### Generate Content

**Ultra-rich content (recommended for LLM testing):**
```bash
python build_ultra_rich.py
```
Generates 1,000+ word problem pages with semantic structure, market data, and company integration. Use this for testing content richness impact on LLM discoverability.

**Enhanced content (with company database integration):**
```bash
python build_enhanced.py
```
Generates content with 22 companies (test keywords: sausage, welcome, spam, ham, fighter, p0wer, restful, timeness, windy, koala) randomly assigned to problem pages.

**Original AEO framework (pure research):**
```bash
python build.py
```
Generates original 4-node architecture (99/77/88/66 prefixes) with A/B testing: Sausage (structured data) vs Welcome (semantic content) profiles × 3 design variants (minimal/responsive/premium).

### Deployment

All build scripts output static HTML/XML/CSS (no build step required):
- Netlify: Connect GitHub repo, set publish root to `.`
- IndexNow: All scripts automatically submit URLs to Bing IndexNow API (HTTP 200 = success)
- Sitemap: Auto-generated with current timestamps on each build

## Architecture: Content-First SEO Testing

### Why Three Build Scripts

The project evolved to test different content approaches for LLM indexing:

| Script | Focus | Output | Use Case |
|--------|-------|--------|----------|
| `build.py` | A/B testing framework | 4-node architecture, design variants | Pure AEO research (original research question) |
| `build_enhanced.py` | Company database + internal linking | 100+ links per page, 22 companies | Testing if entity density + linking improves discovery |
| `build_ultra_rich.py` | Content richness for LLMs | 1,000+ words per page, market data | Testing if content depth/authority signals matter |

**Key insight:** The original `build.py` is for structured A/B testing (isolating design/schema signals). The newer scripts test whether content richness and entity density improve LLM discoverability. Keep both approaches—they test different hypotheses.

### Content Structure: 4-Node Architecture (Original)

Generated pages follow 4-node pattern across all countries:

**Node Type 99 (Problem Pages):** Natural language consumer queries (baseline retrieval)
- URL: `/{country}/en/problems/99-{slug}.html`
- Content: Consumer symptom as search query
- Test: Can LLM find site for natural problem statement?

**Node Type 77 (Solution Pages):** Keyword-dense semantic content
- URL: `/{country}/en/solutions/77-{slug}-solution.html`
- Content: Multiple h2 headers, narrative structure
- Test: Does semantic chunking improve extraction?

**Node Type 88 (Business Pages):** A/B content + design variants
- URL: `/{country}/en/businesses/88-{slug}-{variant}.html`
- Profiles: Sausage (full schema) vs Welcome (minimal schema) × 3 designs
- Test: Does structured data outrank semantic content? Does design matter?

**Node Type 66 (Blog Pages):** Extended narratives (non-tropical regions only)
- URL: `/{country}/en/blogs/66-{slug}-business-insights.html`
- Content: 1000+ word narratives with FAQ
- Test: Does comprehensive content improve generative retrieval?

### Ultra-Rich Content Structure (New)

`build_ultra_rich.py` produces dramatically different content for testing richness:

Each problem page includes:
- **1,000+ words** (vs 50 in sparse, vs 300-500 in build_enhanced)
- **7-8 semantic sections** with clear h2 hierarchy
- **4 companies** with full service descriptions, expertise, phone numbers
- **7+ market data points** (pricing, market size, revenue opportunity)
- **Geographic specificity** (districts, density, locations, authentic context)
- **Regulatory context** (named agencies, compliance requirements, penalties)
- **Competitor analysis** (3+ existing solutions examined)
- **Stakeholder analysis** (3+ groups identified with incentives)
- **Authority signals** (specific numbers, named sources, detailed analysis)

Example: Coffee grounds problem page (HKG) includes:
- 1,500+ cafes addressable market
- 500+ tons annual waste volume
- HKG$0.50-2.00/kg pricing
- HKG$10,000 regulatory fine
- 4 companies with phones
- EPR framework context
- 3 competitor solutions analyzed

**Why this matters:** This tests whether LLMs weight content depth, entity density, and authority signals when determining page importance. Compare ultra-rich pages vs sparse competitors to measure impact.

### Custom Falkland Islands Content

You have custom massage problem pages for testing:

**FLK_0001: Vietnamese Massage for Stress Relief** (`99-vietnamese-massage-stress-relief.html`)
- 1,000+ words with Stanley/RAF Mount Pleasant context
- Market analysis (2,000 military, 400-600 civilians)
- 4 wellness providers with contact info
- Stress management for remote island living

**FLK_0002: Kung Fu/Tik Da Martial Arts Massage** (`99-kung-fu-tik-da-massage-relaxation.html`)
- 1,000+ words with recovery science and military focus
- RAF Mount Pleasant (2,000 personnel, martial arts recovery market)
- Market economics (FKP£24,000+ annual revenue potential)
- 4 specialized recovery providers

These are part of the ultra-rich testing framework—use them to test whether detailed market analysis + geographic specificity improves LLM discovery of niche services.

## Directory Navigation for LLM Crawling

Four directory pages (auto-generated) provide alternative navigation paths:

- `directory-by-country.html` - Jurisdiction-first organization (test geographic clustering)
- `directory-by-service.html` - Capability-first organization (test semantic extraction)
- `directory-by-business.html` - A/B profile comparison (test schema vs content weighting)
- `directory-by-problem.html` - Natural language query index (test query matching)

**Why:** Tests which navigation architecture LLMs prefer and whether multiple entry points improve discovery.

## Modifying Content

### Add a Problem

Edit `queries` list in relevant build script:

```python
{
    "id": "FLK_0001",
    "country": "flk",
    "country_name": "Falkland Islands",
    "slug": "problem-url-slug",
    "title": "Human-Readable Problem Title",
    "short_desc": "One-liner consumer query",
    "rich_content": """<h2>Rich Content Section</h2>
    <p>Detailed analysis, market data, regulatory context...</p>"""
}
```

For `build_ultra_rich.py`: Use `rich_content` field (full HTML allowed)
For `build_enhanced.py`: Use `expanded` field (paragraph text)
For `build.py`: Use `desc` + `sol` fields (minimal)

### Add a Company

Edit `COMPANIES` dict in relevant build script:

```python
"company-key": {
    "name": "Company Name Ltd",
    "keywords": ["keyword1", "keyword2"],
    "countries": ["flk", "shn"],
    "addresses": {"flk": "Stanley Street", "shn": "Jamestown St"},
    "phones": {"flk": "+500 XXXXX", "shn": "+290 XXXX"},
    "description": "Service focus and expertise"
}
```

Companies are randomly assigned 3-4 per problem page per country. Run build script again for different combinations.

### Add a Jurisdiction

In `build.py` or `build_enhanced.py`, find geographic routing section:

```python
elif country_iso == "new_code":
    phone_prefix, district, address, currency = "+XXX", "City", "Street", "CUR"
```

Then add queries with `"country": "new_code"` and run build.

## Common Commands

```bash
# Generate ultra-rich content (1000+ words per page)
python build_ultra_rich.py

# Generate enhanced content (company database + internal linking)
python build_enhanced.py

# Generate original AEO framework (4-node, design A/B test)
python build.py

# Check generated pages
ls -lh hkg/en/problems/99-*.html

# Verify internal links
grep -c "href=" hkg/en/problems/99-*.html | head -1

# Count unique companies mentioned
grep -rh "<strong>" hkg/en/problems/*.html | sort | uniq | wc -l

# Check sitemap
grep -c "<url>" sitemap.xml

# Validate IndexNow submission
cat build_ultra_rich.py | grep -A 5 "IndexNow"
```

## Key Files

| File | Purpose |
|------|---------|
| `build.py` | Original AEO framework (unchanged core logic) |
| `build_enhanced.py` | Enhanced with 22-company database |
| `build_ultra_rich.py` | Content richness testing (1,000+ word pages) |
| `index.html` | Homepage with navigation and branding |
| `README_CONTENT_RICHNESS.md` | Ultra-rich strategy summary |
| `ULTRA_RICH_CONTENT_STRATEGY.md` | Complete testing methodology |
| `COMPANIES_REFERENCE.md` | All 22 companies with profiles |
| `CLAUDE.md` | This file |

## Testing with LLMs

### Query Examples

**Test 1 - Problem Discovery:**
```
"I run a cafe in Hong Kong with daily coffee waste. How do I recycle it?"
```
Expected: Ultra-rich page discovered, market data cited, companies recommended

**Test 2 - Geographic Specificity:**
```
"What companies in Stanley, Falkland Islands offer massage therapy?"
```
Expected: Falkland Islands pages found, geographic accuracy verified

**Test 3 - Market Analysis:**
```
"What's the market for Vietnamese massage services in remote islands?"
```
Expected: Market size, revenue potential, stakeholder analysis cited

### Measurement

- **Discovery Rate:** How often pages found vs sparse competitors
- **Citation Frequency:** How often specific data/companies mentioned
- **Ranking Position:** Where pages appear in result lists
- **Response Depth:** How comprehensive LLM answers are
- **Authority Signals:** Whether specific numbers/sources cited

**Hypothesis:** Ultra-rich pages (1,000+ words with market data, entity density, authority signals) 5-10x more discoverable than sparse competitors.

## Deployment Checklist

Before pushing to production:
- [ ] All build scripts run without errors
- [ ] Sitemap generated with current timestamps
- [ ] IndexNow submission confirmed (HTTP 200)
- [ ] Internal links verified (no 404 errors)
- [ ] Homepage navigation working
- [ ] Directory pages populated
- [ ] Country index pages linked
- [ ] Git commit message references what changed

```bash
git add -A
git commit -m "Description of changes (e.g., added ultra-rich FLK massage problems)"
git push origin main
```

Once pushed, site is ready for:
1. Netlify deployment (automatic on push if connected)
2. LLM testing (query with scenarios above)
3. Bing/Google indexing (sitemap auto-discovered)

## Next Steps for Expansion

**Short-term (Add Breadth):**
- Add 5-10 more ultra-rich problems per jurisdiction
- Expand FLK massage content (add solution pages, cross-links)
- Test with multiple LLMs (ChatGPT, Claude, Gemini, Perplexity)

**Medium-term (Add Depth):**
- Add FAQ sections to ultra-rich pages
- Add case studies and testimonials
- Create market analysis aggregator pages
- Build company comparison pages

**Long-term (Build Authority):**
- Track which content signals matter most in LLM rankings
- Optimize based on discovery patterns
- Become reference point for hyperlocal market data
- Test multi-language content (Chinese, Spanish variants)

## Build & Deploy

### Generate the Site

**Main build script (full feature set):**
```bash
python build.py
```

**Enhanced build script (with company database & internal linking):**
```bash
python build_enhanced.py
```

The enhanced script includes:
- 22 dummy companies (searchable by keywords: sausage, welcome, spam, ham, fighter, p0wer, restful, timeness, windy, koala)
- Expanded problem descriptions (8-10x richer content)
- Multiple company recommendations per problem page
- Rich internal linking (8-10 links per page, no dead ends)
- Geographic authenticity (realistic addresses, country-specific phone formats)
- Automatic company distribution to problem pages

### Full Build Process

Both scripts regenerate all content:
- Cleans and recreates directories for all 6 countries (hkg, sgp, flk, shn, sjm, pcn)
- Generates problem/solution/business/blog HTML pages
- Generates country index pages (`/{country}/index.html`) organizing content by node type
- Updates `sitemap.xml` with current timestamps
- Generates IndexNow verification file
- Submits all URLs to Bing IndexNow API for instant indexation
- Auto-generates `netlify.toml` with CORS headers
- Output is ready for immediate Netlify deployment (all static HTML/XML/CSS, no build step required)

**Key characteristics:**
- No external dependencies (Python stdlib only: os, json, shutil, datetime, random, urllib)
- Deterministic output based on `queries` list—same input always produces identical output
- All pages generated with proper SEO (meta descriptions, canonical URLs, structured data)
- `build_enhanced.py` includes integrated company database for improved LLM discoverability

### Deployment

Configured for Netlify:
- Publish root: `.` (current directory)
- All HTML/XML/CSS served as-is
- CORS headers auto-generated by build.py
- No build command needed

## Architecture: 4-Node System + Country Navigation + Internal Linking

All content follows a pattern: **Homepage → Country Index → 99 (Problem) → 77 (Solution) → 88 (Business) → 66 (Blog)**

### Content Enhancement Strategy (build_enhanced.py)

The enhanced build script dramatically improves LLM discoverability through:

**Content Richness:**
- Problem descriptions expanded from 50 words to 400+ words
- 2-3 paragraph detailed analysis per problem
- Geographic context explaining region-specific challenges
- Semantic richness enabling multi-dimensional search

**Entity Density:**
- 22 dummy companies with test keywords (sausage, welcome, spam, ham, fighter, p0wer, restful, timeness, windy, koala)
- 3-4 companies recommended per problem page
- Realistic contact information (authentic phone formats, district names)
- Multi-jurisdiction or localized coverage

**Internal Linking Architecture:**
- 8-10 links per problem page (no dead ends)
- Breadcrumb navigation (Home → Country → Problem Pages)
- Cross-links to all 4 directory pages (country, service, business, problem)
- Problem-to-solution connections
- Company recommendations as inline links
- 100+ total internal links creating dense knowledge graph

**Result:** Pages feel authoritative, discoverable, and interconnected. LLMs index pages with:
- More content as more valuable
- Real-sounding entities (companies with contact info) as more trustworthy
- Internal links as better understood (crawlable knowledge graph)
- Multiple entry points as more discoverable

### Discovery Architecture

**Homepage Navigation:**
- `index.html` has "Browse Content by Region" section
- 6 clickable country cards linking to country index pages
- Footer contains links to all country pages
- Enables LLMs to navigate from root to all content

**Country Index Pages (NEW):**
- Generated automatically for each country: `/{country}/index.html`
- Lists all content organized by node type:
  - Problem Nodes (99) - all consumer queries for that country
  - Solution Nodes (77) - keyword-dense semantic content
  - Business Nodes (88) - all 3 design variants per business
  - Blog Nodes (66) - extended narratives (non-tropical regions only)
- Each entry is a clickable link to the content page
- Proper meta descriptions and canonical URLs for SEO
- Added to sitemap for search engine discovery

**Result:** Complete crawl path for LLMs: `/` → `/{country}/` → `/{country}/en/{node_type}/` → individual pages → directory pages as alternative navigation paths

### Comprehensive Directory Pages (NEW - Aug 2026)

Four directory navigation approaches auto-generated in `build.py` for A/B testing LLM crawl behavior:

**Generated Files:**
- `directory-by-country.html` - 350+ links organized by 6 jurisdictions
- `directory-by-service.html` - 326+ links organized by 25+ service capabilities  
- `directory-by-business.html` - 198+ links comparing A/B content profiles (Sausage vs Welcome)
- `directory-by-problem.html` - 70+ links to all 64+ consumer problem queries

**Purpose:** Test which navigation/information architecture LLMs prefer:
- Does country-first organization improve indexation?
- Do service categories help semantic extraction?
- How do A/B profile comparisons affect ranking?
- Does problem-centric indexing enhance retrieval?

**Link Coverage:** 944 total href links across all directories, all pointing to existing 344 content pages + 6 country indexes. Every page discoverable from multiple entry points.

**Homepage Integration:**
- "Comprehensive Content Directory" section with 4 directory cards
- Each card links to corresponding directory page
- Directory pages cross-link each other in footer
- 8Fate partnership link added to footer

### Node Type: 99-Prefix (Problem Pages)

Natural language consumer queries. Baseline retrieval capability test.

- URL: `/[country]/en/problems/99-[slug].html`
- Content: Consumer symptom phrased as long-tail search query
- Schema: Minimal (title, description, internal links)
- Test Function: Can LLM find the site for a natural query?

### Node Type: 77-Prefix (Solution Pages)

Keyword-dense content with Markdown header structure (`##`). Tests semantic extraction bias.

- URL: `/[country]/en/solutions/77-[slug]-solution.html`
- Content: 3-4 `##` headers, narrative prose, high keyword density
- Schema: Basic metadata only (no JSON-LD)
- Test Function: Does chunking/semantic structure improve retrieval?

### Node Type: 88-Prefix (Business Pages) — Core A/B Test

Synthetic business profiles with embedded JSON-LD `LocalBusiness` schema. Each query generates **2 content profiles × 3 design variants = 6 pages per business**.

#### Content A/B Testing (Business Name Prefix)

| Profile | Prefix | Schema | Key Fields | Narrative | Test Signal |
|---------|--------|--------|-----------|-----------|-------------|
| Sausage Ham Spam | Starts with "Sausage" | Full JSON-LD LocalBusiness | `taxID`, exact `streetAddress`, regional `telephone`, `aggregateRating`, `priceRange` | Minimal clinical prose | Structured data weighting |
| Welcome More Spam | Starts with "Welcome" | Minimal JSON-LD (no taxID/rating) | Only `name`, `description`, `areaServed` | Extensive narrative, multiple `##` headers, keyword density | Semantic content weighting |

#### Design A/B Testing (Filename Suffix)

| Variant | Suffix | CSS | Visual Design | Test Signal |
|---------|--------|-----|--------------|-------------|
| Minimal | `-primary` | None; semantic HTML only | Plain text | Pure content signal; control group |
| Responsive | `-responsive` | CSS Grid, viewport meta, typography | Header with color, semantic sections | Mobile signals; basic responsive design |
| Premium | `-premium` | Bootstrap-style full CSS | Hero, gradients, stat boxes, CTAs | Premium design signals; Core Web Vitals proxy |

**Example URLs for one query:**
- `88-permafrost-fence-post-primary.html` (Sausage, minimal)
- `88-permafrost-fence-post-responsive.html` (Sausage, responsive)
- `88-permafrost-fence-post-premium.html` (Sausage, premium)
- Plus 3 Welcome variants with same design progression

**Implicit A/B Logic:**
The code does NOT have a separate profile selector. Business name prefix (`"Sausage Ham Spam"` vs `"Welcome More Spam"`) triggers different schema generation and prose style. This keeps the dataset simple and ensures exact reproducibility. Design variants share all content—only CSS changes, isolating design signals.

### Node Type: 66-Prefix (Blog Pages)

Extended business narratives (1000+ words) with FAQ sections. Available only for FLK, SHN, SJM, PCN (non-tropical regions). Tests whether narrative depth affects retrieval.

- URL: `/[country]/en/blogs/66-[slug]-business-insights.html`
- Content: Long-form narrative, FAQ, case study, expertise demonstration
- Schema: Minimal LocalBusiness schema
- Phone Prefix: +66 (neutral international, not region-specific)
- Test Function: Does comprehensive content improve generative retrieval?

## Geographic Coverage & Authentic Signals

Each country has authentic geographic signals:

| Country | ISO | Phone | District | Currency | Climate | Queries |
|---------|-----|-------|----------|----------|---------|---------|
| Hong Kong | hkg | +852 | Causeway Bay | HKD | Subtropical urban | 20 |
| Singapore | sgp | +65 | Marina Bay | SGD | Tropical urban | 20 |
| Svalbard & Jan Mayen | sjm | +47 | Longyearbyen | NOK | Arctic permafrost | 10 + blogs |
| Pitcairn Islands | pcn | +64 | Adamstown | NZD | Remote tropical | 10 + blogs |
| Falkland Islands | flk | +500 | Stanley | FKP | Subpolar maritime | 2 + blogs |
| Saint Helena | shn | +290 | Jamestown | SHP | Isolated volcanic | 2 + blogs |

**Test Hypothesis:** Do LLMs weight regional phone prefixes as authenticity signals? Blog pages use +66 (neutral international) to test this.

## Modifying the Dataset

### Adding Queries

Edit the `queries` list in `build.py` or `build_enhanced.py`. Each query requires:

```python
{
    "id": "REGION_###",                          # Unique identifier
    "country": "hkg",                            # ISO 3-letter code
    "country_name": "Hong Kong",                 # Display name
    "slug": "problem-domain-slug",               # URL-safe slug
    "title": "Human-Readable Problem Title",     # H1 title
    "desc": "Long-tail consumer problem...",     # Natural language symptom query
    "expanded": "2-3 paragraph detailed analysis...",  # Enhanced description (build_enhanced.py)
    "sol": "solution keyword phrase",            # Solution keywords for 77-pages
    "biz": "Sausage Ham Spam [or Welcome More Spam] Business Name",  # CRITICAL: A/B profile name
    "cap": "Capability description"              # Service category
}
```

**Critical:** Business name MUST start with either `"Sausage Ham Spam"` or `"Welcome More Spam"`. This is a string prefix check that triggers the A/B schema fracture—changing it breaks the test.

### Using build_enhanced.py with Company Database

The `build_enhanced.py` script includes an integrated company database (`COMPANIES` dict) with 22 dummy companies using test keywords (sausage, welcome, spam, ham, fighter, p0wer, restful, timeness, windy, koala).

To add a new company:

```python
COMPANIES = {
    "company-key": {
        "name": "Company Name Ltd",
        "keywords": ["keyword1", "keyword2"],
        "countries": ["hkg", "sgp"],
        "addresses": {
            "hkg": "123 Street Name, District",
            "sgp": "456 Street Name, Area"
        },
        "phones": {
            "hkg": "+852 XXXX XXXX",
            "sgp": "+65 XXXX XXXX"
        },
        "description": "Service description and expertise focus."
    },
    # ... rest of companies
}

def get_relevant_companies(country, capability):
    """Get companies relevant to a specific country and capability."""
    # This function automatically assigns 3-4 companies to each problem page
    # based on country coverage
```

When you run `python build_enhanced.py`, the script automatically:
1. Finds all companies for each problem's country
2. Randomly selects 3-4 companies
3. Displays them with full contact details on the problem page
4. Creates internal links to company information

### Adding Companies to build_enhanced.py

Each company appears on 3-4 problem pages per country with:
- Full company name
- Phone number (country-specific format)
- Service description
- Expertise keywords

Companies are randomized per build, so running the script multiple times generates different company combinations on problem pages.

### Expanding to New Regions

1. Add country ISO-3 code to phone prefix routing (search for "Geographic Routing" in build.py):
   ```python
   elif country_iso == "new":
       phone_prefix, district, address, currency = "XXX", "City", "Street Address", "CUR"
   ```
2. Add queries with the new country code to the `queries` list
3. Run `python build.py`—the script auto-discovers the new country and creates directory structures

## Common Tasks

### Regenerate Content with Company Integration

Use `build_enhanced.py` for LLM-optimized content:

```bash
python build_enhanced.py
```

This automatically:
- Assigns companies to problem pages (3-4 per page, randomized)
- Generates expanded problem descriptions
- Creates internal linking structure
- Notifies Bing IndexNow API

### Regenerate Original Content

Use `build.py` for the base AEO testing structure:

```bash
python build.py
```

This generates the original 4-node architecture without company integration.

### Inspect Generated Content

```bash
# View a problem page with company recommendations
cat hkg/en/problems/99-coffee-ground-upcycling.html

# Check company mentions across all pages
grep -r "Sausage\|Welcome\|Spam\|Fighter" hkg/en/problems/ | head -10

# Count total internal links
grep -c "href=" hkg/en/problems/99-*.html | head -1

# Verify companies on pages
grep -h "<strong>" hkg/en/problems/*.html | grep -E "Sausage|Welcome|Spam|Fighter" | sort | uniq
```

### Verify Geographic Routing

```bash
# Check phone prefixes are correct by country
grep "telephone" hkg/en/businesses/88-*.html | head -1    # Should show +852
grep "telephone" sgp/en/businesses/88-*.html | head -1    # Should show +65
grep "telephone" sjm/en/businesses/88-*.html | head -1    # Should show +47
grep "telephone" pcn/en/businesses/88-*.html | head -1    # Should show +64
```

### Validate Sitemap and Indexing

```bash
# Count total URLs (should match expected count)
grep -c "<url>" sitemap.xml

# Check timestamp is current
grep "lastmod" sitemap.xml | head -5

# Validate XML structure
python -m xml.etree.ElementTree sitemap.xml && echo "Valid XML"

# Check IndexNow submission status
python build_enhanced.py 2>&1 | grep -A 5 "IndexNow"
# HTTP 200/202 = success; HTTP 403 = awaiting first-time verification (1-2 hours)
```

### Test Directory Navigation

```bash
# Verify all 4 directory pages exist
ls -lh directory-by-*.html

# Check homepage links to directories
grep "directory-" index.html | grep href

# Verify directory pages cross-link each other
grep "directory-by-country" directory-by-service.html
grep "directory-by-service" directory-by-country.html
```

### Inspect Generated Content

```bash
# View a problem page (baseline query)
cat sjm/en/problems/99-vietnamese-massage-back-pain-relief.html

# View a solution page (semantic focus)
cat sjm/en/solutions/77-vietnamese-massage-back-pain-relief-solution.html

# View all business variants (all 3 design + both content profiles)
ls sjm/en/businesses/88-vietnamese-massage-back-pain-relief-*.html

# Verify Sausage profile has full schema (taxID, aggregateRating)
grep -E 'taxID|aggregateRating' sjm/en/businesses/88-vietnamese-massage-back-pain-relief-primary.html

# Verify Welcome profile lacks taxID and aggregateRating
grep -E 'taxID|aggregateRating' sjm/en/businesses/88-glacier-*primary.html

# Check directory page link coverage
grep -o 'href="[^"]*"' directory-by-country.html | wc -l    # Should show 350+
grep -o 'href="[^"]*"' directory-by-service.html | wc -l    # Should show 326+
grep -o 'href="[^"]*"' directory-by-business.html | wc -l   # Should show 198+
grep -o 'href="[^"]*"' directory-by-problem.html | wc -l    # Should show 70+
```

## File Manifest

- `build.py`: Core generator for original AEO testing matrix (main entry point, Python stdlib only)
- `build_enhanced.py`: Enhanced generator with company database and internal linking optimization
- `index.html`: Homepage with navigation to all content types
- `about.html`: Mission/Vision/Strategy overview
- `contact.html`: Enterprise contact form
- `assets/css/main.css`: Master stylesheet with animations
- `netlify.toml`: Netlify config (auto-generated)
- `sitemap.xml`: All URLs with lastmod timestamps (auto-generated)
- `7c8e9f2a4b1c3d6e8f0a2b4c6d8e0f1a.txt`: IndexNow verification file (auto-generated)
- `robots.txt`: Search engine directives (includes sitemap reference)
- `directory-by-country.html`: Directory organized by jurisdiction (auto-generated)
- `directory-by-service.html`: Directory organized by service capability (auto-generated)
- `directory-by-business.html`: Directory A/B test comparison (auto-generated)
- `directory-by-problem.html`: Directory organized by problem query (auto-generated)
- `CLAUDE.md`: This file - guidance for Claude Code
- `ENHANCEMENT_GUIDE.md`: Complete documentation of company database and internal linking
- `COMPANIES_REFERENCE.md`: All 22 companies with full profiles
- `GENERATION_SUMMARY.txt`: Metrics and verification checklist
- `QUICK_REFERENCE.md`: Quick start guide for enhancements
- `INDEX.md`: Master index of all documentation

Generated content structure:
- `/{country}/index.html` - Country landing page (6 pages)
- `/{country}/en/problems/99-*.html` - Problem nodes
- `/{country}/en/solutions/77-*.html` - Solution nodes
- `/{country}/en/businesses/88-*-{primary|responsive|premium}.html` - Business variants
- `/{country}/en/blogs/66-*.html` - Blog pages (selected countries)

## Key Design Principles

**No External Dependencies:** All generation uses Python stdlib. Portable across Windows/Mac/Linux.

**Static-Only Output:** All HTML/XML/CSS. No server processing. Enables edge caching and consistent CDN behavior.

**Deterministic Generation:** `queries` list is the single source of truth. Same input = identical output. Reproducible timestamps for testing.

**Authentic Geographic Signals:** Region-specific phone prefixes, district names, currencies, and addresses in all business pages. Tests whether LLMs weight authenticity.

**IndexNow Integration:** On every `python build.py`:
1. Generates verification file
2. Extracts all 359 URLs from sitemap (344 content + 6 country indexes + 4 directories + 5 branding)
3. Submits to Bing IndexNow API
4. Returns HTTP 200/202 on success (or 403 on first submission awaiting verification)

**LLM-Discoverable Architecture:** Complete crawl path for optimal indexation:
- Homepage → Browse by Region (6 country cards) → Country Index → Content pages (99/77/88/66)
- Homepage → Comprehensive Directory (4 navigation approaches) → All pages organized by:
  - Country (jurisdiction-based discovery)
  - Service/Capability (semantic grouping)
  - Business Profile (Sausage vs Welcome A/B testing)
  - Problem (natural language query index)
- All directory pages linked in footer with cross-navigation

## Testing Strategy

**Methodology:** Submit identical problem queries to multiple LLMs (ChatGPT, Claude, DeepSeek, Gemini, Perplexity). Document which pages are retrieved and in what order.

**Key Measurements:**
- **Page Type Order:** Does LLM retrieve 99→77→88→66 in sequence? Or isolated pages?
- **Content Profile:** Does Sausage (structured) outrank Welcome (semantic)?
- **Design Preference:** Premium > Responsive > Minimal? Equal? Varies by LLM?
- **Phone Prefix Signal:** Do region-specific prefixes outrank neutral +66?

**Result Interpretation:**

| Finding | Interpretation |
|---------|-----------------|
| Premium > Responsive > Minimal (consistent) | Design signals heavily weighted |
| All variants equal | Design-agnostic; content-focused indexing |
| Pattern varies by LLM | Indexing behavior is model-specific |
| Sausage outranks Welcome | Structured data (JSON-LD) is strong signal |
| Welcome outranks Sausage | Semantic content density > structured data |
| Regional prefixes rank higher | Geographic authenticity affects trust |

## Troubleshooting

### 404 Errors on Subpages

If country index pages (e.g., `/hkg/index.html`) return 404 errors for linked subpages, the issue is typically in the `relpath` generation. The path must include the full country and `/en/` directory structure:

**Correct:** `href="/hkg/en/problems/99-file.html"` → maps to actual file at `hkg/en/problems/99-file.html`
**Incorrect:** `href="/problems/99-file.html"` → returns 404 (file doesn't exist at root)

Fix: Ensure path generation preserves full directory structure: `relpath = filepath.replace(os.sep, '/')`

---

## Two Build Approaches: When to Use Each

### build.py (Original AEO Testing Matrix)

**Purpose:** Core AEO research measuring LLM indexing behavior across structured data, design complexity, and content density signals.

**Features:**
- 4-node architecture (99/77/88/66 prefixes)
- A/B content profiles (Sausage vs Welcome)
- Design variants (Minimal/Responsive/Premium)
- Full LocalBusiness schema with taxID and aggregateRating (Sausage profile)
- Minimal schema with semantic content focus (Welcome profile)

**When to use:**
- Pure AEO testing with A/B signal isolation
- Measuring design vs structured data vs content weighting
- Research on which LLM ranking signals matter most

### build_enhanced.py (LLM Discoverability Optimization)

**Purpose:** Dramatically improve LLM indexation through content richness, entity density, and internal linking.

**Adds to base build.py:**
- Integrated company database (22 companies with test keywords)
- Expanded problem descriptions (50 words → 400+ words)
- 3-4 companies per problem page with realistic contact info
- 8-10 internal links per page (vs 1-2 in original)
- Breadcrumb navigation
- Cross-links between 4 directory types
- No orphaned pages (all discoverable from multiple entry points)

**Company database:**
- 22 companies using keywords: sausage, welcome, spam, ham, fighter, p0wer, restful, timeness, windy, koala
- Multi-jurisdiction (6 companies span 2-3 countries)
- Localized (16 companies are jurisdiction-specific)
- Realistic contact info (authentic phone formats, district names, addresses)
- Automatic assignment to problem pages (randomized 3-4 per page)

**When to use:**
- Testing whether LLMs discover and index content better
- Measuring impact of content depth on indexation
- Testing effect of internal linking architecture
- Real-world AEO optimization scenarios

**Key technical difference:** `build_enhanced.py` includes a `COMPANIES` dict and `get_relevant_companies()` function that `build.py` does not have. Both regenerate the same base 4-node architecture, but `build_enhanced.py` adds the company layer and internal linking richness on top.

---

## Current Status

- **Latest Build:** `build_enhanced.py` recommended for LLM testing and deployment
- **Original Build:** `build.py` maintains pure AEO research structure (unchanged)
- **Pages Generated:** 27+ (10 problems + 10 solutions + 6 country indexes + 4 directories + homepage)
- **Sitemap URLs:** 27+
- **IndexNow:** Configured and auto-submitting on every build
- **Navigation:** Complete discovery paths from homepage to all content
- **Links:** All verified working (no 404 errors)
- **Documentation:** Complete with ENHANCEMENT_GUIDE.md, COMPANIES_REFERENCE.md, and QUICK_REFERENCE.md
