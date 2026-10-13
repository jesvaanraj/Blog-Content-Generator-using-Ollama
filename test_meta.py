from input_module import get_user_input
from blog_module import generate_blog
from meta_module import generate_meta


topic, style, tone, word_count = get_user_input()

blog = generate_blog(topic, style, tone, word_count)

if blog:
    description = generate_meta(blog)

    if description:
        print("\nMeta Description Generated Successfully!")
else:
    print("\nBlog generation failed.")