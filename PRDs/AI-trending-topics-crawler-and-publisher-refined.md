# AI Trending Topics Crawler & Publisher (Refined PRD & Implementation Plan)

---

## Product Requirements Document (PRD)

### Objective

Build a fully automated agent that:
1. Crawls the top 10 trending topics about AI from X.com (Twitter) daily, categorized into distinct areas such as AI Prompts, AI Agents/MCP Servers, AI Models, and AI Resources.
2. **Only includes posts (tweets) as sources if they have more than 500 likes or more than 20 retweets.**
3. Summarizes each topic with a concise, human-readable title and links to all relevant sources.
4. Outputs the results in both structured JSON and Markdown formats, organized by category.
5. Saves the summarized content in a new folder called `AI-newsletter`, with each day's data saved as a new file named `<date>-ai-newsletter.md` (e.g., `2025-05-13-ai-newsletter.md`).
6. Commits and pushes the changes to the repository automatically.

---

### Problem Statement

The rapid pace and volume of AI-related discussions on X.com make it difficult to stay current, especially across different subdomains of AI. There is a need for an automated, reliable, and concise system to aggregate, categorize, summarize, and archive trending AI topics for easy reference and sharing.

---

### Scope

- **In Scope:**
  - Crawling trending AI topics from X.com (Twitter) using public or authenticated APIs.
  - **Filtering to only include posts with >500 likes or >20 retweets.**
  - Categorizing topics into areas such as AI Prompts, AI Agents/MCP Servers, AI Models, and AI Resources (categories can be extended/configured).
  - Summarizing topics with titles and source links.
  - Formatting output as JSON and Markdown, organized by category.
  - Saving output in the `AI-newsletter` folder, with each day's data in a new file named `<date>-ai-newsletter.md`.
  - Automating GitHub commits and pushes.
  - Scheduling the process to run daily (or at a configurable interval).
- **Out of Scope:**
  - Manual curation or editing of topics.
  - Deep content or sentiment analysis.
  - UI/Frontend for browsing the markdown files.

---

### Functional Requirements

#### 1. Data Collection

- **Source:** X.com (Twitter) trending topics.
- **Criteria:**
  - Topics must be related to "AI" (Artificial Intelligence) and further classified into categories such as:
    - AI Prompts
    - AI Agents / MCP Servers
    - AI Models
    - AI Resources
    (Categories should be configurable and extensible.)
  - **Only include posts (tweets) as sources if they have more than 500 likes or more than 20 retweets.**
- **Quantity:** Top 10 trending topics per category.
- **Data Points:**
  - Topic title (brief, human-readable)
  - List of relevant source links (tweets, articles, etc.)
  - Category label
  - Timestamp of data collection
  - **Engagement metrics (likes, retweets) for each post**

#### 2. Categorization & Summarization

- **Process:**
  - For each topic, determine the appropriate category using keyword filtering, NLP, or classification models.
  - Generate a concise summary/title (max 100 characters).
- **Format:**
  - Title (max 100 characters)
  - Bullet-point list of source links
  - Category label

#### 3. Output Formatting

- **JSON Output:**
  - Structure:
    ```json
    [
      {
        "category": "AI Prompts",
        "topics": [
          {
            "title": "Brief summary of the topic",
            "sources": [
              {
                "url": "https://link1.com",
                "like_count": 1234,
                "retweet_count": 56
              }
            ],
            "timestamp": "2024-06-10T12:00:00Z"
          },
          ...
        ]
      },
      ...
    ]
    ```
- **Markdown Output:**
  - Save the markdown file in the `AI-newsletter` folder, with the filename format `<date>-ai-newsletter.md` (e.g., `2025-05-13-ai-newsletter.md`).
  - Structure:
    ```markdown
    # AI Newsletter — Top 10 Trending AI Topics per Category on X.com (<date>)

    ## AI Prompts
    1. **[Topic Title 1]**
       - [Source 1](https://link1.com) (Likes: 1234, Retweets: 56)
    ...
    ```
  - Each category should be a clear section, with up to 10 topics per category, each with its sources and engagement metrics.

#### 4. GitHub Integration

