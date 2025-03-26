
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

track_computer_cards = []
track_player_cards = []

def deal():
    card = random.choice(cards)
    return card

total_cards = 0
def add(card_tracker):
    global total_cards
    total_cards = sum(card_tracker)
    return total_cards

def play():

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if len(play) == 1 and play == "y" and len(track_computer_cards) == 0 and len(track_player_cards) == 0:
        track_player_cards.append(deal())
        track_player_cards.append(deal())
        track_computer_cards.append(deal())

        print(f"Your cards: {track_player_cards}, current score: {add(track_player_cards)}")
        print(f"Computer's first card: {track_computer_cards}")

        get_another = True

        while get_another:
            if add(track_player_cards) < 21:
                play = input("Type 'y' to get another card, type 'n' to pass:" )

                if len(play) == 1 and play == "y":
                    track_player_cards.append(deal())
                    track_computer_cards.append(deal())

                    print("\n")
                    print(f"Your cards: {track_player_cards}, current score: {add(track_player_cards)}")
                    print(f"Computer's first card: {track_computer_cards}")

                elif len(play) == 1 and play == "n":
                    track_computer_cards.append(deal())

                    if add(track_computer_cards) < 17:
                        track_computer_cards.append(deal())

                    if add(track_player_cards) <= 21 and add(track_computer_cards) < add(track_player_cards):
                        print("\n")
                        print(f"Your final hand: {track_player_cards}, final score: {add(track_player_cards)}")
                        print(f"Computer's final hand: {track_computer_cards}, final score: {add(track_computer_cards)}")
                        print("You LOOSE.")
                        get_another = False

                    elif add(track_player_cards) <= 21 and add(track_computer_cards) > add(track_player_cards):
                        print("\n")
                        print(f"Your final hand: {track_player_cards}, final score: {add(track_player_cards)}")
                        print(f"Computer's final hand: {track_computer_cards}, final score: {add(track_computer_cards)}")
                        print("You WIN!!!!.")
                        get_another = False

            elif add(track_player_cards) > 21:
                print("\n")
                print(f"Your final hand: {track_player_cards}, final score: {add(track_player_cards)}")
                print(f"Computer's final hand: {track_computer_cards}, final score: {add(track_computer_cards)}")
                print("You LOOSE.")
                get_another = False

            elif add(track_player_cards) == 21 and add(track_computer_cards) != 21:
                print("\n")
                print(f"Your final hand: {track_player_cards}, final score: {add(track_player_cards)}")
                print(f"Computer's final hand: {track_computer_cards}, final score: {add(track_computer_cards)}")
                print("You WIN!!!!.")
                get_another = False

            elif add(track_player_cards) == add(track_computer_cards):
                print("\n")
                print(f"Your final hand: {track_player_cards}, final score: {add(track_player_cards)}")
                print(f"Computer's final hand: {track_computer_cards}, final score: {add(track_computer_cards)}")
                print("You DRAW.")
                get_another = False

    elif len(play) == 1 and play == "n" and len(track_computer_cards) == 0 and len(track_player_cards) == 0:
        play()

    
play()