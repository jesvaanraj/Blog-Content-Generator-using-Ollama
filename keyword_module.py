import requests


def generate_keywords(topic, blog):

    prompt = f"""
    Generate 10 SEO-friendly keywords for the following blog.

    Topic: {topic}

    Blog Content:
    {blog}

    Requirements:
    1. Generate relevant keywords.
    2. Include short phrases and important terms.
    3. Avoid duplicate keywords.
    4. Display the keywords as a numbered list.
    """

    print("\nGenerating SEO Keywords...\n")

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data, timeout=300)

    if response.status_code == 200:

        result = response.json()
        keywords = result["response"]

        print("===== SEO Keywords =====\n")
        print(keywords)

        return keywords

    else:
        print("Error generating keywords:", response.status_code)
        return ""