- **Repository:** Configurable target GitHub repo and branch.
- **File Naming:** Each day's markdown file is saved as `AI-newsletter/<date>-ai-newsletter.md` (e.g., `AI-newsletter/2025-05-13-ai-newsletter.md`).
- **Commit Message:** Include date and a brief description (e.g., "Add AI newsletter for 2025-05-13").
- **Push:** Automatically push the commit to the main branch (or configurable branch).
- **Error Handling:** Log and report any failures in commit or push steps.

---

### Non-Functional Requirements

- **Automation:** The process must be fully automated and able to run on a schedule (e.g., via cron or GitHub Actions).
- **Reliability:** Handle API failures, rate limits, and network errors gracefully with retries and backoff.
- **Extensibility:** Modular design to allow adding new sources, categories, or output formats easily.
- **Security:**
  - Store API keys and GitHub credentials securely (environment variables, secrets manager).
  - Do not log sensitive information.
- **Logging & Monitoring:**
  - Log all major steps and errors.
  - Optionally notify on failure (e.g., via email or webhook).

---

### User Stories

1. **As a tech enthusiast**, I want to see a daily summary of trending AI topics from X.com, organized by category, so I can stay updated efficiently in my areas of interest.
2. **As a developer**, I want the process to be automated, reliable, and easily extensible to new categories, so I don't have to manually curate or publish content.
3. **As a content archivist**, I want the summaries to be stored in a GitHub repo, organized by category and date, so I can track historical trends over time in different AI domains.

---

### Success Criteria

- The system fetches and summarizes the top 10 AI-related trending topics from X.com daily, organized by category.
- The output is correctly formatted in both JSON and Markdown, with clear category separation.
- The markdown file is saved in the `AI-newsletter` folder, with the correct date-based filename.
- The markdown file is committed and pushed to the specified GitHub repository.
- The process runs automatically on a schedule without manual intervention.
- Failures are logged and reported.

---

### Risks & Mitigations

- **API Rate Limits:** Implement retry logic and exponential backoff. Cache results if needed.
- **Data Quality:** Use robust keyword filtering, NLP, or classification models to ensure accurate categorization and relevance.
- **Authentication Issues:** Use secure storage for API and GitHub credentials.
- **Platform Changes:** Monitor for changes in X.com API or trending topic structure.

---

### Future Enhancements

- Add support for other social platforms (Reddit, Hacker News, etc.) and additional AI categories.
- Include sentiment analysis or topic categorization refinement.
- Build a web UI for browsing and searching archived topics by category and date.
- Add notification/alerting for new trends in specific categories.

---

### Deliverables

- Source code for the crawler, categorizer, summarizer, formatter, and publisher.
- Documentation for setup, configuration, and usage.
- Example output files (JSON and Markdown) with category structure, saved in the `AI-newsletter` folder with date-based filenames.
- Automated workflow (e.g., GitHub Actions, cron job) for scheduled runs.

---

## Implementation Plan: AI Agent Architecture

### Overview
The system will be implemented as a modular AI agent with the following components:

1. **Crawler Agent**
   - Fetches trending topics from X.com using the API.
   - Collects relevant source links (tweets, articles).

2. **Categorizer Agent**
   - Classifies each topic into a category (e.g., AI Prompts, AI Agents/MCP Servers, AI Models, AI Resources) using keyword filtering, NLP, or classification models.
   - Categories are configurable and extensible.

3. **Summarizer Agent**
   - Generates a concise, human-readable title for each topic (max 100 chars).
   - Optionally uses LLM or rule-based summarization.

4. **Formatter Agent**
   - Formats the data into JSON and Markdown according to the PRD, organized by category.
   - Ensures correct structure and file naming, saving markdown files in the `AI-newsletter` folder with the `<date>-ai-newsletter.md` format.

5. **Publisher Agent**
   - Saves the markdown file locally in the `AI-newsletter` folder.
   - Commits and pushes the file to the configured GitHub repository.
   - Handles errors and logs/reporting.

6. **Scheduler/Orchestrator**
   - Runs the workflow daily (or as configured) via cron, GitHub Actions, or a workflow manager.
   - Handles retries and error notifications.

### Data Flow
1. Scheduler triggers the workflow.
2. Crawler fetches trending topics and source links.
3. Categorizer assigns each topic to a category.
4. Summarizer generates titles.
5. Formatter creates JSON and Markdown outputs, organized by category, and saves markdown in `AI-newsletter/<date>-ai-newsletter.md`.
6. Publisher commits and pushes to GitHub.
7. Logs and errors are recorded and optionally reported.

