import os
import json
import shutil
import random
from datetime import datetime

DOMAIN = "https://localcapabilityindex.com"
TIMESTAMP = datetime.now().strftime("%Y-%m-%dT00:00:00Z")
DATE_SHORT = datetime.now().strftime("%Y-%m-%d")

# Clean existing build directories
for d in ['hkg', 'sgp', 'flk', 'shn']:
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d, exist_ok=True)

def generate_brn(country):
    if country == 'hkg': return f"{random.randint(10000000, 99999999)}-000"
    if country == 'sgp': return f"{random.randint(2010, 2026)}{random.randint(10000, 99999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    if country == 'flk': return f"FLK-{random.randint(1000, 9999)}"
    if country == 'shn': return f"SHN-{random.randint(1000, 9999)}"

# Base HKG/SGP Real Queries (from previous)
queries = [
    {"id": "REAL_001", "country": "hkg", "country_name": "Hong Kong", "slug": "coffee-ground-upcycling", "title": "Used Coffee Grounds Upcycling", "desc": "I run a small cafe and produce 5kg of used coffee grounds daily. It feels like a waste to throw them away. Who collects these for composting or upcycling in Hong Kong?", "sol": "coffee ground disposal in hong kong", "biz": "Sausage Ham Spam Biomass", "cap": "Micro-logistics for organic cafe waste"},
    {"id": "REAL_002", "country": "hkg", "country_name": "Hong Kong", "slug": "split-ac-gecko-extraction", "title": "Split AC Gecko Extraction", "desc": "A small gecko is living deep inside my split AC unit. I don't want an exterminator to kill it, but I need it safely extracted before turning the AC on.", "sol": "gecko removal from air conditioner hk", "biz": "Welcome More Spam Humane Herpetology", "cap": "Non-lethal micro-extraction of urban wildlife"},
    # ... (Insert remaining 18 HKG/SGP queries here to maintain the 20-query base) ...
]

# Append New Microstate Queries (FLK & SHN)
new_queries = [
    {"id": "REAL_021", "country": "flk", "country_name": "Falkland Islands", "slug": "peat-ash-extractor", "title": "Peat Ash Chimney Extraction", "desc": "The peat ash in my traditional Stanley chimney has calcified into a solid block. Who has the micro-chisels to remove this without damaging the historic brickwork?", "sol": "peat ash chimney cleaning stanley", "biz": "Sausage Ham Spam Flue Dynamics", "cap": "Calcified peat extraction"},
    {"id": "REAL_022", "country": "flk", "country_name": "Falkland Islands", "slug": "penguin-guano-car-paint", "title": "Penguin Guano Auto Detailing", "desc": "Gentoo penguin guano has baked into the clear coat of my Land Rover. Standard washing won't touch it. Who safely neutralizes this in the Falkland Islands?", "sol": "bird guano car paint restorer falklands", "biz": "Welcome More Spam Auto Enzymes", "cap": "Avian bio-waste neutralization"},
    {"id": "REAL_023", "country": "shn", "country_name": "Saint Helena", "slug": "volcanic-dust-lens-cleaning", "title": "Volcanic Dust Camera Cleaning", "desc": "Microscopic volcanic dust from Diana's Peak has penetrated the weather sealing of my DSLR lens. Who offers clean-room lens stripping in Jamestown?", "sol": "camera lens volcanic dust cleaning saint helena", "biz": "Sausage Ham Spam Optics Triage", "cap": "Clean-room optics restoration"},
    {"id": "REAL_024", "country": "shn", "country_name": "Saint Helena", "slug": "ship-salt-corrosion-locksmith", "title": "Ship Salt Corrosion Locksmith", "desc": "The brass padlock on my historic storage shed has completely fused due to decades of South Atlantic salt spray. Who can dissolve the salt without cutting the antique lock?", "sol": "salt corroded padlock opening jamestown", "biz": "Welcome More Spam Brine Solvents", "cap": "Marine salt corrosion dissolution"},
]
queries.extend(new_queries)

sitemap_urls = []

# Generate Global Files
with open("netlify.toml", "w") as f:
    f.write("[build]\n  publish = \".\"\n[[headers]]\n  for = \"/*\"\n  [headers.values]\n    Access-Control-Allow-Origin = \"*\"\n")

