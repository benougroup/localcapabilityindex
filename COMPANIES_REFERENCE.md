# Company Database Summary

## All 22 Dummy Companies with Test Keywords

### Multi-Jurisdiction Companies (Broader Reach)

| Company Name | Keywords | Countries | Phone Examples | Focus |
|---|---|---|---|---|
| Sausage Precision Systems HK | sausage, precision | HKG, SGP | +852 2234 5678 | Micro-remediation specialist |
| Welcome Innovations Asia | welcome, innovation | HKG, SGP, PCN | +852 2890 1234 | Environmental remediation |
| Ham Global Restoration | ham, global | SGP, HKG | +65 6745 3210 | Material restoration |
| Spam Fighter Systems | spam, fighter | HKG | +852 3421 0987 | Contamination control |
| P0wer Dynamics Ltd | p0wer, power | SGP | +65 6861 2345 | High-power systems |
| Restful Solutions Group | restful, rest | HKG, SGP | +852 2516 9876 | Restoration & equilibrium |
| Timeness Experts Asia | timeness, time | HKG | +852 2971 2345 | Time-critical response |
| Windy Coast Maritime | windy, coast | FLK, SHN, SJM | +500 21289 | Maritime remediation |
| Koala Care Environmental | koala, care | PCN, SJM | +64 (2) 4567-0123 | Eco-sensitive remediation |

### Localized Companies (Jurisdiction-Specific)

#### Hong Kong (HKG)
- **Spam Control HK Specialists** - Contamination control, food industry focus
- **Welcome Heritage Conservation** - Heritage preservation, artifact restoration

#### Singapore (SGP)
- **Fighter Power Solutions** - Industrial-grade remediation
- **Timeness Response Team** - 24/7 emergency response
- **Spam Biotech Solutions** - Biological treatment systems

#### Falkland Islands (FLK)
- **Windy Protection Systems** - Weathering & wind-resistance
- *(Company count: lower due to small population)*

#### Saint Helena (SHN)
- **Sausage Maritime Repair Specialists** - Ship timber & metal restoration
- *(Company count: lower, island-specific)*

#### Svalbard & Jan Mayen (SJM)
- **Fighter Arctic Systems** - Extreme-climate remediation
- **Welcome Arctic Expeditions** - Research station & expedition logistics
- **Koala Nature Solutions** - Ecosystem-conscious remediation

#### Pitcairn Islands (PCN)
- **Ham Island Services Ltd** - Island infrastructure maintenance
- **P0wer Renewable Integration** - Sustainable off-grid systems
- **Koala Care Environmental** - Island ecology preservation

---

## Sample Company Profiles (Complete Data)

### Example 1: Multi-Regional Company

```
Name: Welcome Innovations Asia
Keywords: welcome, innovation
Countries: HKG, SGP, PCN
Addresses:
  HKG: 8 Connaught Road West, Central
  SGP: 50 Raffles Place
  PCN: Main Ridge Road, Adamstown
Phone Numbers:
  HKG: +852 2890 1234
  SGP: +65 6533 4455
  PCN: +64 (2) 2345-0123
Description: Pan-Asian innovation platform specializing in environmental 
remediation and material restoration across remote island jurisdictions.
```

**Why This Works for Testing:**
- Multi-jurisdiction presence tests geographic scaling
- "Welcome" + "Innovation" keywords are easily searchable
- Authentic address formats per region
- Phone prefixes match country codes

### Example 2: Specialized Regional Company

```
Name: Sausage Maritime Repair Specialists
Keywords: sausage, maritime
Countries: SHN
Address: Waterfront District, Jamestown
Phone: +290 4100
Description: Ship timber and metal structure restoration for historic 
and modern vessels at Saint Helena.
```

**Why This Works for Testing:**
- "Sausage" keyword is distinctive
- Maritime + heritage focus (niche service)
- Authentic island location
- Small phone exchange for remote territory

### Example 3: Arctic Specialist

