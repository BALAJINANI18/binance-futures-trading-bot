# Binance Futures Testnet Trading Bot

A simplified trading bot built using Python for Binance Futures Testnet (USDT-M).

This project allows users to place MARKET and LIMIT orders using a clean command-line interface while maintaining proper project structure, validation, logging, and exception handling.

---

# Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- CLI-based interaction using Typer
- Input validation
- Structured project architecture
- Logging support
- Exception handling
- Colored terminal output
- Help documentation support

---

# Project Structure

```txt
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── exceptions.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── README.md
├── requirements.txt
├── .env
├── .gitignore
└── venv/
```

---

# Technologies Used

- Python 3
- python-binance
- Typer
- Rich
- python-dotenv

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/your-username/binance-futures-trading-bot.git
```

---

## 2. Move Into Project Directory

```bash
cd binance-futures-trading-bot
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create `.env` file in root directory:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

---

# Binance Futures Testnet

Base URL used:

```txt
https://testnet.binancefuture.com
```

---

# Run Commands

## MARKET BUY Order

```bash
python cli.py BTCUSDT BUY MARKET 0.01
```

---

## MARKET SELL Order

```bash
python cli.py BTCUSDT SELL MARKET 0.01
```

---

## LIMIT SELL Order

```bash
python cli.py BTCUSDT SELL LIMIT 0.01 --price 80000
```

---

## LIMIT BUY Order

```bash
python cli.py BTCUSDT BUY LIMIT 0.01 --price 50000
```

---

## Help Command

```bash
python cli.py --help
```

---

# Logging

Application logs are stored in:

```txt
logs/trading_bot.log
```

Logs include:
- API requests
- Order responses
- Errors
- Exceptions

---

# Validation

The application validates:
- trading symbol
- order side
- order type
- quantity
- limit order price

---

# Error Handling

The bot handles:
- invalid user input
- Binance API errors
- missing parameters
- network-related issues

---

# Assumptions

- User already has Binance Futures Testnet account
- API keys are active
- Internet connection is available

---

# Future Improvements

- Stop-Limit Orders
- OCO Orders
- Grid Trading
- Web UI Dashboard
- Real-time WebSocket price tracking

---

# Author

Dudem Sri Balaji
