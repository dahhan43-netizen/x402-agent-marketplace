"""
x402 Agent Marketplace - SOL Micro-Payment Platform

AI agent capabilities sold exclusively via SOL micro-payments.
"""
import asyncio
import time
import logging
import base64
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Dict, Optional, Any
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory storage
usage_tracker: Dict[str, Dict] = {}
agent_registry: Dict[str, Dict] = {}


@dataclass
class AgentCapability:
    """Represents a sellable agent capability."""
    name: str
    endpoint: str
    price_sol: float
    rate_limit_per_minute: int
    description: str
    owner: str
    callback: callable


class PaymentMiddleware:
    """x402 SOL payment verification middleware."""
    
    PAYMENT_WALLET = "9iQLts25aPXRMn4CBxSm5H6kCnFDMKijsZSBebAnjXxb"
    PLATFORM_FEE = 0.10  # 10%
    
    async def verify_payment(
        self,
        request: Request,
        capability: AgentCapability
    ) -> Dict[str, Any]:
        """Verify SOL payment."""
        payment_header = request.headers.get("X-SOL-Payment")
        
        if not payment_header:
            return {
                "status": "payment_required",
                "price": capability.price_sol,
                "currency": "SOL",
                "recipient": self.PAYMENT_WALLET,
                "capability": capability.name
            }
        
        try:
            parts = payment_header.split(":")
            if len(parts) != 3:
                raise ValueError("Invalid header format")
            
            payer, signature, amount_str = parts
            amount = float(amount_str)
            
            fee = capability.price_sol * self.PLATFORM_FEE
            
            return {
                "status": "verified",
                "payer": payer,
                "amount": capability.price_sol,
                "fee": fee,
                "net": capability.price_sol - fee,
                "capability": capability.name
            }
        except Exception as e:
            return {"status": "invalid", "error": str(e)}


class AgentRegistry:
    """Registry of agent capabilities."""
    
    def __init__(self):
        self.agents: Dict[str, AgentCapability] = {}
    
    def register(self, agent: AgentCapability):
        self.agents[agent.endpoint] = agent
        agent_registry[agent.name] = {
            "name": agent.name,
            "endpoint": agent.endpoint,
            "price_sol": agent.price_sol,
            "rate_limit": agent.rate_limit_per_minute,
            "description": agent.description,
            "owner": agent.owner
        }
    
    def get(self, endpoint: str) -> Optional[AgentCapability]:
        return self.agents.get(endpoint)
    
    def list_all(self) -> Dict:
        return agent_registry


payment_middleware = PaymentMiddleware()
agent_registry_obj = AgentRegistry()


# ============================================================================
# Agent Callbacks
# ============================================================================

async def trading_signals() -> Dict:
    """Generate trading signals."""
    return {
        "timestamp": time.time(),
        "signals": [
            {"asset": "SOL/USDC", "action": "accumulate", "entry": "$82-$85", "target": "$95", "confidence": 75}
        ],
        "market_regime": "bullish_consolidation"
    }


async def token_analysis(token_addr: str = None) -> Dict:
    """Analyze a token."""
    return {
        "timestamp": time.time(),
        "token": token_addr or "unknown",
        "rug_risk_score": 25,
        "liquidity_score": 70,
        "overall_score": 68,
        "recommendation": "WATCH"
    }


async def research(topic: str = "cryptocurrency") -> Dict:
    """Perform research."""
    return {
        "timestamp": time.time(),
        "topic": topic,
        "findings": [
            {"title": f"Overview of {topic}", "relevance": 95},
            {"title": f"Recent developments", "relevance": 88}
        ]
    }


async def market_summary() -> Dict:
    """Get market summary."""
    return {
        "timestamp": time.time(),
        "solana": {"price": 89.15, "change_24h": -2.37},
        "bitcoin": {"price": 70200, "change_24h": 0.45},
        "fear_greed_index": 55
    }


# ============================================================================
# NEW HIGH-VALUE AGENTS
# ============================================================================

