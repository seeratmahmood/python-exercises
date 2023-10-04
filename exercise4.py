#create story 

def fill_blanks():
    adjectives = []
    nouns = []
    verbs = []
    adverbs = []

    print("Create your own story!")
    print("Enter the following words:")

    for i in range(3):
        adjectives.append(input("Adjective: "))
    for i in range(2):
        nouns.append(input("Noun: "))
    for i in range(3):
        verbs.append(input("Verb: "))
    for i in range(2):
        adverbs.append(input("Adverb: "))

    user_input = {
        "adjectives": adjectives,
        "nouns": nouns,
        "verbs": verbs,
        "adverbs": adverbs
    }

    return user_input

def create_story(user_input):
    story = (
        f" Once upon a time there lived a {user_input['adjectives'][0]} {user_input['nouns'][0]}.\n "
        f"The {user_input['nouns'][0]} would {user_input['adverbs'][0]} {user_input['verbs'][0]} the {user_input['adjectives'][1]} {user_input['nouns'][1]} every day until one day the {user_input['nouns'][0]} {user_input['verbs'][1]} to the {user_input['nouns'][1]}\n"
        f" This made the {user_input['nouns'][1]} feel very {user_input['adjectives'][2]}.\n "
        f"From that day, the {user_input['nouns'][0]} and the {user_input['nouns'][1]} {user_input['verbs'][2]} {user_input['adverbs'][1]} ever after."
    )
    return story

def main():
    user_input = fill_blanks()
    story = create_story(user_input)
    print("\nYour Story:\n")
    print(story)

if __name__ == "__main__":
    main()