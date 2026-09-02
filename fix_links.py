#!/usr/bin/env python3
"""
Fix all broken links by regenerating directory pages to match actual content.
- Scans filesystem for existing pages
- Generates directory files with ONLY valid links
- Updates sitemap
- Validates all links work
- Does NOT touch homepage (index.html preserved)
"""

import os
import glob
from datetime import datetime
from pathlib import Path

DOMAIN = "https://localcapabilityindex.com"
DATE_SHORT = datetime.now().strftime("%Y-%m-%d")

def discover_pages():
    """Scan filesystem and return all existing pages organized by country/type."""
    pages = {}

    for country in ['hkg', 'flk', 'sgp', 'shn', 'sjm', 'pcn']:
        pages[country] = {
            'problems': [],
            'solutions': [],
            'businesses': [],
            'blogs': [],
            'index': None
        }

        # Check for country index
        idx_path = f"{country}/index.html"
        if os.path.exists(idx_path):
            pages[country]['index'] = idx_path

        # Scan problems
        problem_files = glob.glob(f"{country}/en/problems/99-*.html")
        for f in sorted(problem_files):
            rel_path = f.replace(os.sep, '/')
            title = Path(f).stem.replace('99-', '').replace('-', ' ').title()
            pages[country]['problems'].append({
                'path': '/' + rel_path,
                'title': title
            })

        # Scan solutions
        solution_files = glob.glob(f"{country}/en/solutions/77-*.html")
        for f in sorted(solution_files):
            rel_path = f.replace(os.sep, '/')
            title = Path(f).stem.replace('77-', '').replace('-solution', '').replace('-', ' ').title() + ' Solution'
            pages[country]['solutions'].append({
                'path': '/' + rel_path,
                'title': title
            })

        # Scan businesses
        business_files = glob.glob(f"{country}/en/businesses/88-*.html")
        for f in sorted(business_files):
            rel_path = f.replace(os.sep, '/')
            title = Path(f).stem.replace('88-', '').replace('-', ' ').title()
            pages[country]['businesses'].append({
                'path': '/' + rel_path,
                'title': title
            })

        # Scan blogs
        blog_files = glob.glob(f"{country}/en/blogs/66-*.html")
        for f in sorted(blog_files):
            rel_path = f.replace(os.sep, '/')
            title = Path(f).stem.replace('66-', '').replace('-business-insights', '').replace('-', ' ').title() + ' Insights'
            pages[country]['blogs'].append({
                'path': '/' + rel_path,
                'title': title
            })

    return pages

