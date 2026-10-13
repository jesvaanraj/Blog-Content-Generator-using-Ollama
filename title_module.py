import requests


def generate_titles(topic):

    prompt = f"""
    Generate exactly five attractive and engaging blog titles
    about the topic: {topic}.

    Requirements:
    1. Generate exactly five titles.
    2. Make each title interesting and informative.
    3. Avoid repeating the same idea.
    4. Display the titles as a numbered list.
    """

    print("\nGenerating Blog Titles...\n")

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data, timeout=300)

    if response.status_code == 200:

        result = response.json()
        titles = result["response"]

        print("===== Suggested Titles =====\n")
        print(titles)

        return titles

    else:
        print("Error generating titles:", response.status_code)
        return ""