# AI-trending-topics-crawler-and-publisher

This project is an automated Python system that crawls the top 10 trending AI topics per category from X.com (Twitter), summarizes and categorizes them, and publishes a daily markdown newsletter to the `AI-newsletter` folder and your GitHub repository. Each day's file is named `<date>-ai-newsletter.md`.

## Features
- Crawls trending AI topics and categorizes them (e.g., AI Prompts, AI Agents, AI MCP Servers, AI Learnings, AI Resources)
- Summarizes and formats results in both JSON and Markdown
- Saves daily newsletters in `AI-newsletter/` with date-based filenames
- Publishes newsletters to your GitHub repository (requires credentials)
- Modular, testable Python codebase
- Logging for all workflow steps and errors
- (Optional) Error notification hooks for failures

## Running the Workflow
1. Install dependencies: `pip install -r requirements.txt`
2. Set required environment variables in a `.env` file:
   ```
   X_BEARER_TOKEN=your_x_bearer_token
   GITHUB_TOKEN=your_github_token
   GITHUB_REPO=yourusername/yourrepo
   GITHUB_BRANCH=main
   ```
3. Run the main workflow: `python main.py`

## Running Tests
- All unit tests are in the `tests/` directory.
- Run tests with: `pytest tests/`

## Logging & Error Notification
- All steps and errors are logged to the console.
- You can add your own notification logic (e.g., email, Slack, webhook) in the error handling sections of `main.py` and `publisher.py`.
