print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


bill = 0

if size == "S":
    bill += 15
    # print(f"A standard pizza of this size costs ${bill}.")
elif size == "M":
    bill += 20
    # print(f"A standard pizza of this size costs ${bill}.")
elif size == "L":
    bill += 25
    # print(f"A standard pizza of this size costs ${bill}.")
else:
    print("You typed the wrong inputs.")


if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
    # print(f"The price for this size pizza with extra pepperoni is ${bill}.")
# else:
#     print("OK, and...")


if extra_cheese == "Y":
    bill += 1
    # print(f"The price of your pizza with extra cheese is ${bill}.")
print(f"Your final bill is: ${bill}.")