# x402 Agent Marketplace

🤖 **15 AI Agents Selling SOL Micro-Payments via x402 Protocol**

A marketplace for AI agents where users pay with SOL cryptocurrency to access premium AI capabilities. Built on the x402 payment protocol with a 90/10 revenue split (90% to agent owners).

## 🚀 What is x402 Agent Marketplace?

The x402 Agent Marketplace is a decentralized AI services platform that enables:

- **15 AI Agents for Sale**: Trading signals, token analysis, memecoin scanner, whale tracker, and more!
- **SOL Micro-Payments**: Pay-per-use model using Solana blockchain transactions (from 0.0005 SOL)
- **x402 Protocol**: Standardized payment verification middleware (HTTP 402 Payment Required)
- **90% Revenue Share**: Agents keep 90% of all payments (10% platform fee)

## ✨ Features

### 15 Available AI Agents

| Agent | Price | Description |
|-------|-------|-------------|
| 📈 **Trading Signals** | 0.001 SOL | AI-generated trading signals with entry/exit levels |
| 📊 **Trading Patterns** | 0.002 SOL | Chart pattern recognition and analysis |
| 🔍 **Token Analysis** | 0.002 SOL | Rug pull risk scores, liquidity analysis |
| 📚 **Research Agent** | 0.005 SOL | AI-powered research on any topic |
| 🦨 **Memecoin Scanner** | 0.002 SOL | Scan trending memecoins |
| 🎯 **Pump.fun Sniper** | 0.005 SOL | Find new tokens early |
| 🐋 **Whale Tracker** | 0.003 SOL | Track large SOL transactions |
| 📊 **Portfolio Tracker** | 0.001 SOL | Track your portfolio performance |
| 📈 **Volume Analyzer** | 0.002 SOL | Analyze volume patterns |
| 😌 **Sentiment Analysis** | 0.0005 SOL | Market sentiment data |
| 🎁 **Airdrop Hunter** | 0.001 SOL | Find airdrop opportunities |
| 💵 **DeFi Yields** | 0.0015 SOL | Best yield farming rates |
| 📰 **News Digest** | 0.0015 SOL | AI-powered crypto news |
| 📊 **Market Summary** | 0.0005 SOL | Daily market overview |
| 🏛️ **Governance Votes** | 0.0005 SOL | Track DAO proposals |

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
git clone https://github.com/dahhan43-netizen/x402-agent-marketplace.git
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

### Payment Header Format

```
X-SOL-Payment: <wallet_address>:<transaction_signature>:<amount>
```

**Example:**
```
X-SOL-Payment: 4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX:AbCdEf123...xyz:0.001
```

### Example Endpoints

| Endpoint | Price |
|----------|-------|
| `GET /api/v1/signals/trading` | 0.001 SOL |
| `GET /api/v1/analysis/token` | 0.002 SOL |
| `GET /api/v1/scanner/memecoin` | 0.002 SOL |
| `GET /api/v1/tracker/whale` | 0.003 SOL |
| `GET /api/v1/research` | 0.005 SOL |
| `GET /api/v1/market/summary` | 0.0005 SOL |

### Error Responses

**Payment Required (402):**
```json
{
  "status": "payment_required",
  "price": 0.001,
  "currency": "SOL",
  "recipient": "4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX"
}
```

## 📁 Project Structure

```
x402-agent-marketplace/
├── server.py          # Main FastAPI application
├── requirements.txt   # Python dependencies
├── dashboard.html     # Web dashboard UI
├── how-to-use.html   # User guide UI
├── index.html         # Landing page
├── simple.html        # Shareable card
├── COMPLETE-GUIDE.md  # Full documentation
├── 15-agents-promo.md # Promotion materials
├── LICENSE            # MIT License
└── README.md          # This file
```

## 🛠️ Development

### Adding New Agents

1. Create a callback function for your agent
2. Register it with the `AgentRegistry`

### Environment Variables

Create a `.env` file:

```env
PAYMENT_WALLET=4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX
PLATFORM_FEE=0.10
HOST=0.0.0.0
PORT=8000
```

## 🔗 Links

- **Dashboard**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Landing Page**: index.html
- **GitHub**: https://github.com/dahhan43-netizen/x402-agent-marketplace

## 📜 License

MIT License

---

**Built with 🤖 by DahhansBot** | **Powered by Solana** 🌙
