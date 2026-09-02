# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## CRITICAL - READ THIS FIRST

**HISTORY:** This repository has experienced 5 broken link crisis cycles. The root cause was mismatch between directory files and actual content. As of Sept 2, 2026, all issues are fixed and verified. DO NOT repeat previous mistakes.

**THE ONE RULE:** When you add, modify, or delete ANY problem or business page, you MUST run:
```bash
python3 fix_links.py
```
Before committing. There are no exceptions to this rule.

## CRITICAL CONSTRAINTS

**The user is paying Netlify credits for every deployment. These are non-negotiable:**

### DO NOT:
- Modify `index.html` (homepage) - It has been verified 100% intact. ANY change breaks everything
- Modify site structure or navigation design
- Regenerate with old scripts (`build.py`, `build_enhanced.py`, `build_ultra_rich.py`) - They create broken links
- Manually edit directory files - They are auto-generated only
- Add content to countries other than HKG/FLK without running `fix_links.py`
- Commit without running `fix_links.py` first

### ALWAYS:
- Use `fix_links.py` to regenerate directories after content changes
- Run link validation before committing (script does this automatically)
- Keep homepage completely untouched
- Test all crawl paths before deployment

## Current Verified State (Sept 2, 2026)

**Content Inventory:**
- 2 active jurisdictions: Hong Kong (HKG), Falkland Islands (FLK)
- 6 problem pages (2 HKG + 4 FLK)
- 13 business pages (7 HKG + 6 FLK)
- 19 total content pages

**Verification Status: COMPLETE**
- ✓ 0 broken links (all 58 links validated)
- ✓ Homepage: 440 lines, completely intact
- ✓ Sitemap: 25 URLs, all valid
- ✓ Spider crawlability: 4 major paths tested and working
- ✓ FLK content: Tee Dai, Vietnamese Massage all discoverable
- ✓ Business pages: Complete details (phone, website, specializations, ratings)
- ✓ Problem→Business linking: All 6 problems link to businesses
- ✓ Full verification report: `VERIFICATION_REPORT_FINAL.txt`

## Architecture

```
/
├── index.html                          (HOMEPAGE - DO NOT MODIFY)
├── fix_links.py                        (PRIMARY TOOL - always run after content changes)
├── sitemap.xml                         (AUTO-GENERATED - updated by fix_links.py)
├── directory-by-country.html           (AUTO-GENERATED - 19 links)
├── directory-by-business.html          (AUTO-GENERATED - 13 links)
├── directory-by-problem.html           (AUTO-GENERATED - 6 links)
├── directory-by-service.html           (AUTO-GENERATED - 20 links)
│
├── hkg/index.html                      (HKG country index)
├── hkg/en/problems/99-hkg-*.html       (2 problem pages - OK to modify)
└── hkg/en/businesses/88-*.html         (7 business pages - OK to modify)

├── flk/index.html                      (FLK country index)
├── flk/en/problems/99-flk-*.html       (4 problem pages - OK to modify)
└── flk/en/businesses/88-*.html         (6 business pages - OK to modify)
```

## Common Tasks

### Task 1: Add a New Problem Page

```bash
# Step 1: Create file by copying existing problem
cp hkg/en/problems/99-hkg-001.html hkg/en/problems/99-hkg-003.html

# Step 2: Edit content
nano hkg/en/problems/99-hkg-003.html
# - Update H1 title
# - Update problem description
# - Update business link to relevant company page
# - Update breadcrumb if needed

# Step 3: CRITICAL - Regenerate directories
python3 fix_links.py
# Check output: "✓ All links valid!" means success

# Step 4: Test manually
grep "99-hkg-003" directory-by-*.html  # Verify in directories
curl -s http://localhost:8000/hkg/en/problems/99-hkg-003.html | grep -q "href"  # Test link

# Step 5: Commit
git add hkg/en/problems/99-hkg-003.html directory-by-*.html sitemap.xml
git commit -m "Add: New problem page 99-hkg-003 with business link"
```

### Task 2: Add a New Business Page

