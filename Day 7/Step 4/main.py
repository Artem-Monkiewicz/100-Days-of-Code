import random

# world list
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# game place
display = ["_" for letter in chosen_word]  # list for easy adding
print("".join(display))

game_over = False
correct_letters = []

while not game_over:
    letter_guess = str(input("What letter do you think will be in this word? ")).lower()
    # letter check
    for index, letter in enumerate(chosen_word):
        if letter == letter_guess:
            display[index] = letter_guess

    # display refresh
    print("".join(display))

    # Viс check
    if "_" not in display:
        game_over = True
        print("You won!")
