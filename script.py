import requests
from datetime import datetime

def get_price_at_time(symbol: str, timestamp: datetime):
    par = f"{symbol.upper()}BRL"
    url = "https://api.binance.com/api/v3/aggTrades"
    millis = int(timestamp.timestamp() * 1000)
    params = {
        "symbol": par,
        "startTime": millis,
        "endTime": millis + 60_000,  # 1 minuto
        "limit": 1
    }
    response = requests.get(url, params=params)
    print(f"Requisição: {response.url}")
    data = response.json()
    print("Resposta da API:", data)
    if isinstance(data, list) and data:
        return float(data[0]['p'])
    return None

if __name__ == "__main__":
    symbol = "BTC"
    timestamp = datetime.utcnow()
    price = get_price_at_time(symbol, timestamp)
    print(f"Preço {symbol} em {timestamp}: {price}")