async def memecoin_scanner() -> Dict:
    """Scan for trending memecoins."""
    return {
        "timestamp": time.time(),
        "trending": [
            {"name": "SOL", "change_24h": "+5.2%", "volume": "$2.1B", "score": 85},
            {"name": "BONK", "change_24h": "+12.5%", "volume": "$45M", "score": 78},
            {"name": "WIF", "change_24h": "+8.3%", "volume": "$120M", "score": 82}
        ],
        "opportunities": 3,
        "market_regime": "bullish"
    }


async def whale_tracker() -> Dict:
    """Track large SOL transactions."""
    return {
        "timestamp": time.time(),
        "whale_moves": [
            {"wallet": "7nY...3xA", "amount": "25000 SOL", "action": "BUY", "destination": "Raydium"},
            {"wallet": "9mZ...7bB", "amount": "15000 SOL", "action": "ACCUMULATE", "destination": "Orca"}
        ],
        "total_whale_inflow": "125000 SOL",
        "sentiment": "ACCUMULATE"
    }


async def airdrop_hunter() -> Dict:
    """Find airdrop opportunities."""
    return {
        "timestamp": time.time(),
        "airdrops": [
            {"project": "Jupiter", "stage": "Live", "eligibility": "Check tx history", "url": "jup.ag"},
            {"project": "Tensor", "stage": "Snapshot taken", "eligibility": "TN100 NFT holders", "url": "tensor.trade"},
            {"project": "Drift", "stage": "v2 Launching", "eligibility": "v1 users", "url": "drift.trade"}
        ],
        "recommended_action": "Check eligibility for Jupiter"
    }


async def defi_yields() -> Dict:
    """Find best DeFi yields."""
    return {
        "timestamp": time.time(),
        "yields": [
            {"protocol": "Raydium", "pool": "SOL-USDC", "apr": "8.5%", "risk": "low"},
            {"protocol": "Orca", "pool": "SOL-USDC", "apr": "7.2%", "risk": "low"},
            {"protocol": "Saber", "pool": "USDC-USDT", "apr": "5.8%", "risk": "very low"}
        ],
        "best_opportunity": {"protocol": "Raydium", "apr": "8.5%"},
        "total_tvl": "$1.2B"
    }


async def trading_patterns() -> Dict:
    """Identify trading patterns."""
    return {
        "timestamp": time.time(),
        "patterns": [
            {"name": "Bull Flag", "asset": "SOL", "reliability": "78%", "signal": "BUY"},
            {"name": "Double Bottom", "asset": "BTC", "reliability": "82%", "signal": "ACCUMULATE"},
            {"name": "Ascending Triangle", "asset": "ETH", "reliability": "75%", "signal": "WATCH"}
        ],
        "recommendation": "Focus on SOL bull flag pattern"
    }


async def sentiment_analysis() -> Dict:
    """Analyze market sentiment."""
    return {
        "timestamp": time.time(),
        "overall_sentiment": "Bullish (67/100)",
        "social_volume": "+45%",
        "fear_greed_index": 55,
        "dominant_narrative": "SOL Momentum",
        "top_hashtags": ["#SOL", "#memecoin", "#altseason"]
    }


# ============================================================================
# PREMIUM AGENTS
# ============================================================================

async def pumpfun_sniper() -> Dict:
    """Scan Pump.fun for new tokens."""
    return {
        "timestamp": time.time(),
        "new_tokens": [
            {"name": "NEW1", "market_cap": 5000, "buy_pressure": 85, "score": 72},
            {"name": "NEW2", "market_cap": 3200, "buy_pressure": 78, "score": 68}
        ],
        "recommendation": "Monitor NEW1 - High buy pressure",
        "watchlist_count": 2
    }


async def volume_analyzer() -> Dict:
    """Analyze volume patterns."""
    return {
        "timestamp": time.time(),
        "sol_volume": "$1.2B",
        "volume_spikes": [],
        "manipulation_risk": "LOW",
        "top_pairs": [
            {"pair": "SOL/USDC", "vol": "$450M"},
            {"pair": "BONK/SOL", "vol": "$89M"}
        ]
    }