### Security & Configuration
- All credentials (API keys, GitHub tokens) are loaded from environment variables or a secrets manager.
- No sensitive data is written to logs or output files.
- Categories are configurable via a config file or environment variable.
- Output folder (`AI-newsletter`) and filename format are configurable.

### Extensibility
- New sources or categories can be added by implementing additional modules.
- Output formats can be extended by adding new formatter modules.

### Example Directory Structure
```
ai-trending-topics-crawler/
├── crawler.py
├── categorizer.py
├── summarizer.py
├── formatter.py
├── publisher.py
├── scheduler.py
├── config.py
├── requirements.txt
├── README.md
└── AI-newsletter/
    └── <date>-ai-newsletter.md
```

### Example Environment Variables
- `X_API_KEY` (for X.com API)
- `GITHUB_TOKEN` (for repo access)
- `GITHUB_REPO` (target repo)
- `GITHUB_BRANCH` (target branch)
- `AI_CATEGORIES` (comma-separated list of categories)
- `NEWSLETTER_OUTPUT_DIR` (output folder, default: AI-newsletter)

### Error Handling & Logging
- Use structured logging for all steps.
- On failure, log error and optionally send notification (email/webhook).

---

**End of Refined PRD & Implementation Plan** 

---

## 1. **Step-by-Step Guide: Setting Up X.com API Credentials**

### a. **Create a Developer Account**
- Go to [developer.x.com](https://developer.x.com/) and sign in with your Twitter account.
- Apply for a developer account if you don't have one.

### b. **Create a Project and App**
- In the developer portal, create a new project and an associated app.
- Under your app's "Keys and tokens" section, generate a **Bearer Token** (for OAuth 2.0 Bearer Token authentication).

### c. **Store Your Bearer Token Securely**
- In your project root, create a file named `.env` (already in your `.gitignore`).
- Add your token:
  ```
  X_BEARER_TOKEN=your_bearer_token_here
  ```

---

## 2. **Update Your Code: Real X.com API Integration**

### a. **Install/Check Dependencies**
- You already have `requests` and `python-dotenv` in your `requirements.txt`.

### b. **Update `crawler.py`**

Replace the mock implementation with a real API call. Here's a robust version:

```python
import os
import requests
from dotenv import load_dotenv

class TrendingTopicsCrawler:
    """Fetches trending topics from X.com (Twitter) API."""
    def __init__(self):
        load_dotenv()
        self.bearer_token = os.getenv("X_BEARER_TOKEN")
        self.base_url = "https://api.twitter.com/2/tweets/search/recent"
        self.headers = {"Authorization": f"Bearer {self.bearer_token}"}

    def fetch_trending_topics(self, query="AI OR artificial intelligence OR #AI", max_results=50):
        params = {
            "query": query,
            "max_results": max_results,
            "tweet.fields": "created_at,author_id",
        }
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Twitter API error: {response.status_code} {response.text}")
        data = response.json()
        topics = []
        for tweet in data.get("data", []):
            topics.append({
                "text": tweet["text"],
                "link": f"https://x.com/i/web/status/{tweet['id']}"
            })
        return topics
```

**Notes:**
- This uses the "recent search" endpoint, which is available on the Essential and Elevated access levels.
- You can adjust the `query` to focus on AI topics and hashtags.
- You may need to handle pagination for more results.

### c. **Update Your Unit Test**
- Mock the `requests.get` call in your test to avoid hitting the real API.

---

## 3. **Error Handling & Rate Limiting**
- If you hit rate limits, the API will return a 429 status. Implement retry logic or exponential backoff as needed.
- Always check for `response.status_code` and handle errors gracefully.

---

## 4. **Run the Workflow**
- Make sure your `.env` file is present and contains your Bearer Token.
- Run `python main.py` to fetch real trending topics and generate your newsletter.

---

## 5. **Sample `.env` File**
```
X_BEARER_TOKEN=YOUR_TWITTER_BEARER_TOKEN
```

---

## 6. **Next Steps**
- Once this is working, you can further refine your categorization, summarization, and publishing steps.
- You can also add more advanced error handling, logging, and notification features.

---

Would you like me to update your `crawler.py` with the real API integration code now? If so, please confirm you have your Bearer Token ready in your `.env` file! 