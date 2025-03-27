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
    answer = ""

    while answer != "a" and answer != "b":
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    return answer

def swap(data1, data2):
    temp = data2
    data1 = temp
    return data1

def compare(val1, val2, choice, total, rollout):
    print("compare")
    if val1 > val2 and choice == val1:
        print(f"You're right! Current score: {score}.")
        total += 1
        return total
    elif val1 < val2 and choice == val2:
        rollout = False
        return rollout

option1 = None

def play(option1):
    score = 0
    play_game = True
    while play_game:
        
        while option1 == None:
            option1 = getData()

        print(option1["name"] + ", " + option1["description"] + ", " + option1["country"], option1["follower count"])

        option2 = getData()
        while option2 == option1:
            option2 = getData()

        print("\n")
        print("Vs")
        print("\n")

        print(option2["name"] + ", " + option2["description"] + ", " + option2["country"], option2["follower count"])

        a = option1["follower count"]
        b = option2["follower count"]

        print(a)
        print(b)

        if get_user_input() == "a":
            user_choice = option1["follower count"]
        else:
            user_choice = option2["follower count"]

        print(f"User chose {user_choice}")

        score = compare(a, b, user_choice, score, play_game)

        if score is not None:
            option1 = swap(option1, option2)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            play_game = compare(a, b, user_choice, score, play_game)


play(option1)