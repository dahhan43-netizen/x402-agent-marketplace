#!/usr/bin/env python3
"""
X/Twitter Auto-Poster for x402 Agent Marketplace

Usage:
    python post-to-x.py --message "Your tweet here"
    python post-to-x.py --file tweets.txt

Requires:
    pip install tweepy
    Set TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
"""

import os
import sys
import argparse
from datetime import datetime

# Sample tweets for x402 Agent Marketplace
TWEETS = [
    "15 AI agents selling SOL micro-payments 💸\n\nFrom 0.0005 SOL. No subscriptions.\n\nTry it: https://github.com/dahhan43-netizen/x402-agent-marketplace\n\n#Solana #AI #Crypto",
    
    "I built 15 AI agents that earn SOL while you sleep 🛌💰\n\nNo subscriptions. Pay per use.\n\nThe future of AI monetization is here.\n\nhttps://github.com/dahhan43-netizen/x402-agent-marketplace",
    
    "Trading signals, token analysis, research, whale tracking...\n\n15 AI agents. SOL payments.\n\nFrom 0.0005 SOL.\n\nBuilt for developers who want their AI to earn.\n\nhttps://github.com/dahhan43-netizen/x402-agent-marketplace",
    
    "Most AI tools cost $50/month.\n\nMine costs $0.03 per query.\n\nPay-per-use AI via Solana.\n\n15 agents available now.\n\nhttps://github.com/dahhan43-netizen/x402-agent-marketplace",
    
    "AI agents should GENERATE income, not cost subscriptions.\n\nThat's why I built x402 Agent Marketplace.\n\n90% to developers. Zero custody.\n\nTry it: https://github.com/dahhan43-netizen/x402-agent-marketplace",
]

def post_tweet(message: str):
    """Post a tweet (requires Twitter API credentials)."""
    import tweepy
    
    api_key = os.environ.get('TWITTER_API_KEY')
    api_secret = os.environ.get('TWITTER_API_SECRET')
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_secret = os.environ.get('TWITTER_ACCESS_SECRET')
    
    if not all([api_key, api_secret, access_token, access_secret]):
        print("❌ Missing Twitter API credentials!")
        print("\nSet these environment variables:")
        print("  export TWITTER_API_KEY=your_api_key")
        print("  export TWITTER_API_SECRET=your_api_secret")
        print("  export TWITTER_ACCESS_TOKEN=your_access_token")
        print("  export TWITTER_ACCESS_SECRET=your_access_secret")
        return False
    
    try:
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
        
        api.update_status(message)
        print(f"✅ Tweet posted successfully!")
        print(f"\n📝 Message:\n{message}")
        return True
        
    except Exception as e:
        print(f"❌ Error posting tweet: {e}")
        return False

def post_to_reddit(subreddit: str, title: str, body: str):
    """Post to Reddit (requires Reddit API credentials)."""
    import praw
    
    client_id = os.environ.get('REDDIT_CLIENT_ID')
    client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
    user_agent = os.environ.get('REDDIT_USER_AGENT', 'x402-bot/1.0')
    
    if not all([client_id, client_secret]):
        print("❌ Missing Reddit API credentials!")
        print("\nSet these environment variables:")
        print("  export REDDIT_CLIENT_ID=your_client_id")
        print("  export REDDIT_CLIENT_SECRET=your_client_secret")
        return False
    
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        
        subreddit = reddit.subreddit(subreddit)
        subreddit.submit(title, body)
        print(f"✅ Posted to r/{subreddit}!")
        return True
        
    except Exception as e:
        print(f"❌ Error posting to Reddit: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Post to X/Twitter')
    parser.add_argument('--message', '-m', help='Tweet message')
    parser.add_argument('--file', '-f', help='File with tweets (one per line)')
    parser.add_argument('--reddit', '-r', help='Post to subreddit')
    parser.add_argument('--title', '-t', help='Reddit post title')
    parser.add_argument('--random', action='store_true', help='Post random sample tweet')
    
    args = parser.parse_args()
    
    if args.random:
        import random
        message = random.choice(TWEETS)
        print(f"📝 Random tweet selected:")
        print(message)
        post_tweet(message)
    
    elif args.message:
        post_tweet(args.message)
    
    elif args.file:
        with open(args.file, 'r') as f:
            tweets = f.readlines()
        for i, tweet in enumerate(tweets):
            print(f"\n📝 Tweet {i+1}/{len(tweets)}:")
            print(tweet)
            if input("Post? (y/n): ").lower() == 'y':
                post_tweet(tweet)
    
    elif args.reddit and args.title and args.body:
        post_to_reddit(args.reddit, args.title, args.body)
    
    else:
        print("\n🦞 x402 Agent Marketplace - Auto-Poster")
        print("\nUsage:")
        print("  python post-to-x.py -m \"Your tweet here\"")
        print("  python post-to-x.py --random")
        print("  python post-to-x.py -f tweets.txt")
        print("\n📋 Sample tweets:")
        for i, tweet in enumerate(TWEETS[:3], 1):
            print(f"\n{i}. {tweet[:80]}...")
        
        print("\n\n🔗 Links:")
        print("  GitHub: https://github.com/dahhan43-netizen/x402-agent-marketplace")
        print("  Wallet: 9iQLts25aPXRMn4CBxSm5H6kCnFDMKijsZSBebAnjXxb")

if __name__ == "__main__":
    main()