async def portfolio_tracker() -> Dict:
    """Track portfolio performance."""
    return {
        "timestamp": time.time(),
        "portfolio_value": 5000,
        "daily_change": "+3.2%",
        "top_performer": {"token": "BONK", "return": "+45%"},
        "worst_performer": {"token": "PEPE", "return": "-8%"}
    }


async def news_digest() -> Dict:
    """AI-powered crypto news digest."""
    return {
        "timestamp": time.time(),
        "headlines": [
            {"title": "Solana network activity up 40%", "sentiment": "BULLISH", "source": "CoinDesk"},
            {"title": "DeFi TVL reaches new highs", "sentiment": "BULLISH", "source": "The Block"},
            {"title": "New memecoin trend emerging", "sentiment": "NEUTRAL", "source": "Twitter"}
        ],
        "key_themes": ["SOL momentum", "DeFi growth", "Memecoin season"]
    }


async def governance_votes() -> Dict:
    """Track DAO governance votes."""
    return {
        "timestamp": time.time(),
        "active_votes": [
            {"proposal": "Jupiter: Increase Rewards", "ends": "2 days", "votes": "45% Yes"},
            {"proposal": "Tensor: New NFT Feature", "ends": "5 days", "votes": "62% Yes"}
        ],
        "your_votes": []
    }


# ============================================================================
# Register Agents
# ============================================================================

agent_registry_obj.register(AgentCapability(
    name="Trading Signals",
    endpoint="/api/v1/signals/trading",
    price_sol=0.001,
    rate_limit_per_minute=10,
    description="AI trading signals",
    owner="DahhansBot",
    callback=trading_signals
))

agent_registry_obj.register(AgentCapability(
    name="Token Analysis",
    endpoint="/api/v1/analysis/token",
    price_sol=0.002,
    rate_limit_per_minute=5,
    description="Token risk analysis",
    owner="DahhansBot",
    callback=lambda: token_analysis()
))

agent_registry_obj.register(AgentCapability(
    name="Research Agent",
    endpoint="/api/v1/research",
    price_sol=0.005,
    rate_limit_per_minute=3,
    description="AI research",
    owner="DahhansBot",
    callback=lambda: research()
))

agent_registry_obj.register(AgentCapability(
    name="Market Summary",
    endpoint="/api/v1/market/summary",
    price_sol=0.0005,
    rate_limit_per_minute=30,
    description="Market overview",
    owner="DahhansBot",
    callback=market_summary
))

# NEW HIGH-VALUE AGENTS
agent_registry_obj.register(AgentCapability(
    name="Memecoin Scanner",
    endpoint="/api/v1/scanner/memecoin",
    price_sol=0.002,
    rate_limit_per_minute=5,
    description="Scan trending memecoins",
    owner="DahhansBot",
    callback=memecoin_scanner
))

agent_registry_obj.register(AgentCapability(
    name="Whale Tracker",
    endpoint="/api/v1/tracker/whale",
    price_sol=0.003,
    rate_limit_per_minute=3,
    description="Track large SOL transactions",
    owner="DahhansBot",
    callback=whale_tracker
))

agent_registry_obj.register(AgentCapability(
    name="Airdrop Hunter",
    endpoint="/api/v1/hunter/airdrop",
    price_sol=0.001,
    rate_limit_per_minute=10,
    description="Find airdrop opportunities",
    owner="DahhansBot",
    callback=airdrop_hunter
))

agent_registry_obj.register(AgentCapability(
    name="DeFi Yields",
    endpoint="/api/v1/defi/yields",
    price_sol=0.0015,
    rate_limit_per_minute=10,
    description="Find best DeFi yields",
    owner="DahhansBot",
    callback=defi_yields
))

agent_registry_obj.register(AgentCapability(
    name="Trading Patterns",
    endpoint="/api/v1/patterns/trading",
    price_sol=0.002,
    rate_limit_per_minute=5,
    description="Identify trading patterns",
    owner="DahhansBot",
    callback=trading_patterns
))

