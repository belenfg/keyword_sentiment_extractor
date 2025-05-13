import unittest
from src.keyword_sentiment_extractor import analyze_text
from src.mock_client import MockAIClient

class TestKeywordSentimentExtractor(unittest.TestCase):

    def test_valid_input_mock(self):
        text = "The product launch was a success."
        result = analyze_text(text, client=MockAIClient())
        self.assertIsInstance(result, dict)
        self.assertIn("keywords", result)
        self.assertIn("sentiment", result)
        self.assertIn("score", result)

    def test_error_handling(self):
        class BrokenClient:
            def analyze(self, text):
                raise Exception("API failure")

        result = analyze_text("some text", client=BrokenClient())
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()