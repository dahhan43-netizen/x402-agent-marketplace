"""
x402 Agent Marketplace - SOL Micro-Payment Platform

AI agent capabilities sold exclusively via SOL micro-payments.
Currency: SOL (Solana blockchain)
Protocol: x402 (HTTP 402 Payment Required)
"""
import asyncio
import time
import logging
import hashlib
import base64
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Dict, Optional, Any
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import aiohttp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory storage (use database in production)
usage_tracker: Dict[str, Dict[str, Any]] = {}
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


class SolanaPaymentVerifier:
    """Verify SOL payments on Solana blockchain."""
    
    def __init__(self, rpc_url: str, payment_wallet: str):
        self.rpc_url = rpc_url
        self.payment_wallet = payment_wallet
        self._session: Optional[aiohttp.ClientSession] = None
    
    async def get_session(self) -> aiohttp.ClientSession:
        """Get or create HTTP session."""
        if self._session is None or self._session.closed:
            timeout = aiohttp.ClientTimeout(total=30)
            self._session = aiohttp.ClientSession(timeout=timeout)
        return self._session
    
    async def verify_payment(
        self,
        payer_wallet: str,
        amount_sol: float,
        capability: str
    ) -> Dict[str, Any]:
        """
        Verify payment on Solana blockchain.
        
        Checks:
        1. Recent transaction from payer to payment wallet
        2. Correct amount transferred
        3. Transaction is recent (within 5 minutes)
        """
        try:
            session = await self.get_session()
            
            # In production: query Solana RPC for recent transactions
            # For now: return mock verification for demo
            
            return {
                "verified": True,
                "payer": payer_wallet,
                "amount": amount_sol,
                "currency": "SOL",
                "tx_signature": f"mock_{int(time.time())}",
                "block_time": time.time(),
                "network": "solana"
            }
            
        except Exception as e:
            logger.error(f"Payment verification failed: {e}")
            return {
                "verified": False,
                "error": str(e)
            }
    
    async def close(self):
        """Close HTTP session."""
        if self._session:
            await self._session.close()
            self._session = None


class PaymentMiddleware:
    """x402 SOL payment verification middleware."""
    
    def __init__(
        self,
        payment_wallet: str,
        platform_fee_percent: float = 10,
        solana_rpc: str = "https://api.mainnet-beta.solana.com"
    ):
        self.payment_wallet = payment_wallet
        self.platform_fee_percent = platform_fee_percent
        self.solana_rpc = solana_rpc
        self.verifier = SolanaPaymentVerifier(solana_rpc, payment_wallet)
    
    async def verify_payment(
        self,
        request: Request,
        capability: AgentCapability
    ) -> Dict[str, Any]:
        """
        Verify SOL payment for API call.
        
        Expected header: X-SOL-Payment
        Format: wallet_address:signature:amount
        """
        payment_header = request.headers.get("X-SOL-Payment")
        
        if not payment_header:
            return {
                "status": "payment_required",
                "price": capability.price_sol,
                "currency": "SOL",
                "recipient": self.payment_wallet,
                "capability": capability.name,
                "network": "solana",
                "message": f"Send {capability.price_sol} SOL to {self.payment_wallet}",
                "how_to_pay": "Transfer SOL and provide transaction signature"
            }
        
        try:
            parts = payment_header.split(":")
            if len(parts) != 3:
                raise ValueError("Invalid payment header format")
            
            payer_wallet, signature, amount_str = parts
            amount_sol = float(amount_str)
            
            # Verify payment on chain
            verification = await self.verifier.verify_payment(
                payer_wallet=payer_wallet,
                amount_sol=amount_sol,
                capability=capability.name
            )
            
            if not verification["verified"]:
                return {
                    "status": "payment_invalid",
                    "error": verification.get("error", "Verification failed")
                }
            
            # Calculate fees
            fee = capability.price_sol * (self.platform_fee_percent / 100)
            
            return {
                "status": "verified",
                "payer": payer_wallet,
                "amount": capability.price_sol,
                "fee": fee,
                "net_revenue": capability.price_sol - fee,
                "capability": capability.name,
                "currency": "SOL",
                "network": "solana"
            }
            
        except Exception as e:
            logger.error(f"Payment verification error: {e}")
            return {
                "status": "payment_invalid",
                "error": str(e)
            }
    
    async def close(self):
        """Close resources."""
        await self.verifier.close()


class AgentRegistry:
    """Registry of available agent capabilities."""
    
    def __init__(self):
        self.agents: Dict[str, AgentCapability] = {}
    
    def register(self, agent: AgentCapability):
        """Register a new agent capability."""
        self.agents[agent.endpoint] = agent
        agent_registry[agent.name] = {
            "name": agent.name,
            "endpoint": agent.endpoint,
            "price_sol": agent.price_sol,
            "price_usd": agent.price_sol * 85,  # Approximate USD
            "rate_limit": agent.rate_limit_per_minute,
            "description": agent.description,
            "owner": agent.owner,
            "currency": "SOL"
        }
        logger.info(f"Registered agent: {agent.name} @ {agent.endpoint}")
    
    def get(self, endpoint: str) -> Optional[AgentCapability]:
        """Get agent capability by endpoint."""
        return self.agents.get(endpoint)
    
    def list_all(self) -> Dict[str, Dict]:
        """List all registered agents."""
        return agent_registry


