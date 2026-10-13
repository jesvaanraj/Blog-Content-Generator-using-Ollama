from title_module import generate_titles

topic = input("Enter Blog Topic: ")

titles = generate_titles(topic)

if titles:
    print("\nTitles generated successfully!")
else:
    print("\nTitle generation failed.")