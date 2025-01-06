import string

alfabet = list(string.ascii_lowercase)
# alfabet = [chr(i) for i in range(ord("a"), ord("z")+1)]
print(alfabet)


oryginal_text = input("Enter text to encrypt: ")
shift_amount = int(input("Enter shift amount: "))

def encrypt(oryginal_text, shift_amount):
    cipher_text = ""

    for letter in oryginal_text:
        shifted_position = alfabet.index(letter) + shift_amount
        shifted_position %= len(alfabet) # 0 - 25
        cipher_text += alfabet[shifted_position]
    print(f"The encoded text is {cipher_text}")

encrypt(oryginal_text, shift_amount)