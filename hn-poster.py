#!/usr/bin/env python3
"""
Hacker News Auto-Poster for x402 Agent Marketplace

Usage:
    python hn-poster.py
    python hn-poster.py --check

Note: HN submissions are manually reviewed and may take hours to appear.
"""

import os
import sys
import requests
from datetime import datetime

GITHUB_LINK = "https://github.com/dahhan43-netizen/x402-agent-marketplace"
TITLE = "15 AI Agents Selling SOL Micro-Payments"
TEXT = """I built x402 Agent Marketplace - 15 AI agents selling SOL micro-payments.

**What it does:**
- Trading signals (0.001 SOL)
- Token analysis (0.002 SOL)
- Memecoin scanner (0.002 SOL)
- Whale tracker (0.003 SOL)
- Research agent (0.005 SOL)
- Market summary (0.0005 SOL)
+ 9 more agents!

**How it works:**
1. Send SOL to the wallet
2. Get transaction signature
3. Call API with payment header
4. Receive AI response instantly!

**Why I built this:**
Most AI tools charge $20-100/month in subscriptions. I wanted pay-per-use with crypto.

**Tech stack:**
- FastAPI (Python)
- Solana blockchain
- x402 payment protocol
- CoinGecko API for market data

**Pricing:**
- From 0.0005 SOL ($0.03) per query
- 90% to developers
- Zero custody

**Links:**
- GitHub: {github}
- Wallet: 9iQLts25aPXRMn4CBxSm5H6kCnFDMKijsZSBebAnjXxb

Would love feedback from the HN community!""".format(github=GITHUB_LINK)

def submit_hn():
    """Submit to Hacker News (requires authentication)."""
    # HN uses a5Cookie for authentication
    cookie = os.environ.get('HN_COOKIE')
    
    if not cookie:
        print("❌ Missing HN cookie!")
        print("\nTo submit to HN:")
        print("1. Go to https://news.ycombinator.com/submit")
        print("2. Login or create account")
        # Or use the direct submit link:
        print(f"\n🔗 Direct submit link:")
        print(f"https://news.ycombinator.com/submitlink?u={GITHUB_LINK}&t={TITLE.replace(' ', '+')}")
        return False
    
    try:
        # HN submit requires specific parameters
        payload = {
            'fnid': '',  # Need to get this from the submit page
            'fnop': 'submit',
            'title': TITLE,
            'url': GITHUB_LINK,
            'text': TEXT
        }
        
        headers = {
            'Cookie': f'a5={cookie}',
            'User-Agent': 'x402-bot/1.0'
        }
        
        response = requests.post(
            'https://news.ycombinator.com/submit',
            data=payload,
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ HN submission received!")
            print("   (May take hours to appear - manually reviewed)")
            return True
        else:
            print(f"❌ HN submission failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error submitting to HN: {e}")
        return False

def print_submit_link():
    """Print the direct submit link."""
    print("\n🔗 Hacker News Submit Link:")
    encoded_url = GITHUB_LINK.replace('&', '%26').replace('=', '%3D')
    encoded_title = TITLE.replace(' ', '+')
    print(f"https://news.ycombinator.com/submitlink?u={encoded_url}&t={encoded_title}")
    print(f"\n📝 Title: {TITLE}")
    print(f"🔗 URL: {GITHUB_LINK}")

if __name__ == "__main__":
    print("🤖 x402 Agent Marketplace - Hacker News")
    print(f"\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print_submit_link()
    print("\n💰 Wallet: 9iQLts25aPXRMn4CBxSm5H6kCnFDMKijsZSBebAnjXxb")
