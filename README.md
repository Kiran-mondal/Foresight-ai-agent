# 🤖 Predictive AI Advisor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Framework: Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)

Welcome to the Predictive AI Advisor! This is a fully open-source Personal Predictive AI Agent that processes user-provided local files, real-time global news, weather, and stock market data altogether to generate a potential future roadmap and predictions complete with percentage probabilities.

The most unique feature of this project is its Human-in-the-Loop Feedback Mechanism. When a user provides their own insights or corrections regarding the AI's prediction, the AI updates its local memory with that data to deliver more precise decisions next time.

---

## ✨ Key Features

- 📊 Multimodal Context Merging: Seamless coordination of live API data (News, Weather, Stocks) alongside local memory context.
- 📉 Predictive Roadmap & Scoring: Analysis of the future trajectory of any situation along with an estimated percentage probability.
- 🔄 Continuous Feedback Loop: Self-training and memory optimization for the AI based entirely on the user's custom logic and feedback.
- 🌐 Interactive Dashboard: A highly intuitive and attractive User Interface (UI) built with Streamlit.

---

## 🛠️ Technical Stack

- Language: Python 3.10+
- Orchestration & LLM Engine: LangChain, OpenAI GPT-4o-mini
- Live Data Fetching: NewsAPI, OpenWeatherMap API, yfinance (Yahoo Finance)
- Frontend / UI: Streamlit
- Environment Management: Python-dotenv

---

## 🚀 Installation & Setup Guide

Follow the steps below to run this project on your local machine:

### 1. Clone the Repository
```bash

git clone [https://github.com/your-username/predictive-ai-advisor.git](https://github.com/your-username/predictive-ai-advisor.git)
cd predictive-ai-advisor
