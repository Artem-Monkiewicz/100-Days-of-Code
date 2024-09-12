print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"The price of your ticket is ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"The price of your ticket is ${bill}.")
    else:
        bill = 12
        print(f"The price of your ticket is ${bill}.")

    wants_photo = input("Photo coast $3. Would you like to take a photo? (y/n) ")
    if wants_photo == "y":
        #add $3 to bill
        bill += 3
        print(f"Cool! Your final bill is ${bill}.")
    elif wants_photo == "n":
        print(f"Ok, your final bill is ${bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")

# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# if round(bmi, 1) <= 18.4:
#     print("underweight")
# elif round(bmi, 1) <= 24.9:
#     print("normal weight")
# else:
#     print("overweight")