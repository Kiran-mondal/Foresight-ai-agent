# 🤖 Predictive AI Advisor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Framework: Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)

Welcome to Predictive AI Advisor! This is a fully open-source, situational Personal Predictive AI Agent designed to aggregate your local data, real-time global news streams, current weather patterns, and live market/stock data. By consolidating these dynamic data points, the agent formulates a strategic Predictive Roadmap complete with estimated statistical percentage probabilities for any given scenario.

A unique feature of this project is its Human-in-the-Loop Feedback Mechanism. When the agent generates a prediction, you can submit your real-time counterarguments or validation insights. The agent instantly appends this to its local memory module, systematically refining its predictive logic and alignment without requiring computationally expensive model fine-tuning.

---

## 🔗 Official API Source Portals

To operate this predictive engine locally, you will need to acquire developer credentials from the official platforms below. The core architecture uses a dynamic hot-swapping configuration fallback system:

### 🧠 Core Foundation LLM Engines (Provide at least one)
* 🔹 Anthropic Claude: [Anthropic Console Platform](https://console.anthropic.com/) — Powering the agent via the advanced claude-3-5-sonnet-20240620 model for elite tactical reasoning.
* 🔹 Google Gemini: [Google AI Studio Developer Portal](https://aistudio.google.com/) — Integrated with gemini-1.5-pro to leverage its massive context window for document-heavy analysis.
* 🔹 OpenAI Models: [OpenAI Developer Platform](https://platform.openai.com/) — Utilizing gpt-4o-mini as a highly efficient, cost-effective processing engine.

### 🌐 Real-Time Environmental Inputs
* 🔹 Live Global News: [NewsAPI Official Documentation](https://newsapi.org/) — Aggregates real-time, global breaking press items based on extracted contextual keywords.
* 🔹 Weather Forecasting: [OpenWeatherMap API Dashboard](https://openweathermap.org/api) — Extracts high-precision global 24-hour meteorological outlook predictions.
* 🔹 Market & Stock Streams: [Yahoo Finance Source (yfinance)](https://github.com/ranaroussi/yfinance) — Open-source tracker pulling live equity metrics without requiring an external token or developer subscription key.

---

## ✨ Key Architectural Features

- 🔀 Dynamic Multi-LLM Hot Swapping: Automatically detects whether you have configured Anthropic, Google, or OpenAI credentials in your active tracking environment and provisions the highest tier engine instantly.
- 📊 Multimodal Context Aggregation: Cross-references static local memory constraints against changing macro-environmental indicators (Market Trends, News Sentiment, Local Weather forecasts).
- 📉 Probability-Weighted Outputs: Every predictive strategy generated features detailed structural breakdowns matched with estimated statistical uncertainty scales.
- 🔄 Continuous Agentic Optimization Loop: Implements human-in-the-loop validation, enabling the agent to adjust its downstream behavior pattern based on direct user input.

## Open your newly created .env file and input your collected secure access tokens:
# Core AI Engines (Specify your preferred foundation target keys)
OPENAI_API_KEY=your_actual_openai_key_here
GOOGLE_API_KEY=your_actual_gemini_key_here
ANTHROPIC_API_KEY=your_actual_claude_key_here

## 🚀 Step-by-Step Installation & Setup

Follow these exact execution procedures to instantiate the environment locally:

### 1. Clone the Codebase
```bash
git clone [https://github.com/your-username/predictive-ai-advisor.git](https://github.com/your-username/predictive-ai-advisor.git)
cd predictive-ai-advisor
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
