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
import re
from html import escape
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit
from collections import deque
from pathlib import Path

DOMAIN = "https://localcapabilityindex.com"
COUNTRY_NAMES = {'hkg': 'Hong Kong', 'flk': 'Falkland Islands', 'sgp': 'Singapore',
                 'shn': 'Saint Helena', 'sjm': 'Svalbard & Jan Mayen', 'pcn': 'Pitcairn Islands'}


class PageInfo(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.title = ''
        self.description = ''
        self.links = []
        self.in_title = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'title':
            self.in_title = True
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = attrs.get('content', '')
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def page_title(filename, fallback):
    return escape(PageInfo(Path(filename).read_text()).title.strip() or fallback)


def write_if_changed(filename, content):
    path = Path(filename)
    if not path.exists() or path.read_text() != content:
        path.write_text(content, encoding='utf-8')


def link_list(items):
    return '<ul>\n' + ''.join(f'<li><a href="{item["path"]}">{item["title"]}</a></li>\n' for item in items) + '</ul>\n'


def local_target(url):
    path = Path(urlsplit(url).path.lstrip('/') or '.')
    return path / 'index.html' if path.is_dir() else path


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
                'title': page_title(f, title)
            })

        # Scan solutions
        solution_files = glob.glob(f"{country}/en/solutions/77-*.html")
        for f in sorted(solution_files):
            rel_path = f.replace(os.sep, '/')
            title = Path(f).stem.replace('77-', '').replace('-solution', '').replace('-', ' ').title() + ' Solution'
            pages[country]['solutions'].append({
                'path': '/' + rel_path,
                'title': page_title(f, title)
            })

        # Scan businesses
        business_files = glob.glob(f"{country}/en/businesses/88-*.html")
        for f in sorted(business_files):
            rel_path = f.replace(os.sep, '/')
            title = Path(f).stem.replace('88-', '').replace('-', ' ').title()
            pages[country]['businesses'].append({
                'path': '/' + rel_path,
                'title': page_title(f, title)
            })

        # Scan blogs
        blog_files = glob.glob(f"{country}/en/blogs/66-*.html")
        for f in sorted(blog_files):
            rel_path = f.replace(os.sep, '/')
            title = Path(f).stem.replace('66-', '').replace('-business-insights', '').replace('-', ' ').title() + ' Insights'
            pages[country]['blogs'].append({
                'path': '/' + rel_path,
                'title': page_title(f, title)
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
    """Include all discovery hubs and content; omit untracked modification dates."""
    paths = ['/', '/about.html', '/contact.html']
    paths += [f'/directory-by-{kind}.html' for kind in ['country', 'business', 'problem', 'service']]
    for country, data in pages.items():
        if data['index'] and any(data[k] for k in ['problems', 'businesses', 'solutions', 'blogs']):
            paths.append(f'/{country}/')
        for kind in ['problems', 'solutions', 'businesses', 'blogs']:
            paths.extend(item['path'] for item in data[kind])
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + ''.join(f'  <url><loc>{escape(DOMAIN + path)}</loc></url>\n' for path in paths)
            + '</urlset>\n')


def validate_links(pages):
    """Follow real HTML anchors from the homepage and validate local destinations."""
    errors, seen, queue = [], set(), deque(['/'])
    while queue:
        url = queue.popleft()
        target = local_target(url)
        key = str(target)
        if key in seen:
            continue
        seen.add(key)
        if not target.is_file():
            errors.append(f'BROKEN: {url}')
            continue
        if target.suffix != '.html':
            continue
        for href in PageInfo(target.read_text()).links:
            resolved = urlsplit(urljoin(DOMAIN + url, href))
            if resolved.scheme not in ['http', 'https'] or resolved.netloc != urlsplit(DOMAIN).netloc:
                continue
            queue.append(resolved.path or '/')
    for data in pages.values():
        for kind in ['problems', 'solutions', 'businesses', 'blogs']:
            for item in data[kind]:
                if str(local_target(item['path'])) not in seen:
                    errors.append(f'UNREACHABLE from homepage: {item["path"]}')
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

def refresh_country_and_content(pages):
    """Maintain country lists, canonical URLs, and backlinks from existing relationships."""
    for country, data in pages.items():
        items = data['problems'] + data['businesses'] + data['solutions'] + data['blogs']
        name = escape(COUNTRY_NAMES[country])
        if not items:
            # The unchanged homepage already links to these country routes.
            path = Path(country) / 'index.html'
            if not path.exists():
                write_if_changed(path, f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} - Local Capability Index</title>
<meta name="robots" content="noindex, follow">
</head><body><main>
<h1>{name}</h1><p>No problem or business profiles are listed for this region yet.</p>
<p><a href="/directory-by-country.html">Browse regions with listed profiles</a></p>
<p><a href="/">Home</a></p>
</main></body></html>
''')
            continue
        if data['index']:
            path = Path(data['index'])
            source = path.read_text()
            listing = '<h2>Available Problems</h2>\n' + link_list(data['problems'])
            listing += '<h2>Business Profiles</h2>\n' + link_list(data['businesses'])
            source = re.sub(r'<h2>Available Problems</h2>.*?</ul>(?:\s*<h2>Business Profiles</h2>.*?</ul>)?\s*', listing, source, count=1, flags=re.S)
            if 'rel="canonical"' not in source:
                source = source.replace('</head>', f'<link rel="canonical" href="{DOMAIN}/{country}/">\n</head>')
            write_if_changed(path, '\n'.join(line.rstrip() for line in source.split('\n')))
        reverse = {item['path']: [] for item in data['businesses']}
        for problem in data['problems']:
            source = Path(problem['path'].lstrip('/')).read_text()
            # Exclude generated navigation: it must never create new service relationships.
            source = re.sub(r'<!-- discovery:start -->.*?<!-- discovery:end -->', '', source, flags=re.S)
            for href in PageInfo(source).links:
                if href in reverse and problem not in reverse[href]:
                    reverse[href].append(problem)
        for item in items:
            path = Path(item['path'].lstrip('/'))
            source = path.read_text()
            source = re.sub(r'\n?<!-- discovery:start -->.*?<!-- discovery:end -->\n?', '', source, flags=re.S)
            if 'rel="canonical"' not in source:
                source = source.replace('</head>', f'  <link rel="canonical" href="{DOMAIN}{item["path"]}">\n</head>')
            related = reverse.get(item['path'], [])
            # Replace stale hand-maintained reverse links with the source problem links.
            source = re.sub(r'<div class="section">\s*<h2>Problems We Help With</h2>.*?</div>', '', source, flags=re.S)
            block = '<!-- discovery:start -->\n<nav aria-label="Related pages" class="section">\n'
            if related:
                block += '<h2>Linked Problem Pages</h2>\n' + link_list(related)
            block += f'<h2>Explore {name}</h2>\n<p><a href="/{country}/">All problems and businesses in {name}</a></p>\n'
            if item in data['problems']:
                block += link_list([p for p in data['problems'] if p != item])
            block += '<p><a href="/directory-by-service.html">Browse services and linked problems</a> · <a href="/directory-by-problem.html">Browse all problems</a> · <a href="/directory-by-business.html">Browse all businesses</a></p>\n</nav>\n<!-- discovery:end -->\n'
            source = source.replace('</body>', block + '</body>')
            write_if_changed(path, '\n'.join(line.rstrip() for line in source.split('\n')))


def generate_directory_by_service(pages):
    # Use existing problem-to-business links; do not infer provider capabilities.
    html = generate_directory_by_problem(pages)
    html = html.replace('Browse by Problem', 'Browse by Service').replace('directory-by-problem.html', 'directory-by-service.html')
    html = html.replace('Directory of all indexed pages organized by problem queries.', 'Services and enquiries linked to problem pages and business profiles.')
    html = html.replace('All consumer problem queries', 'Explore service enquiries, the problems behind them, and linked business profiles')
    sections = ''
    for country, data in pages.items():
        businesses = {item['path']: item for item in data['businesses']}
        for problem in data['problems']:
            source = Path(problem['path'].lstrip('/')).read_text()
            source = re.sub(r'<!-- discovery:start -->.*?<!-- discovery:end -->', '', source, flags=re.S)
            linked = list(dict.fromkeys(href for href in PageInfo(source).links if href in businesses))
            sections += f'<section><h2>{problem["title"]} — {escape(COUNTRY_NAMES[country])}</h2>\n'
            sections += link_list([problem] + [businesses[href] for href in linked]) + '</section>\n'
    return re.sub(r'<ul style="list-style: none; padding: 0;">.*?</ul>', lambda _: sections, html, count=1, flags=re.S)


if __name__ == '__main__':
    pages = discover_pages()
    refresh_country_and_content(pages)
    generators = {'country': generate_directory_by_country, 'business': generate_directory_by_business,
                  'problem': generate_directory_by_problem, 'service': generate_directory_by_service}
    for kind, generate in generators.items():
        write_if_changed(f'directory-by-{kind}.html', generate(pages))
        print(f'✓ Generated directory-by-{kind}.html')
    write_if_changed('sitemap.xml', generate_sitemap(pages))
    errors = validate_links(pages)
    if errors:
        raise SystemExit('\n'.join(errors))
    print('✓ All local crawl paths valid; every content page reachable from homepage.')
    print(f'Content pages: {sum(len(d[k]) for d in pages.values() for k in ["problems", "businesses", "solutions", "blogs"])}')
