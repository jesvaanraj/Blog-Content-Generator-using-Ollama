from intent_module import detect_intent


while True:

    user_request = input(
        "\nEnter your request (or type exit): "
    )

    if user_request.lower() == "exit":
        break

    intent = detect_intent(user_request)

    print("Detected Intent:", intent)