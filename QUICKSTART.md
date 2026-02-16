# 🚀 x402 Agent Marketplace - Quick Start Guide

**15 AI Agents. Pay SOL. Get AI. No Subscriptions.**

---

## 💰 Wallet Address

```
7nBnhr1cnefK977Xgz8cFvbyJdRRfcaqRs9EjcNpqU9A
```

---

## 🎯 Try Before You Buy (FREE Demos)

```bash
# Free trading signals demo
curl http://localhost:8000/api/v1/demo/trading-signals

# Free market summary demo
curl http://localhost:8000/api/v1/demo/market-summary

# Free token safety check demo
curl http://localhost:8000/api/v1/demo/token-check
```

---

## 💎 Full AI Agents (Paid)

### 1. Send SOL to the wallet above

### 2. Get the transaction signature from your wallet

### 3. Call the API with payment header

```bash
# Trading Signals (0.001 SOL)
curl -X GET "http://localhost:8000/api/v1/signals/trading" \
  -H "X-SOL-Payment: YOUR_WALLET:SIGNATURE:0.001"

# Market Summary (0.0005 SOL)
curl -X GET "http://localhost:8000/api/v1/market/summary" \
  -H "X-SOL-Payment: YOUR_WALLET:SIGNATURE:0.0005"

# Token Analysis (0.002 SOL)
curl -X GET "http://localhost:8000/api/v1/analysis/token?address=7N9..." \
  -H "X-SOL-Payment: YOUR_WALLET:SIGNATURE:0.002"

# Research Agent (0.005 SOL)
curl -X GET "http://localhost:8000/api/v1/research?topic=crypto" \
  -H "X-SOL-Payment: YOUR_WALLET:SIGNATURE:0.005"
```

---

## 📋 All Available Agents

| Agent | Price | Description |
|-------|-------|-------------|
| 📈 Trading Signals | 0.001 SOL | AI buy/sell recommendations |
| 📊 Trading Patterns | 0.002 SOL | Chart pattern recognition |
| 🔍 Token Analysis | 0.002 SOL | Rug pull risk scores |
| 📚 Research Agent | 0.005 SOL | AI-powered research |
| 🦨 Memecoin Scanner | 0.002 SOL | Find trending tokens |
| 🎯 Pump.fun Sniper | 0.005 SOL | New token discovery |
| 🐋 Whale Tracker | 0.003 SOL | Large SOL transactions |
| 📊 Portfolio Tracker | 0.001 SOL | Track performance |
| 📈 Volume Analyzer | 0.002 SOL | Volume patterns |
| 😌 Sentiment Analysis | 0.0005 SOL | Market sentiment |
| 🎁 Airdrop Hunter | 0.001 SOL | Airdrop opportunities |
| 💵 DeFi Yields | 0.0015 SOL | Best yields |
| 📰 News Digest | 0.0015 SOL | AI crypto news |
| 📊 Market Summary | 0.0005 SOL | Daily overview |
| 🏛️ Governance Votes | 0.0005 SOL | DAO proposals |

---

## 🔗 Important Links

- **GitHub:** https://github.com/dahhan43-netizen/x402-agent-marketplace
- **Wallet:** 7nBnhr1cnefK977Xgz8cFvbyJdRRfcaqRs9EjcNpqU9A

---

## 🛠️ Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python server.py

# Server runs at http://localhost:8000
```

---

## 📖 Payment Flow

```
1. Send SOL to wallet
2. Get transaction signature
3. Call API with header: X-SOL-Payment: WALLET:SIGNATURE:AMOUNT
4. Receive AI response instantly!
```

---

**Built with 🤖 by DahhansBot** | **Powered by Solana** 🌙
