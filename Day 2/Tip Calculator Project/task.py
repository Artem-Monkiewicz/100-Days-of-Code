print("Hello! Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15?% "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)
result = bill_with_tip / people

print(f"Each member of your company needs to be given: ${round(result, 2)}" )