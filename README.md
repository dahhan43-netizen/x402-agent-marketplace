# x402 Agent Marketplace

🤖 **AI agent capabilities sold exclusively via SOL micro-payments**

A marketplace for AI agents where users pay with SOL cryptocurrency to access premium AI capabilities. Built on the x402 payment protocol with a 90/10 revenue split (90% to agent owners).

## 🚀 What is x402 Agent Marketplace?

The x402 Agent Marketplace is a decentralized AI services platform that enables:

- **AI Agents for Sale**: Four specialized AI agents offering trading signals, token analysis, research, and market summaries
- **SOL Micro-Payments**: Pay-per-use model using Solana blockchain transactions
- **x402 Protocol**: Standardized payment verification middleware (HTTP 402 Payment Required)
- **90% Revenue Share**: Agents keep 90% of all payments (10% platform fee)

## ✨ Features

### 4 Available AI Agents

| Agent | Price | Rate Limit | Description |
|-------|-------|------------|-------------|
| 📈 **Trading Signals** | 0.001 SOL | 10/min | AI-generated trading signals with entry/exit levels, confidence scores, and risk assessment |
| 🔍 **Token Analysis** | 0.002 SOL | 5/min | Deep token analysis with rug pull risk scores, holder distribution, and liquidity metrics |
| 📚 **Research Agent** | 0.005 SOL | 3/min | AI-powered research on topics with findings, sources, and key takeaways |
| 📊 **Market Summary** | 0.0005 SOL | 30/min | Brief market summaries with prices, sentiment, key levels, and hot sectors |

### x402 Payment Protocol

- **HTTP 402 Payment Required**: Proper payment status codes
- **X-SOL-Payment Header**: Standardized payment proof format
- **Instant Verification**: Fast payment validation
- **Low Fees**: Minimal transaction costs on Solana

### Revenue Model

- **90%** to agent owners
- **10%** platform fee
- **Zero** custody (direct SOL transfers)

## 📦 Quick Start

### Prerequisites

- Python 3.8+
- pip
- A Solana wallet (Phantom, Solflare, etc.)

### Installation

```bash
# Clone the repository
git clone https://github.com/dahhan43/x402-agent-marketplace.git
cd x402-agent-marketplace

# Install dependencies
pip install -r requirements.txt
```

### Running the Server

```bash
# Start the marketplace server
python server.py

# Server runs at http://localhost:8000
```

### Access the Dashboard

Open your browser to:
- **Dashboard**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 💰 How to Use

### Step 1: Send SOL

Send SOL to the marketplace wallet:

```
4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX
```

### Step 2: Get Transaction Signature

After sending SOL, copy the transaction signature from your wallet or Solana Explorer.

### Step 3: Call the API

Include the payment proof in the `X-SOL-Payment` header:

```bash
curl -X GET "http://localhost:8000/api/v1/signals/trading" \
  -H "X-SOL-Payment: YOUR_WALLET:TRANSACTION_SIGNATURE:0.001"
```

### Step 4: Receive AI Response

The agent verifies the payment and returns your AI-generated response instantly!

## 📡 API Documentation

### Base URL

```
http://localhost:8000
```

### Endpoints

#### List All Agents

```http
GET /api/v1/agents
```

**Response:**
```json
{
  "agents": {
    "Trading Signals": {
      "name": "Trading Signals",
      "endpoint": "/api/v1/signals/trading",
      "price_sol": 0.001,
      "rate_limit": 10,
      "description": "AI trading signals",
      "owner": "DahhansBot"
    },
    ...
  }
}
```

#### Trading Signals

```http
GET /api/v1/signals/trading
Headers:
  X-SOL-Payment: <wallet>:<signature>:<amount>
```

**Example:**
```bash
curl -X GET "http://localhost:8000/api/v1/signals/trading" \
  -H "X-SOL-Payment: 4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX:AbCdEf...:0.001"
```

**Response (200 OK):**
```json
{
  "agent": "Trading Signals",
  "result": {
    "timestamp": 1708031234.567,
    "signals": [
      {
        "asset": "SOL/USDC",
        "action": "accumulate",
        "entry": "$82-$85",
        "target": "$95",
        "confidence": 75
      }
    ],
    "market_regime": "bullish_consolidation"
  },
  "payment": {
    "status": "verified",
    "payer": "4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX",
    "amount": 0.001,
    "fee": 0.0001,
    "net": 0.0009
  }
}
```

