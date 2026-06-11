import json
import random
def load_messages():
    with open('messages.json', 'r', encoding="utf-8") as file:
        return json.load(file)

def get_random_message(messages):
    return random.choice(messages)

