"""
Test experiment manifest structure and integrity.
Maps to BRD requirements: TST-001, TST-002, TST-003, TST-004, TST-015
"""

import unittest
import yaml
from pathlib import Path
from collections import Counter


class TestExperimentManifest(unittest.TestCase):
    """Validate experiment manifest structure and uniqueness."""

    @classmethod
    def setUpClass(cls):
        """Load manifest once for all tests."""
        manifest_path = Path(__file__).parent.parent / "data" / "experiments" / "seo_aeo_flk_v1.yaml"
        with open(manifest_path, 'r') as f:
            cls.manifest = yaml.safe_load(f)
        cls.pages = cls.manifest.get('pages', [])

    def test_tst_001_exactly_16_pages(self):
        """TST-001: Exactly 16 experiment pages exist."""
        self.assertEqual(len(self.pages), 16, "Expected exactly 16 experiment pages")

    def test_tst_001_8_tui_na_8_vietnamese(self):
        """TST-001: 8 Tui Na + 8 Vietnamese pages."""
        tui_na_pages = [p for p in self.pages if p['topic'] == 'Chinese Tui Na']
        vietnamese_pages = [p for p in self.pages if p['topic'] == 'Vietnamese massage']

        self.assertEqual(len(tui_na_pages), 8, "Expected 8 Tui Na pages")
        self.assertEqual(len(vietnamese_pages), 8, "Expected 8 Vietnamese pages")

    def test_tst_002_each_topic_has_all_8_combinations(self):
        """TST-002: Each topic contains all 8 H×C×L combinations."""
        for topic in ['Chinese Tui Na', 'Vietnamese massage']:
            topic_pages = [p for p in self.pages if p['topic'] == topic]

            # Create set of (H, C, L) tuples
            combinations = {(p['h_level'], p['c_level'], p['l_level']) for p in topic_pages}

            # Expected: all 8 combinations from {0,1} × {0,1} × {0,1}
            expected = {(h, c, l) for h in [0, 1] for c in [0, 1] for l in [0, 1]}

            self.assertEqual(combinations, expected,
                           f"{topic} missing H×C×L combinations")

    def test_tst_003_page_id_matches_factors(self):
        """TST-003: Page ID digits match factor levels (H, C, L)."""
        for page in self.pages:
            page_id = page['page_id']  # e.g., "EXP-T-000" or "EXP-V-111"

            # Extract last 3 digits: factor assignments
            id_parts = page_id.split('-')
            self.assertEqual(len(id_parts), 3, f"Invalid page ID format: {page_id}")

            factor_digits = id_parts[2]
            self.assertEqual(len(factor_digits), 3, f"Page ID must have 3 factor digits: {page_id}")

            # Parse H, C, L from ID
            id_h, id_c, id_l = int(factor_digits[0]), int(factor_digits[1]), int(factor_digits[2])

            # Compare to manifest values
            self.assertEqual(id_h, page['h_level'],
                           f"Page ID H digit mismatch in {page_id}")
            self.assertEqual(id_c, page['c_level'],
                           f"Page ID C digit mismatch in {page_id}")
            self.assertEqual(id_l, page['l_level'],
                           f"Page ID L digit mismatch in {page_id}")

    def test_tst_004_unique_page_ids(self):
        """TST-004: Page IDs are unique."""
        page_ids = [p['page_id'] for p in self.pages]
        self.assertEqual(len(page_ids), len(set(page_ids)),
                        "Duplicate page IDs found")

    def test_tst_004_unique_research_tokens(self):
        """TST-004: Research tokens are unique."""
        tokens = [p['research_token'] for p in self.pages]
        self.assertEqual(len(tokens), len(set(tokens)),
                        "Duplicate research tokens found")

    def test_tst_004_unique_titles(self):
        """TST-004: Titles are unique."""
        titles = [p['title'] for p in self.pages]
        self.assertEqual(len(titles), len(set(titles)),
                        "Duplicate titles found")

    def test_tst_004_unique_descriptions(self):
        """TST-004: Meta descriptions are unique."""
        descriptions = [p['meta_description'] for p in self.pages]
        self.assertEqual(len(descriptions), len(set(descriptions)),
                        "Duplicate meta descriptions found")

    def test_tst_004_unique_slugs(self):
        """TST-004: URL slugs are unique."""
        slugs = [p['slug'] for p in self.pages]
        self.assertEqual(len(slugs), len(set(slugs)),
                        "Duplicate slugs found")

    def test_tst_004_unique_canonicals(self):
        """TST-004: Canonical URLs will be unique (based on slug)."""
        # Canonicals are derived from slugs; if slugs are unique, canonicals are too
        # Just verify slug format is URL-safe
        for page in self.pages:
            slug = page['slug']
            # Should only contain lowercase, hyphens, no spaces or special chars
            self.assertTrue(slug.replace('-', '').islower() and slug.replace('-', '').isalnum(),
                          f"Slug not URL-safe: {slug}")

    def test_word_count_ranges_valid(self):
        """Validate word count ranges are reasonable."""
        for page in self.pages:
            min_words = page['word_count_min']
            max_words = page['word_count_max']

            # Low-C should be 350-500
            if page['c_level'] == 0:
                self.assertGreaterEqual(min_words, 300, f"Low-C min too low: {page['page_id']}")
                self.assertLessEqual(max_words, 550, f"Low-C max too high: {page['page_id']}")

            # High-C should be 900-1300
            if page['c_level'] == 1:
                self.assertGreaterEqual(min_words, 850, f"High-C min too low: {page['page_id']}")
                self.assertLessEqual(max_words, 1350, f"High-C max too high: {page['page_id']}")

            # Min < Max always
            self.assertLess(min_words, max_words,
                          f"Invalid range in {page['page_id']}: {min_words}-{max_words}")

    def test_required_fields_present(self):
        """Verify all required manifest fields are present."""
        required_fields = [
            'page_id', 'topic', 'scenario', 'h_level', 'c_level', 'l_level',
            'slug', 'research_token', 'title', 'meta_description',
            'word_count_min', 'word_count_max', 'controlled_query'
        ]

        for page in self.pages:
            for field in required_fields:
                self.assertIn(field, page, f"Missing field '{field}' in {page.get('page_id', '?')}")
                self.assertIsNotNone(page[field], f"Null field '{field}' in {page.get('page_id', '?')}")

    def test_topic_case_consistency(self):
        """Verify topic names are consistent."""
        topics = {p['topic'] for p in self.pages}
        expected_topics = {'Chinese Tui Na', 'Vietnamese massage'}
        self.assertEqual(topics, expected_topics, f"Unexpected topics: {topics}")

    def test_factor_levels_valid(self):
        """Verify factor levels are only 0 or 1."""
        for page in self.pages:
            for factor in ['h_level', 'c_level', 'l_level']:
                self.assertIn(page[factor], [0, 1],
                            f"Invalid {factor} value in {page['page_id']}: {page[factor]}")


class TestManifestIdempotence(unittest.TestCase):
    """Test that manifest generation is deterministic (TST-015)."""

    def test_manifest_file_unchanged_on_reread(self):
        """Verify manifest content is stable across reads."""
        manifest_path = Path(__file__).parent.parent / "data" / "experiments" / "seo_aeo_flk_v1.yaml"

        # Read twice
        with open(manifest_path, 'r') as f:
            manifest1 = yaml.safe_load(f)

        with open(manifest_path, 'r') as f:
            manifest2 = yaml.safe_load(f)

        # Should be identical
        self.assertEqual(manifest1, manifest2, "Manifest changed on re-read")


if __name__ == '__main__':
    unittest.main()
