#!/usr/bin/env python3
"""
Simple Demo Client for x402 Agent Marketplace

Run this to see the agents in action!

Usage:
    python demo_client.py
    python demo_client.py --agent trading
    python demo_client.py --all
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:8000"

DEMO_AGENTS = {
    "trading": {
        "name": "📈 Trading Signals",
        "endpoint": "/api/v1/demo/trading",
        "price": "0.001 SOL",
        "description": "AI-powered market analysis"
    },
    "token": {
        "name": "🔍 Token Analysis", 
        "endpoint": "/api/v1/demo/token",
        "price": "0.002 SOL",
        "description": "Deep dive token metrics"
    },
    "memecoin": {
        "name": "🦨 Memecoin Scanner",
        "endpoint": "/api/v1/demo/memecoin",
        "price": "0.002 SOL",
        "description": "Find emerging tokens"
    },
    "whale": {
        "name": "🐋 Whale Tracker",
        "endpoint": "/api/v1/demo/whale",
        "price": "0.003 SOL",
        "description": "Monitor smart money"
    },
    "research": {
        "name": "📚 Research Agent",
        "endpoint": "/api/v1/demo/research",
        "price": "0.005 SOL",
        "description": "Comprehensive research"
    },
    "summary": {
        "name": "📊 Market Summary",
        "endpoint": "/api/v1/demo/summary",
        "price": "0.0005 SOL",
        "description": "Daily market overview"
    }
}

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def print_agent(agent_key, agent_info):
    print(f"\n{agent_info['name']}")
    print(f"  Price: {agent_info['price']}")
    print(f"  {agent_info['description']}")
    print(f"  Endpoint: {agent_info['endpoint']}")

def call_demo_endpoint(endpoint):
    """Call a demo endpoint and return the response."""
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Status {response.status_code}", "message": response.text}
    except requests.exceptions.ConnectionError:
        return {"error": "Connection failed", "message": "Is the server running?"}
    except Exception as e:
        return {"error": str(e)}

def run_demo(agent_key=None):
    """Run demo for specific agent or all agents."""
    if agent_key and agent_key in DEMO_AGENTS:
        agents_to_run = {agent_key: DEMO_AGENTS[agent_key]}
    else:
        agents_to_run = DEMO_AGENTS
    
    print_header("🤖 x402 Agent Marketplace - Demo")
    print(f"\nBase URL: {BASE_URL}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    for agent_key, agent_info in agents_to_run.items():
        print_agent(agent_key, agent_info)
        
        response = call_demo_endpoint(agent_info['endpoint'])
        
        if "error" in response:
            print(f"  ❌ Error: {response['error']}")
        else:
            print(f"  ✅ Response received!")
            if isinstance(response, dict):
                # Pretty print the response
                preview = json.dumps(response, indent=2)[:500]
                if len(json.dumps(response)) > 500:
                    preview += "\n  ... (truncated)"
                print(f"  {preview}")
        
        time.sleep(0.5)  # Small delay between calls
    
    print_header("💰 To Unlock Full Access")
    print(f"\nWallet: 9iQLts25aPXRMn4CBxSm5H6kCnFDMKijsZSBebAnjXxb")
    print(f"\nGitHub: https://github.com/dahhan43-netizen/x402-agent-marketplace")

def check_server():
    """Check if the server is running."""
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running!")
            return True
    except:
        pass
    print("❌ Server not running. Start it with: python main.py")
    return False

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Demo client for x402 Agent Marketplace')
    parser.add_argument('--agent', '-a', choices=list(DEMO_AGENTS.keys()), help='Specific agent to demo')
    parser.add_argument('--all', '-A', action='store_true', help='Run all demos')
    parser.add_argument('--check', '-c', action='store_true', help='Check if server is running')
    
    args = parser.parse_args()
    
    if args.check:
        check_server()
    elif args.agent:
        run_demo(args.agent)
    elif args.all:
        run_demo()
    else:
        # Show available agents
        print_header("🤖 Available Demo Agents")
        for key, info in DEMO_AGENTS.items():
            print_agent(key, info)
        print("\n\nUsage:")
        print("  python demo_client.py --all          # Run all demos")
        print("  python demo_client.py --agent trading  # Specific agent")
        print("  python demo_client.py --check        # Check server")
        print("\nTo start server: python main.py")
        print("\n💰 Wallet: 9iQLts25aPXRMn4CBxSm5H6kCnFDMKijsZSBebAnjXxb")

if __name__ == "__main__":
    main()
