import random

words = ["canary", "postgraduate", "anadromous", "heehaw", "subsolar", "scenography", "clinch", "sortie", "nursemaid", "inceptive", "consecrate", "ferroelectric", "culture", "radio", "frost", "cuff"]

number_of_lives = 4

word_to_guess = words[random.randint(0,len(words)-1)]

print(word_to_guess)

print("Guess a word to fill the following blanks.")
print("\n")

status = "X" * len(word_to_guess)
print(status)
print("\n")

guessed_letters = []

guessed_word = ""

def manage_lives():
    global number_of_lives
    number_of_lives -= 1
    print(f"You guessed wrong! You have {str(number_of_lives)} lives left!")


while status != word_to_guess and number_of_lives > 0:
    guessed_letter = input("Please guess a letter: ").lower()

    if len(guessed_letter) == 1 and guessed_letter.isalpha():

        if guessed_letter not in guessed_letters:
            guessed_letters.append(guessed_letter)
            print(guessed_letters)

            if guessed_letter in word_to_guess:
                new_status = ""
                print(new_status)

                for i, char in enumerate(word_to_guess):
                    if char in guessed_letters:
                        new_status += char
                    else:
                        new_status += "X"
                status = new_status
                print(status)

            else:
                manage_lives()

        else:
            print("You have already guessed that letter")
            
    else:
        print("Please enter a single character to continue.")

if status == word_to_guess:
    print("\n")
    print("You win!")

elif number_of_lives == 0:
    print("\n")
    print(f"You have {number_of_lives} lives left!")
    print("GAME OVER!")
