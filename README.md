# AI-trending-topics-crawler-and-publisher

This project is an automated Python system that crawls the top 10 trending AI topics per category from X.com (Twitter), summarizes and categorizes them, and publishes a daily markdown newsletter to the `AI-newsletter` folder. Each day's file is named `<date>-ai-newsletter.md`.

## Features
- Crawls trending AI topics and categorizes them (e.g., AI Prompts, AI Agents, AI MCP Servers, AI Learnings, AI Resources)
- Summarizes and formats results in both JSON and Markdown
- Saves daily newsletters in `AI-newsletter/` with date-based filenames
- Automated GitHub publishing
- Modular, testable Python codebase

## Running the Workflow
1. Install dependencies: `pip install -r requirements.txt`
2. Set required environment variables (see PRD for details)
3. Run the main workflow: `python main.py`

## Running Tests
- All unit tests are in the `tests/` directory.
- Run tests with: `pytest tests/`
