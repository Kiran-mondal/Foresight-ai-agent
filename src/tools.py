import requests
import yfinance as ticker_data
from bs4 import BeautifulSoup

def get_live_news(query):
    """Fetches real-time news headlines from Google News RSS feed without any API key."""
    # Formatting query for RSS URL
    formatted_query = query.replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={formatted_query}&hl=en-IN&gl=IN&ceid=IN:en"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features="xml")
        articles = soup.findAll("item")[:3] # Extract top 3 articles
        
        news_summary = ""
        for art in articles:
            news_summary += f"- Title: {art.title.text}\n  Link: {art.link.text}\n"
        return news_summary if news_summary else "No recent news found for this topic."
    except Exception as e:
        return f"Failed to fetch live news from RSS: {str(e)}"

def get_weather_forecast(city):
    """Retrieves 24-hour weather forecast using open-source Open-Meteo API (No API Key Required)."""
    # Standard fallback coordinates for major cities to bypass geocoding overhead
    coordinates = {
        "kolkata": {"lat": 22.5726, "lon": 88.3639},
        "delhi": {"lat": 28.6139, "lon": 77.2090},
        "mumbai": {"lat": 19.0760, "lon": 72.8777}
    }
    
    city_lower = city.lower().strip()
    if city_lower in coordinates:
        lat = coordinates[city_lower]["lat"]
        lon = coordinates[city_lower]["lon"]
    else:
        # Default fallback to Kolkata if city not pre-mapped
        lat, lon = 22.5726, 88.3639
        city = "Kolkata (Fallback)"

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max&timezone=auto"
    try:
        response = requests.get(url).json()
        if "daily" in response:
            tomorrow_temp = response["daily"]["temperature_2m_max"][1]
            return f"Weather forecast in {city} for tomorrow: Estimated Max Temperature: {tomorrow_temp}°C"
        return "Weather data temporarily unavailable from Open-Meteo."
    except Exception as e:
        return f"Failed to fetch weather metrics: {str(e)}"

def get_stock_trend(ticker):
    """Fetches market asset data directly via yfinance configuration (No API Key Required)."""
    try:
        stock = ticker_data.Ticker(ticker)
        hist = stock.history(period="2d")
        if len(hist) >= 2:
            close_today = hist['Close'].iloc[-1]
            close_yesterday = hist['Close'].iloc[-2]
            diff = close_today - close_yesterday
            direction = "Up" if diff > 0 else "Down"
            return f"Market Asset {ticker} is trending {direction} today by {abs(diff):.2f}. Current Price: {close_today:.2f}"
    except Exception:
        pass
    return f"Could not fetch metrics for stock ticker: {ticker}"