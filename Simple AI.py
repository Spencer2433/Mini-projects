# Simple AI

import random

# predefined responses
responses = {
    "greetings" : ["Hi", "Hello", "Hey!"],
    "how_are_you" : ["I'm doing well, thank you", "I'm great!", "I'm good!"],
    "goodbye" : ["Goodbye!", "See you later!", "Bye"]
}

# Simple AI chatbot function
def chatbot(message):
    if "hello" in message.lower():
        return random.choice(responses["greetings"])
    if "how are you" in message.lower():
        return random.choice(responses["how_are_you"])
    elif "bye" in message.lower():
        return random.choice(responses["goodbye"])
    else:
        return "I'm not sure how to answer that."
    
print(chatbot('hello'))
print(chatbot('how are you'))
print(chatbot('bye'))
print(chatbot('unaitwa?'))
