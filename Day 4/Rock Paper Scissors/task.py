import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose_list = [rock,paper,scissors]


print(""" 
    What do you choose?
    0 for rock; 
    1 for paper; 
    2 for scissors""")

choose_player = int(input("And... you choose?"))
print(choose_list[choose_player])

choose_computer = random.randint(0, 2)
print(f"Computer choise: \n{choose_list[choose_computer]}")

if choose_player >= 3 or choose_player < 0:
    print("Invalid input. You lose!")
elif choose_player == 0 and choose_computer == 2:
    print("You win!")
elif choose_computer == 0 and choose_player == 2:
    print("You lose!")
elif choose_computer > choose_player:
    print("You lose!")
elif choose_computer < choose_player:
    print("You win!")
elif choose_computer == choose_player:
    print("It's a draw!")

# # Rock
# if choose_player == 0 and choose_computer == [0]:
#     print("It's a draw")
# elif choose_player == 0 and choose_computer == [1]:
#     print("You lost")
# elif choose_player == 0 and choose_computer == [2]:
#     print("You won")
# else:
#     print("Error")
#
# # Paper
# if choose_player == 1 and choose_computer == [1]:
#     print("It's a draw")
# elif choose_player == 1 and choose_computer == [0]:
#     print("You won")
# elif choose_player == 1 and choose_computer == [2]:
#     print("You lost")
# else:
#     print("Error")
#
# # Scissors
# if choose_player == 2 and choose_computer == [2]:
#     print("It's a draw")
# elif choose_player  == 2 and choose_computer == [1]:
#     print("You won")
# elif choose_player == 2 and choose_computer == [0]:
#     print("You lost")
# else:
#     print("Error")

