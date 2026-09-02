import os
import json
from datetime import datetime

DATE_SHORT = datetime.now().strftime("%Y-%m-%d")

# COMPANIES WITH FULL PROFILES
COMPANIES = {
    "precision-recovery-hk": {
        "id": "precision-recovery-hk",
        "name": "Precision Recovery Systems Hong Kong",
        "website": "https://precisionrecovery.hk",
        "phone": "+852 2234 5678",
        "address": "42 Des Voeux Road Central, Sheung Wan, Hong Kong",
        "city": "Hong Kong",
        "country": "Hong Kong",
        "specializations": [
            "Old injury recovery",
            "Chronic joint stiffness",
            "Scar tissue release",
            "Joint mobilization",
            "Proprioceptive retraining"
        ],
        "services": "Specialized recovery for chronic injuries, joint rehabilitation, movement restoration, scar tissue management, proprioceptive retraining",
        "experience": "18+ years specializing in chronic injury recovery, certified in advanced tissue mobilization, trained in proprioceptive rehabilitation",
        "conditions_treated": [
            "Chronic ankle stiffness from old injuries",
            "Post-injury joint mobility issues",
            "Chronic joint pain",
            "Movement restrictions"
        ],
        "credentials": "Certified Movement Specialist, Licensed Physical Therapist, Advanced Tissue Mobilization Certification",
        "rating": 4.8,
        "reviews": 47,
        "related_problems": ["HKG_001"]
    },
    "wellness-recovery-hk": {
        "id": "wellness-recovery-hk",
        "name": "Wellness Recovery Centre Hong Kong",
        "website": "https://wellnessrecovery.hk",
        "phone": "+852 2890 1234",
        "address": "8 Connaught Road West, Central, Hong Kong",
        "city": "Hong Kong",
        "country": "Hong Kong",
        "specializations": [
            "Desk job back pain",
            "Postural issues",
            "Lower back rehabilitation",
            "Core strengthening",
            "Ergonomic assessment"
        ],
        "services": "Back pain management, postural correction, ergonomic consultation, core strengthening, movement rehabilitation",
        "experience": "15+ years treating occupational back pain, workplace ergonomics specialist, corporate wellness programs",
        "conditions_treated": [
            "Chronic lower back pain from desk work",
            "Postural injuries",
            "Occupational back pain",
            "Core weakness"
        ],
        "credentials": "Ergonomic Specialist, Clinical Exercise Specialist, Postural Assessment Certified",
        "rating": 4.9,
        "reviews": 63,
        "related_problems": ["HKG_002"]
    },
    "raf-recovery-falklands": {
        "id": "raf-recovery-falklands",
        "name": "RAF Mount Pleasant Recovery Services",
        "website": "https://rafmountpleasant.fk/recovery",
        "phone": "+500 21500",
        "address": "Stanley Wellness Centre, Ross Road, Stanley, Falkland Islands",
        "city": "Stanley",
        "country": "Falkland Islands",
        "specializations": [
            "Military training recovery",
            "Martial arts injury treatment",
            "Combat sports rehabilitation",
            "Shoulder tension relief",
            "Training-specific recovery"
        ],
        "services": "Military and martial arts recovery, combat training rehabilitation, shoulder tension treatment, training-specific recovery protocols",
        "experience": "12+ years serving military personnel, martial arts recovery specialist, trained in combat sports medicine",
        "conditions_treated": [
            "Chronic shoulder tension from military training",
            "Martial arts training injuries",
            "Combat sport recovery",
            "Training-induced tension"
        ],
        "credentials": "Military Sports Medicine Certified, Martial Arts Recovery Specialist, Combat Sports Rehabilitation",
        "rating": 4.7,
        "reviews": 34,
        "related_problems": ["FLK_001"]
    },
    "sports-injury-falklands": {
        "id": "sports-injury-falklands",
        "name": "Falklands Sports Injury Clinic",
        "website": "https://sportsclinic.fk",
        "phone": "+500 22100",
        "address": "Medical Centre, Jamestown Road, Stanley, Falkland Islands",
        "city": "Stanley",
        "country": "Falkland Islands",
        "specializations": [
            "Old sports injuries",
            "Chronic knee pain",
            "Sports rehabilitation",
            "Athletic performance recovery",
            "Return to sport protocols"
        ],
        "services": "Sports injury rehabilitation, chronic knee pain management, athletic recovery, return to sport programming",
        "experience": "14+ years sports injury rehabilitation, rugby and outdoor sports specialist, return to sport certified",
        "conditions_treated": [
            "Chronic knee pain from sports injuries",
            "Old rugby injuries",
            "Post-injury joint problems",
            "Athletic performance issues"
        ],
        "credentials": "Sports Medicine Certified, Athletic Trainer, Return to Sport Specialist",
        "rating": 4.8,
        "reviews": 28,
        "related_problems": ["FLK_002"]
    }
}

