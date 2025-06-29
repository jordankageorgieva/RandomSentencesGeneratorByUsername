import random

names = ["Peter", "Michell", "Jane", "Steve" ]
places = ["Sofia", "Plovdiv", "Varna", "Burgas" ]
verbs = ["eats", "holds", "sees", "plays with", "brings" ]
nouns = ["stones", "cake", "apple", "laptop", "bikes" ]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly" ]
details = ["near the river", "at home", "in the park" ]

def get_random_word(words):
    return random.choice(words)

while True:
    random_name = get_random_word(names)
    random_places = get_random_word(places)
    random_verbs = get_random_word(verbs)
    random_nouns = get_random_word(nouns)
    random_adverbs = get_random_word(adverbs)
    random_details = get_random_word(details)

    print(f"{random_name} from {random_places} {random_adverbs} {random_verbs} {random_nouns}")

    user_input = input("Click [Enter] to generate a new one or type 'exit' to quit: ")
    if user_input.lower() == "exit" or user_input.lower() == "q":
        break
