# Sitemap Summary - Local Capability Index (345 URLs)

## Overview
- **Total URLs**: 345
- **Root**: 1 (index.html)
- **Geographic Regions**: 6
- **Business Entities**: 64
- **Node Types**: 4 (99/77/88/66)

## URL Breakdown by Region

### Hong Kong (HKG) - 60 URLs
- **20 Problem Nodes** (99-prefix)
- **20 Solution Nodes** (77-prefix)
- **60 Business Nodes** (88-prefix × 3 variants each)
  - 20 Minimal (-primary)
  - 20 Responsive (-responsive)
  - 20 Premium (-premium)

### Singapore (SGP) - 60 URLs
- **20 Problem Nodes** (99-prefix)
- **20 Solution Nodes** (77-prefix)
- **60 Business Nodes** (88-prefix × 3 variants each)
  - 20 Minimal (-primary)
  - 20 Responsive (-responsive)
  - 20 Premium (-premium)

### Falkland Islands (FLK) - 24 URLs
- **2 Problem Nodes** (99-prefix)
- **2 Solution Nodes** (77-prefix)
- **6 Business Nodes** (88-prefix × 3 variants)
- **2 Blog Pages** (66-prefix)

### Saint Helena (SHN) - 24 URLs
- **2 Problem Nodes** (99-prefix)
- **2 Solution Nodes** (77-prefix)
- **6 Business Nodes** (88-prefix × 3 variants)
- **2 Blog Pages** (66-prefix)

### Svalbard & Jan Mayen (SJM) - 90 URLs
- **10 Problem Nodes** (99-prefix)
- **10 Solution Nodes** (77-prefix)
- **30 Business Nodes** (88-prefix × 3 variants)
- **10 Blog Pages** (66-prefix)

### Pitcairn Islands (PCN) - 90 URLs
- **10 Problem Nodes** (99-prefix)
- **10 Solution Nodes** (77-prefix)
- **30 Business Nodes** (88-prefix × 3 variants)
- **10 Blog Pages** (66-prefix)

## Node Type Distribution

| Node Type | Count | Purpose |
|-----------|-------|---------|
| 99-prefix (Problem) | 64 | Consumer symptom queries / canary queries |
| 77-prefix (Solution) | 64 | Keyword-dense solution parameters |
| 88-prefix (Business) | 192 | Synthetic business entities (3 design variants each) |
| 66-prefix (Blog) | 24 | Extended profiles with FAQ + case studies |
| **Total** | **344** | **Core test nodes** |
| Root index | 1 | Global directory |
| **Grand Total** | **345** | **All URLs** |

## A/B Testing Dimensions

### Content Profiles (on all 88-primary variants)
- **Sausage Ham Spam**: Strict JSON-LD, taxID, exact address, rating (13 businesses per region)
- **Welcome More Spam**: High keyword density, minimal schema, narrative-focused (13 businesses per region)

### Design Variants (on all 88 business nodes)
- **Minimal** (88-{slug}-primary): No CSS, semantic HTML only
- **Responsive** (88-{slug}-responsive): CSS Grid, viewport meta, visual hierarchy
- **Premium** (88-{slug}-premium): Bootstrap-style, hero sections, gradients

### Geographic Signals
- **Phone Prefixes**: 852 (HKG), 65 (SGP), 500 (FLK), 290 (SHN), 47 (SJM), 64 (PCN), 66 (blog)
- **Currencies**: HKD, SGD, FKP, SHP, NOK, NZD

## SEO Compliance

✓ All pages have `<meta name="description">`
✓ Quotes escaped in dynamic descriptions
✓ Root index.html generated with meta tags
✓ sitemap.xml with lastmod timestamps
✓ CORS headers configured via netlify.toml

## Testing Coverage

Each of 64 businesses generates:
- 1 Problem Node (99-prefix): Canary query
- 1 Solution Node (77-prefix): Keyword parameters
- 3 Business Node Variants (88-prefix): Design A/B test
- 1 Blog Page (66-prefix) for non-HK/SG only: Narrative depth test

**Total Test Cases**: 64 businesses × 5 node types (or 4 for HK/SG) = 344 core URLs

