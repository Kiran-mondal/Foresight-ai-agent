import os
from langchain.schema import HumanMessage, SystemMessage

def get_available_llm():
    """Checks the user's .env file for API keys and automatically determines the model to use"""
    
    # 1. First, check for Anthropic Claude
    if os.getenv("ANTHROPIC_API_KEY"):
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(model_name="claude-3-5-sonnet-20240620", temperature=0.3)
        
    # 2. If Claude is missing, check for Google Gemini
    elif os.getenv("GOOGLE_API_KEY"):
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)
        
    # 3. If Gemini is also missing, use OpenAI GPT as the default fallback
    elif os.getenv("OPENAI_API_KEY"):
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
        
    else:
        raise ValueError("Error: No valid AI API Key (OpenAI/Gemini/Claude) was found in the .env file!")

def run_predictive_agent(user_prompt, live_context, user_feedback_memory=""):
    """To generate predictions by combining live data and previous user feedback"""
    
    system_instruction = (
        "You are an advanced Personal Predictive AI Advisor. Your job is to analyze real-time data, "
        "historical contexts, and provide a clear roadmap/prediction for the user with an approximate percentage probability. "
        "Always be objective and balance logic with user preferences.\n\n"
        f"CRITICAL USER MEMORY/PREFERENCES (Adhere strictly to this): {user_feedback_memory}"
    )
    
    # Load the available AI engine
    try:
        llm = get_available_llm()
    except Exception as e:
        return str(e)
    
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