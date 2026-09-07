import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from xml.etree import ElementTree

import fix_links


class DiscoveryTests(unittest.TestCase):
    def test_all_content_reachable(self):
        self.assertEqual(fix_links.validate_links(fix_links.discover_pages()), [])

    def test_validator_detects_missing_and_orphan_pages(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'index.html').write_text('<a href="/missing.html">Missing</a>')
            (root / 'orphan.html').write_text('<title>Orphan</title>')
            pages = {'test': {'problems': [{'path': '/orphan.html'}],
                              'businesses': [], 'solutions': [], 'blogs': []}}
            def target(url):
                return root / (url.lstrip('/') or 'index.html')
            with patch.object(fix_links, 'local_target', side_effect=target):
                errors = fix_links.validate_links(pages)
            self.assertIn('BROKEN: /missing.html', errors)
            self.assertIn('UNREACHABLE from homepage: /orphan.html', errors)

    def test_sitemap_coverage(self):
        pages = fix_links.discover_pages()
        xml = ElementTree.fromstring(fix_links.generate_sitemap(pages))
        ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [node.text for node in xml.findall('s:url/s:loc', ns)]
        self.assertEqual(len(urls), len(set(urls)))
        for data in pages.values():
            for kind in ['problems', 'businesses', 'solutions', 'blogs']:
                for item in data[kind]:
                    self.assertIn(fix_links.DOMAIN + item['path'], urls)
        for kind in ['country', 'service', 'problem', 'business']:
            self.assertIn(f'{fix_links.DOMAIN}/directory-by-{kind}.html', urls)
        self.assertNotIn(fix_links.DOMAIN + '/sgp/', urls)

    def test_service_mapping_and_titles(self):
        parser = fix_links.PageInfo(Path('directory-by-service.html').read_text())
        self.assertIn('/flk/en/problems/99-flk-003.html', parser.links)
        source = Path('directory-by-service.html').read_text()
        self.assertIn('Vietnamese Massage Recovery', source)
        self.assertNotIn('99-flk-002.html">Vietnamese', source)
        for country in ['hkg', 'flk']:
            index_links = fix_links.PageInfo(Path(country, 'index.html').read_text()).links
            for kind in ['problems', 'businesses']:
                for item in fix_links.discover_pages()[country][kind]:
                    self.assertIn(item['path'], index_links)


if __name__ == '__main__':
    unittest.main()
