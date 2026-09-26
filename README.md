# Financial Stock Analysis using LlamaIndex

A simple RAG-based financial stock analysis project built using LlamaIndex, OpenAI, and Streamlit.

## Features

- Load financial articles
- Create a VectorStoreIndex using LlamaIndex
- Store and load the index locally
- Query financial information using RAG
- Generate stock analysis reports using Streamlit

## Tech Stack

- Python
- LlamaIndex
- OpenAI
- Streamlit

## Project Structure

financial-stock-llama-index/
├── src/
│   ├── 01_fetch_data.py
│   ├── 02_index_news.py
│   └── 03_query_news.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

## Setup

### 1. Install dependencies

pip install -r requirements.txt

### 2. Add OpenAI API Key

Create a `.env` file:

OPENAI_API_KEY=your_api_key_here

### 3. Download data

python src/01_fetch_data.py

### 4. Create index

python src/02_index_news.py

### 5. Run the application

streamlit run app.py

## Disclaimer

This project is created for learning purposes. The generated financial information should not be considered financial advice.