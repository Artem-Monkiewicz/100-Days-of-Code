import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
# - Create an empty String called `placeholder`.
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)


letter_guess = str(input("What letter do you think will be in this word? ")).lower()
print(letter_guess)

display = ""
for letter in chosen_word:
    if letter == letter_guess:
        display += letter
    else:
        display += "_"
print(display)

# for letter in chosen_word:
#     if letter == letter_guess:
#         print("Super! You guessed right!")
#     else:
#         print("Ouch! You guessed wrong.")


