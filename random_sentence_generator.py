import random


names = ["Giuseppe", "Izabela", "Oscar The Neighbour", "Grandma Elena"]
places = ["Toilet", "Balcony", "Basement", "WonderLand"]
verbs = ["eats", "bites", "sees", "plays with", "screams"]
nouns = ["human food", "whiskas", "meat", "banana", "hamburger"]
adverbs = ["slowly", "diligently", "warmly", "quickly", "rapidly"]
details = ["near the sofa", "close to the table", "near the window", "on the fridge", "under the bed"]


def get_random_word(words):
    return random.choice(words)


print("\nHi, this is your first random sentence:")
data = input("\nPress [y] to start! ")
while True:

    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    if data != "y":
        print("Exiting the program, Bye Bye...")
        break
    else:
        print(f"---<<<<<*>>>>>---\n<<--{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}->>")
        print("\n------<< Press [ y ] for new or press any button for Exit! >>------")

    data = input()
