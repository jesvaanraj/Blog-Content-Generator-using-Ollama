from input_module import get_user_input
from blog_module import generate_blog


topic, style, tone, word_count = get_user_input()

blog = generate_blog(topic, style, tone, word_count)

if blog:
    print("\nBlog generated successfully!")
else:
    print("\nBlog generation failed.")