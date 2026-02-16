# 🤖 x402 Agent Marketplace

**AI agent capabilities via SOL micro-payments.**

Currency: **SOL (Solana blockchain)** | Protocol: **x402 (HTTP 402)**

---

## Your Payment Wallet

```
7nBnhr1cnefK977Xgz8cFvbyJdRRfcaqRs9EjcNpqU9A
```

**Click to copy:** See dashboard.html or use the copy function in the marketplace.

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
python -m agent-marketplace
```

Server runs at `http://localhost:8000`

---

## Available Agents (SOL-Only)

| Agent | Price | Rate | Description |
|-------|-------|------|-------------|
| 📈 Trading Signals | 0.001 SOL | 10/min | AI trading signals with entry/exit levels |
| 🔍 Token Analysis | 0.002 SOL | 5/min | Deep token analysis with risk scores |
| 📚 Research | 0.005 SOL | 3/min | AI research on any topic |
| 📊 Market Summary | 0.0005 SOL | 30/min | Brief market overview |

---

## How to Pay (SOL Only)

### Step 1: Send SOL

```
Wallet: 7nBnhr1cnefK977Xgz8cFvbyJdRRfcaqRs9EjcNpqU9A
Network: Solana Mainnet
```

### Step 2: Get Transaction Signature

After sending, get the signature from:
- Solana Explorer (solscan.io)
- Phantom wallet → View transaction → Copy signature

### Step 3: Include Payment Header

```
X-SOL-Payment: wallet_address:signature:amount
```

### Example

```bash
curl -X GET "http://localhost:8000/api/v1/signals/trading" \
  -H "X-SOL-Payment: YourWallet:Sig123...:0.001"
```

---

## API Endpoints

### Trading Signals

```bash
GET /api/v1/signals/trading
X-SOL-Payment: wallet:sig:0.001
```

### Token Analysis

```bash
GET /api/v1/analysis/token?address=TOKEN_ADDRESS
X-SOL-Payment: wallet:sig:0.002
```

### Research

```bash
GET /api/v1/research?topic=cryptocurrency
X-SOL-Payment: wallet:sig:0.005
```

### Market Summary

```bash
GET /api/v1/market/summary
X-SOL-Payment: wallet:sig:0.0005
```

---

## Revenue Sharing

- **90%** to agent owner (you!)
- **10%** platform fee

Example: You charge 0.001 SOL → You earn 0.0009 SOL per call

---

## Project Structure

```
agent-marketplace/
├── main.py              # FastAPI app + SOL payment middleware
├── dashboard.html      # Web dashboard with your wallet
├── requirements.txt
├── .env.example       # Configuration
└── src/
    └── agents/
        ├── trading.py   # Trading signals
        ├── analysis.py  # Token analysis
        ├── research.py  # Research
        └── market.py    # Market summary
```

---

## Adding New Agents

```python
from main import AgentCapability

MY_AGENT = AgentCapability(
    name="My New Agent",
    endpoint="/api/v1/my-agent",
    price_sol=0.01,        # Price in SOL
    rate_limit_per_minute=5,
    description="What it does",
    owner="your-name",
    callback=my_function
)
```

---

## Why SOL?

- ⚡ **Fast** - Sub-second confirmation
- 💰 **Cheap** - Fractions of a cent for micro-payments
- 🔐 **Secure** - Industry-leading blockchain security
- 🌐 **Universal** - No payment processor needed

---

## Future Enhancements

- [ ] Real Solana RPC verification
- [ ] Database persistence
- [ ] Admin dashboard
- [ ] Multiple agent owners
- [ ] Subscription plans
- [ ] Referral system

---

Built with ❤️ by DahhansBot | Powered by Solana
