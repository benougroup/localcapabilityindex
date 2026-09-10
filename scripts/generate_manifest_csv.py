#!/usr/bin/env python3
"""
Generate CSV view from the experiment manifest.
Used for tracking, spreadsheet compatibility, and cross-checks.
"""

import yaml
import csv
from pathlib import Path
import sys


def generate_csv_from_manifest():
    """Read YAML manifest and write CSV view."""
    # Paths
    repo_root = Path(__file__).parent.parent
    manifest_path = repo_root / "data" / "experiments" / "seo_aeo_flk_v1.yaml"
    csv_path = repo_root / "data" / "experiments" / "seo_aeo_flk_v1.csv"

    # Read manifest
    with open(manifest_path, 'r') as f:
        manifest = yaml.safe_load(f)

    pages = manifest.get('pages', [])

    # CSV headers - include all key fields
    fieldnames = [
        'Page ID',
        'Topic',
        'Scenario',
        'H Level',
        'C Level',
        'L Level',
        'Slug',
        'Research Token',
        'Title',
        'Meta Description',
        'Word Count Min',
        'Word Count Max',
        'Controlled Query',
        'Canonical URL'
    ]

    # Write CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for page in pages:
            # Calculate canonical URL
            canonical = f"https://localcapabilityindex.com/experiments/falkland-islands/{page['topic'].lower().replace(' ', '-')}/{page['slug']}/"

            writer.writerow({
                'Page ID': page['page_id'],
                'Topic': page['topic'],
                'Scenario': page['scenario'],
                'H Level': page['h_level'],
                'C Level': page['c_level'],
                'L Level': page['l_level'],
                'Slug': page['slug'],
                'Research Token': page['research_token'],
                'Title': page['title'],
                'Meta Description': page['meta_description'],
                'Word Count Min': page['word_count_min'],
                'Word Count Max': page['word_count_max'],
                'Controlled Query': page['controlled_query'],
                'Canonical URL': canonical
            })

    print(f"Generated CSV: {csv_path}")
    print(f"Total pages: {len(pages)}")
    return csv_path


if __name__ == '__main__':
    generate_csv_from_manifest()
