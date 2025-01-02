import random

# world list
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
#PÓZNIEJ WYWALIĆ!
print(chosen_word)

# pole
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    letter_guess = str(input("What letter do you think will be in this word? ")).lower()

    display = ""
    
    for letter in chosen_word:
        if letter == letter_guess:
            display += letter
            correct_letters.append(letter_guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You won!")



# TTODO-1
# - Use a while loop to let the user guess again. 
# - The loop should only stop once the user has guessed all the letters in the chosen_word.
# - At that point `display` has no more blanks ("_"). Then you can tell the user they've won.

# TTODO-2
# - Update the for loop so that previous guesses are added to the `display` String.
# - At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.

#RIGHT

import random

# Список слов
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# Для теста
print(chosen_word)

# Поле игры
display = ["_" for _ in chosen_word]  # Список для простого обновления
print("".join(display))

game_over = False

while not game_over:
    # Пользователь вводит букву
    guess = input("What letter do you think will be in this word? ").lower()

    # Проверка каждой буквы в слове
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    # Вывод текущего состояния слова
    print("".join(display))

    # Проверка на победу
    if "_" not in display:
        game_over = True
        print("You won!")
