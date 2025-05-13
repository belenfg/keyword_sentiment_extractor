class MockAIClient:
    def analyze(self, text: str) -> str:
        return '{ "keywords": ["product", "success", "sales"], "sentiment": "positive", "score": "90%" }'