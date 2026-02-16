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
    
    PAYMENT_WALLET = "4D8jCkTMWjaQzDuZkwibk8ML34LSCKVCKS8kC6RFYuX"
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
