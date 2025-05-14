import os
from github import Github
from dotenv import load_dotenv
import logging

class NewsletterPublisher:
    """Publishes the newsletter markdown file to GitHub."""
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("GITHUB_TOKEN")
        self.repo_name = os.getenv("GITHUB_REPO")
        self.branch = os.getenv("GITHUB_BRANCH", "main")
        logging.basicConfig(level=logging.INFO)

    def publish(self, file_path, commit_message):
        try:
            g = Github(self.token)
            repo = g.get_repo(self.repo_name)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Path in repo (strip local folder prefix if present)
            repo_path = file_path
            if repo_path.startswith("AI-newsletter/"):
                repo_path = repo_path[len("AI-newsletter/"):]
            repo_path = f"AI-newsletter/{repo_path}" if not repo_path.startswith("AI-newsletter/") else repo_path
            # Check if file exists
            try:
                contents = repo.get_contents(repo_path, ref=self.branch)
                repo.update_file(repo_path, commit_message, content, contents.sha, branch=self.branch)
                logging.info(f"Updated {repo_path} in {self.repo_name} on branch {self.branch}")
            except Exception:
                repo.create_file(repo_path, commit_message, content, branch=self.branch)
                logging.info(f"Created {repo_path} in {self.repo_name} on branch {self.branch}")
        except Exception as e:
            logging.error(f"Failed to publish newsletter: {e}")
            # Optionally: send notification here 