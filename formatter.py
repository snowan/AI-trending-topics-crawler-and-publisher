class NewsletterFormatter:
    """Formats summarized topics into markdown newsletter."""
    def to_markdown(self, summarized, date):
        md = f"# AI Newsletter — Top 10 Trending AI Topics per Category on X.com ({date})\n\n"
        for cat, topics in summarized.items():
            md += f"## {cat}\n"
            for i, topic in enumerate(topics[:10], 1):
                md += f"{i}. **{topic['title']}**\n"
                for src in topic['sources']:
                    md += f"   - [{src}]({src})\n"
            md += "\n"
        return md 