
print("The calculate_love_score() function checks the compatibility of two names to calculate the love score between two people.")

def calculate_love_score(name1, name2):
    combin_names = list((name1 + name2).replace(" ","").lower())
    check1 = "true"
    check2 = "love"
    total1 = sum(combin_names.count(letter) for letter in check1)
    total2 = sum(combin_names.count(letter) for letter in check2)
    love_score = str(total1) + str(total2)
    print(f"Your score is {love_score}")




calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")