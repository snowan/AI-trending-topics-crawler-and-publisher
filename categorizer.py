class TopicCategorizer:
    """Categorizes topics into predefined categories."""
    def __init__(self, categories):
        self.categories = categories
        self.keywords = {
            'AI Prompts': ['prompt'],
            'AI Agents': ['agent'],
            'AI MCP Servers': ['MCP server'],
            'AI Learnings': ['learning', 'learn'],
            'AI Resources': ['resource'],
        }

    def categorize(self, topics):
        categorized = {cat: [] for cat in self.categories}
        for topic in topics:
            assigned = False
            for cat, kws in self.keywords.items():
                if any(kw.lower() in topic['text'].lower() for kw in kws):
                    categorized[cat].append(topic)
                    assigned = True
                    break
            if not assigned:
                categorized.setdefault('Other', []).append(topic)
        return categorized 