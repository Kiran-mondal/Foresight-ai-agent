import requests
import yfinance as ticker_data

def get_live_news(query, api_key):
    """Fetches the latest global news headlines and descriptions based on a search query."""
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}"
    try:
        response = requests.get(url).json()
        articles = response.get('articles', [])[:3]
        news_summary = ""
        for art in articles:
            news_summary += f"- Title: {art['title']}\n  Description: {art['description']}\n"
        return news_summary if news_summary else "No recent news found for this topic."
    except Exception as e:
        return f"Failed to fetch live news due to an unexpected error: {str(e)}"

def get_weather_forecast(city, api_key):
    """Retrieves the weather forecast for approximately 24 hours out for a targeted location."""
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        if response.get('list'):
            tomorrow = response['list'][8]  # Extracts approximate 24-hour ahead data point
            return f"Weather forecast in {city} for tomorrow: {tomorrow['weather'][0]['description']}, Temperature: {tomorrow['main']['temp']}°C"
        return f"Weather data unavailable for the specified location: {city}."
    except Exception as e:
        return f"Failed to fetch weather data: {str(e)}"

def get_stock_trend(ticker):
    """Fetches real-time equity/index data directly via scraping without requiring external API keys."""
    try:
        stock = ticker_data.Ticker(ticker)
        hist = stock.history(period="2d")
        if len(hist) >= 2:
            close_today = hist['Close'].iloc[-1]
            close_yesterday = hist['Close'].iloc[-2]
            diff = close_today - close_yesterday
            direction = "Up" if diff > 0 else "Down"
            return f"Market Asset {ticker} is trending {direction} today by {abs(diff):.2f}. Current Valuation: {close_today:.2f}"
    except Exception:
        pass
    return f"Could not structuralize data or fetch metrics for stock ticker: {ticker}"