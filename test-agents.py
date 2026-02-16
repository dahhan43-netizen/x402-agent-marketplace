#!/usr/bin/env python3
"""
x402 Agent Marketplace - Usage Examples

How to call each agent with payment verification.
"""
import asyncio
import httpx

WALLET = "9iQLts25aPXRMn4CBxSm5H6kCnFDMKijsZSBebAnjXxb"
BASE_URL = "http://localhost:8000"

def make_payment_header(signature: str, amount: float) -> str:
    """Create X-SOL-Payment header."""
    return f"{WALLET}:{signature}:{amount}"

async def test_agent(endpoint: str, name: str, price: float):
    """Test an agent endpoint."""
    print(f"\n🤖 Testing {name} ({endpoint})")
    print("-" * 40)
    
    # For demo, use a fake signature
    fake_sig = "DEMO_SIGNATURE_PLACEHOLDER"
    header = make_payment_header(fake_sig, price)
    
    try:
        async with httpx.AsyncClient() as client:
            # First call without payment (should return 402)
            r = await client.get(f"{BASE_URL}{endpoint}")
            print(f"Status: {r.status_code}")
            
            if r.status_code == 402:
                print("✅ Payment required (as expected)")
                data = r.json()
                print(f"Required: {data.get('price', 'unknown')} SOL")
                print(f"Wallet: {data.get('recipient')}")
            elif r.status_code == 200:
                print("✅ Success! (payment verified)")
                print(f"Response: {r.json()}")
            else:
                print(f"❌ Unexpected status: {r.status_code}")
                print(f"Response: {r.text[:200]}")
                
    except Exception as e:
        print(f"❌ Error: {e}")

async def list_agents():
    """List all available agents."""
    print("\n📋 Available Agents")
    print("=" * 50)
    
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{BASE_URL}/api/v1/agents")
            if r.status_code == 200:
                data = r.json()
                agents = data.get("agents", {})
                for name, info in agents.items():
                    print(f"\n🤖 {name}")
                    print(f"   Price: {info.get('price_sol', '?')} SOL")
                    print(f"   Endpoint: {info.get('endpoint')}")
                    print(f"   {info.get('description')}")
    except Exception as e:
        print(f"❌ Error: {e}")

async def main():
    """Run all tests."""
    print("🚀 x402 Agent Marketplace - Usage Examples")
    print("=" * 50)
    
    # List agents first
    await list_agents()
    
    # Test each agent
    agents = [
        ("/api/v1/signals/trading", "Trading Signals", 0.001),
        ("/api/v1/analysis/token", "Token Analysis", 0.002),
        ("/api/v1/scanner/memecoin", "Memecoin Scanner", 0.002),
        ("/api/v1/tracker/whale", "Whale Tracker", 0.003),
        ("/api/v1/research", "Research Agent", 0.005),
        ("/api/v1/market/summary", "Market Summary", 0.0005),
        ("/api/v1/sniper/pumpfun", "Pump.fun Sniper", 0.005),
        ("/api/v1/sentiment", "Sentiment Analysis", 0.0005),
    ]
    
    for endpoint, name, price in agents:
        await test_agent(endpoint, name, price)
    
    print("\n" + "=" * 50)
    print("💰 To use with real payment:")
    print("1. Send SOL to:", WALLET)
    print("2. Get transaction signature")
    print("3. Call API with header:")
    print("   X-SOL-Payment: YOUR_WALLET:SIGNATURE:AMOUNT")
    print("\n📖 Docs: http://localhost:8000/docs")

if __name__ == "__main__":
    asyncio.run(main())
