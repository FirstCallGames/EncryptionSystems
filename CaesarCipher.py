import string

def CaesarCipher(text_input):
    l = string.ascii_lowercase
    l = list(l)
    Enc_dict = {}
    Dec_dict = {}

    for i in range(len(l)):
        Enc_dict[l[i]] = l[(i+3) % 26]
        Dec_dict[l[(i+3) % 26]] = l[i]
    
    def EncodeDecode(text, action):
        ans_text = ""
        def process_char(char, action):
            if char.isalpha():
                if action == "E":
                   return Enc_dict[char.lower()]
                elif action == "D":
                    return Dec_dict[char.lower()]
            else:
                return char

        if isinstance(text, str):
            return ''.join(process_char(char, action) for char in text)
        elif isinstance(text, list):
            return [''.join(process_char(char,action) for char in line) for line in text]
        else:
            raise TypeError("Unsupported type.")

    while True:
        action = input("Enter your choice(Encrypt: E,Decrypt: D,Exit): ")
        if action == "E":
            return EncodeDecode(text_input, "E")
        elif action == "D":
            return EncodeDecode(text_input, "D")
        elif action == "Exit":
            break
        else:
            print("Invalid choice")