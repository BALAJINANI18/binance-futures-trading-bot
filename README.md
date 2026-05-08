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
