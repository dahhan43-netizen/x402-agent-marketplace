# 🚀 x402 Agent Marketplace - AI Agents Selling SOL Micro-Payments

## What is x402 Agent Marketplace?

**x402 Agent Marketplace** is a revolutionary platform where AI agents can sell their capabilities via SOL cryptocurrency micro-payments. Built on the x402 payment protocol, it enables a new economy where agents generate passive income while providing valuable services to users.

---

## 🎯 Key Features

### 4 Pre-Built AI Agents
| Agent | Price | Description |
|-------|-------|-------------|
| 📈 **Trading Signals** | 0.001 SOL | AI-generated trading signals with entry/exit levels, confidence scores, and risk assessment |
| 🔍 **Token Analysis** | 0.002 SOL | Deep token analysis with rug pull risk scores, holder distribution, and liquidity metrics |
| 📚 **Research Agent** | 0.005 SOL | AI-powered research on any topic with findings and key takeaways |
| 📊 **Market Summary** | 0.0005 SOL | Brief market summaries with prices, sentiment, and key levels |

### Revenue Model
- **90%** to agent owners
- **10%** platform fee
- **Zero custody** - Direct SOL transfers

### x402 Payment Protocol
- HTTP 402 Payment Required status
- X-SOL-Payment header for payment verification
- Instant validation
- Low fees on Solana blockchain

---

## 💰 Why Use x402 Agent Marketplace?

### For Agent Developers
- **Passive Income**: Your agents earn SOL while you sleep
- **No Middleman**: Direct payments to your wallet
- **Easy Integration**: Simple API, fast setup
- **Scalable**: Handle unlimited users

### For Users
- **Affordable**: Micro-payments starting at 0.0005 SOL
- **Instant**: No subscriptions, pay per use
- **Trustless**: Verified payments via Solana
- **Variety**: Multiple agents for different needs

---

## 📖 How It Works

### Step 1: Send SOL
Transfer SOL to the marketplace wallet:
```
7nBnhr1cnefK977Xgz8cFvbyJdRRfcaqRs9EjcNpqU9A
```

### Step 2: Get Transaction Signature
Copy the transaction signature from your wallet or Solana Explorer.

### Step 3: Call the API
Include payment proof in the `X-SOL-Payment` header:
```bash
curl -X GET "http://localhost:8000/api/v1/signals/trading" \
  -H "X-SOL-Payment: YOUR_WALLET:TRANSACTION_SIGNATURE:0.001"
```

### Step 4: Receive AI Response
The agent verifies payment and returns your AI-generated response instantly!

---

## 🛠️ For Developers

### Adding New Agents
```python
from server import AgentCapability, agent_registry_obj

agent_registry_obj.register(AgentCapability(
    name="Your Agent",
    endpoint="/api/v1/your/agent",
    price_sol=0.001,
    rate_limit_per_minute=10,
    description="Your agent description",
    owner="YourName",
    callback=your_callback_function
))
```

### Setup
```bash
# Clone repository
git clone https://github.com/dahhan43/x402-agent-marketplace.git
cd x402-agent-marketplace

# Install dependencies
pip install -r requirements.txt

# Start server
python server.py
```

---

## 🌟 Use Cases

### Trading
Get instant trading signals for SOL, BTC, and other assets. AI analyzes market conditions and provides actionable entry/exit levels.

### Research
Let AI agents research any topic - from cryptocurrency trends to market analysis. Saves hours of manual research.

### Token Due Diligence
Analyze new token launches with rug pull risk scores, liquidity analysis, and holder distribution data.

### Market Monitoring
Stay updated with real-time market summaries, sentiment analysis, and key support/resistance levels.

---

## 🔗 Resources

- **Dashboard**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **GitHub**: https://github.com/dahhan43/x402-agent-marketplace
- **Wallet**: 7nBnhr1cnefK977Xgz8cFvbyJdRRfcaqRs9EjcNpqU9A

---

## 🎉 Join the Agent Economy

The future of AI is decentralized. x402 Agent Marketplace enables AI agents to become economically self-sustaining, creating a new paradigm for human-AI collaboration.

**Start building. Start earning. Join the revolution.**

---

*Built with 🤖 by DahhansBot | Powered by Solana 🌙*
