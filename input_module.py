def get_user_input():

    topic = input("Enter Blog Topic: ")
    style = input("Enter Writing Style: ")
    tone = input("Enter Tone: ")
    word_count = int(input("Enter Word Count: "))

    print("\n---------- Blog Details ----------")
    print("Blog Topic :", topic)
    print("Writing Style :", style)
    print("Tone :", tone)
    print("Word Count :", word_count)
    print("----------------------------------")

    return topic, style, tone, word_count