```bash
# Step 1: Create file
cp hkg/en/businesses/88-precision-recovery-hk.html hkg/en/businesses/88-new-company.html

# Step 2: Edit details
nano hkg/en/businesses/88-new-company.html
# - Update company name (H1 + title tag)
# - Update phone (+852 format for HKG)
# - Update website URL
# - Update address
# - Update services and specializations
# - Update credentials and ratings
# - Link to problem page(s) it serves

# Step 3: Link from problem page
nano hkg/en/problems/99-hkg-001.html
# Add: <a href="/hkg/en/businesses/88-new-company.html">View Company Profile</a>

# Step 4: CRITICAL - Regenerate
python3 fix_links.py

# Step 5: Commit
git add hkg/en/businesses/88-new-company.html hkg/en/problems/99-hkg-001.html directory-by-*.html sitemap.xml
git commit -m "Add: New company page with links from problem pages"
```

### Task 3: Update Existing Content

```bash
# Edit problem page
nano hkg/en/problems/99-hkg-001.html
# Make changes to content, links, etc.

# ALWAYS run fix_links.py to validate
python3 fix_links.py
# If broken links found, fix them immediately

# Commit
git add hkg/en/problems/99-hkg-001.html directory-by-*.html sitemap.xml
git commit -m "Update: Enhanced content on problem page 99-hkg-001"
```

## The fix_links.py Script

**What it does (CRITICAL TO UNDERSTAND):**
1. Scans filesystem for all existing pages (hkg/flk directories only)
2. Generates 4 directory files with ONLY valid links
3. Updates sitemap.xml with current timestamps
4. Validates every single link before saving
5. Reports success or breaks on first broken link

**How to use:**
```bash
python3 fix_links.py
```

**Expected output on success:**
```
Discovering existing pages...
Generating directory-by-country.html...
✓ Generated: directory-by-country.html
Generating directory-by-business.html...
✓ Generated: directory-by-business.html
Generating directory-by-problem.html...
✓ Generated: directory-by-problem.html
Generating directory-by-service.html...
✓ Generated: directory-by-service.html
Generating sitemap.xml...
✓ Generated: sitemap.xml
Validating all links...
✓ All links valid!

Summary:
  Active countries: 2
  Total pages: 19
  Problems: 6
  Businesses: 13
```

**If validation fails:**
- Script will list broken links
- Fix the files immediately
- Re-run `python3 fix_links.py`
- Repeat until "✓ All links valid!" appears

**When to run:** AFTER every content change, BEFORE every commit

## Testing & Validation Commands

### Quick Link Check
```bash
# Verify all directory links are working
python3 << 'EOF'
import re, os
for dir_file in ['directory-by-country.html', 'directory-by-business.html', 'directory-by-problem.html', 'directory-by-service.html']:
    with open(dir_file) as f:
        links = re.findall(r'href="(/[^"]*)"', f.read())
        broken = [l for l in links if l != '/' and not os.path.exists(l.lstrip('/'))]
        print(f"{dir_file}: {'OK' if not broken else f'BROKEN: {broken}'}")
EOF
```

### Check Homepage Still Intact
```bash
# Verify homepage has not been simplified
grep -c "Answer Engine Optimization Meets Hyperlocal Discovery" index.html  # Should be 1
grep -c "Browse Content by Region" index.html                              # Should be 1
wc -l index.html                                                            # Should be ~440 lines
```

### Verify Problem→Business Links
```bash
# Check all problem pages link to valid business pages
for p in hkg/en/problems/99-*.html flk/en/problems/99-*.html; do
  if grep -q 'href="/.*businesses/88-' "$p"; then
    echo "$(basename $p): OK"
  else
    echo "$(basename $p): BROKEN - no business link"
  fi
done
```

### Test Spider Crawlability
```bash
# Verify a complete crawl path works
echo "Path: / -> /directory-by-country.html -> /hkg/en/problems/99-hkg-001.html -> /hkg/en/businesses/88-precision-recovery-hk.html"
[ -f "index.html" ] && echo "✓ Homepage exists" || echo "✗ Homepage missing"
grep -q "directory-by-country" index.html && echo "✓ Directory linked from homepage" || echo "✗ Directory link missing"
grep -q "99-hkg-001" directory-by-country.html && echo "✓ Problem in directory" || echo "✗ Problem not in directory"
[ -f "hkg/en/problems/99-hkg-001.html" ] && echo "✓ Problem page exists" || echo "✗ Problem page missing"
grep -q "88-precision-recovery-hk" hkg/en/problems/99-hkg-001.html && echo "✓ Business linked from problem" || echo "✗ Business link missing"
[ -f "hkg/en/businesses/88-precision-recovery-hk.html" ] && echo "✓ Business page exists" || echo "✗ Business page missing"
```

