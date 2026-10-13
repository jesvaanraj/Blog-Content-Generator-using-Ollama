import os

from input_module import get_user_input
from blog_module import generate_blog
from title_module import generate_titles
from keyword_module import generate_keywords
from summary_module import generate_summary
from meta_module import generate_meta
from intent_module import detect_intent


def main():

    os.makedirs("outputs", exist_ok=True)

    blog = ""
    topic = ""

    while True:

        print("\n====================================")
        print("       AI BLOG CONTENT GENERATOR")
        print("====================================")
        print("1. Generate Blog")
        print("2. Generate Blog Titles")
        print("3. Generate SEO Keywords")
        print("4. Generate Blog Summary")
        print("5. Generate Meta Description")
        print("6. Detect User Intent")
        print("7. Exit")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            topic, style, tone, word_count = get_user_input()

            blog = generate_blog(
                topic, style, tone, word_count
            )

            if blog:

                with open(
                    "outputs/generated_blog.txt",
                    "w",
                    encoding="utf-8"
                ) as file:
                    file.write(blog)

                print("\nBlog saved successfully!")

        elif choice == "2":

            topic = input("Enter Blog Topic: ")
            generate_titles(topic)

        elif choice == "3":

            if blog:
                generate_keywords(topic, blog)
            else:
                print("Please generate a blog first.")

        elif choice == "4":

            if blog:
                generate_summary(blog)
            else:
                print("Please generate a blog first.")

        elif choice == "5":

            if blog:
                generate_meta(blog)
            else:
                print("Please generate a blog first.")

        elif choice == "6":

            request = input("Enter your request: ")
            intent = detect_intent(request)

            print("Detected Intent:", intent)

        elif choice == "7":

            print("Thank you for using AI Blog Generator!")
            break

        else:

            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()