import pytest
from crawler import TrendingTopicsCrawler

def test_fetch_trending_topics():
    crawler = TrendingTopicsCrawler()
    topics = crawler.fetch_trending_topics()
    assert isinstance(topics, list)
    assert len(topics) > 0
    for topic in topics:
        assert 'text' in topic
        assert 'link' in topic 