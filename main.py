from crawler import TrendingTopicsCrawler
from categorizer import TopicCategorizer
from summarizer import TopicSummarizer
from formatter import NewsletterFormatter
from publisher import NewsletterPublisher
import os
from datetime import datetime

CATEGORIES = os.getenv('AI_CATEGORIES', 'AI Prompts,AI Agents,AI MCP Servers,AI Learnings,AI Resources').split(',')
OUTPUT_DIR = os.getenv('NEWSLETTER_OUTPUT_DIR', 'AI-newsletter')

def main():
    # 1. Crawl trending topics
    crawler = TrendingTopicsCrawler()
    raw_topics = crawler.fetch_trending_topics()

    # 2. Categorize topics
    categorizer = TopicCategorizer(categories=CATEGORIES)
    categorized_topics = categorizer.categorize(raw_topics)

    # 3. Summarize topics
    summarizer = TopicSummarizer()
    summarized = summarizer.summarize(categorized_topics)

    # 4. Format newsletter
    formatter = NewsletterFormatter()
    today = datetime.now().strftime('%Y-%m-%d')
    md_filename = f"{today}-ai-newsletter.md"
    md_path = os.path.join(OUTPUT_DIR, md_filename)
    md_content = formatter.to_markdown(summarized, date=today)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    # 5. Publish to GitHub
    publisher = NewsletterPublisher()
    publisher.publish(md_path, commit_message=f"Add AI newsletter for {today}")

if __name__ == "__main__":
    main() 