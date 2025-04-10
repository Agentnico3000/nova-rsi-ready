# Nova RSI Bot 🚀

This is a plug-and-play RSI-based trading bot built with Flask and yFinance.

## 🔧 How It Works
- Accepts a stock symbol via POST
- Calculates RSI (14) using last 30 days of candles
- Returns action recommendation (BUY / SELL / HOLD)

## ▶️ Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/Agentnico3000/nova-rsi-ready)

## 🔗 Endpoint Example

**POST** `/run`  
```json
{
  "symbol": "AAPL"
}
```

## 📂 Environment Variables (`.env`)
```env
ALPACA_KEY=your_alpaca_api_key
ALPACA_SECRET=your_alpaca_secret_key
MODE=paper
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

## 🛠 Requirements
- Flask
- yFinance
- Railway / Replit ready

Built by Nova Forge 🧠🔥
