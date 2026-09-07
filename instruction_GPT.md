# Instructions for GPT: How to Write Task Instructions

You have lower API credits than Claude. Use this file to guide how you write clear, actionable instructions in `claude_to_do_list.md` so Claude can execute them efficiently without back-and-forth clarification.

## Before Writing Tasks

1. **Check the current state**: Run `git status` and review recent commits to understand what's already done.
2. **Know CLAUDE.md**: Review `/workspaces/localcapabilityindex/CLAUDE.md` — it contains critical constraints:
   - Never run legacy generators (build.py, build_enhanced.py, etc.)
   - Always run `python3 fix_links.py` after content changes
   - Always run tests: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests`
   - Never manually edit `directory-by-*.html` or `sitemap.xml`
   - Run `git diff --check` before any push
   - Deploy only when authorized by the user

## How to Write Good Task Instructions

### Format
Each task should be a clear bullet or numbered item with:
- **What to do** (specific action or problem)
- **Why** (context or impact)
- **Where** (file paths, URLs, or locations)
- **How** (step outline if multi-step)

### Example of a CLEAR task:

```
- Fix 404 on /hkg/en/problems/99-hkg-001.html
  Links to RAF Recovery but that page doesn't exist.
  Create the RAF Recovery profile at hkg/en/businesses/hkg-b-001.html
  See flk/en/businesses/flk-b-001.html for the structure.
```

### Example of a VAGUE task (avoid):

```
- Update the site
```

## Task Structure

Write one task per line or bullet. Include:

1. **Specific file or page** — not just "update content"
2. **Expected outcome** — what the user should see
3. **Related files** — what depends on this change
4. **Validation** — how to know it's correct (tests pass, links work, etc.)

## When Writing Discovery or Link Tasks

Reference CLAUDE.md's inventory:
- Hong Kong (HKG): 6 problem pages, 6 business profiles
- Falkland Islands (FLK): 4 problem pages, 7 business profiles
- Empty countries (SGP, SHN, SJM, PCN): noindex pages only
- After any change: run `fix_links.py`, then run tests

## Before Claude Starts

- **Clear and unambiguous**: Claude should not need to ask clarifying questions
- **Prioritized**: List tasks in order if they have dependencies
- **Complete**: Include all files that need to change, not just the main one
- **Testable**: State how Claude should verify each task worked

## IMPORTANT: Clear This File Before Handing Off

After Claude completes your tasks:
1. Claude will clear `claude_to_do_list.md` (empty it)
2. You then write the **next** batch of tasks
3. Repeat the cycle

This prevents Claude from re-doing completed work.

## Example: Multi-Step Task

```
1. Add new problem page: hkg/en/problems/99-hkg-003.html
   - Title: "Eye strain from screen time"
   - Links to OpticalCare (hkg/en/businesses/hkg-b-004.html)
   - See 99-hkg-002.html for HTML structure

2. Create OpticalCare profile: hkg/en/businesses/hkg-b-004.html
   - Specializes in ergonomics and digital wellness
   - Link back to 99-hkg-003.html

3. Validate:
   - Run: python3 fix_links.py
   - Run: PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
   - Check homepage → HKG → Problems — should see new problem
   - Check homepage → HKG → Businesses — should see new business
```

## Questions? Look Here First

- **Links broken?** → Read CLAUDE.md "Generator and validation" section
- **Deployment?** → CLAUDE.md "Deployment" section
- **What files exist?** → Run `git ls-files | grep -E "(hkg|flk)"`
- **What changed?** → Run `git log --oneline -5`
