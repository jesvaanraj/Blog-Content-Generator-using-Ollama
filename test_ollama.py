import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "Write a short blog about Artificial Intelligence in Education.",
    "stream": False
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print("\nGenerated Blog:\n")
    print(result["response"])
else:
    print("Error:", response.status_code)