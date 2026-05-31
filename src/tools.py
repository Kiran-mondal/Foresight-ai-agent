import requests
import yfinance as ticker_data

def get_live_news(query, api_key):
    """To fetch the latest news updates"""
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}"
    try:
        response = requests.get(url).json()
        articles = response.get('articles', [])[:3]
        news_summary = ""
        for art in articles:
            news_summary += f"- Title: {art['title']}\n  Description: {art['description']}\n"
        return news_summary if news_summary else "No recent news found."
    except Exception:
        return "Failed to fetch live news."

def get_weather_forecast(city, api_key):
    """To find out tomorrow's weather forecast"""
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        if response.get('list'):
            tomorrow = response['list'][8] # Weather data for 24 hours later
            return f"Weather in {city} tomorrow: {tomorrow['weather'][0]['description']}, Temp: {tomorrow['main']['temp']}°C"
        return "Weather data unavailable."
    except Exception:
        return "Failed to fetch weather data."

def get_stock_trend(ticker):
    """To know the recent stock market trends"""
    try:
        stock = ticker_data.Ticker(ticker)
        hist = stock.history(period="2d")
        if len(hist) >= 2:
            close_today = hist['Close'].iloc[-1]
            close_yesterday = hist['Close'].iloc[-2]
            diff = close_today - close_yesterday
            direction = "Up" if diff > 0 else "Down"
            return f"Stock {ticker} is {direction} today by {abs(diff):.2f}. Current Price: {close_today:.2f}"
    except Exception:
        pass
    return f"Could not fetch data for stock ticker: {ticker}"