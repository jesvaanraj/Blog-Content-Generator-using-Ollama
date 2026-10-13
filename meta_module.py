import requests


def generate_meta(blog):

    prompt = f"""
    Write one SEO-friendly meta description for the following blog.

    Requirements:
    1. Maximum 160 characters.
    2. Make it informative and engaging.
    3. Include the main topic.
    4. Return only the meta description.

    Blog Content:
    {blog}
    """

    print("\nGenerating Meta Description...\n")

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data, timeout=300)

    if response.status_code == 200:

        result = response.json()
        description = result["response"].strip()

        # Keep the description within 160 characters
        if len(description) > 160:
            description = description[:157].rstrip() + "..."

        print("=" * 40)
        print("SEO META DESCRIPTION")
        print("=" * 40)
        print(description)
        print("Character Count:", len(description))
        print("=" * 40)

        return description

    else:
        print("Error generating meta description:", response.status_code)
        return ""