responses = {
    "hello":            "Hey there! 👋 I'm ZeyadBot. How can I help?",
    "hi":               "Hi! Great to see you. What's on your mind?",
    "hey":              "Hey! What can I do for you?",
    "good morning":     "Good morning! ☀️ Hope your day is great!",
    "good evening":     "Good evening! 🌙 How can I assist tonight?",
    "how are you":      "I'm just lines of code, but running perfectly! 😄",
    "are you real":     "As real as logic gets! No hallucinations here. 🧠",
    "your name":        "My name is ZeyadBot! Nice to meet you. 😊",
    "help":             "You can type: hello, how are you, your name, weather, or bye.",
    "bye":              "Goodbye! 👋 Keep coding!",
    "goodbye":          "See you next time! 🌟",
    "quit":             "Shutting down... Goodbye! 🤖",
    "exit":             "Exiting ZeyadBot. Happy coding! 👨‍💻",
}

exit_words = {"quit", "exit", "bye", "goodbye"}


print("=" * 40)
print("   Welcome to ZeyadBot 🤖")
print("   Type 'help' or 'exit' to quit")
print("=" * 40 + "\n")

while True:
    raw = input("You: ")
    clean = raw.lower().strip()

    if not clean:
        print("ZeyadBot: Please type something! ")
        continue

    if clean in exit_words:
        print("ZeyadBot: Goodbye! See you next time. ")
        break

    reply = None
    for keyword in responses:
        if keyword in clean:
            reply = responses[keyword]
            break

    if not reply:
        reply = "I don't understand that yet. Try 'help'."

    print("ZeyadBot:", reply, "\n")
