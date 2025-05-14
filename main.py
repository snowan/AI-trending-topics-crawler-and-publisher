from crawler import TrendingTopicsCrawler
from categorizer import TopicCategorizer
from summarizer import TopicSummarizer
from formatter import NewsletterFormatter
from publisher import NewsletterPublisher
from filtering import is_relevant_to_ai
import os
from datetime import datetime
import logging

CATEGORIES = os.getenv('AI_CATEGORIES', 'AI prompts,AI agents,AI MCP servers,AI models,AI resources').split(',')
OUTPUT_DIR = os.getenv('NEWSLETTER_OUTPUT_DIR', 'AI-newsletter')
logging.basicConfig(level=logging.INFO)

def main():
    try:
        logging.info('Starting AI newsletter workflow')
        # 1. Crawl trending topics
        logging.info('Crawling trending topics...')
        crawler = TrendingTopicsCrawler()
        raw_topics = crawler.fetch_trending_topics()

        # 1.5. Filter for AI relevance
        logging.info('Filtering for AI relevance...')
        raw_topics = [t for t in raw_topics if is_relevant_to_ai(t['text'])]
        logging.info(f'{len(raw_topics)} relevant topics after filtering.')

        # 2. Categorize topics
        logging.info('Categorizing topics...')
        categorizer = TopicCategorizer(categories=CATEGORIES)
        categorized_topics = categorizer.categorize(raw_topics)

        # 3. Summarize topics
        logging.info('Summarizing topics...')
        summarizer = TopicSummarizer()
        summarized = summarizer.summarize(categorized_topics)

        # 4. Format newsletter
        logging.info('Formatting newsletter...')
        formatter = NewsletterFormatter()
        today = datetime.now().strftime('%Y-%m-%d')
        md_filename = f"{today}-ai-newsletter.md"
        md_path = os.path.join(OUTPUT_DIR, md_filename)
        md_content = formatter.to_markdown(summarized, date=today)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        logging.info(f'Newsletter saved to {md_path}')

        # 5. Publish to GitHub
        logging.info('Publishing to GitHub...')
        publisher = NewsletterPublisher()
        publisher.publish(md_path, commit_message=f"Add AI newsletter for {today}")
        logging.info('Workflow completed successfully')
    except Exception as e:
        logging.error(f'Workflow failed: {e}')
        # Optionally: send notification here

if __name__ == "__main__":
    main() 