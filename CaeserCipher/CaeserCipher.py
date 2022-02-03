import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
end_of_program = False


def caeser(word, shift_number, direction):
    if direction == "encode":
        cipher_text = ""
        for letter in word:
            if letter in alphabet:
                new_letter = letter
                letter_position = alphabet.index(letter)
                new_position = letter_position + int(shift_number)
                if new_position <= 26:
                    if new_position == 26:
                        new_letter = alphabet[25]
                    else:
                        new_letter = alphabet[new_position]
                    cipher_text += new_letter
                elif new_position > 26:
                    corrected_position = new_position % 26
                    new_letter = alphabet[corrected_position]
                    cipher_text += new_letter
            else:
                new_letter = letter
                cipher_text += letter
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        decrypted_text = ""
        for letter in word:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_number
                if new_position >= 0:
                    decrypted_letter = alphabet[new_position]
                    decrypted_text += decrypted_letter
                if new_position < 0:
                    corrected_position = new_position + 26
                    decrypted_letter = alphabet[corrected_position]
                    decrypted_text += decrypted_letter
            else:
                decrypted_letter = letter
                decrypted_text += decrypted_letter
        print(f"The decoded text is {decrypted_text}")


while end_of_program == False:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caeser(text, shift, direction)
    choice = input(
        ("Type 'yes' if you want to go again. Otherwise type 'no'.").lower())
    if choice == "no":
        end_of_program = True
    else:
        end_of_program = False
