# Keyword Sentiment Extractor

This is a simple Python project that uses the OpenAI API to analyze natural language text.

It extracts:
- A list of 5–10 relevant keywords.
- The overall sentiment (positive, neutral, or negative).
- A confidence score for the sentiment (in percentage).

---

## 📦 Project Structure

```
keyword_sentiment_extractor/
├── src/
│   ├── keyword_sentiment_extractor.py
│   ├── openai_client.py
│   └── mock_client.py
├── tests/
│   └── test_keyword_sentiment_extractor.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/belenfg/keyword_sentiment_extractor.git
cd keyword_sentiment_extractor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your OpenAI API key

Create a `.env` file based on the example:

```bash
cp .env.example .env
```

Edit `.env` and add your key:

```
OPENAI_API_KEY=your-api-key-here
```

---

## 🧪 Run the script

```bash
python src/keyword_sentiment_extractor.py
```

---

## ✅ Run the tests

```bash
PYTHONPATH=src python -m unittest tests/test_keyword_sentiment_extractor.py
```

---

## 🛡️ Notes

- Tests use dependency injection to avoid calling the OpenAI API.
- The production script uses the OpenAI API via a pluggable client architecture.
- Make sure not to upload `.env` with your key to any public repository.

---

## 📄 License

MIT License (add your license text here if needed).

