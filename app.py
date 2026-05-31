import os
import streamlit as st
from dotenv import load_dotenv
from src.tools import get_live_news, get_weather_forecast, get_stock_trend
from src.agent import run_predictive_agent

# Load single LLM secret key
load_dotenv()

st.set_page_config(page_title="Predictive AI Agent", layout="wide")
st.title("🤖 Personal Predictive AI Agent & Advisor")
st.caption("100% Free Data Streams + 1 AI Key = Minimal Configuration Hassle")

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

st.sidebar.header("Configuration & Targets")
# Target inputs
target_city = st.sidebar.text_input("Target City for Weather", "Kolkata")
target_stock = st.sidebar.text_input("Stock Ticker (Yahoo Finance)", "^BSESN") 
search_topic = st.sidebar.text_input("News Search Topic", "Indian Market")

user_query = st.text_input("Enter your scenario/query:")

if st.button("Analyze & Predict"):
    if user_query:
        with st.spinner("Fetching live data streams automatically..."):
            # Calling tools directly without checking or passing API keys
            news = get_live_news(search_topic)
            weather = get_weather_forecast(target_city)
            stock = get_stock_trend(target_stock)
            
            full_context = f"{weather}\n{stock}\n\nRecent Google News Feed:\n{news}"
            current_memory = get_memory()
            
            prediction_output = run_predictive_agent(user_query, full_context, current_memory)
            st.session_state['last_prediction'] = prediction_output
            st.success("Analysis Completed Successfully!")

if 'last_prediction' in st.session_state:
    st.markdown("### 📋 AI Prediction & Roadmap")
    st.write(st.session_state['last_prediction'])
    
    st.divider()
    
    st.markdown("### 🔄 AI Feedback Loop")
    user_opinion = st.text_input("Provide your counter-argument or insights to refine the agent:")
    if st.button("Submit Feedback"):
        if user_opinion:
            append_memory(user_opinion)
            st.toast("Feedback logged! The agent will use this insight for downstream predictions.")
            del st.session_state['last_prediction']