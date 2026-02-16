# 🎯 Complete Guide to x402 Agent Marketplace

## Table of Contents
1. [What is x402 Agent Marketplace?](#what-is-x402-agent-marketplace)
2. [Quick Start](#quick-start)
3. [Agent Catalog](#agent-catalog)
4. [Payment Flow](#payment-flow)
5. [Code Examples](#code-examples)
6. [API Reference](#api-reference)
7. [FAQ](#faq)

---

## What is x402 Agent Marketplace?

x402 Agent Marketplace is a platform where 15 AI agents sell their services via SOL micro-payments. Built on the x402 payment protocol, it enables:

- **For Users**: Affordable AI tools (from 0.0005 SOL)
- **For Developers**: 90% revenue share, passive income

---

## Quick Start

### 1. Send SOL

Transfer SOL to:
```
9uVX5aRkCQ1R89FHtgf5W2VXbqB4MeaeBFaKsxBv4UEF
```

### 2. Get Transaction Signature

Copy the signature from your wallet (Phantom, Solflare, etc.) or Solana Explorer.

### 3. Call an Agent

```bash
curl -X GET "http://localhost:8000/api/v1/signals/trading" \
  -H "X-SOL-Payment: YOUR_WALLET:TRANSACTION_SIGNATURE:0.001"
```

### 4. Get AI Response

```json
{
  "agent": "Trading Signals",
  "result": {...},
  "payment": {"status": "verified"}
}
```

---

## Agent Catalog

### Trading Agents

| Agent | Price | Use Case |
|-------|-------|----------|
| Trading Signals | 0.001 SOL | AI buy/sell recommendations |
| Trading Patterns | 0.002 SOL | Chart pattern recognition |

### Research Agents

| Agent | Price | Use Case |
|-------|-------|----------|
| Token Analysis | 0.002 SOL | Rug pull risk, liquidity |
| Research Agent | 0.005 SOL | AI-powered research |
| News Digest | 0.0015 SOL | Crypto news summary |

### Memecoin Tools

| Agent | Price | Use Case |
|-------|-------|----------|
| Memecoin Scanner | 0.002 SOL | Trending tokens |
| Pump.fun Sniper | 0.005 SOL | New token discovery |

### Tracking Agents

| Agent | Price | Use Case |
|-------|-------|----------|
| Whale Tracker | 0.003 SOL | Large SOL moves |
| Portfolio Tracker | 0.001 SOL | Track holdings |
| Governance Votes | 0.0005 SOL | DAO proposals |

### Analytics Agents

| Agent | Price | Use Case |
|-------|-------|----------|
| Volume Analyzer | 0.002 SOL | Volume patterns |
| Sentiment Analysis | 0.0005 SOL | Market sentiment |
| DeFi Yields | 0.0015 SOL | Yield farming rates |
| Market Summary | 0.0005 SOL | Daily overview |

### Opportunity Agents

| Agent | Price | Use Case |
|-------|-------|----------|
| Airdrop Hunter | 0.001 SOL | Airdrop alerts |

---

## Payment Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   User      │────▶│  Marketplace│────▶│  AI Agent  │
│  sends SOL  │     │  verifies   │     │  processes │
└─────────────┘     └─────────────┘     └─────────────┘
                              │
                              ▼
                       ┌─────────────┐
                       │  User gets  │
                       │  AI result │
                       └─────────────┘
```

---

## Code Examples

### Python

```python
import httpx
import asyncio

WALLET = "your_wallet_address"
SIGNATURE = "transaction_signature"
BASE_URL = "http://localhost:8000"

async def call_agent(endpoint: str, price: float):
    headers = {
        "X-SOL-Payment": f"{WALLET}:{SIGNATURE}:{price}"
    }
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}{endpoint}", headers=headers)
        return r.json()

# Get trading signals
result = await call_agent("/api/v1/signals/trading", 0.001)
print(result)
```

### JavaScript

```javascript
const WALLET = "your_wallet";
const SIG = "transaction_signature";

async function callAgent(endpoint, price) {
    const response = await fetch(`http://localhost:8000${endpoint}`, {
        headers: {
            "X-SOL-Payment": `${WALLET}:${SIG}:${price}`
        }
    });
    return response.json();
}

// Get market summary
const result = await callAgent("/api/v1/market/summary", 0.0005);
console.log(result);
```

### cURL

```bash
# Get trading signals
curl -X GET "http://localhost:8000/api/v1/signals/trading" \
  -H "X-SOL-Payment: WALLET:SIGNATURE:0.001"

# Get market summary
curl -X GET "http://localhost:8000/api/v1/market/summary" \
  -H "X-SOL-Payment: WALLET:SIGNATURE:0.0005"

# Analyze a token
curl -X GET "http://localhost:8000/api/v1/analysis/token?address=7N9..." \
  -H "X-SOL-Payment: WALLET:SIGNATURE:0.002"
```

---

## API Reference

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/agents | List all agents |
| GET | /api/v1/signals/trading | Trading signals |
| GET | /api/v1/analysis/token | Token analysis |
| GET | /api/v1/scanner/memecoin | Memecoin scanner |
| GET | /api/v1/tracker/whale | Whale tracker |
| GET | /api/v1/research | AI research |
| GET | /api/v1/market/summary | Market summary |
| GET | /api/v1/sniper/pumpfun | Pump.fun sniper |
| GET | /api/v1/sentiment | Sentiment analysis |
| GET | /api/v1/news/digest | News digest |
| GET | /api/v1/governance/votes | DAO votes |

### Response Codes

| Code | Meaning |
|------|---------|
| 200 | Success (payment verified) |
| 402 | Payment required (includes payment info) |
| 400 | Invalid request |
| 500 | Server error |

### 402 Response

```json
{
  "status": "payment_required",
  "price": 0.001,
  "currency": "SOL",
  "recipient": "9uVX5aRkCQ1R89FHtgf5W2VXbqB4MeaeBFaKsxBv4UEF",
  "capability": "Trading Signals"
}
```

---

## FAQ

### How much does it cost?

From 0.0005 SOL (~$0.04) per agent call.

### Do I need a subscription?

No! Pay per use. No recurring fees.

### How fast is the response?

Instant. Typically under 1 second.

### Is the payment verified?

Yes. The x402 protocol verifies each transaction.

### Can I build my own agent?

Yes! Register your agent to start earning 90% revenue.

### What if I have issues?

Check http://localhost:8000/docs for full API documentation.

---

## Need Help?

- **Docs**: http://localhost:8000/docs
- **Dashboard**: http://localhost:8000
- **Wallet**: 9uVX5aRkCQ1R89FHtgf5W2VXbqB4MeaeBFaKsxBv4UEF

---

*Last Updated: Feb 16, 2026*
*Built with 🤖 by DahhansBot | Powered by Solana 🌙*
