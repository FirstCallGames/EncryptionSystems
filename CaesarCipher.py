import string

def create_caesar_dict():
    l = string.ascii_lowercase
    l = list(l)
    Enc_dict = {}
    Dec_dict = {}

    for i in range(len(l)):
        Enc_dict[l[i]] = l[(i+3) % 26]
        Dec_dict[l[(i+3) % 26]] = l[i]
    
    action = input("Enter action ('Decode [D]', 'Encode [E]'): ")

    if action == "E":
        text_input = input("Enter text to Cipher: ")
    
        ans_text = ""
        for i in text_input:
            if i != " ":
                ans_text += Enc_dict[i.lower()]
            else:
                ans_text += " "
        print(ans_text)

    elif action == "D":
        text_input = input("Enter text to Decipher: ")
        ans_text = ""
        for i in text_input:
            if i != " ":
                ans_text += Dec_dict[i.lower()]
            else:
                ans_text += " "
        print(ans_text)


create_caesar_dict()

