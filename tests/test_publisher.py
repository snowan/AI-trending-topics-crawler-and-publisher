from publisher import NewsletterPublisher
import logging
from unittest.mock import patch, MagicMock

def test_publish(monkeypatch, caplog):
    publisher = NewsletterPublisher()
    # Mock Github and repo methods
    with patch("publisher.Github") as MockGithub:
        mock_repo = MagicMock()
        MockGithub.return_value.get_repo.return_value = mock_repo
        mock_repo.get_contents.side_effect = Exception("Not found")
        mock_repo.create_file.return_value = None
        with caplog.at_level(logging.INFO):
            publisher.publish('AI-newsletter/2025-05-13-ai-newsletter.md', 'Add AI newsletter for 2025-05-13')
            assert "Created" in caplog.text or "Updated" in caplog.text 