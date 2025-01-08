import string

# alfabet
alfabet = list(string.ascii_lowercase)
# alfabet = [chr(i) for i in range(ord("a"), ord("z")+1)]


def encrypt(text, shift):  
    # encrypting text  
    cipher_text = ""

    for letter in text:
        if letter in alfabet:
            shifted_position = (alfabet.index(letter) + shift) % len(alfabet)
            cipher_text += alfabet[shifted_position]
        else:
            cipher_text += letter # for spaces, numbers, etc.
    return cipher_text


def decrypt(text, shift):
    # decrypting text
    cipher_text = ""

    for letter in text:
        if letter in alfabet:
            shifted_position = (alfabet.index(letter) - shift) % len(alfabet)
            cipher_text += alfabet[shifted_position]
        else:
            cipher_text += letter # for spaces, numbers, etc.
    return cipher_text

print("""
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝

░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
      """)

# General cycle of program
print("""
      Hello, welcome to Caesar Cipher program!
      You can encrypt or decrypt your text using this tool. 
      """)

while True:
    program = input("""
                    Type '1' for encryption or '2' for decryption. 
                    Type 'q' to quit the program. 
                    """)

    if program == "1":
        text = input("Enter the text you want to encrypt: ").lower()
        shift = int(input("Enter the shift amount: "))
        print(f"Encrypted text: {encrypt(text, shift)}")
    elif program == "2":
        text = input("Enter the text you want to decrypt: ").lower()
        shift = int(input("Enter the shift amount: "))
        print(f"Decrypted text: {decrypt(text, shift)}")
    elif program.lower() == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")