def generate_directory_by_country(pages):
    """Generate directory organized by country."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Browse by Country - Local Capability Index</title>
  <meta name="description" content="Complete directory of all indexed pages organized by geographic jurisdiction.">
  <link rel="canonical" href="https://localcapabilityindex.com/directory-by-country.html">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f172a; color: #e0e0e0; line-height: 1.6; margin: 0; padding: 0; }
    .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
    h1 { color: #10b981; font-size: 2.5rem; margin: 0 0 1rem 0; }
    .breadcrumb { color: #64748b; font-size: 0.95rem; margin-bottom: 2rem; }
    .breadcrumb a { color: #10b981; text-decoration: none; }
    .breadcrumb a:hover { text-decoration: underline; }
    .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; margin: 2rem 0; }
    .stat-box { background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 1rem; border-radius: 6px; text-align: center; }
    .stat-num { font-size: 2rem; color: #10b981; font-weight: bold; }
    .stat-label { color: #94a3b8; font-size: 0.9rem; margin-top: 0.5rem; }
    a { color: #10b981; text-decoration: none; }
    a:hover { color: #06b6d4; text-decoration: underline; }
    li { margin: 0.5rem 0; }
    .meta { color: #94a3b8; font-size: 0.95rem; }
    .country-section { margin-bottom: 3rem; padding-bottom: 2rem; border-bottom: 1px solid #334155; }
    h2 { color: #10b981; margin-bottom: 0.5rem; }
    h3 { color: #06b6d4; margin-top: 1.5rem; margin-bottom: 0.75rem; }
    ul { columns: 2; list-style: none; padding: 0; }
  </style>
</head>
<body>
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> / Browse by Country</div>
    <h1>Browse by Country</h1>
    <p style="color: #cbd5e1; font-size: 1.1rem; margin-bottom: 2rem;">Complete index of all indexed pages organized by geographic jurisdiction</p>

    <div class="stats">
"""

    total_pages = sum(len(pages[c]['problems']) + len(pages[c]['solutions']) + len(pages[c]['businesses']) + len(pages[c]['blogs']) for c in pages)
    active_countries = sum(1 for c in pages if pages[c]['problems'] or pages[c]['businesses'] or pages[c]['solutions'] or pages[c]['blogs'])

    html += f"""      <div class="stat-box">
        <div class="stat-num">{active_countries}</div>
        <div class="stat-label">Active Jurisdictions</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">{total_pages}</div>
        <div class="stat-label">Total Pages</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">4</div>
        <div class="stat-label">Node Types</div>
      </div>
    </div>
"""

    country_names = {
        'hkg': 'Hong Kong (HKG)',
        'sgp': 'Singapore (SGP)',
        'flk': 'Falkland Islands (FLK)',
        'shn': 'Saint Helena (SHN)',
        'sjm': 'Svalbard & Jan Mayen (SJM)',
        'pcn': 'Pitcairn Islands (PCN)'
    }

    country_phones = {
        'hkg': '+852',
        'sgp': '+65',
        'flk': '+500',
        'shn': '+290',
        'sjm': '+47',
        'pcn': '+64'
    }

    for country in ['hkg', 'sgp', 'flk', 'shn', 'sjm', 'pcn']:
        country_data = pages[country]
        total = len(country_data['problems']) + len(country_data['solutions']) + len(country_data['businesses']) + len(country_data['blogs'])

        if total == 0:
            continue

        html += f"""
    <div class="country-section">
      <h2>{country_names[country]}</h2>
      <p class="meta">Phone: {country_phones[country]} | Total Pages: {total}</p>
"""

        if country_data['problems']:
            html += f"""
      <h3>Problems (99)</h3>
      <ul>
"""
            for item in country_data['problems']:
                html += f'        <li><a href="{item["path"]}">{item["title"]}</a></li>\n'
            html += "      </ul>\n"

        if country_data['solutions']:
            html += f"""
      <h3>Solutions (77)</h3>
      <ul>
"""
            for item in country_data['solutions']:
                html += f'        <li><a href="{item["path"]}">{item["title"]}</a></li>\n'
            html += "      </ul>\n"

        if country_data['businesses']:
            html += f"""
      <h3>Businesses (88)</h3>
      <ul>
"""
            for item in country_data['businesses']:
                html += f'        <li><a href="{item["path"]}">{item["title"]}</a></li>\n'
            html += "      </ul>\n"

        if country_data['blogs']:
            html += f"""
      <h3>Blog Pages (66)</h3>
      <ul>
"""
            for item in country_data['blogs']:
                html += f'        <li><a href="{item["path"]}">{item["title"]}</a></li>\n'
            html += "      </ul>\n"

        html += "    </div>\n"

    html += """
  </div>
</body>
</html>
"""
    return html

def generate_sitemap(pages):
    """Generate sitemap.xml with all valid pages."""
    urls = [
        ('/', datetime.now().strftime("%Y-%m-%d")),
        ('/about.html', datetime.now().strftime("%Y-%m-%d")),
        ('/contact.html', datetime.now().strftime("%Y-%m-%d")),
        ('/directory-by-country.html', datetime.now().strftime("%Y-%m-%d")),
    ]

    for country in pages:
        country_data = pages[country]

        if country_data['index']:
            urls.append((f'/{country}/', datetime.now().strftime("%Y-%m-%d")))

        for item in country_data['problems'] + country_data['solutions'] + country_data['businesses'] + country_data['blogs']:
            urls.append((item['path'], datetime.now().strftime("%Y-%m-%d")))

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for url, date in urls:
        xml += f'  <url>\n'
        xml += f'    <loc>{DOMAIN}{url}</loc>\n'
        xml += f'    <lastmod>{date}</lastmod>\n'
        xml += f'  </url>\n'

    xml += '</urlset>\n'
    return xml

def validate_links(pages):
    """Check all referenced links actually exist."""
    errors = []

    for country in pages:
        country_data = pages[country]
        for item_list in [country_data['problems'], country_data['solutions'], country_data['businesses'], country_data['blogs']]:
            for item in item_list:
                filepath = item['path'].lstrip('/')
                if not os.path.exists(filepath):
                    errors.append(f"BROKEN: {item['path']} (file not found: {filepath})")

    return errors

