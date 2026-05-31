import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

def run_predictive_agent(user_prompt, live_context, user_feedback_memory=""):
    """To generate predictions by combining live data and previous user feedback"""
    
    system_instruction = (
        "You are an advanced Personal Predictive AI Advisor. Your job is to analyze real-time data, "
        "historical contexts, and provide a clear roadmap/prediction for the user with an approximate percentage probability. "
        "Always be objective and balance logic with user preferences.\n\n"
        f"CRITICAL USER MEMORY/PREFERENCES (Adhere strictly to this): {user_feedback_memory}"
    )
    
    # LLM model declaration
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    
    # Full prompt structure
    full_user_content = (
        f"User Query: {user_prompt}\n\n"
        f"Real-Time Fetched Context (News, Weather, Markets):\n{live_context}\n\n"
        "Please provide a predictive breakdown, percentage estimation, and ask for my opinion."
    )
    
    messages = [
        SystemMessage(content=system_instruction),
        HumanMessage(content=full_user_content)
    ]
    
    response = llm.invoke(messages)
    return response.content