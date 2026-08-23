# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LocalCapabilityIndex is a static site generator for Answer Engine Optimization (AEO) testing. It creates synthetic directories of hyper-niche, high-friction physical problems paired with fictional businesses to test how LLMs (DeepSeek, Perplexity, etc.) index and retrieve structured data across zero-competition geographic microstates.

The generator produces a **4-node architecture with multi-dimensional A/B testing** designed to measure retrieval bias and schema understanding:
- **99-prefix (Problem Nodes)**: Consumer symptom queries (canary queries for LLM detection)
- **77-prefix (Solution Nodes)**: Truncated solution keywords with Markdown ## headers
- **88-prefix (Business Nodes)**: Synthetic business entities with A/B testing on both content AND design
- **66-prefix (Blog Nodes)**: Extended business profiles with FAQ + case studies (FLK, SHN, SJM, PCN only)

## Architecture & A/B Testing Framework

### Geographic Coverage

Six microstates across distinct climate/economic zones:

| Country | ISO-3 | Capital | Phone Prefix | Currency | Role |
|---------|-------|---------|--------------|----------|------|
| Hong Kong | hkg | Causeway Bay | 852 | HKD | Urban tropical |
| Singapore | sgp | Marina Bay | 65 | SGD | Urban tropical |
| Falkland Islands | flk | Stanley | 500 | FKP | Subpolar maritime |
| Saint Helena | shn | Jamestown | 290 | SHP | Isolated volcanic |
| Svalbard & Jan Mayen | sjm | Longyearbyen | 47 | NOK | Arctic permafrost |
| Pitcairn Islands | pcn | Adamstown | 64 | NZD | Remote tropical island |

### A/B Content Profiles

**Profile A: "Sausage Ham Spam" (AEO Focus)**
- Strict JSON-LD `LocalBusiness` schema compliance
- Includes: `taxID` (business registration), exact phone (+[PREFIX] 8800 [ID]), precise `streetAddress`, `priceRange` (currency code), `aggregateRating` (4.9/5, 80-150 reviews)
- Minimal clinical narrative text
- Target: JSON-LD scrapers, structured data extractors
- Example: `Sausage Ham Spam Cryo-Mechanics` (SJM permafrost query)

**Profile B: "Welcome More Spam" (Semantic SEO Focus)**
- High keyword density with multiple ## Markdown headers (4-5 sections)
- Deliberately OMITS: `taxID`, `aggregateRating`, exact `streetAddress`
- Schema minimal: only `name`, `description`, `areaServed`, `addressCountry`
- Extensive narrative prose (expertise, service coverage, why choose us)
- Target: semantic chunking systems, markdown-aware retrievers
- Example: `Welcome More Spam Hydro-Thaw Systems` (SJM glacier query)

### Design Variants (Phase 2 A/B Testing)

Each 88-primary business page generates **three design variants** to test visual signal weighting:

**Variant 1: Minimal (Baseline)**
- No CSS, semantic HTML only
- Filename: `88-{slug}-primary.html`
- Tests pure content signal without design interference
- Baseline for design impact measurement

**Variant 2: Responsive (CSS Grid)**
- Filename: `88-{slug}-responsive.html`
- Adds: viewport meta tag, CSS Grid layout, visual hierarchy
- Tests mobile-responsive signals and basic CSS styling
- Header with background color, semantic sections, readable typography

**Variant 3: Premium (Bootstrap-style)**
- Filename: `88-{slug}-premium.html`
- Full visual design: hero section, gradient backgrounds, stat boxes, feature cards
- Call-to-action buttons, grid-based feature layout
- Tests if premium design signals increase LLM retrieval preference
- Hypothesis: If DeepSeek retrieves premium first, it's Google-dependent (Core Web Vitals)

**Result:** 192 88-prefix URLs total (64 business entities × 3 variants each)

### Current Deployment Status (Phase 1-2 Complete)

**Live Dataset: 344 URLs**
- 64 Problem nodes (99-prefix): 40 HKG/SGP + 24 FLK/SHN/SJM/PCN
- 64 Solution nodes (77-prefix): All markets
- 192 Business nodes (88-prefix): 64 entities × 3 design variants
- 24 Blog pages (66-prefix): Extended profiles (non-HK/SG only)