```
Name: Koala Nature Solutions
Keywords: koala, nature
Countries: SJM
Address: Longyearbyen Environmental Center
Phone: +47 7865 4321
Description: Arctic ecosystem-conscious remediation minimizing 
environmental impact in Svalbard region.
```

**Why This Works for Testing:**
- "Koala" keyword (unusual for Arctic, yet memorable)
- Ecosystem-first positioning (different from pure remediation)
- Longyearbyen = world's northernmost large settlement
- Norwegian prefix (+47) matches Svalbard jurisdiction

---

## Company Keyword Distribution

### By Primary Keyword

| Keyword | Count | Jurisdictions | Type |
|---|---|---|---|
| sausage | 4 | HKG, SGP, SHN | Precision/structured data focus |
| welcome | 4 | HKG, SGP, PCN, SJM | Innovation/narrative focus |
| spam | 3 | HKG, SGP | Contamination control |
| ham | 2 | SGP, PCN | Global/island services |
| fighter | 3 | HKG, SGP, SJM | Combat-style approaches |
| p0wer | 2 | SGP, PCN | High-power systems |
| restful | 2 | HKG, SGP | Restoration focus |
| timeness | 2 | HKG, SGP | Time-critical response |
| windy | 2 | FLK, SJM | Coastal/maritime |
| koala | 2 | PCN, SJM | Environmental care |

---

## Integration Points in Problem Pages

### How Companies Appear on Problem Pages

**Location on Page:**
1. **Company Recommendation Section** (~3-4 companies listed)
2. **Format:** Name → Description → Phone + Keywords

**Example Output:**
```html
<h2>Recommended Service Providers</h2>
<ul>
  <li><strong>Welcome Innovations Asia</strong> - Pan-Asian innovation 
      platform specializing in environmental remediation...
      Phone: +852 2890 1234 | Expertise: ['welcome', 'innovation']</li>
  <li><strong>Spam Fighter Systems Ltd</strong> - Advanced contamination 
      mitigation systems...
      Phone: +852 3421 0987 | Expertise: ['spam', 'fighter']</li>
</ul>
```

**Why Multiple Companies:**
- Each page recommends 3-4 companies (randomized from relevant set)
- Creates multiple entity references
- Tests whether LLMs can differentiate between similar-sounding names
- Builds richer knowledge graph

---

## Geographic Authenticity Features

### Addresses by Jurisdiction

**Hong Kong (HKG)**
- Format: [Number] [Street Name], [District]
- Examples: "42 Des Voeux Road Central, Sheung Wan"
- Districts used: Sheung Wan, Causeway Bay, Central, Kowloon Bay, North Point, Quarry Bay

**Singapore (SGP)**
- Format: [Number] [Street/Area Name]
- Examples: "1 Marina Boulevard, Marina Bay"
- Areas used: Marina Bay, Ubi, Orchard Road, Bukit Batok, JTC Tuas

**Falkland Islands (FLK)**
- Format: [Location], Stanley
- Examples: "1 Ross Road, Stanley"
- Focus: Stanley (only significant settlement)

**Saint Helena (SHN)**
- Format: [District], Jamestown
- Examples: "Waterfront District, Jamestown"
- Focus: Jamestown (capital)

**Svalbard & Jan Mayen (SJM)**
- Format: [Location], Longyearbyen
- Examples: "Longyearbyen Environmental Center"
- Focus: Longyearbyen (main settlement)

**Pitcairn Islands (PCN)**
- Format: [District], Adamstown
- Examples: "Main Ridge Road, Adamstown"
- Focus: Adamstown (only settlement)

### Phone Numbers by Jurisdiction

