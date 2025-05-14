from formatter import NewsletterFormatter

def test_to_markdown():
    summarized = {
        'AI Prompts': [
            {'title': 'Prompt engineering', 'sources': ['x1']},
        ],
        'AI Agents': [
            {'title': 'Agent update', 'sources': ['x2']},
        ],
    }
    formatter = NewsletterFormatter()
    md = formatter.to_markdown(summarized, date='2025-05-13')
    assert '# AI Newsletter' in md
    assert '## AI Prompts' in md
    assert '1. **Prompt engineering**' in md
    assert '[x1](x1)' in md
    assert '## AI Agents' in md
    assert '1. **Agent update**' in md
    assert '[x2](x2)' in md 