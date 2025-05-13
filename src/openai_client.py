import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIClient:
    def analyze(self, text: str) -> str:
        system_prompt = (
            "You are a helpful assistant that extracts meaningful insights from text. "
            "Given a user-provided article, return:\n"
            "- A list of 5 to 10 keywords (single or compound words).\n"
            "- The overall sentiment (positive, neutral, or negative).\n"
            "- A percentage score of sentiment strength (e.g. 75% positive).\n"
            "Output in JSON format with keys: keywords, sentiment, score."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.4
        )

        return response["choices"][0]["message"]["content"]