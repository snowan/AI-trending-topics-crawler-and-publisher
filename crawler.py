class TrendingTopicsCrawler:
    """Fetches trending topics from X.com (Twitter)."""
    def fetch_trending_topics(self):
        # Mock data for testing: list of dicts with 'text' and 'link'
        return [
            {'text': 'Prompt engineering breakthrough', 'link': 'https://x.com/tweet1'},
            {'text': 'New AI agent released', 'link': 'https://x.com/tweet2'},
            {'text': 'MCP server open source', 'link': 'https://x.com/tweet3'},
            {'text': 'Top AI learning resources', 'link': 'https://x.com/tweet4'},
            {'text': 'Prompt tips for GPT-4', 'link': 'https://x.com/tweet5'},
        ] 