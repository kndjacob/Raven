import os
import random

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_menu():
    clear_screen()
    print("""
    888d888 8888b. 888  888 .d88b. 88888b.  
    888P"      "88b888  888d8P  Y8b888 "88b 
    888    .d888888Y88  88P88888888888  888 
    888    888  888 Y8bd8P Y8b.    888  888 
    888    "Y888888  Y88P   "Y8888 888  888

    Encryption made easy.
    """)

def get_user_input():
    return input("\n(E)ncrypt - Encrypt a .txt\n(D)ecrypt - Decrypt a .txt\n(G)enerate Key - Generate a 1024 character key\n(N)ew Message - Create your own .txt\n(I)nformation - FIRST TIME USERS READ ME!\n(Q)uit - Exits the application\n").upper()

def generate_new_message():
    print("GENERATING NEW MESSAGE . . . Q to QUIT")
    message = input("Message: ")
    if message.upper() == "Q":
        return
    file_name = input("\nSave as: ")
    if file_name.upper() == "Q":
        return
    with open(file_name + ".txt", 'w') as f:
        f.write(message)

def display_information():
    print("""
    ! ! ! IMPORTANT ! ! !

    DO NOT USE FILE EXTENSIONS IN YOUR NAMES! THE APPLICATION AUTOMATICALLY SAVES AND LOADS FILENAMES AS "{FILENAME}.txt"

    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                                            MODULE INFORMATION

    Encryption - To Encrypt a message you will need a key. This can be any .txt file. It is recommended to generate a random key. Please see the Generation manual.

    Decryption - To decrypt a message you will need a key. This can be any .txt file. TO DECRYPT A MESSAGE YOU WILL NEED TO USE THE SAME KEY IT WAS ENCRYPTED WITH. ELSE IT WILL BE JUMBLED RANDOMNESS!

    Message Generation - The message generation module is used to create a .txt file that contains your message to be encrypted and sent to another user.

    Key Generation - The Key Generator generates a randomized 1024 character cipher key that is used to encrypt and decrypt messages. Use this to create keys to keep things secret!

                                            HOW IT WORKS

    The Raven application is a python program that utilizes a simple replacement process that is obtained from the decimal value of ASCII characters. To do so, the program takes a key and loops through it at the same time it does the message, and counts the length and value of characters, and then replaces the values of each.

                                            EXAMPLE PROCESS

    Step 1.) Generate a new key

        Select the Generate Key module.
        Once the application finishes, save the key as a memorable name.
        It is important that you use the same key to decrypt later.

    Step 2.) Generate a Message to use

        Select the Generate New Message module.
        Type out your message and then save it with a memorable name.

    Step 3.) Encrypt a message

        Select the Encryption Module
        Select the cipher you want to use.
        Select the plaintext message you want to encrypt.
        Save the encrypted message as a memorable name.

    Step 4.) Decrypt a message

        Select the Decryption Module
        Select the cipher you want to use (must be the same one used during encryption).
        Select the ciphertext message you want to decrypt.
        Save the decrypted (now plaintext) message.
    """)
    input("\n\nPress enter to return to main menu.")

def generate_key():
    print("GENERATING NEW CIPHER KEY\n\nPRESS Q TO EXIT")
    key = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(1024))
    file_name = input("KEY NAME: ")
    if file_name.upper() == "Q":
        return
    with open(file_name + ".txt", 'w') as f:
        f.write(key)
    input("Saved " + file_name + " successfully! Press enter to return to main menu.")

def select_file(prompt):
    while True:
        file_name = input(prompt) + ".txt"
        if file_name.upper() == "Q":
            return None
        try:
            with open(file_name, encoding="utf8") as f:
                return f.read()
        except FileNotFoundError:
            print("Invalid file name.\n\n\tCURRENT FILES IN DIRECTORY: ")
            for file in os.listdir():
                print("\t" + file)

def encrypt_decrypt_message(is_encrypt=True):
    clear_screen()
    action = "ENCRYPTING" if is_encrypt else "DECRYPTING"
    print(f"\t{action}\n\nFILES IN CURRENT DIRECTORY:\n\n")
    for file in os.listdir():
        print("\t" + file)
    print("\n------------------------------\nPRESS Q TO EXIT\n")

    key_text = select_file("Cipher Key: ")
    if not key_text:
        return
    message_text = select_file("Message: ")
    if not message_text:
        return

    out_message = ""
    key_len = len(key_text)

    for i, char in enumerate(message_text):
        key_char = key_text[i % key_len]
        if is_encrypt:
            new_char = (ord(char) + len(key_char)) % 128
        else:
            new_char = (ord(char) - len(key_char)) % 128
        out_message += chr(new_char)

    print("MESSAGE: \n\n" + out_message)
    message_save = input("Save message? (Y/N): ").upper()
    if message_save == "Y":
        file_name = input("FILENAME: ")
        with open(file_name + ".txt", 'w') as f:
            f.write(out_message)
    input("Press enter to return to main menu.")

def main():
    VALID_INPUTS = {"E", "D", "Q", "G", "N", "I"}
    while True:
        display_menu()
        user_input = get_user_input()
        if user_input not in VALID_INPUTS:
            input("Invalid input... Press enter to continue.")
            continue
        clear_screen()
        if user_input == "N":
            generate_new_message()
        elif user_input == "I":
            display_information()
        elif user_input == "G":
            generate_key()
        elif user_input == "Q":
            break
        elif user_input == "E":
            encrypt_decrypt_message(True)
        elif user_input == "D":
            encrypt_decrypt_message(False)

if __name__ == "__main__":
    main()