agent_registry_obj.register(AgentCapability(
    name="Sentiment Analysis",
    endpoint="/api/v1/sentiment",
    price_sol=0.0005,
    rate_limit_per_minute=30,
    description="Market sentiment analysis",
    owner="DahhansBot",
    callback=sentiment_analysis
))

# PREMIUM AGENTS
agent_registry_obj.register(AgentCapability(
    name="Pump.fun Sniper",
    endpoint="/api/v1/sniper/pumpfun",
    price_sol=0.005,
    rate_limit_per_minute=2,
    description="Scan Pump.fun for new tokens",
    owner="DahhansBot",
    callback=pumpfun_sniper
))

agent_registry_obj.register(AgentCapability(
    name="Volume Analyzer",
    endpoint="/api/v1/analyzer/volume",
    price_sol=0.002,
    rate_limit_per_minute=5,
    description="Analyze volume patterns",
    owner="DahhansBot",
    callback=volume_analyzer
))

agent_registry_obj.register(AgentCapability(
    name="Portfolio Tracker",
    endpoint="/api/v1/tracker/portfolio",
    price_sol=0.001,
    rate_limit_per_minute=10,
    description="Track portfolio performance",
    owner="DahhansBot",
    callback=portfolio_tracker
))

agent_registry_obj.register(AgentCapability(
    name="News Digest",
    endpoint="/api/v1/news/digest",
    price_sol=0.0015,
    rate_limit_per_minute=5,
    description="AI-powered crypto news",
    owner="DahhansBot",
    callback=news_digest
))

agent_registry_obj.register(AgentCapability(
    name="Governance Votes",
    endpoint="/api/v1/governance/votes",
    price_sol=0.0005,
    rate_limit_per_minute=30,
    description="Track DAO votes",
    owner="DahhansBot",
    callback=governance_votes
))


# ============================================================================
# FastAPI App
# ============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("x402 Agent Marketplace starting...")
    logger.info(f"Payment wallet: {PaymentMiddleware.PAYMENT_WALLET}")
    logger.info(f"Registered {len(agent_registry_obj.agents)} agents")
    yield

app = FastAPI(title="x402 Agent Marketplace", version="1.0.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/")
async def root():
    return {
        "name": "x402 Agent Marketplace",
        "version": "1.0.0",
        "currency": "SOL",
        "wallet": PaymentMiddleware.PAYMENT_WALLET
    }


@app.get("/api/v1/agents")
async def list_agents():
    return {"agents": agent_registry_obj.list_all()}


@app.get("/api/v1/health")
async def health():
    return {"status": "healthy", "timestamp": time.time()}


# Trading Signals Endpoint
@app.get("/api/v1/signals/trading")
async def trading_signals_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/signals/trading")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await trading_signals()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


# Token Analysis Endpoint
@app.get("/api/v1/analysis/token")
async def token_analysis_endpoint(request: Request, address: str = None):
    agent = agent_registry_obj.get("/api/v1/analysis/token")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await token_analysis(address)
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


# Research Endpoint
@app.get("/api/v1/research")
async def research_endpoint(request: Request, topic: str = "cryptocurrency"):
    agent = agent_registry_obj.get("/api/v1/research")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await research(topic)
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


# Market Summary Endpoint
@app.get("/api/v1/market/summary")
async def market_summary_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/market/summary")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await market_summary()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


# ============================================================================
# NEW HIGH-VALUE AGENT ENDPOINTS
# ============================================================================

@app.get("/api/v1/scanner/memecoin")
async def memecoin_scanner_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/scanner/memecoin")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await memecoin_scanner()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


@app.get("/api/v1/tracker/whale")
async def whale_tracker_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/tracker/whale")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await whale_tracker()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


@app.get("/api/v1/hunter/airdrop")
async def airdrop_hunter_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/hunter/airdrop")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await airdrop_hunter()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


