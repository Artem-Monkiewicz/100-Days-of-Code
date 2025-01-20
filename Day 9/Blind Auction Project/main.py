# TODO-1: Ask the user for input and bid
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids = {}
continue_bidding = True

while continue_bidding == True:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    print(bids)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        break

print(bids)