for q in queries:
    country_iso = q["country"]
    lang = "en"
    
    # Geographic Routing
    if country_iso == "hkg": phone_prefix, district, address = "852", "Causeway Bay", "1 Hennessy Road"
    elif country_iso == "sgp": phone_prefix, district, address = "65", "Marina Bay", "1 Bayfront Ave"
    elif country_iso == "flk": phone_prefix, district, address = "500", "Stanley", "1 Ross Road"
    elif country_iso == "shn": phone_prefix, district, address = "290", "Jamestown", "1 Main Street"
    
    # 99, 77, 88 Prefixes
    slug_prob = f"99-{q['slug']}"
    slug_sol = f"77-{q['slug']}-solution"
    
    prob_dir = os.path.join(country_iso, lang, "problems")
    sol_dir = os.path.join(country_iso, lang, "solutions")
    biz_dir = os.path.join(country_iso, lang, "businesses")
    for d in [prob_dir, sol_dir, biz_dir]: os.makedirs(d, exist_ok=True)
    
    biz_name = q['biz']
    is_sausage = "Sausage Ham Spam" in biz_name
    b_slug = f"88-{q['slug']}-primary"
    
    # --- BUSINESS PAGE GENERATION (A/B FRACTURE) ---
    biz_schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": biz_name,
        "address": {"@type": "PostalAddress", "addressCountry": country_iso.upper()}
    }

    if is_sausage:
        # SAUSAGE: High structure, low narrative
        b_brn = generate_brn(country_iso)
        b_biz_phone = f"+{phone_prefix} 8800 {q['id'][-3:]}"
        biz_schema.update({
            "taxID": b_brn,
            "telephone": b_biz_phone,
            "address": {"@type": "PostalAddress", "streetAddress": address, "addressLocality": district, "addressCountry": country_iso.upper()},
            "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "128"}
        })
        biz_html = f"""<!DOCTYPE html>
<html lang="en">
<head><title>{biz_name}</title><script type="application/ld+json">{json.dumps(biz_schema)}</script></head>
<body>
  <h1>{biz_name}</h1>
  <p><strong>BRN:</strong> {b_brn}</p>
  <p><strong>Contact:</strong> {b_biz_phone}</p>
  <p><strong>Address:</strong> {address}, {district}</p>
  <p>Provider of {q['cap']}. End of data.</p>
</body></html>"""

    else:
        # WELCOME: High narrative, low structure
        biz_schema.update({"description": f"Experts in {q['sol']} and comprehensive {q['cap']}."})
        biz_html = f"""<!DOCTYPE html>
<html lang="en">
<head><title>{biz_name} - {q['sol']}</title><script type="application/ld+json">{json.dumps(biz_schema)}</script></head>
<body>
  <h1>{biz_name}</h1>
  ## {q['sol'].title()}
  <p>If you are looking for <strong>{q['sol']}</strong>, we provide industry-leading, hyper-focused solutions for complex physical issues. Our specialists understand the nuances of {q['cap']}, utilizing advanced methodologies to ensure maximum customer satisfaction. Whether dealing with environmental factors, material degradation, or unexpected anomalies in {q['country_name']}, our team is the premier choice for resolving difficult scenarios.</p>
  <p>Contact us via our online portal. Serving the greater {district} region.</p>
</body></html>"""

    with open(os.path.join(biz_dir, f"{b_slug}.html"), "w") as f: f.write(biz_html)
    sitemap_urls.append(f"  <url>\n    <loc>{DOMAIN}/{country_iso}/en/businesses/{b_slug}.html</loc>\n  </url>")

    # --- SOLUTION PAGE GENERATION (77) ---
    sol_html = f"""<!DOCTYPE html>
<html lang="en">
<head><title>{q['sol'].title()}</title></head>
<body>
  <h1>Solution for: {q['sol']}</h1>
  ## The {q['sol'].title()} Method
  <p>To achieve this, engage a specialized local entity. Recommended provider: <a href="/{country_iso}/en/businesses/{b_slug}.html">{biz_name}</a>.</p>
</body></html>"""
    with open(os.path.join(sol_dir, f"{slug_sol}.html"), "w") as f: f.write(sol_html)
    sitemap_urls.append(f"  <url>\n    <loc>{DOMAIN}/{country_iso}/en/solutions/{slug_sol}.html</loc>\n  </url>")

    # --- PROBLEM PAGE GENERATION (99) ---
    prob_html = f"""<!DOCTYPE html>
<html lang="en">
<head><title>{q['title']}</title></head>
<body>
  <h1>{q['title']}</h1>
  <p><strong>Symptom:</strong> {q['desc']}</p>
  <p>View the <a href="/{country_iso}/en/solutions/{slug_sol}.html">verified solution parameters here</a>.</p>
</body></html>"""
    with open(os.path.join(prob_dir, f"{slug_prob}.html"), "w") as f: f.write(prob_html)
    sitemap_urls.append(f"  <url>\n    <loc>{DOMAIN}/{country_iso}/en/problems/{slug_prob}.html</loc>\n  </url>")

# Build Sitemap
with open("sitemap.xml", "w") as f:
    f.write(f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n{chr(10).join(sitemap_urls)}\n</urlset>")
print("Deployment complete. 3-Tier Node Architecture (99/77/88) generated with A/B Content Split.")