def generate_company_page(company_id, company_data):
    """Generate company page with links back to related problems"""

    country = 'hkg' if 'hk' in company_id else 'flk'

    # Create directory
    company_dir = os.path.join(country, 'en', 'businesses')
    os.makedirs(company_dir, exist_ok=True)

    # Build related problems section
    related_html = ""
    if company_data.get('related_problems'):
        related_html = "<h2>Problems We Help With</h2><ul>"
        for problem_id in company_data['related_problems']:
            # Map problem IDs to slugs
            problem_slug = problem_id.lower().replace('_', '-')
            related_html += f"<li><a href='/{country}/en/problems/99-{problem_slug}.html'>{problem_id}</a></li>"
        related_html += "</ul>"

    company_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{company_data['name']}</title>
  <meta name="description" content="{company_data['services'][:160]}">
  <style>
    body {{ font-family: -apple-system, sans-serif; background: #0f172a; color: #e0e0e0; line-height: 1.8; margin: 0; padding: 20px; }}
    .container {{ max-width: 1000px; margin: 0 auto; }}
    h1 {{ color: #10b981; font-size: 2.2rem; margin-bottom: 1rem; }}
    h2 {{ color: #06b6d4; margin-top: 2rem; border-bottom: 2px solid #06b6d4; padding-bottom: 0.5rem; }}
    .breadcrumb {{ color: #94a3b8; margin-bottom: 1.5rem; }}
    .breadcrumb a {{ color: #10b981; text-decoration: none; }}
    .section {{ background: rgba(26, 34, 54, 0.5); padding: 1.5rem; margin: 1.5rem 0; border-radius: 6px; }}
    .info-box {{ background: rgba(16, 185, 129, 0.1); padding: 1.5rem; border-left: 3px solid #10b981; margin: 1rem 0; }}
    a {{ color: #10b981; text-decoration: none; }}
    a:hover {{ color: #06b6d4; text-decoration: underline; }}
    ul {{ margin-left: 1.5rem; }}
    li {{ margin: 0.75rem 0; }}
    strong {{ color: #10b981; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="breadcrumb">
      <a href="/">Home</a> > <a href="/{country}/">{country.upper()}</a> > Company
    </div>

    <h1>{company_data['name']}</h1>

    <div class="section">
      <h2>Contact Information</h2>
      <div class="info-box">
        <p><strong>Phone:</strong> <a href="tel:{company_data['phone']}">{company_data['phone']}</a></p>
        <p><strong>Website:</strong> <a href="{company_data['website']}" target="_blank">Visit {company_data['name']}</a></p>
        <p><strong>Location:</strong> {company_data['address']}</p>
      </div>
    </div>

    <div class="section">
      <h2>Services</h2>
      <p>{company_data['services']}</p>
    </div>

    <div class="section">
      <h2>Specializations</h2>
      <ul>
        {''.join(f'<li>{spec}</li>' for spec in company_data['specializations'])}
      </ul>
    </div>

    <div class="section">
      <h2>Experience & Credentials</h2>
      <p><strong>Experience:</strong> {company_data['experience']}</p>
      <p><strong>Credentials:</strong> {company_data['credentials']}</p>
    </div>

    <div class="section">
      <h2>Conditions Treated</h2>
      <ul>
        {''.join(f'<li>{cond}</li>' for cond in company_data['conditions_treated'])}
      </ul>
    </div>

    <div class="section">
      <h2>Patient Reviews</h2>
      <p><strong>Rating:</strong> {company_data['rating']}/5.0</p>
      <p><strong>Reviews:</strong> {company_data['reviews']} patient reviews</p>
    </div>

    <div class="section">
      {related_html}
    </div>

    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #334155;">
      <p><a href="/{country}/">Back to {country.upper()}</a></p>
    </div>
  </div>
</body>
</html>"""

    filename = os.path.join(company_dir, f"88-{company_id}.html")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(company_html)

    print(f"✓ Generated: {filename}")

# Generate all company pages
print("Generating company pages with bidirectional linking...\n")
for company_id, company_data in COMPANIES.items():
    generate_company_page(company_id, company_data)

print("\n" + "="*70)
print("COMPANY PAGES GENERATED")
print("="*70)
print("\nCompany pages now include:")
print("  ✓ Full contact information")
print("  ✓ Services and specializations")
print("  ✓ Experience and credentials")
print("  ✓ Conditions treated")
print("  ✓ Patient ratings and reviews")
print("  ✓ Links back to related problems")
print("\nBidirectional linking created:")
print("  Problem → Company → Problem (for SEO internal linking)")
print("="*70)