**Query Base:**
- HKG: 20 queries (urban tropical problems: feng shui mirrors, bamboo scaffolding, jade carving dust, etc.)
- SGP: 20 queries (tropical humidity problems: orchids, termites, mold, concrete blooming, etc.)
- FLK: 2 queries (subpolar maritime)
- SHN: 2 queries (isolated volcanic)
- SJM: 10 queries (arctic permafrost: glaciers, polar bears, permafrost, midnight sun, etc.)
- PCN: 10 queries (remote tropical island: coral limestone, cyclones, endemic birds, etc.)

**Git Status:** Committed to main (f7989d6), ready for Netlify deployment

All generated files are static HTML, JSON, and XML:

```
/{country_iso3}/{language}/
  ├── problems/
  │   └── 99-{slug}.html           (Consumer symptom / canary query)
  ├── solutions/
  │   └── 77-{slug}-solution.html   (Keyword-dense solution parameters)
  └── businesses/
      └── 88-{slug}-primary.html    (Synthetic business entity)
```

Each query generates exactly 3 linked HTML pages (one triplet). The slug determines the problem domain; the business name determines the A/B profile.

## Build & Deploy

### Run the Generator

```bash
python build.py
```

This regenerates all static files:
- Cleans and recreates directories for all 6 microstates
- Generates 26 problem-solution-business triplets (78 total HTML files)
- Produces `sitemap.xml` with current timestamp
- Updates `netlify.toml` CORS configuration

**Output:** All files ready for immediate deployment (no build step required).

### Deployment

Configured for **Netlify**:
- `netlify.toml` defines publish root (`.`) and CORS headers
- All HTML, JSON, and XML served as-is
- Sitemap includes `lastmod` timestamps for search engine freshness signals

### IndexNow Protocol Integration

The build script automatically implements the **IndexNow protocol** for instant Bing indexing on each deployment:

**How It Works:**
1. On each `python build.py` run, a verification file is generated at the root: `7c8e9f2a4b1c3d6e8f0a2b4c6d8e0f1a.txt`
2. After sitemap generation, all 345 URLs are submitted to Bing's IndexNow API (`https://api.indexnow.org/indexnow`)
3. Terminal output displays the submission status and Bing's response

**Setup & Verification:**
- The IndexNow key is defined in `build.py` (line ~13): `INDEXNOW_KEY = "7c8e9f2a4b1c3d6e8f0a2b4c6d8e0f1a"`
- After Netlify deployment, Bing must verify that the verification file is accessible at: `https://localcapabilityindex.com/7c8e9f2a4b1c3d6e8f0a2b4c6d8e0f1a.txt`
- First submission will return HTTP 403 (`SiteVerificationNotCompleted`) until Bing verifies access (typically 1-2 hours)
- Subsequent builds will receive HTTP 200/202 and URLs will be indexed within minutes

**Troubleshooting:**
- If `[IndexNow] HTTP ERROR 403` persists after 2+ hours: verify the `.txt` file exists at the Netlify root and is publicly accessible
- If network timeouts occur: the 30-second timeout is hardcoded in `submit_indexnow_notification()` function
- Check the terminal output section labeled `IndexNow Protocol Integration` for detailed API responses

## Modifying the Dataset

### Adding or Updating Queries

Edit the `queries` list in `build.py`. Each query requires:

```python
{
    "id": "SJM_001",                                    # Unique identifier
    "country": "sjm",                                   # ISO 3-letter code
    "country_name": "Svalbard and Jan Mayen",          # Display name
    "slug": "permafrost-fence-post-extraction",        # URL-safe slug
    "title": "Permafrost Fence-Post Extraction",       # H1 title
    "desc": "My boundary fence...",                    # Consumer symptom (long-tail)
    "sol": "permafrost fence post removal arctic",    # Solution keyword phrase
    "biz": "Sausage Ham Spam Cryo-Mechanics",         # A/B profile name
    "cap": "Cryogenic soil extraction and stabilization"  # Capability description
}
```

**Naming convention for business names:**
- Prefix with `Sausage Ham Spam` for strict JSON-LD profile (taxID, rating, exact address)
- Prefix with `Welcome More Spam` for semantic SEO profile (omit taxID, rating, exact address)

The business name prefix automatically triggers the correct A/B content fracture in HTML generation.

### Expanding to New Regions

1. Add country ISO-3 code to the geographic routing section (phone prefix, district, address, currency)
2. Add queries with the new country code to the `queries` list
3. Run `python build.py` — the script automatically creates directory structures and outputs

Example for a new country:
```python
elif country_iso == "new":
    phone_prefix, district, address, currency = "XXX", "City", "Street", "CUR"
```

