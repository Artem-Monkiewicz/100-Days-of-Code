import random
# !pip install nltk
from nltk.corpus import words
import nltk
# # !" pip install pillow"
# from PIL import Image

# Logo
# logo_path = "Step 5\logo_hm.webp"
# logo = Image.open(logo_path)
# logo.show()
print("""
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║      ██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
""")


# Lives
stages = [
        """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
        """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
        """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
        """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
        """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
        """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """
]

lives = 6

# Choose a random word
nltk.download("words") # list download
word_list = words.words()
chosen_word = random.choice(word_list).lower()
# Optional for debugging
# print("The word is: ", chosen_word)

# game setup
display = ["_" for letter in chosen_word]  # list for easy adding
correct_letters = set()  # To track guessed letters
print("".join(display))

# List of correctly guessed letters
guessed_correctly = set()

game_over = False

while not game_over:
    #  Get user input
    letter_guess = str(input("What letter do you think will be in this word? ")).lower()

    if len(letter_guess) != 1 or not letter_guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if letter_guess in correct_letters:
        print(f"You already guessed '{letter_guess}'. Try another letter.")
        continue

    # Add the entered letter to the list of all guessed letters
    correct_letters.add(letter_guess)

    if letter_guess in chosen_word:
        # Reveal guessed letters in the display
        for index, letter in enumerate(chosen_word):
            if letter == letter_guess:
                display[index] = letter_guess
        # display refresh
        print("Good guess!")
        print(stages[lives])
        print("".join(display))
    else:
        # Decrement lives and print the hangman stage
        lives -= 1
        print(stages[lives])
        print(f"Wrong guess! You have {lives} lives left.")


    # Display current progress
    print(" ".join(display))
    print(f"You have guessed {len(guessed_correctly)} letters correctly.")
    print(f"You have {lives} lives remaining.")

    # Check for game over conditions
    if "_" not in display:
        game_over = True
        print("Congratulations! You guessed the word!")
    elif lives == 0:
        game_over = True
        print("You lose! The word was:", chosen_word)