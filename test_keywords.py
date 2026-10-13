from input_module import get_user_input
from blog_module import generate_blog
from keyword_module import generate_keywords


topic, style, tone, word_count = get_user_input()

blog = generate_blog(topic, style, tone, word_count)

if blog:
    keywords = generate_keywords(topic, blog)

    if keywords:
        print("\nSEO Keyword Generation Successful!")
else:
    print("\nBlog generation failed.")