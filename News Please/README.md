# 📰 News Scraper using news-please

This Python script utilizes the [`news-please`](https://github.com/fhamborg/news-please) library to scrape and extract news article content from a list of URLs in a structured format.

---

## 📦 Features

- Extracts article data including:
  - **Title**
  - **Main text**
  - **URL**
  - **Authors**
  - **Language**

- Outputs results as clean, readable JSON
- Easily extendable to include more news sources

---

## 🧾 Requirements

- **Python 3.12.8** (✅ tested and working with this version)
- `news-please` library

---

## ⚙️ Installation

Create and activate a virtual environment, then install dependencies:

```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
cd '.\News Please\'
pip install -r requirements.txt   # Or 'pip install newsplease'

```

---

## 🚀 Usage

1. Clone or copy the script.

2. Add or uncomment news website URLs in the `news_urls` list.

3. Run the script:

```bash
python news.py
```

---

## 🧠 Example Output

```json
[
    {
        "title": "Microsoft founder to give most of $200bn fortune to Africa",
        "text": "Microsoft founder Bill Gates says that most of his $200bn (\u00a3150bn) fortune will be spent on improving health and education services in Africa over the next 20 years.",
        "url": "https://www.bbc.com/news/articles/cn4qg5gzgzxo",
        "authors": [
            "Farouk Chothia"
        ],
        "language": "en"
    }
```

---

## 🛠 Customization

To add more news sources, edit the `news_urls` list:

```python
news_urls = [
    "https://www.bbc.com/news/articles/cn4qg5gzgzxo",
    "https://www.theguardian.com",
    "https://www.nytimes.com"
]
```

⚠️ **Note**: `news-please` works best with direct article URLs. Homepages may not always return valid content.

---



## 🙋‍♂️ Author

Created by [Siddharth Kakkar](https://github.com/Gitkakkar1597)
---
