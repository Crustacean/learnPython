
database = {}

print("Welcome to the secre aution program.")

add_new = True

while add_new:

    name = input("What is your name?_")
    bid = int(input("what is your bid?_ $"))
    database[name] = bid

    another_bidder = input("Is there another Bidder? Type 'Yes' if there is another Bidder: ").lower()

    if another_bidder != "yes":
        print("Thank you for bidding.")
        add_new = False
    else:
        print("\n" * 100)

max = 0

for key in database:
    if database[key] > max:
        max = database[key]

print(database)
print(max)