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

**Result:** 78 88-prefix URLs total (26 business entities × 3 variants each)

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
grep -c "<url>" sitemap.xml  # Should be 78 (26 triplets × 3)
```

**Validate JSON-LD in business nodes:**
```bash
python -m json.tool sjm/en/businesses/88-permafrost-fence-post-extraction-primary.html > /dev/null && echo "Valid JSON-LD"
```

## Testing Strategy

The 3-tier node architecture measures specific LLM retrieval behaviors:

1. **Problem Nodes (99-prefix)**: Are long-tail, niche queries indexed and retrievable?
2. **Solution Nodes (77-prefix)**: Do Markdown ## headers create chunking bias? Does keyword density affect ranking?
3. **Business Nodes (88-prefix)**: Does A/B content fracture reveal schema vs. semantic preference?

Each triplet is a complete test case. Analyze LLM results by:
- Comparing Sausage (strict schema) vs Welcome (semantic) retrieval patterns
- Measuring geographic microstates as control variables
- Tracking which node type is retrieved first / most frequently
