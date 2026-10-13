import requests


def detect_intent(user_request):

    prompt = f"""
    You are an intent detection system.

    Identify the intent of the user's request.

    Choose exactly one category from the following:

    BLOG_GENERATION
    SUMMARY
    KEYWORD_GENERATION
    META_DESCRIPTION

    Examples:
    User: Write a blog about Cyber Security
    Intent: BLOG_GENERATION

    User: Summarize this blog
    Intent: SUMMARY

    User: Give SEO keywords
    Intent: KEYWORD_GENERATION

    User: Create a meta description
    Intent: META_DESCRIPTION

    User Request: {user_request}

    Return only the category name.
    """

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data, timeout=300)
    response.raise_for_status()

    result = response.json()
    intent = result["response"].strip().upper()

    valid_intents = [
        "BLOG_GENERATION",
        "SUMMARY",
        "KEYWORD_GENERATION",
        "META_DESCRIPTION"
    ]

    # Identify the category returned by the model
    for category in valid_intents:
        if category in intent:
            return category

    return "UNKNOWN"