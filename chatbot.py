from nltk.chat.util import Chat, reflections

# Extended chatbot responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you?"]],
    [r"how are you?", ["I'm a bot, but I'm doing great!", "I'm here to help!"]],
    [r"what is your name?", ["I'm ChatBot, your virtual assistant."]],
    [r"bye|goodbye", ["Goodbye!", "See you later!", "Take care!"]],
    [r"who created you?", ["I was created by a Python developer!", "I'm a Python-based chatbot."]],
    [r"what can you do?", ["I can chat with you, answer simple questions, and assist with basic tasks."]],
    [r"tell me a joke", ["Why don’t programmers like nature? It has too many bugs!",
                         "I told my computer I needed a break, and now it won’t stop sending me vacation ads."]],
    [r"what is python?", ["Python is a powerful programming language used for web development, data science, "
                          "and automation."]],
]


# Unknown response handling
def custom_response(text):
    default_responses = [
        "I'm not sure about that. Can you ask something else?",
        "I don't have an answer for that yet.",
        "Hmm... that's interesting! I'll learn more about it."
    ]
    return default_responses[len(text) % len(default_responses)]


def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    chat = Chat(pairs, reflections)

    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chat.respond(user_input)
        print("Chatbot:", response if response else custom_response(user_input))


if __name__ == "__main__":
    chatbot()
