import os
import requests
from dotenv import load_dotenv
import logging
import time

class TrendingTopicsCrawler:
    """
    Fetches trending topics from X.com (Twitter) API.
    Includes retry logic for rate limiting (429 errors).
    Only includes posts with >500 likes or >20 retweets.
    Note: To avoid hitting rate limits, schedule this workflow to run at most 2 times a day.
    """
    def __init__(self):
        load_dotenv()
        self.bearer_token = os.getenv("X_BEARER_TOKEN")
        self.base_url = "https://api.twitter.com/2/tweets/search/recent"
        self.headers = {"Authorization": f"Bearer {self.bearer_token}"}

    def fetch_trending_topics(self, query="AI OR artificial intelligence OR #AI", max_results=50, retries=3):
        params = {
            "query": query,
            "max_results": max_results,
            "tweet.fields": "created_at,author_id,public_metrics",
        }
        for attempt in range(retries):
            response = requests.get(self.base_url, headers=self.headers, params=params)
            if response.status_code == 200:
                data = response.json()
                topics = []
                for tweet in data.get("data", []):
                    metrics = tweet.get("public_metrics", {})
                    if metrics.get("like_count", 0) > 500 or metrics.get("retweet_count", 0) > 20:
                        topics.append({
                            "text": tweet["text"],
                            "link": f"https://x.com/i/web/status/{tweet['id']}"
                        })
                return topics
            elif response.status_code == 429:
                wait_time = 60 * (2 ** attempt)  # Exponential backoff: 1min, 2min, 4min
                logging.warning(f"Rate limited by Twitter API. Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
            else:
                raise Exception(f"Twitter API error: {response.status_code} {response.text}")
        raise Exception("Exceeded maximum retries due to rate limiting.") 