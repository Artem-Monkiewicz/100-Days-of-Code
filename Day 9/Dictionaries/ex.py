slown1 = {"slowo1.1": "slowo1.1.1", "slowo2.1": "slowo2.1.1", "slowo3.1": "slowo3.1.1"}
slown2 = {"slowo1.2": ["slowo1.2.1", "slowo1.2.2", "slowo1.2.3"], "slowo2.2": ["slowo2.1.1", "slowo2.1.2", "slowo2.1.3"], "slowo3.2": ["slowo3.1.1", "slowo3.1.2", "slowo3.1.3"]}

print(slown2["slowo1.2"][1]) # slowo1.2.2

nested_dict = ["A", "B", ["C", "D", "E", "F", "G", "H", "I", "J"]]
print(nested_dict[2][1]) # D

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
        },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
        }
}

print(travel_log["Germany"]["cities_visited"][2]) # Stuttgart