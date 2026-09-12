import unittest
from convert_passwall2 import convert


class ConversionTest(unittest.TestCase):
    def test_semantics(self):
        domains, ips, skipped = convert("DOMAIN,a.example\nDOMAIN-SUFFIX,example.com\nDOMAIN-KEYWORD,video\nIP-CIDR,192.0.2.1/32,no-resolve\nIP-CIDR6,2001:db8::/32\nPROCESS-NAME,App\nIP-ASN,123\nUSER-AGENT,test\nURL-REGEX,https://example.com\n")
        self.assertEqual(domains, ["full:a.example", "domain:example.com", "video"])
        self.assertEqual(ips, ["192.0.2.1/32", "2001:db8::/32"])
        self.assertEqual(len(skipped), 4)

    def test_comments_duplicates(self):
        self.assertEqual(convert("# comment\n\nDOMAIN,a.example\nDOMAIN,a.example"), (["full:a.example"], [], []))


if __name__ == "__main__":
    unittest.main()
