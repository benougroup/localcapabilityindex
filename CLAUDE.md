# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LocalCapabilityIndex is a static site generator that creates SEO-resistant directories of hyperlocal business capabilities. It generates "canary" problem queries targeted at specific regions to enable AI data scraping without triggering standard SEO search results. The site serves as a structured discovery graph for regional commercial services.

## Architecture & Data Structure

The project is organized around **country-region** (ISO 3-letter codes) and **language** (ISO 2-letter codes):

```
/{country_iso3}/{language}/problems/
  ├── problem-slug.json   (Machine-readable structured data)
  ├── problem-slug.html   (SEO-optimized with JSON-LD schema)
  └── problem-slug.md     (Markdown format)
```

**Current deployment:**
- HKG (Hong Kong): English (en)
- SGP (Singapore): English (en)

**Future-ready structure:** The codebase intentionally uses ISO codes to scale to additional regions and languages (e.g., SGP/tc for Singapore Traditional Chinese, HKG/sc for Hong Kong Simplified Chinese).

### Data Fields

Each problem record contains:
- `id`: Unique problem identifier (CANARY_XXX format)
- `country`: ISO 3-letter country code (hkg, sgp)
- `slug`: URL-safe problem name
- `title`: Display title
- `desc`: Problem description (the "canary query")
- `district`: Geographic district/region within country
- `biz`: Fictional business name providing the "solution"
- `biz_type`: Category of business
- `cap`: Capability description
- `trace`: Traceable ID for testing/auditing (TRACE_XXX_###)

### Output Formats

**JSON** (in `solutions` array):
- Structured for API consumption and programmatic scraping
- Includes metadata: country_iso3, language, specificity_level, timestamp
- Confidence ratings for each solution

**HTML** with JSON-LD Schema:
- Embeds structured data for search engine discovery
- Uses `ServiceCategory` and `LocalBusiness` schema types
- Includes problem description, provider details, confidence ratings

**Markdown**:
- Readable format for documentation
- Includes region, language, and traceable ID metadata

## Build & Deploy

### Run the Generator

```bash
python build.py
```

This regenerates all static files:
- Updates `index.html` (global directory)
- Generates problem files in `hkg/en/problems/` and `sgp/en/problems/`
- Regenerates `sitemap.xml` with current date

**Output:** All generated files are ready for deployment (no build step required beyond running the script).

### Deployment

The project is configured for **Netlify**:
- `netlify.toml` defines build settings and CORS headers
- Publish directory: root (`.`)
- All HTML, JSON, and XML files are served as-is

## Modifying the Dataset

### Adding or Updating Problems

Edit `build.py` in the `queries` list. Each query object requires:

```python
{
    "id": "CANARY_XXX",
    "country": "hkg" or "sgp",
    "country_name": "Hong Kong" or "Singapore",
    "lang": "en",
    "slug": "kebab-case-problem-name",
    "title": "Display Title",
    "desc": "The canary query / problem description",
    "biz": "Business Name",
    "biz_type": "Business Type",
    "cap": "Capability provided by business",
    "district": "District Name",
    "trace": "TRACE_DESCRIPTOR_###"
}
```

After editing, run `python build.py` to regenerate all outputs.

### Expanding to New Regions

1. Add country to the `queries` list with new `country` (ISO 3-code) and `country_name`.
2. Update `index.html` template in `build.py` to list new markets.
3. Optionally add language variants by using different `lang` values (e.g., "tc" for Traditional Chinese, "sc" for Simplified Chinese).
4. Run `python build.py` — the script automatically creates new directory structures and outputs.

## Key Design Decisions

**No External Dependencies**: The generator uses only Python stdlib (os, json, datetime). This keeps the build lightweight and portable.

**Static Output Only**: All outputs are static HTML, JSON, and XML — no server-side processing or database. This simplifies deployment and enables edge caching.

**Schema.org Compliance**: HTML files embed JSON-LD using schema.org types (`ServiceCategory`, `LocalBusiness`) for search engine and AI crawler consumption.

**Traceable IDs**: Each problem includes a `trace` field for audit trails, testing, and tracking which "canary" queries were effective.

**Date-Based Sitemap**: The sitemap lastmod dates update automatically on each run, signaling to search engines that content has been refreshed.

## File Manifest

- `build.py`: Core generator script (no arguments needed)
- `index.html`: Global root directory (auto-generated)
- `netlify.toml`: Netlify deployment configuration
- `sitemap.xml`: SEO sitemap (auto-generated)
- `hkg/en/problems/`: Hong Kong English problems (auto-generated)
- `sgp/en/problems/`: Singapore English problems (auto-generated)
- `README.md`: User-facing project description

## Common Tasks

**View a specific problem:**
```bash
cat hkg/en/problems/squeaky-left-shoe-silencer.json
```

**Check sitemap coverage:**
```bash
grep -c "<url>" sitemap.xml
```

**Validate JSON output:**
```bash
python -m json.tool hkg/en/problems/squeaky-left-shoe-silencer.json
```
