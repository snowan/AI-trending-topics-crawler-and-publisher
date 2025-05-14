"""
AI relevance filtering utilities for tweets/posts.
Includes:
- is_relevant_to_ai: simple keyword-based
- is_relevant_to_ai_ml: spaCy-based (optional, requires spaCy)
- is_relevant_to_ai_llm: OpenAI LLM-based (optional, requires openai)
"""

def is_relevant_to_ai(text):
    """Return True if text contains strong AI keywords."""
    keywords = [
        'ai', 'artificial intelligence', 'machine learning', 'deep learning',
        'neural network', 'gpt', 'llm', 'prompt', 'agent', 'mcp server'
    ]
    text_lower = text.lower()
    return any(kw in text_lower for kw in keywords)

# --- Advanced: spaCy-based filtering ---
try:
    import spacy
    _nlp = spacy.load("en_core_web_sm")
    def is_relevant_to_ai_ml(text):
        """Return True if text contains AI keywords as lemmatized tokens (requires spaCy)."""
        ai_keywords = {'ai', 'artificial intelligence', 'machine learning', 'deep learning', 'neural network', 'gpt', 'llm', 'prompt', 'agent', 'mcp server'}
        doc = _nlp(text)
        for token in doc:
            if token.lemma_.lower() in ai_keywords:
                return True
        return False
except ImportError:
    def is_relevant_to_ai_ml(text):
        raise NotImplementedError("spaCy is not installed. Run 'pip install spacy' and download the model.")

# --- Advanced: OpenAI LLM-based filtering ---
def is_relevant_to_ai_llm(text):
    """Return True if OpenAI LLM says the text is about AI (requires openai, API key)."""
    try:
        import openai
        import os
        openai.api_key = os.getenv("OPENAI_API_KEY")
        prompt = f"Is the following tweet about artificial intelligence or related technologies? Answer yes or no.\nTweet: \"{text}\""
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1,
            temperature=0
        )
        answer = response.choices[0].text.strip().lower()
        return answer == "yes"
    except ImportError:
        raise NotImplementedError("openai is not installed. Run 'pip install openai'.")
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return False 