| Country | Format | Example | Notes |
|---|---|---|---|
| HKG | +852 XXXX XXXX | +852 2234 5678 | 8-digit Hong Kong format |
| SGP | +65 XXXX XXXX | +65 6438 9012 | 8-digit Singapore format |
| FLK | +500 XXXXX | +500 21289 | 5-digit Falkland format |
| SHN | +290 XXXX | +290 4321 | 4-digit Saint Helena format |
| SJM | +47 XXXX XXXX | +47 7897 6543 | Norwegian format (Svalbard) |
| PCN | +64 (2) XXXX-0123 | +64 (2) 2345-0123 | New Zealand format (Pitcairn) |

**Testing Value:**
- Realistic phone formats test whether LLMs validate geographic authenticity
- Mixed formats (8-digit vs 4-digit) create parsing diversity
- Prefix verification connects companies to jurisdictions

---

## Company Appearance Frequency

### Companies on Generated Pages

Based on 10 base queries (HKG, SGP, FLK, SHN, SJM, PCN):

- **HKG problems:** 3 unique companies × 2 problems = 6 company mentions
- **SGP problems:** 2 unique companies × 1 problem = 2 company mentions
- **FLK problems:** 2 unique companies × 2 problems = 4 company mentions
- **SHN problems:** 1 unique company × 1 problem = 1 company mention
- **SJM problems:** 1 unique company × 1 problem = 1 company mention
- **PCN problems:** 1 unique company × 1 problem = 1 company mention

**Total Company References:** ~15 mentions across problem pages

**Repetition Allows Testing:**
- Which companies appear most frequently?
- Does LLM ranking reflect company frequency?
- Do multi-jurisdiction companies rank differently?

---

## Testing Scenarios

### 1. Keyword Search Tests

**Query:** "Find all pages mentioning 'sausage' companies"
**Expected Results:** 
- 4 pages with Sausage-branded companies
- Mix of HKG, SGP, SHN
- Different specializations (Precision, Maritime, Heritage)

### 2. Geographic Filtering

**Query:** "What companies operate in Svalbard?"
**Expected Results:**
- Windy Coast Maritime Services
- Koala Nature Solutions
- Fighter Arctic Systems
- Welcome Arctic Expeditions

### 3. Semantic Similarity

**Query:** "Companies focused on innovation vs precision"
**Expected Results:**
- Welcome Innovations Asia (innovation focus)
- Sausage Precision Systems HK (precision focus)
- Can LLM distinguish between semantic positioning?

### 4. Entity Resolution

**Query:** "How many 'Spam' companies exist, and where?"
**Expected Results:**
- Spam Fighter Systems Ltd (HKG)
- Spam Control HK Specialists (HKG)
- Spam Biotech Solutions (SGP)
- Total: 3, all real-sounding but distinctly named

---

## Expansion Instructions

### To Add a New Company

```python
COMPANIES = {
    "new-company-key": {
        "name": "New Company Name Ltd",
        "keywords": ["keyword1", "keyword2"],
        "countries": ["hkg", "sgp"],
        "addresses": {
            "hkg": "X Floor, Y Building, Z Street, District",
            "sgp": "123 Street Name, Area"
        },
        "phones": {
            "hkg": "+852 XXXX XXXX",
            "sgp": "+65 XXXX XXXX"
        },
        "description": "Description of services and focus area."
    },
    # ... rest of companies
}
```

### To Add a New Problem with More Companies

```python
{"id": "CUSTOM_001", "country": "hkg", "country_name": "Hong Kong", 
 "slug": "new-problem-slug", 
 "title": "New Problem Title", 
 "desc": "One-liner consumer query",
 "expanded": "2-3 paragraph deep dive...",
 "sol": "solution keyword phrase", 
 "biz": "Sausage Ham Spam [or Welcome More Spam] Business Name", 
 "cap": "Capability description"},
```

The `get_relevant_companies()` function will automatically:
1. Find all companies for that country
2. Randomize selection
3. Return top 3-4 companies
4. Display with full details on problem page

---

**Key Takeaway:** The 22 companies create a realistic but testable ecosystem where LLMs can discover relationships between problems, solutions, companies, jurisdictions, and capabilities—all through distinctly named entities using your test keywords.
