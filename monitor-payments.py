#!/usr/bin/env python3
"""
x402 Agent Marketplace - Payment Monitor

Checks wallet balance and logs transactions.
"""
import asyncio
import httpx
import time

WALLET = "9uVX5aRkCQ1R89FHtgf5W2VXbqB4MeaeBFaKsxBv4UEF"
HELIUS_API = "c28c481f-866c-4f42-b2d0-62e428475b68"

async def check_balance():
    """Check wallet SOL balance."""
    url = f"https://api.mainnet-beta.solana.com"
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [WALLET]
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(url, json=payload, headers=headers, timeout=10)
            data = r.json()
            if "result" in data:
                lamports = data["result"]["value"]
                sol = lamports / 1_000_000_000
                return sol
    except Exception as e:
        print(f"Error: {e}")
    return None

async def get_recent_transactions():
    """Get recent transactions for wallet."""
    # Using Helius for better API
    url = f"https://api.helius.xyz.com/v0/addresses/{WALLET}/transactions?api-key={HELIUS_API}"
    
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url, timeout=10)
            if r.status_code == 200:
                return r.json()
    except Exception as e:
        print(f"Error getting transactions: {e}")
    return []

async def monitor():
    """Main monitoring loop."""
    print(f"🔍 Monitoring wallet: {WALLET}")
    print("-" * 50)
    
    last_balance = None
    
    while True:
        try:
            balance = await check_balance()
            if balance is not None:
                if balance != last_balance:
                    if last_balance is not None:
                        change = balance - last_balance
                        print(f"💰 BALANCE: {balance:.4f} SOL ({change:+.4f} since last check)")
                    else:
                        print(f"💰 Current balance: {balance:.4f} SOL")
                    last_balance = balance
                
                # Check for new transactions
                transactions = await get_recent_transactions()
                if transactions:
                    latest = transactions[0] if transactions else None
                    if latest:
                        print(f"📝 Latest: {latest.get('type', 'unknown')} - {latest.get('status', 'unknown')}")
            
            await asyncio.sleep(60)  # Check every minute
            
        except KeyboardInterrupt:
            print("\n👋 Stopping monitor...")
            break

if __name__ == "__main__":
    print("🚀 x402 Agent Marketplace - Payment Monitor")
    print("=" * 50)
    asyncio.run(monitor())
