# AI-Powered Blog Content Generator using Ollama

## 📌 Project Overview

The AI-Powered Blog Content Generator is a Python-based application that uses Ollama and the Llama 3.2 Large Language Model (LLM) to generate blog content automatically.

Users can provide a topic, writing style, tone, and word count to generate blogs. The application also generates attractive blog titles, SEO keywords, summaries, and meta descriptions. It includes an LLM-based intent detection module to identify user requests.

## ✨ Features

- 📝 **AI Blog Generation:** Generate blogs based on user-provided topics and preferences.
- 💡 **Blog Title Generator:** Generate five attractive blog titles.
- 🔍 **SEO Keyword Generator:** Generate relevant SEO-friendly keywords.
- 📄 **Blog Summary Generator:** Summarize generated blogs in approximately 100 words.
- 🌐 **Meta Description Generator:** Generate SEO meta descriptions within 160 characters.
- 🧠 **Intent Detection:** Identify user requests using an LLM.
- 💾 **Save Blog:** Save generated blog content to a text file.
- 🔄 **Interactive Menu:** Access different functionalities through a menu-driven interface.

## 🛠️ Technologies Used

- Python
- Ollama
- Llama 3.2
- Requests Library
- Large Language Models (LLMs)
- Prompt Engineering

## 📂 Project Structure

```text
Blog-Content-Generator-using-Ollama/
│
├── main.py
├── input_module.py
├── blog_module.py
├── title_module.py
├── keyword_module.py
├── summary_module.py
├── meta_module.py
├── intent_module.py
├── utils.py
├── outputs/
│   └── generated_blog.txt
└── README.md
