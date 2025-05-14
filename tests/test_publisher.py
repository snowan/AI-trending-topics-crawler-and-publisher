from publisher import NewsletterPublisher

def test_publish(capsys):
    publisher = NewsletterPublisher()
    publisher.publish('AI-newsletter/2025-05-13-ai-newsletter.md', 'Add AI newsletter for 2025-05-13')
    captured = capsys.readouterr()
    assert "Publishing AI-newsletter/2025-05-13-ai-newsletter.md to GitHub" in captured.out 