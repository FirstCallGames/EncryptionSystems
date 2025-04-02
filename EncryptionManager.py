from CaesarCipher import CaesarCipher
from SubstitutionCipher import SubstitutionCipher

def Encrypt(Text_Export):
    while True:
        encryption = input("Enter Encryption Type{type help to get list/Exit}: ")
        if encryption == "help":
            listofencryption = ["Caesar Cipher: CC", "Substitution Cipher: SC"]
            for i in listofencryption:
                print(i)
        elif encryption == "CC": return CaesarCipher(Text_Export)
        elif encryption == "SC": return SubstitutionCipher(Text_Export)
        elif encryption == "Exit": break
        else:print("Invalid Encryption Type")


def process_file(file_text, file_export, encryption_function):
    with open(file_export, "r") as file:
        lines = file.readlines()

    encrypted_lines = encryption_function(lines)

    with open(file_text, "w") as file:
        file.writelines(f"{line}\n" for line in encrypted_lines)

while True:
    input_mode = input("Enter mode of input[Text: T ; File : F ; Exit]: ")
    if input_mode == "T":
        text = input("Enter text: ")
        print(Encrypt(text))
    elif input_mode == "F":
        file_text = input("Enter location of file with text: ")
        file_export = input("Enter location of file to export: ")
        process_file()

    elif input_mode == "Exit":
        print("Thank you for using EncryptionManager")
        break
    else: print("Invalid Input")


"""
Mechanism's Broken: 

1) CC -> Type: File || Writing to a file with multiple lines {Possible Tried: E and D}
2) SC -> Type: File || Writing to a file just copies the text into multiple lines, i.e., every character is just every line.
3) 
"""