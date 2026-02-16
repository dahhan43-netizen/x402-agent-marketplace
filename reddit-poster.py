#!/usr/bin/env python3
"""
Reddit Auto-Poster for x402 Agent Marketplace

Requires praw library:
    pip install praw

Setup:
1. Create Reddit app: https://www.reddit.com/prefs/apps
2. Set environment variables:
    export REDDIT_CLIENT_ID=your_client_id
    export REDDIT_CLIENT_SECRET=your_client_secret
    export REDDIT_USERNAME=your_username
    export REDDIT_PASSWORD=your_password
"""

import os
import sys
import praw
from datetime import datetime

# Reddit credentials from environment
CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET')
USERNAME = os.environ.get('REDDIT_USERNAME')
PASSWORD = os.environ.get('REDDIT_PASSWORD')

REDDIT_WALLET = "9iQLts25aPXRMn4CBxSm5H6kCnFDMKijsZSBebAnjXxb"
GITHUB_LINK = "https://github.com/dahhan43-netizen/x402-agent-marketplace"

SUBREDDITS = {
    "CryptoCurrency": {
        "title": "I built 15 AI agents that sell SOL micro-payments 🎉",
        "body": """I built x402 Agent Marketplace - 15 AI agents selling SOL micro-payments!

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
I wanted AI agents that GENERATE income, not cost subscriptions.

**Wallet:** {wallet}

**GitHub:** {github}

Would love feedback! 🚀""".format(wallet=REDDIT_WALLET, github=GITHUB_LINK)
    },
    "solana": {
        "title": "Built on Solana: 15 AI Agents Selling SOL Micro-Payments",
        "body": """Hey Solana community! 👋

Built x402 Agent Marketplace - 15 AI agents selling SOL micro-payments on Solana!

**Agents:**
- Trading Signals - 0.001 SOL
- Token Analysis - 0.002 SOL
- Memecoin Scanner - 0.002 SOL
- Whale Tracker - 0.003 SOL
- And 10 more!

**Try it:**
{github}

**Wallet:** {wallet}

Built this to explore AI + Solana monetization. Thoughts?""".format(github=GITHUB_LINK, wallet=REDDIT_WALLET)
    },
    "AI_Agents": {
        "title": "15 AI Agents Selling Crypto Micro-Payments - Pay Per Use",
        "body": """Built 15 AI agents that sell SOL micro-payments!

**Pricing:**
- From 0.0005 SOL ($0.03)
- Up to 0.005 SOL ($0.30)

**Agents:**
- Trading signals
- Token analysis
- Research
- Market summaries
- Memecoin scanner
- Whale tracking

**Tech:** FastAPI + Solana + x402 protocol

Open source: {github}

Thoughts on AI agent monetization?""".format(github=GITHUB_LINK)
    }
}

def post_to_reddit(subreddit_name, title, body):
    """Post to a specific subreddit."""
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent="x402-bot/1.0",
            username=USERNAME,
            password=PASSWORD
        )
        
        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title, body)
        
        print(f"✅ Posted to r/{subreddit_name}!")
        print(f"   URL: https://reddit.com{submission.permalink}")
        return True
        
    except Exception as e:
        print(f"❌ Error posting to r/{subreddit_name}: {e}")
        return False

def post_all():
    """Post to all configured subreddits."""
    if not all([CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD]):
        print("❌ Missing Reddit credentials!")
        print("\nSet these environment variables:")
        print("  export REDDIT_CLIENT_ID=your_client_id")
        print("  export REDDIT_CLIENT_SECRET=your_client_secret")
        print("  export REDDIT_USERNAME=your_username")
        print("  export REDDIT_PASSWORD=your_password")
        return False
    
    print("🤖 x402 Agent Marketplace - Reddit Auto-Poster")
    print(f"\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    success_count = 0
    for subreddit_name, content in SUBREDDITS.items():
        print(f"\n📤 Posting to r/{subreddit_name}...")
        if post_to_reddit(subreddit_name, content['title'], content['body']):
            success_count += 1
        # Small delay to avoid rate limiting
        import time
        time.sleep(2)
    
    print(f"\n✅ Posted to {success_count}/{len(SUBREDDITS)} subreddits")
    print(f"\n💰 Wallet: {REDDIT_WALLET}")
    print(f"🔗 GitHub: {GITHUB_LINK}")
    
    return success_count > 0

if __name__ == "__main__":
    post_all()
