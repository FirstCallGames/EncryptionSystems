import string

def caesar():
    l = string.ascii_lowercase
    l = list(l)
    Enc_dict = {}
    Dec_dict = {}

    for i in range(len(l)):
        Enc_dict[l[i]] = l[(i+3) % 26]
        Dec_dict[l[(i+3) % 26]] = l[i]
    
    def Encode(text):
        ans_text = ""
        for i in text:
            if i.isalpha():
                ans_text += Enc_dict[i.lower()]
            else:
                ans_text += i
        return ans_text
    
    def Decode(text):
        ans_text = ""
        for i in text:
            if i.isalpha():
                ans_text += Dec_dict[i.lower()]
            else:
                ans_text += i
        return ans_text

    action = input("Enter action ('File [F]', 'Text [T]'): ")

    if action.lower() == "t":
        action = input("Enter action ('Decode [D]', 'Encode [E]'): ")

        if action == "E":
            text_input = input("Enter text to Cipher: ")
            print(Encode(text_input))

        elif action == "D":
            text_input = input("Enter text to Decipher: ")
            print(Decode(text_input))

    elif action.lower() == "f":
        file_location = input("Enter the location of file: ")
        file_save_location = input("Enter location to save file: ")
        action = input("Enter action ('Decode [D]', 'Encode [E]'): ")

        if action == "E":
            try:
                with open(file_location, "r") as file:
                    text_file = file.read()
                with open(file_save_location, "w") as file2:
                    file2.write(Encode(text_file))
                print("The Ciphered data is saved.")
            except FileNotFoundError:
                print("File does not exist.")

        elif action == "D":
            try:
                with open(file_location, "r") as file:
                    text_file = file.read()
                with open(file_save_location, "w") as file2:
                    file2.write(Decode(text_file))
                print("The deciphered data is saved.")
            except FileNotFoundError:
                print("File does not exist.")

caesar()