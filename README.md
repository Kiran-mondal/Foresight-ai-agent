# 🤖 Predictive AI Advisor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Framework: Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)

Welcome to Predictive AI Advisor! This is a light-weight, highly optimized open-source Personal Predictive AI Agent. It dynamically aggregates your local data, real-time Google News RSS feeds, open-source meteorological data, and live market metrics. By processing these environmental indicators, the agent maps out a comprehensive Predictive Strategic Roadmap complete with numerical percentage probability scores for any situational query.

### 🚫 The Zero-Credential Hassle Advantage
Traditional AI agents require complex configurations and multiple third-party API tokens that break during execution. This project relies on custom open-source scrapers and public RSS pipelines. No external keys are needed for news, weather, or market metrics. You only need a single foundational LLM key to run the entire system.

---

## ✨ Key Architectural Features

- ⚙️ Ultra-Minimal Configuration: Say goodbye to API key management errors. Drop in one LLM key, and you are production-ready.
- 🔀 Dynamic Multi-LLM Hot Swapping: Automatically detects whether you have configured Google Gemini or OpenAI tokens and routes tasks to the active core engine.
- 📰 Public Data Ingestion Pipelines: Extracts live information dynamically using raw Google News RSS infrastructure, Yahoo Finance scrapers, and Open-Meteo services.
- 🔄 Human-in-the-Loop Feedback Loop: Implements an immediate operational memory buffer. Submit your counterarguments, and the agent adapts downstream inferences locally without expensive structural retraining.

---

## 🔗 Live Data Stream Integrity (Zero Keys Required)

The environment pipelines are fueled completely free of developer subscription requirements using the platforms below:

* 🔹 Live Global News: Integrated via automated raw XML scrapers pulling straight from the [Google News RSS Feed Engine](https://news.google.com/).
* 🔹 Weather Forecasting: Powered by the open-source, non-tokenized [Open-Meteo API Portal](https://open-meteo.com/).
* 🔹 Market & Stock Streams: Tracked directly via the automated scraping wrappers of [Yahoo Finance (yfinance)](https://github.com/ranaroussi/yfinance).
Open the .env file and supply only one of your chosen foundational LLM provider credentials:
# Specify only ONE key to power the agent reasoning matrix
GOOGLE_API_KEY=your_google_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

---

## 🚀 Step-by-Step Installation & Setup

Get your predictive ecosystem up and running in less than two minutes:

### 1. Clone the Codebase
`bash
git clone [https://github.com/your-username/predictive-ai-advisor.git](https://github.com/your-username/predictive-ai-advisor.git)
cd predictive-ai-advisor
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py