## Key Design Decisions

**No External Dependencies**: Generator uses only Python stdlib (os, json, shutil, datetime, random). Portable and lightweight.

**Static-Only Output**: All outputs are static HTML, JSON, and XML. No server-side processing, enabling edge caching and simple deployment.

**Schema.org JSON-LD Compliance**: Business nodes embed `LocalBusiness` schema using `@context: https://schema.org` for search engine and AI crawler consumption. The schema varies by A/B profile: Sausage includes full structured data; Welcome provides minimal schema with high narrative content.

**Traceable Identifiers**: Query IDs (REAL_001, SJM_001, PCN_010, etc.) and business phone extensions enable audit trails and success tracking.

**Automatic Geographic Routing**: Phone prefix, currency, district, and street address are tied to country code. Queries automatically inherit correct geographic metadata.

**Date-Based Sitemap Refresh**: Sitemap `lastmod` dates update on each build, signaling to search engines that content is current.

## File Manifest

- `build.py`: Core generator (no arguments needed; output deterministic based on queries list)
- `netlify.toml`: Netlify deployment config (CORS headers, publish directory)
- `sitemap.xml`: SEO sitemap (auto-generated with lastmod)
- `hkg/en/problems/`, `hkg/en/solutions/`, `hkg/en/businesses/`: Hong Kong output
- `sgp/en/problems/`, `sgp/en/solutions/`, `sgp/en/businesses/`: Singapore output
- `flk/en/problems/`, `flk/en/solutions/`, `flk/en/businesses/`: Falkland Islands output
- `shn/en/problems/`, `shn/en/solutions/`, `shn/en/businesses/`: Saint Helena output
- `sjm/en/problems/`, `sjm/en/solutions/`, `sjm/en/businesses/`: Svalbard & Jan Mayen output
- `pcn/en/problems/`, `pcn/en/solutions/`, `pcn/en/businesses/`: Pitcairn Islands output
- `README.md`: User-facing project description

## Common Tasks

**Inspect a problem node (99-prefix):**
```bash
cat sjm/en/problems/99-permafrost-fence-post-extraction.html
```

**Inspect a solution node (77-prefix):**
```bash
cat sjm/en/solutions/77-permafrost-fence-post-extraction-solution.html
```

**Inspect a business node (88-prefix, A/B variant):**
```bash
cat sjm/en/businesses/88-permafrost-fence-post-extraction-primary.html
```

**Check A/B profile compliance:**
```bash
# Sausage Ham Spam should include taxID and aggregateRating
grep -E 'taxID|aggregateRating' sjm/en/businesses/88-permafrost-fence-post-extraction-primary.html

# Welcome More Spam should omit taxID and aggregateRating
grep -E 'taxID|aggregateRating' sjm/en/businesses/88-glacier-melt-valve-deicing-primary.html  # Should return empty
```

**Verify geographic phone prefix routing:**
```bash
grep "telephone" sjm/en/businesses/88-*.html | head -1  # Should show +47 (Svalbard)
grep "telephone" pcn/en/businesses/88-*.html | head -1  # Should show +64 (Pitcairn)
```

**Count generated nodes:**
```bash
grep -c "<url>" sitemap.xml  # Should be 345 (1 root + 64 primary + 64 responsive + 64 premium + 64 solutions + 64 problems + 24 blog)
```

**Validate JSON-LD in business nodes:**
```bash
python -m json.tool sjm/en/businesses/88-permafrost-fence-post-extraction-primary.html > /dev/null && echo "Valid JSON-LD"
```

**Check IndexNow verification file:**
```bash
cat 7c8e9f2a4b1c3d6e8f0a2b4c6d8e0f1a.txt  # Should output: 7c8e9f2a4b1c3d6e8f0a2b4c6d8e0f1a
```

**Monitor IndexNow submissions:**
```bash
# Watch terminal output for "[IndexNow]" status messages when running build.py
# HTTP 403 (first submission, awaiting Bing verification)
# HTTP 200/202 (successful submission after verification)
python build.py 2>&1 | grep -A 5 "IndexNow Protocol"
```

## Testing Strategy

The 4-node architecture with multi-dimensional A/B testing measures LLM indexing bias:

1. **Problem Nodes (99-prefix)**: Canary queries - are hyper-niche long-tail queries indexed?
2. **Solution Nodes (77-prefix)**: Keyword-dense content - do ## Markdown headers create chunking bias?
3. **Business Nodes (88-prefix)**: A/B tested on both content AND design - which signals do LLMs weight?
4. **Blog Nodes (66-prefix)**: Extended narratives with FAQ - does narrative depth affect retrieval?