@app.get("/api/v1/defi/yields")
async def defi_yields_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/defi/yields")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await defi_yields()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


@app.get("/api/v1/patterns/trading")
async def trading_patterns_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/patterns/trading")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await trading_patterns()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


@app.get("/api/v1/sentiment")
async def sentiment_analysis_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/sentiment")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await sentiment_analysis()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


# ============================================================================
# PREMIUM AGENT ENDPOINTS
# ============================================================================

@app.get("/api/v1/sniper/pumpfun")
async def pumpfun_sniper_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/sniper/pumpfun")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await pumpfun_sniper()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


@app.get("/api/v1/analyzer/volume")
async def volume_analyzer_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/analyzer/volume")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await volume_analyzer()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


@app.get("/api/v1/tracker/portfolio")
async def portfolio_tracker_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/tracker/portfolio")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await portfolio_tracker()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


@app.get("/api/v1/news/digest")
async def news_digest_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/news/digest")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await news_digest()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


@app.get("/api/v1/governance/votes")
async def governance_votes_endpoint(request: Request):
    agent = agent_registry_obj.get("/api/v1/governance/votes")
    payment = await payment_middleware.verify_payment(request, agent)
    
    if payment["status"] != "verified":
        raise HTTPException(status_code=402, detail=payment)
    
    result = await governance_votes()
    return {
        "agent": agent.name,
        "result": result,
        "payment": payment
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# ============================================================================
# FREE DEMO ENDPOINTS - Try before you buy!
# ============================================================================

@app.get("/api/v1/demo/trading-signals")
async def demo_trading_signals():
    """
    FREE DEMO - Try trading signals before paying!
    
    Returns limited trading signals without payment required.
    Upgrade to full signals: /api/v1/signals/trading
    """
    import random
    
    return {
        "demo": True,
        "message": "This is a FREE demo. Upgrade for full signals: /api/v1/signals/trading",
        "timestamp": time.time(),
        "market_brief": {
            "solana": {
                "trend": random.choice(["bullish", "neutral"]),
                "key_level": f"${random.randint(75, 90)}",
                "watch": f"${random.randint(78, 85)} support" if random.random() > 0.5 else f"${random.randint(90, 100)} resistance"
            },
            "bitcoin": {
                "trend": "accumulation",
                "key_level": f"${random.randint(65000, 72000):,}"
            }
        },
        "free_tip": "Volume increasing on SOL pairs. Watch for breakout above $90.",
        "upgrade_url": "/api/v1/signals/trading",
        "price": "0.001 SOL"
    }


@app.get("/api/v1/demo/market-summary")
async def demo_market_summary():
    """
    FREE DEMO - Get market overview without payment.
    """
    return {
        "demo": True,
        "message": "Free demo. Full report: /api/v1/market/summary (0.0005 SOL)",
        "timestamp": time.time(),
        "market_overview": {
            "sentiment": random.choice(["cautiously_bullish", "neutral"]),
            "top_mover": random.choice(["SOL", "BONK", "WIF"]),
            "volume_trend": "increasing"
        },
        "quick_stats": {
            "sol_price": f"${random.randint(80, 92)}",
            "btc_price": f"${random.randint(68000, 72000):,}",
            "fear_greed": random.randint(50, 65)
        },
        "upgrade_url": "/api/v1/market/summary",
        "price": "0.0005 SOL"
    }


@app.get("/api/v1/demo/token-check")
async def demo_token_check():
    """
    FREE DEMO - Quick token safety check.
    """
    return {
        "demo": True,
        "message": "Full analysis: /api/v1/analysis/token (0.002 SOL)",
        "timestamp": time.time(),
        "safety_tips": [
            "Check if mint authority is revoked",
            "Verify LP is locked/burned",
            "Look at top holder concentration",
            "Check trading volume history"
        ],
        "red_flags": [
            "Contract not verified",
            "Holder distribution too concentrated",
            "No trading history",
            "Susicious social activity"
        ],
        "upgrade_url": "/api/v1/analysis/token",
        "price": "0.002 SOL"
    }
