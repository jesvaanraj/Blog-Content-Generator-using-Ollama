import requests


def generate_blog(topic, style, tone, word_count):

    prompt = f"""
    Write a complete blog on the topic: {topic}.

    Writing Style: {style}
    Tone: {tone}
    Word Count: Approximately {word_count} words.

    Structure:
    1. Title
    2. Introduction
    3. Main Content
    4. Conclusion

    Write clear and informative content.
    """

    print("\nGenerating Blog...\n")

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data, timeout=300)

    if response.status_code == 200:

        result = response.json()
        blog = result["response"]

        print("=" * 50)
        print(blog)
        print("=" * 50)

        return blog

    else:
        print("Error generating blog:", response.status_code)
        return ""