from summarizer import TopicSummarizer

def test_summarize():
    categorized = {
        'AI Prompts': [{'text': 'Prompt engineering', 'link': 'x1'}],
        'AI Agents': [{'text': 'Agent update', 'link': 'x2'}],
    }
    summarizer = TopicSummarizer()
    result = summarizer.summarize(categorized)
    assert 'AI Prompts' in result
    assert 'AI Agents' in result
    assert result['AI Prompts'][0]['title'] == 'Prompt engineering'
    assert result['AI Prompts'][0]['sources'] == ['x1']
    assert result['AI Agents'][0]['title'] == 'Agent update'
    assert result['AI Agents'][0]['sources'] == ['x2'] 