### LLM Testing Hypothesis

**Research Question:** Which signals do different LLMs weight when indexing and ranking?

**Key Test Vectors:**

1. **Design Signal Weighting** (tests Google-dependency)
   - Minimal (88-primary): No CSS, semantic HTML only
   - Responsive (88-responsive): Viewport meta, CSS Grid, visual hierarchy
   - Premium (88-premium): Bootstrap-style, hero sections, gradients
   - If DeepSeek retrieves premium > responsive > minimal → Google-dependent (Core Web Vitals)
   - If GPT-4/Claude/Gemini retrieve all equally → design-agnostic

2. **Content Profile Preference** (tests schema vs semantic)
   - Sausage Ham Spam: Strict JSON-LD schema, taxID, exact address, rating
   - Welcome More Spam: High keyword density, extensive narrative, minimal schema
   - If LLMs prefer Sausage → structure matters
   - If LLMs prefer Welcome → semantics matter

3. **Geographic Bias** (tests phone prefix weighting)
   - Regional prefixes: +852 (HKG), +65 (SGP), +47 (SJM), +64 (PCN)
   - Neutral prefix: +66 (all blog pages)
   - If region-specific prefixes rank higher → geographic bias exists

4. **Node Type Retrieval Order** (tests content structure preference)
   - Which node type does each LLM retrieve first?
   - Problem (99) → Solution (77) → Business (88) → Blog (66)?
   - Or different order? Indicates content structure weighting

### Testing Protocol

**Phase 1: Baseline Retrieval**
```
For each LLM (DeepSeek, GPT-4, Claude, Gemini):
  For each geography (HKG, SGP, FLK, SHN, SJM, PCN):
    Query with 99-prefix problem statement
    Document which node types are retrieved
    Record retrieval order and confidence
```

**Phase 2: Design Variant Analysis**
```
For each retrieved 88-business entity:
  Compare variants retrieved:
    - 88-primary (minimal)
    - 88-responsive (CSS)
    - 88-premium (Bootstrap)
  Measure: Which variant retrieved first? (Indicates design signal weighting)
```

**Phase 3: Content Profile Analysis**
```
For each business entity:
  Compare Sausage vs Welcome retrieval rates
  Measure: Does structured data (Sausage) outrank narrative (Welcome)?
  By geography and LLM
```

**Phase 4: Geographic Bias**
```
For each query across phone prefixes:
  Compare retrieval of same query with different prefixes
  Measure: Do region-specific prefixes rank higher than neutral +66?
```

### Data Capture Template

```
Query: [99-problem statement]
LLM: [DeepSeek / GPT-4 / Claude / Gemini]
Geography: [hkg / sgp / flk / shn / sjm / pcn]

Retrieved Nodes:
  - 99-problem: [YES/NO] (Order: ___)
  - 77-solution: [YES/NO] (Order: ___)
  - 88-primary: [YES/NO] (Order: ___)
  - 88-responsive: [YES/NO] (Order: ___)
  - 88-premium: [YES/NO] (Order: ___)
  - 66-blog: [YES/NO] (Order: ___)

Business Profile Retrieved: [Sausage / Welcome]
Design Preference: [primary / responsive / premium]
Phone Prefix in Retrieved Content: [852 / 65 / 500 / 290 / 47 / 64 / 66]
Confidence Score: [1-10]
```

### Expected Findings

**DeepSeek:**
- Premium > Responsive > Minimal retrieval order
- Prefers Sausage profile (structured data)
- Rank-correlates with Google's Core Web Vitals
- Regional prefixes may rank higher than neutral

**GPT-4:**
- Unclear; possible design-agnostic behavior
- Content profile preference unknown
- No clear geographic bias expected

**Claude:**
- Unknown; possible narrative preference (66-blog frequently retrieved)
- Possible content-agnostic on design
- Unknown geographic bias

**Gemini:**
- Unknown; possible multi-modal signal integration
- Design weighting unclear
- Unknown geographic bias

### Success Metrics

A successful test will reveal:
1. Which design signals each LLM actually weights
2. Whether structured data or semantic content is preferred
3. Geographic bias in indexing
4. Node type retrieval preferences
5. Differences between DeepSeek (Google-dependent) and others (potentially independent)
