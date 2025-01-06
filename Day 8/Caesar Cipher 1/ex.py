# 90 y.o.
# You have x weeks left.
print("This model show how many days, weeks, and months you have left to live based on your age.")

def life_in_weeks():
    name = str(input("What is your name? "))
    age = int(input(f"{name}, how old are you? "))
    years_reamining = 90 - age
    weeks_remaining = years_reamining * 52
    days_remaining = years_reamining * 365
    months_remaining = years_reamining * 12
    print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

life_in_weeks()

# def life_in_weeks(age):
#     years_reamining = 90 - age
#     weeks_remaining = years_reamining * 52
#     print(f"You have {weeks_remaining} weeks left.")

# life_in_weeks(56)