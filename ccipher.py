
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_dictionary = {}

for char in alphabet:
    alphabet_dictionary[alphabet.index(char)] = char

retry = True

def ceasar_cipher(text, movement, encode_or_decode):
    global retry

    result = ""

    if encode_or_decode == "decode":
        movement *= -1

    for word in text.split():
        temp = ""
        for char in word:

            if char not in alphabet:
                temp += char
            else:
                i = [key for key, val in alphabet_dictionary.items() if val == char][0]
                j = (i + movement) % len(alphabet)

                temp += alphabet_dictionary[j]

        result += (temp + " ")

    print(result)

    another_one = input("Do you want to go again? Type 'Yes' or 'No': \n").lower()
    if another_one == "yes":
        retry = True
    elif another_one == 'no':
        retry = False
        print("Goodbye")
    else:
        retry = False
        print("Wrong command. Goodbye!")

while retry == True:

    direction = input("Enter 'encode' to encrypt and 'decode' to decrypt: ")
    original_text = input("Enter your text: \n")
    shift = int(input("Enter the shift number: "))

    if direction == "encode" or direction == "decode":
        ceasar_cipher(original_text, shift, direction)
    else:
        print("Incorrect command.")