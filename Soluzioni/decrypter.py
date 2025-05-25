def encrypt(string):
    encripted_str = ''
    for index,char in enumerate(string):
        encripted_str += chr(ord(char) + index)
    return encripted_str

def decrypt(string):
    decripted_string = ''
    for index, char in enumerate(string):
        decripted_string += chr(ord(char) - index)
    return decripted_string

file_path = raw_input("Inserisci path del file:")

try:
    with open(file_path, "r") as file:
        token = file.read().strip()
        print(decrypt(token))
except IOError:
    print("Errore apertura file")