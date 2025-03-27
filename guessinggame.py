from game_data import data
import random

compareA = ""
compareB = ""

score = 0

def getData():
    value = random.choice(data)
    #print(value["name"] + ", " + value["description"] + ", " + value["country"])
    return value

def get_user_input():
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    return answer

def swap():
    print("here")

def compare(val1, val2, choice):
    if val1 > val2 and choice == val1:
        score += 1
        swap()
    elif val1 < val2 and choice == val2:
        print(f"Sorry, that's wrong. Final score: {score}")
        play_game = False
        return

play_game = True

def play():
    while play_game:
        option1 = getData()
        print(option1["name"] + ", " + option1["description"] + ", " + option1["country"])

        option2 = getData()
        print(option2["name"] + ", " + option2["description"] + ", " + option2["country"])

        a = option1["follower count"]
        b = option2["follower count"]

        compare(a, b, get_user_input())


