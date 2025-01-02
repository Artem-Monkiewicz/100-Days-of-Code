# TODO1 
# Randomly choose a word from the word_list and assign it to a variable called `chosen_word`. Then print it.
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO2
# Ask the user to guess a letter and assign their answer to a variable called `guess`. Make the String stored in `guess` lowercase.
letter_guess = str(input("What letter do you think will be in this word? ")).lower()
print(letter_guess)

# TODO3
# Check if the letter the user guessed `guess` is one of the letters in the `chosen_word`. Loop through each of the letters in the `chosen_word`  and print "Right" if the letter is a match, "Wrong" if it's not.
for letter in chosen_word:
    if letter == letter_guess:
        print("Super! You guessed right!")
    else:
        print("Ouch! You guessed wrong.")
