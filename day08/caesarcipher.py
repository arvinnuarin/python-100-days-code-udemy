# Caesar Cipher
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encrypt
def encrypt(message, shift_amount):
    encrypted = ""

    for letter in message:
        encrypted += alphabet[alphabet.index(letter) + shift_amount]

    print(f"Here's the encoded result: {encrypted}")

# Decrypt
def decrypt(message, shift_amount):
    decrypted = ""

    for letter in message:
        decrypted += alphabet[alphabet.index(letter) - shift_amount]

    print(f"Here's the decoded result: {decrypted}")

# Caesar (combination)
def caesar(message, shift_amount, direction):
    output = ""

    if shift_amount > 25:
        shift_amount = shift_amount % 26
    
    if direction == "decode":
        shift_amount *= -1

    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            output += alphabet[position + shift_amount]
        else:
            output += letter

    print(f"The {direction}d text is: {output}")

# Menu
def menu():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if(direction != "encode" and direction != "decode"):
        print("Invalid direction! Please use (encode, decode) only!")
        exit()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)


######### START #########
print(art.logo + "\n")
menu()
tryagain = input(("Type 'yes' if you want to go again. Otherwise type 'no'\n"))

while(tryagain == "yes"):
    print("\n===========")
    menu()

print("Goodbye!")

#if direction == "encode":
 #   encrypt(text, shift)
#elif direction == "decode":
 #   decrypt(text, shift)
 