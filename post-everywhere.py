#!/usr/bin/env python3
"""
Unified Social Media Poster for x402 Agent Marketplace

Posts to X/Twitter, Reddit, and prints links for other platforms.

Usage:
    python post-everywhere.py --twitter
    python post-everywhere.py --reddit
    python post-everywhere.py --all
    python post-everywhere.py --links
"""

import os
import sys
import requests
from datetime import datetime

GITHUB_LINK = "https://github.com/dahhan43-netizen/x402-agent-marketplace"
WALLET = "9iQLts25aPXRMn4CBxSm5H6kCnFDMKijsZSBebAnjXxb"

TWITTER_POST = """15 AI agents selling SOL micro-payments 💸

From 0.0005 SOL. No subscriptions.

Pay per use. 90% to developers.

Built for the future of AI monetization.

Try it: {github}

#Solana #AI #Crypto #Web3""".format(github=GITHUB_LINK)

REDDIT_POSTS = {
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

**Why:** No subscriptions. Pay per use with SOL.

**Wallet:** {wallet}

**GitHub:** {github}

Would love feedback! 🚀""".format(wallet=WALLET, github=GITHUB_LINK)
    }
}

def post_twitter():
    """Post to X/Twitter using API (requires credentials)."""
    api_key = os.environ.get('TWITTER_API_KEY')
    api_secret = os.environ.get('TWITTER_API_SECRET')
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_secret = os.environ.get('TWITTER_ACCESS_SECRET')
    
    if not all([api_key, api_secret, access_token, access_secret]):
        print("❌ Missing Twitter credentials!")
        print("\n🔗 Direct X post link:")
        encoded = TWITTER_POST.replace(' ', '%20').replace('\n', '%0A')
        print(f"https://twitter.com/intent/tweet?text={encoded}")
        return False
    
    print("✅ Would post to Twitter (API credentials found)")
    print("   Use the baoyu-post-to-x skill for actual posting")
    return True

def post_reddit():
    """Post to Reddit (requires credentials)."""
    client_id = os.environ.get('REDDIT_CLIENT_ID')
    client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
    
    if not all([client_id, client_secret]):
        print("\n🔗 Reddit submit links:")
        for sub, content in REDDIT_POSTS.items():
            encoded_url = GITHUB_LINK.replace('&', '%26').replace('=', '%3D')
            encoded_title = content['title'].replace(' ', '+')
            print(f"  r/{sub}: https://reddit.com/r/{sub}/submit?url={encoded_url}&title={encoded_title}")
        return False
    
    print("✅ Reddit API credentials found (use reddit-poster.py)")
    return True

def print_all_links():
    """Print all platform submit links."""
    print("\n" + "="*60)
    print("  🔗 ALL PLATFORM LINKS")
    print("="*60)
    
    print("\n📱 Twitter/X:")
    encoded = TWITTER_POST.replace(' ', '%20').replace('\n', '%0A')
    print(f"   https://twitter.com/intent/tweet?text={encoded}")
    
    print("\n📝 Reddit:")
    for sub, content in REDDIT_POSTS.items():
        encoded_url = GITHUB_LINK.replace('&', '%26').replace('=', '%3D')
        encoded_title = content['title'].replace(' ', '+')
        print(f"   r/{sub}: https://reddit.com/r/{sub}/submit?url={encoded_url}&title={encoded_title}")
    
    print("\n👾 Hacker News:")
    encoded_url = GITHUB_LINK.replace('&', '%26').replace('=', '%3D')
    encoded_title = "15 AI Agents Selling SOL Micro-Payments".replace(' ', '+')
    print(f"   https://news.ycombinator.com/submitlink?u={encoded_url}&t={encoded_title}")
    
    print("\n💼 Indie Hackers:")
    print("   https://www.indiehackers.com/post")
    
    print("\n🚀 Product Hunt:")
    print("   https://www.producthunt.com/products/new")
    
    print("\n" + "="*60)
    print(f"  💰 WALLET: {WALLET}")
    print(f"  🔗 GITHUB: {GITHUB_LINK}")
    print("="*60)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Post to social media')
    parser.add_argument('--twitter', action='store_true', help='Post to Twitter')
    parser.add_argument('--reddit', action='store_true', help='Post to Reddit')
    parser.add_argument('--all', action='store_true', help='Post to all')
    parser.add_argument('--links', action='store_true', help='Show all links')
    
    args = parser.parse_args()
    
    print("\n🤖 x402 Agent Marketplace - Social Poster")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if args.links or not any([args.twitter, args.reddit, args.all]):
        print_all_links()
    
    if args.twitter or args.all:
        post_twitter()
    
    if args.reddit or args.all:
        post_reddit()
    
    print(f"\n💰 Wallet: {WALLET}")
    print(f"🔗 GitHub: {GITHUB_LINK}")

if __name__ == "__main__":
    main()