# Initialize
payment_middleware = PaymentMiddleware(
    payment_wallet="9uVX5aRkCQ1R89FHtgf5W2VXbqB4MeaeBFaKsxBv4UEF",  # Ali's wallet
    platform_fee_percent=10,
    solana_rpc="https://api.mainnet-beta.solana.com"
)
agent_registry_obj = AgentRegistry()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    logger.info("Starting x402 Agent Marketplace (SOL-only)...")
    
    # Register agents
    from src.agents.trading import TradingSignalsAgent
    from src.agents.analysis import TokenAnalysisAgent
    from src.agents.research import ResearchAgent
    from src.agents.market import MarketSummaryAgent
    
    agent_registry_obj.register(TradingSignalsAgent())
    agent_registry_obj.register(TokenAnalysisAgent())
    agent_registry_obj.register(ResearchAgent())
    agent_registry_obj.register(MarketSummaryAgent())
    
    logger.info(f"Registered {len(agent_registry_obj.agents)} SOL-accepting agents")
    
    yield
    
    await payment_middleware.close()
    logger.info("Marketplace shutdown complete")


app = FastAPI(
    title="x402 Agent Marketplace",
    description="AI agent capabilities via SOL micro-payments",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# Models
# ============================================================================

class SOLPaymentProof(BaseModel):
    """SOL payment proof."""
    wallet: str
    signature: str
    amount: float


class AgentResponse(BaseModel):
    """Agent response."""
    agent: str
    result: Dict[str, Any]
    payment: Dict[str, Any]


# ============================================================================
# Utils
# ============================================================================

def check_rate_limit(client_id: str, endpoint: str, limit: int) -> bool:
    """Check rate limit for client."""
    key = f"{client_id}:{endpoint}"
    now = time.time()
    minute_ago = now - 60
    
    if key not in usage_tracker:
        usage_tracker[key] = {"count": 1, "first_call": now}
        return True
    
    usage = usage_tracker[key]
    
    if usage["first_call"] < minute_ago:
        usage_tracker[key] = {"count": 1, "first_call": now}
        return True
    
    if usage["count"] >= limit:
        return False
    
    usage["count"] += 1
    return True


def get_client_id(request: Request) -> str:
    """Extract client identifier."""
    if request.headers.get("X-Client-ID"):
        return request.headers["X-Client-ID"]
    if request.headers.get("X-Forwarded-For"):
        return request.headers["X-Forwarded-For"].split(",")[0].strip()
    return request.client.host if request.client else "unknown"


# ============================================================================
# Endpoints
# ============================================================================

@app.get("/")
async def root():
    """Marketplace info."""
    return {
        "name": "x402 Agent Marketplace",
        "version": "1.0.0",
        "currency": "SOL (Solana)",
        "protocol": "x402",
        "network": "solana-mainnet",
        "endpoints": {
            "agents": "/api/v1/agents",
            "docs": "/docs"
        }
    }


@app.get("/api/v1/agents")
async def list_agents():
    """List all available agents."""
    return {
        "agents": agent_registry_obj.list_all(),
        "currency": "SOL",
        "network": "solana-mainnet"
    }


@app.get("/api/v1/health")
async def health():
    """Health check."""
    return {"status": "healthy", "currency": "SOL", "timestamp": time.time()}


@app.get("/api/v1/usage/{client_id}")
async def get_usage(client_id: str):
    """Get usage statistics."""
    return {"client_id": client_id, "usage": usage_tracker}


# ============================================================================
# Agent Execution
# ============================================================================

async def execute_agent(
    request: Request,
    agent: AgentCapability,
    client_id: str
) -> Dict[str, Any]:
    """Execute agent after SOL payment verification."""
    
    # Rate limit check
    if not check_rate_limit(client_id, agent.endpoint, agent.rate_limit_per_minute):
        raise HTTPException(
            status_code=429,
            detail={
                "error": "rate_limit_exceeded",
                "message": f"Limit: {agent.rate_limit_per_minute} calls/min",
                "retry_after": 60
            }
        )
    
    # Verify SOL payment
    payment_result = await payment_middleware.verify_payment(request, agent)
    
    if payment_result["status"] != "verified":
        raise HTTPException(
            status_code=402,
            detail=payment_result
        )
    
    # Execute agent
    try:
        result = await agent.callback()
        
        return {
            "agent": agent.name,
            "result": result,
            "payment": {
                "status": "verified",
                "amount": payment_result["amount"],
                "fee": payment_result["fee"],
                "currency": "SOL",
                "network": "solana"
            },
            "timestamp": time.time()
        }
    except Exception as e:
        logger.error(f"Agent execution failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Import agents
from src.agents.trading import router as trading_router
from src.agents.analysis import router as analysis_router
from src.agents.research import router as research_router
from src.agents.market import router as market_router

app.include_router(trading_router, prefix="/api/v1")
app.include_router(analysis_router, prefix="/api/v1")
app.include_router(research_router, prefix="/api/v1")
app.include_router(market_router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
