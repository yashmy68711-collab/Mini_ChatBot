import random
print("Mini ChatBot")
print("Type 'bye' to exit\n")

message_count = 0

while True:
    user = input("You: ").lower().strip()

    message_count += 1

    if user == "hello" or user == "hi":
        greetings = ["Hello!", "Hi there!", "Hey!", "Nice to meet you!"]
        print("Bot:", random.choice(greetings))

    elif user == "how are you":
        print("Bot: I'm fine!")

    elif user == "what is your name":
        print("Bot: I'm a Python chatbot.")

    elif "thank you" in user:
        print("Bot: You're welcome!")

    elif user == "help":
        print("Bot: Try saying hello or ask my name.")

    elif user == "bye":
        print("Bot: Goodbye!")
        print("Total messages:", message_count)
        break

    else:
        print("Bot: Sorry, I don't understand.")