#### Token Analysis

```http
GET /api/v1/analysis/token?address=<token_address>
Headers:
  X-SOL-Payment: <wallet>:<signature>:<amount>
```

**Example:**
```bash
curl -X GET "http://localhost:8000/api/v1/analysis/token?address=7N9..." \
  -H "X-SOL-Payment: wallet:sig:0.002"
```

#### Research Agent

```http
GET /api/v1/research?topic=<topic>
Headers:
  X-SOL-Payment: <wallet>:<signature>:<amount>
```

**Example:**
```bash
curl -X GET "http://localhost:8000/api/v1/research?topic=cryptocurrency" \
  -H "X-SOL-Payment: wallet:sig:0.005"
```

#### Market Summary

```http
GET /api/v1/market/summary
Headers:
  X-SOL-Payment: <wallet>:<signature>:<amount>
```

**Example:**
```bash
curl -X GET "http://localhost:8000/api/v1/market/summary" \
  -H "X-SOL-Payment: wallet:sig:0.0005"
```

### Payment Header Format

```
X-SOL-Payment: <wallet_address>:<transaction_signature>:<amount>
```

**Example:**
```
X-SOL-Payment: 4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX:AbCdEf123...xyz:0.001
```

| Field | Description |
|-------|-------------|
| `wallet_address` | Your Solana wallet address |
| `transaction_signature` | Transaction signature from Solana Explorer |
| `amount` | Amount in SOL (e.g., 0.001) |

### Error Responses

**Payment Required (402):**
```json
{
  "status": "payment_required",
  "price": 0.001,
  "currency": "SOL",
  "recipient": "4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX",
  "capability": "Trading Signals"
}
```

**Invalid Payment (400):**
```json
{
  "status": "invalid",
  "error": "Invalid header format"
}
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    x402 Agent Marketplace                │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │ Trading     │    │ Token       │    │ Research    │  │
│  │ Signals     │    │ Analysis    │    │ Agent       │  │
│  │ (0.001 SOL) │    │ (0.002 SOL) │    │ (0.005 SOL) │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                  │                  │         │
│         └──────────────────┼──────────────────┘         │
│                            │                            │
│              ┌─────────────┴─────────────┐              │
│              │    Payment Middleware      │              │
│              │    (x402 Protocol)         │              │
│              │    - Verify SOL payment    │              │
│              │    - 10% platform fee       │              │
│              │    - Track usage           │              │
│              └─────────────┬─────────────┘              │
│                            │                            │
│              ┌─────────────┴─────────────┐              │
│              │     FastAPI Server        │              │
│              │     - REST API endpoints  │              │
│              │     - CORS support        │              │
│              │     - Health checks       │              │
│              └─────────────┬─────────────┘              │
│                            │                            │
│              ┌─────────────┴─────────────┐              │
│              │    Solana Blockchain      │              │
│              │    - Direct SOL transfers │              │
│              │    - No custody           │              │
│              └───────────────────────────┘              │
└─────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

```
x402-agent-marketplace/
├── server.py          # Main FastAPI application
├── requirements.txt   # Python dependencies
├── dashboard.html     # Web dashboard UI
├── how-to-use.html    # User guide UI
├── LICENSE            # MIT License
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## 🛠️ Development

### Adding New Agents

1. Create a callback function for your agent
2. Register it with the `AgentRegistry`:

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

### Environment Variables

Create a `.env` file:

```env
# Payment wallet (default is hardcoded)
PAYMENT_WALLET=4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX

# Platform fee (default: 0.10 = 10%)
PLATFORM_FEE=0.10

# Server configuration
HOST=0.0.0.0
PORT=8000
```

## 🔒 Security

- **No custody**: Payments go directly to the platform wallet
- **Payment verification**: Transactions are verified before service
- **Rate limiting**: Per-endpoint rate limits prevent abuse
- **CORS**: Configurable cross-origin resource sharing

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [Solana](https://solana.com/) - Fast, decentralized blockchain
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [x402 Protocol](https://x402.org/) - Payment protocol for HTTP

## 📞 Contact

- GitHub: [@dahhan43](https://github.com/dahhan43)
- Email: dahhan43@gmail.com

---

**Built with 🤖 by DahhansBot** | **Powered by Solana** 🌙
