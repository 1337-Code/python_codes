alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def decrypt(word, shift_number):
    decrypted_text = ""
    for letter in word:
        position = alphabet.index(letter)
        new_position = position - shift_number
        if new_position > 0:
            decrypted_letter = alphabet[new_position]
            decrypted_text += decrypted_letter
        if new_position < 0:
            corrected_position = new_position + 26
            decrypted_letter = alphabet[corrected_position]
            decrypted_text += decrypted_letter
    print(f"The decoded text is {decrypted_text}")


decrypt(text, shift)
