from flask import Flask, request, jsonify
import yfinance as yf
import os

app = Flask(__name__)

def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

@app.route('/run', methods=['POST'])
def run_rsi():
    try:
        content = request.get_json()
        symbol = content.get("symbol", "AAPL").upper()
        data = yf.download(symbol, period="30d", interval="1d")
        rsi_series = calculate_rsi(data)
        latest_rsi = round(rsi_series.dropna().iloc[-1], 2)

        if latest_rsi < 30:
            action = "BUY (RSI below 30)"
        elif latest_rsi > 70:
            action = "SELL (RSI above 70)"
        else:
            action = "HOLD (RSI neutral)"

        return jsonify({
            "symbol": symbol,
            "latest_rsi": latest_rsi,
            "action": action
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
