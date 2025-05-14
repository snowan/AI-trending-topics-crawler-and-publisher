class TopicSummarizer:
    """Summarizes each topic with a concise title."""
    def summarize(self, categorized_topics):
        summarized = {}
        for cat, topics in categorized_topics.items():
            summarized[cat] = []
            for topic in topics:
                title = topic['text'][:100]
                summarized[cat].append({
                    'title': title,
                    'sources': [topic['link']],
                })
        return summarized 