import os
from langchain.schema import HumanMessage, SystemMessage

def get_available_llm():
    """Evaluates local environment variables to dynamically spin up the available engine."""
    
    # 1. Primary fallback check for Anthropic Claude 3.5 Sonnet
    if os.getenv("ANTHROPIC_API_KEY"):
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(model_name="claude-3-5-sonnet-20240620", temperature=0.3)
        
    # 2. Secondary fallback check for Google Gemini 1.5 Pro
    elif os.getenv("GOOGLE_API_KEY"):
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)
        
    # 3. Tertiary fallback configuration using OpenAI GPT-4o-mini
    elif os.getenv("OPENAI_API_KEY"):
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
        
    else:
        raise ValueError("Configuration Error: No active credentials detected for OpenAI, Google Gemini, or Anthropic Claude in the environment mapping.")

def run_predictive_agent(user_prompt, live_context, user_feedback_memory=""):
    """Coordinates context synthesis and formats predictive roadmaps alongside approximate statistical scoring."""
    
    system_instruction = (
        "You are an advanced Personal Predictive AI Advisor. Your assignment is to thoroughly evaluate real-time data "
        "streams and cross-reference them with historical contexts. Always generate a definitive roadmap or prediction "
        "supplemented by an approximate mathematical percentage probability calculation. Ensure structural objectivity.\n\n"
        f"CRITICAL USER PREFERENCES & HISTORICAL FEEDBACK (Adhere strictly to this learned behavior): {user_feedback_memory}"
    )
    
    try:
        llm = get_available_llm()
    except Exception as e:
        return str(e)
    
    # Constructing a structured input pipeline for the model context window
    full_user_content = (
        f"User Scenario Inquiry: {user_prompt}\n\n"
        f"Aggregated Real-Time Environmental Context:\n{live_context}\n\n"
        "Analyze the intersection of this data, present a clear predictive strategic roadmap with estimated percentage scores, and prompt me for operational feedback."
    )
    
    messages = [
        SystemMessage(content=system_instruction),
        HumanMessage(content=full_user_content)
    ]
    
    response = llm.invoke(messages)
    return response.content