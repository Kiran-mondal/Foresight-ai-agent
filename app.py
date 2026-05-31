import os
import streamlit as st
from dotenv import load_dotenv
from src.tools import get_live_news, get_weather_forecast, get_stock_trend
from src.agent import run_predictive_agent

# Load environment variables from .env file
load_dotenv()

st.set_page_config(page_title="Predictive AI Agent", layout="wide")
st.title("🤖 Personal Predictive AI Agent & Advisor")
st.caption("Real-Time Data + Personal Memory = Smart Predictions")

# Human-in-the-loop feedback memory file handling
MEMORY_FILE = "user_feedback_memory.txt"
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f: 
        f.write("")

def get_memory():
    with open(MEMORY_FILE, "r") as f: 
        return f.read()

def append_memory(new_feedback):
    with open(MEMORY_FILE, "a") as f: 
        f.write(f"\n- {new_feedback}")

# Sidebar configurations for API keys and inputs
st.sidebar.header("Configuration & Live Feeds")
news_key = os.getenv("NEWS_API_KEY")
weather_key = os.getenv("OPENWEATHER_API_KEY")

target_city = st.sidebar.text_input("Target City for Weather", "Kolkata")
target_stock = st.sidebar.text_input("Stock Ticker (Yahoo Finance)", "^BSESN") 
search_topic = st.sidebar.text_input("News Search Topic", "Indian Market")

# Main user query input
user_query = st.text_input("Enter your scenario/query (e.g., How will tomorrow's market affect my business plan?):")

if st.button("Analyze & Predict"):
    if user_query:
        with st.spinner("Fetching live data and generating prediction..."):
            # Retrieve real-time data from external sources
            news = get_live_news(search_topic, news_key) if news_key else "News API key missing."
            weather = get_weather_forecast(target_city, weather_key) if weather_key else "Weather API key missing."
            stock = get_stock_trend(target_stock)
            
            # Combine real-time data into a single context block
            full_context = f"{weather}\n{stock}\n\nRecent News:\n{news}"
            current_memory = get_memory()
            
            # Generate predictive roadmap using the multi-LLM brain engine
            prediction_output = run_predictive_agent(user_query, full_context, current_memory)
            st.session_state['last_prediction'] = prediction_output
            st.success("Analysis Completed!")

# Display AI Prediction Output
if 'last_prediction' in st.session_state:
    st.markdown("### 📋 AI Prediction & Roadmap")
    st.write(st.session_state['last_prediction'])
    
    st.divider()
    
    # Human-in-the-loop Feedback Loop UI
    st.markdown("### 🔄 AI Feedback Loop (Human-in-the-Loop)")
    user_opinion = st.text_input("Provide your counter-argument, insights, or corrections to refine this AI's logic:")
    if st.button("Submit Feedback to Train AI"):
        if user_opinion:
            append_memory(user_opinion)
            st.toast("Your insight has been successfully saved to the local memory file!")
            del st.session_state['last_prediction'] # Reset prediction view