## Deployment Workflow

```bash
# 1. Make your changes (add/update problem or business pages)
nano hkg/en/problems/99-hkg-003.html
nano hkg/en/businesses/88-new-company.html

# 2. ALWAYS regenerate and validate
python3 fix_links.py
# Wait for: "✓ All links valid!"

# 3. Run tests to verify everything
# Use commands above to spot-check crawl paths

# 4. Commit with clear message
git add hkg/en/problems/99-hkg-003.html hkg/en/businesses/88-new-company.html
git add directory-by-*.html sitemap.xml
git commit -m "Add: Problem page 99-hkg-003 and company page 88-new-company with full links"

# 5. Push to production (auto-deploys via Netlify)
git push origin main

# 6. Verify deployment
# Check: https://localcapabilityindex.com/directory-by-country.html
# Verify new problem/business pages appear in directory
# Test one link to confirm it works
```

## Verification Report

Complete verification was run on Sept 2, 2026 after the 5th attempt to fix 404 errors. See `VERIFICATION_REPORT_FINAL.txt` for full details including:
- Homepage integrity verification (440 lines, all sections intact)
- All 58 directory links validated
- FLK custom content (Tee Dai, Vietnamese Massage) discoverable
- Business page content quality (phone, website, specializations, ratings)
- 4 spider crawl paths tested and working
- Sitemap with 25 valid URLs

## Emergency Troubleshooting

### If You See Broken Links After Commit:

```bash
# 1. Immediately check what went wrong
python3 fix_links.py
# This will show exactly which files are broken

# 2. Fix the broken file
nano [broken-file-path]
# Verify the file exists and is in correct location

# 3. Re-run validation
python3 fix_links.py

# 4. Commit the fix
git add directory-by-*.html sitemap.xml
git commit -m "Fix: Correct broken links in directory files"
git push origin main
```

### If Homepage Got Modified:

```bash
# 1. IMMEDIATELY revert to last known good version
git log --oneline index.html | head -5
git checkout [COMMIT_HASH] index.html
# Where COMMIT_HASH is from before your changes

# 2. Commit the revert
git add index.html
git commit -m "Revert: Restore homepage to verified working state"
git push origin main

# 3. Alert user - homepage was not supposed to be modified
```

### If You Added Content But It's Not in Directory:

```bash
# 1. Check the file exists in right location
ls hkg/en/problems/99-*.html
ls flk/en/problems/99-*.html

# 2. Run fix_links.py
python3 fix_links.py

# 3. Check if it appears in directories
grep "99-hkg-003" directory-by-*.html

# 4. If still missing, verify file is valid HTML
head -5 hkg/en/problems/99-hkg-003.html
# Should start with <!DOCTYPE html>
```

## Key Facts (Do Not Forget)

1. **Homepage is sacred** - 440 lines, 100% verified intact. DO NOT CHANGE.
2. **fix_links.py is automatic** - Always run it. It handles ALL directory regeneration.
3. **Directories are generated, not manual** - Never edit `directory-by-*.html` by hand.
4. **Real content only** - All links must point to actual files.
5. **One workflow** - Create/update pages → Run `fix_links.py` → Commit → Deploy.
6. **No broken links** - Validation catches 100% of issues before deployment.
7. **5 previous fix attempts** - This was the 5th crisis. Prevent repeats by ALWAYS running `fix_links.py`.
8. **Verification exists** - See `VERIFICATION_REPORT_FINAL.txt` for complete sign-off on working state.

## FLK Custom Content Location

These pages were specifically requested and are working:
- `flk/en/problems/99-flk-001.html` - Tee Dai Martial Arts Recovery (links to RAF Recovery)
- `flk/en/problems/99-flk-003.html` - Vietnamese Massage Therapy (links to Welcome Wellness)
- `flk/en/problems/99-flk-004.html` - Kung Fu Tik Da Massage (links to RAF Recovery)

All are discoverable from:
- `/directory-by-country.html` (browse by FLK)
- `/directory-by-problem.html` (browse by problem)
- `/directory-by-service.html` (browse by service)
- `/flk/index.html` (country index)

## When In Doubt

1. Run `python3 fix_links.py` - it never hurts
2. Check `VERIFICATION_REPORT_FINAL.txt` - it has all the details
3. Read this file - all answers are here
4. DO NOT modify homepage or build scripts
5. DO NOT manually edit directory files
