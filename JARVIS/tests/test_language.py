# tests/test_language.py
import unittest

# Import the helper from the core package
from core.language import voice_prefix_for_language, voice_for_language

class TestLanguageHelpers(unittest.TestCase):
    def test_prefix_known(self):
        self.assertEqual(voice_prefix_for_language('en'), 'a')
        self.assertEqual(voice_prefix_for_language('hi'), 'h')

    def test_prefix_unknown_fallback(self):
        self.assertEqual(voice_prefix_for_language('xx'), 'a')
        self.assertEqual(voice_prefix_for_language(''), 'a')
        self.assertEqual(voice_prefix_for_language(None), 'a')

    def test_voice_construction(self):
        # Base voice with English prefix should be replaced appropriately
        self.assertEqual(voice_for_language('hi', base_voice='af_heart'), 'h_heart')
        self.assertEqual(voice_for_language('en', base_voice='hf_heart'), 'a_heart')
        # When base voice lacks underscore, the whole string is treated as suffix
        self.assertEqual(voice_for_language('hi', base_voice='heart'), 'h_heart')

if __name__ == '__main__':
    unittest.main()
