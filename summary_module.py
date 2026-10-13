import requests


def generate_summary(blog):

    prompt = f"""
    Summarize the following blog in approximately 100 words.

    Make the summary clear, concise, and informative.
    Include the main points and conclusion.

    Blog Content:
    {blog}

    Return only the summary.
    """

    print("\nGenerating Blog Summary...\n")

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data, timeout=300)

    if response.status_code == 200:

        result = response.json()
        summary = result["response"]

        print("=" * 40)
        print("BLOG SUMMARY")
        print("=" * 40)
        print(summary)
        print("=" * 40)

        return summary

    else:
        print("Error generating summary:", response.status_code)
        return ""