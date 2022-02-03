alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(word, shift_number):
    cipher_text = ""
    for letter in word:
        letter_position = alphabet.index(letter)
        new_position = letter_position + int(shift_number)
        if new_position < 26:
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        elif new_position > 26:
            corrected_position = new_position % 26
            new_letter = alphabet[corrected_position]
            cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


encode(text, shift)
