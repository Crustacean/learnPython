from game_data import data
import random

score = 0

def getData():
    value = random.choice(data)
    return value

def get_user_input():
    while True:
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        if answer in ("a", "b"):
            return answer
        else:
            print("Wrong input. Please type 'A' or 'B' ")

def compare(val1, val2, choice, total):
    if val1 > val2 and choice == val1:
        total += 1
        print(f"You're right! Current score: {total}.")
        return total
    elif val1 < val2 and choice == val2:
        return total
    else:
        return total

def play():

    global score

    play_game = True
    option1 = getData()

    while play_game:

        option2 = getData()
        while option2 == option1:
            option2 = getData()
        
        print(option1["name"] + ", " + option1["description"] + ", " + option1["country"], option1["follower_count"])
        print("\n")
        print("Vs")
        print("\n")
        print(option2["name"] + ", " + option2["description"] + ", " + option2["country"], option2["follower_count"])

        a = option1["follower_count"]
        b = option2["follower_count"]

        user_choice = a if get_user_input() == "a" else b

        score = compare(a, b, user_choice, score)

        if (user_choice == "a" and a > b) or (user_choice == "b" and b > a):
            option1 = option2
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            play_game = False


play()