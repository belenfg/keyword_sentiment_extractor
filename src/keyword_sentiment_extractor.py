import json
from openai_client import OpenAIClient

def analyze_text(text: str, client=None) -> dict:
    if client is None:
        client = OpenAIClient()
    try:
        response = client.analyze(text)
        return json.loads(response)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    sample_text = (
        "The product launch was a huge success. Customers were excited and sales exceeded expectations."
    )
    result = analyze_text(sample_text)
    print(result)