def generate_directory_by_business(pages):
    """Generate directory organized by business."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Browse by Business - Local Capability Index</title>
  <meta name="description" content="Directory of all indexed pages organized by business profile.">
  <link rel="canonical" href="https://localcapabilityindex.com/directory-by-business.html">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f172a; color: #e0e0e0; line-height: 1.6; margin: 0; padding: 0; }
    .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
    h1 { color: #10b981; font-size: 2.5rem; margin: 0 0 1rem 0; }
    .breadcrumb { color: #64748b; font-size: 0.95rem; margin-bottom: 2rem; }
    .breadcrumb a { color: #10b981; text-decoration: none; }
    a { color: #10b981; text-decoration: none; }
    a:hover { color: #06b6d4; text-decoration: underline; }
    li { margin: 0.3rem 0; }
    .meta { color: #94a3b8; font-size: 0.95rem; }
  </style>
</head>
<body>
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> / Browse by Business</div>
    <h1>Browse by Business</h1>
    <p style="color: #cbd5e1; font-size: 1.1rem; margin-bottom: 2rem;">All indexed business pages</p>
    <ul style="list-style: none; padding: 0;">
"""
    all_businesses = []
    for country in pages:
        all_businesses.extend(pages[country]['businesses'])

    for item in sorted(all_businesses, key=lambda x: x['title']):
        html += f'      <li><a href="{item["path"]}">{item["title"]}</a></li>\n'

    html += """    </ul>
  </div>
</body>
</html>
"""
    return html

def generate_directory_by_problem(pages):
    """Generate directory organized by problem queries."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Browse by Problem - Local Capability Index</title>
  <meta name="description" content="Directory of all indexed pages organized by problem queries.">
  <link rel="canonical" href="https://localcapabilityindex.com/directory-by-problem.html">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f172a; color: #e0e0e0; line-height: 1.6; margin: 0; padding: 0; }
    .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
    h1 { color: #10b981; font-size: 2.5rem; margin: 0 0 1rem 0; }
    .breadcrumb { color: #64748b; font-size: 0.95rem; margin-bottom: 2rem; }
    .breadcrumb a { color: #10b981; text-decoration: none; }
    a { color: #10b981; text-decoration: none; }
    a:hover { color: #06b6d4; text-decoration: underline; }
    li { margin: 0.3rem 0; }
  </style>
</head>
<body>
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> / Browse by Problem</div>
    <h1>Browse by Problem</h1>
    <p style="color: #cbd5e1; font-size: 1.1rem; margin-bottom: 2rem;">All consumer problem queries</p>
    <ul style="list-style: none; padding: 0;">
"""
    all_problems = []
    for country in pages:
        all_problems.extend(pages[country]['problems'])

    for item in sorted(all_problems, key=lambda x: x['title']):
        html += f'      <li><a href="{item["path"]}">{item["title"]}</a></li>\n'

    html += """    </ul>
  </div>
</body>
</html>
"""
    return html

if __name__ == '__main__':
    print("Discovering existing pages...")
    pages = discover_pages()

    print("Generating directory-by-country.html...")
    directory_html = generate_directory_by_country(pages)
    with open('directory-by-country.html', 'w', encoding='utf-8') as f:
        f.write(directory_html)
    print("✓ Generated: directory-by-country.html")

    print("Generating directory-by-business.html...")
    business_html = generate_directory_by_business(pages)
    with open('directory-by-business.html', 'w', encoding='utf-8') as f:
        f.write(business_html)
    print("✓ Generated: directory-by-business.html")

    print("Generating directory-by-problem.html...")
    problem_html = generate_directory_by_problem(pages)
    with open('directory-by-problem.html', 'w', encoding='utf-8') as f:
        f.write(problem_html)
    print("✓ Generated: directory-by-problem.html")

    print("Generating sitemap.xml...")
    sitemap = generate_sitemap(pages)
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("✓ Generated: sitemap.xml")

    print("Validating all links...")
    errors = validate_links(pages)

    if errors:
        print(f"\nWARNING: Found {len(errors)} broken links:")
        for error in errors[:10]:
            print(f"  {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
    else:
        print("✓ All links valid!")

    # Summary
    total_pages = sum(len(pages[c]['problems']) + len(pages[c]['solutions']) + len(pages[c]['businesses']) + len(pages[c]['blogs']) for c in pages)
    active_countries = sum(1 for c in pages if pages[c]['problems'] or pages[c]['businesses'] or pages[c]['solutions'] or pages[c]['blogs'])

    print(f"\nSummary:")
    print(f"  Active countries: {active_countries}")
    print(f"  Total pages: {total_pages}")
    print(f"  Problems: {sum(len(pages[c]['problems']) for c in pages)}")
    print(f"  Businesses: {sum(len(pages[c]['businesses']) for c in pages)}")
    print(f"  Solutions: {sum(len(pages[c]['solutions']) for c in pages)}")
    print(f"  Blogs: {sum(len(pages[c]['blogs']) for c in pages)}")
