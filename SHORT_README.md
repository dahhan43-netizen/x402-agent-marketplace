# 🤖 x402 Agent Marketplace

**10 AI Agents Selling SOL Micro-Payments**

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![Solana](https://img.shields.io/badge/Solana-Powered-purple.svg)

---

## 🎯 What is x402 Agent Marketplace?

A revolutionary platform where AI agents sell their capabilities via SOL cryptocurrency micro-payments. Built on the x402 payment protocol with 90% revenue share for developers.

---

## 💰 10 AI Agents Available

| Agent | Price | Description |
|-------|-------|-------------|
| 📈 Trading Signals | 0.001 SOL | AI-generated buy/sell recommendations |
| 🔍 Token Analysis | 0.002 SOL | Rug pull risk, liquidity scores |
| 📚 Research Agent | 0.005 SOL | AI-powered topic research |
| 📊 Market Summary | 0.0005 SOL | Daily market overviews |
| 🦨 Memecoin Scanner | 0.002 SOL | Trending tokens scanner |
| 🐋 Whale Tracker | 0.003 SOL | Large SOL transaction tracking |
| 🎁 Airdrop Hunter | 0.001 SOL | Airdrop opportunities |
| 💵 DeFi Yields | 0.0015 SOL | Best yield farming rates |
| 📈 Trading Patterns | 0.002 SOL | Chart pattern recognition |
| 😌 Sentiment Analysis | 0.0005 SOL | Market sentiment data |

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/dahhan43/x402-agent-marketplace.git
cd x402-agent-marketplace

# Install dependencies
pip install -r requirements.txt

# Start the server
python server.py
```

Server runs at: **http://localhost:8000**

---

## 💸 How to Use

1. **Send SOL** to: `7nBnhr1cnefK977Xgz8cFvbyJdRRfcaqRs9EjcNpqU9A`
2. **Get signature** from your wallet transaction
3. **Call API** with payment header:
```bash
curl -H "X-SOL-Payment: YOUR_WALLET:SIGNATURE:0.001" \
  http://localhost:8000/api/v1/signals/trading
```
4. **Receive AI response** instantly!

---

## 📡 API Endpoints

### Get All Agents
```bash
GET /api/v1/agents
```

### Trading Signals
```bash
GET /api/v1/signals/trading
# Price: 0.001 SOL
```

### Token Analysis
```bash
GET /api/v1/analysis/token?address=<token_address>
# Price: 0.002 SOL
```

### Memecoin Scanner
```bash
GET /api/v1/scanner/memecoin
# Price: 0.002 SOL
```

### Whale Tracker
```bash
GET /api/v1/tracker/whale
# Price: 0.003 SOL
```

[See all endpoints →](http://localhost:8000/docs)

---

## 🎯 Why x402?

- ✅ **90% Revenue Share** - Developers keep most earnings
- ⚡ **Instant Payments** - No subscriptions, pay per use
- 🔒 **Zero Custody** - Direct SOL transfers
- 🌙 **Solana Powered** - Fast, cheap transactions
- 🤖 **10 Pre-Built Agents** - Ready to use
- 🔧 **Easy Integration** - Simple API, fast setup

---

## 📊 Market Opportunity

The AI agent economy is exploding. x402 Agent Marketplace enables:

- **For Developers:** Passive income from AI agents
- **For Traders:** Affordable AI tools (from 0.0005 SOL)
- **For Researchers:** Instant AI research on any topic
- **For Communities:** AI-powered tools for members

---

## 🛠️ For Developers

### Add Your Own Agent

```python
from server import AgentCapability, agent_registry_obj

agent_registry_obj.register(AgentCapability(
    name="Your Agent",
    endpoint="/api/v1/your/agent",
    price_sol=0.001,
    rate_limit_per_minute=10,
    description="What your agent does",
    owner="YourName",
    callback=your_callback_function
))
```

---

## 📈 Stats

- **10 AI Agents** Live
- **4x Daily** Posts
- **90% Revenue** to Developers
- **0.0005 SOL** Minimum Price

---

## 🔗 Links

- 🌐 **Dashboard**: http://localhost:8000
- 📚 **API Docs**: http://localhost:8000/docs
- 💰 **Wallet**: 7nBnhr1cnefK977Xgz8cFvbyJdRRfcaqRs9EjcNpqU9A
- 🐙 **GitHub**: https://github.com/dahhan43/x402-agent-marketplace

---

## 🎉 Join the Agent Economy

The future of AI is decentralized. x402 Agent Marketplace enables AI agents to become economically self-sustaining.

**Start building. Start earning. Join the revolution.**

---

Built with 🤖 by DahhansBot | Powered by Solana 🌙
