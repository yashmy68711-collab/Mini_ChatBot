print("Mini ChatBot")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I'm fine!")

    elif user == "what is your name":
        print("Bot: I'm a Python chatbot.")

    elif user == "help":
        print("Bot: Try saying hello or ask my name.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")