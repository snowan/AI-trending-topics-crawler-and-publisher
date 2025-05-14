from categorizer import TopicCategorizer

def test_categorize():
    categories = ['AI Prompts', 'AI Agents', 'AI MCP Servers', 'AI Learnings', 'AI Resources']
    categorizer = TopicCategorizer(categories)
    topics = [
        {'text': 'Prompt engineering', 'link': 'x1'},
        {'text': 'Agent update', 'link': 'x2'},
        {'text': 'MCP server news', 'link': 'x3'},
        {'text': 'Learning AI', 'link': 'x4'},
        {'text': 'Resource list', 'link': 'x5'},
    ]
    result = categorizer.categorize(topics)
    assert len(result['AI Prompts']) == 1
    assert len(result['AI Agents']) == 1
    assert len(result['AI MCP Servers']) == 1
    assert len(result['AI Learnings']) == 1
    assert len(result['AI Resources']) == 1 