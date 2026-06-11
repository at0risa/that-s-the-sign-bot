import json
import random
def load_messages(language):
    with open(f"messages_{language}.json", 'r', encoding="utf-8") as file:
        return json.load(file)

def get_random_message(language):
    messages = load_messages(language)
    return random.choice(messages)


