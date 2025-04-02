import string

Smallletters = list(string.ascii_lowercase)
Capletters = list(string.ascii_uppercase)

Capencr_letters = ['Q', 'A', 'Z', 'W', 'S', 'X', 'E', 'D', 'C', 'R', 'F', 'V', 'T', 'G', 'B', 'Y', 'H', 'N', 'U', 'J', 'M', 'I', 'K', 'O', 'L', 'P']
Smallencr_letters = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']

def EncryptDecrypt(text, mode):
    result_sentence = ''
    print("EncDecr Received: ", type(text))

    if mode == "E":
        encryptCapDict = dict(zip(Capletters, Capencr_letters))
        encryptSmallDict = dict(zip(Smallletters, Smallencr_letters))
    else:
        encryptCapDict = dict(zip(Capencr_letters, Capletters))
        encryptSmallDict = dict(zip(Smallencr_letters, Smallletters))

    for line in text:
        result_sentence = ''
        for char in line:
            if char in Capletters:
                result_sentence += encryptCapDict[char]
            elif char in Smallletters:
                result_sentence += encryptSmallDict[char]
            else:
                result_sentence += char
        result_sentence += result_sentence
    return result_sentence

def SubstitutionCipher(text):
    opt = input("Enter your choice(Encrypt: E,Decrypt: D,Exit): ")

    while True:
        if opt == "E":
            return EncryptDecrypt(text,"E")
        elif opt == "D":
            return EncryptDecrypt(text,"D")
        elif opt == "Exit":
            break
        else:
            print("Please enter valid option")
            SubstitutionCipher(text)