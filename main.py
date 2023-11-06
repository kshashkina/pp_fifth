def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            key_value = (ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')) + key
            if char.isupper():
                encrypted_text += chr(((key_value % 26) + ord('A')))
            else:
                encrypted_text += chr(((key_value % 26) + ord('a')))
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)



def readFile(path):
    with open(path, 'r') as file:
        return file.read()


def writeFile(path, text):
    with open(path, 'w') as file:
        file.write(text)


def main():
 while True:
    command = int(input("Choose your command\n1 - Encrypt text into the file\n2 - decrypt text from the file\n"))
    result_text = ""

    key = int(input("Enter the key value: "))
    read = input("Enter the name of the input file: ").strip()
    write = input("Enter the name of the output file: ").strip()
    text = readFile(read)

    if command == 1:
        result_text = caesar_encrypt(text, key)
    elif command == 2:
        result_text = caesar_decrypt(text, key)
    else:
        print("Invalid input")
        return

    writeFile(write, result_text)

if __name__ == "__main__":
    main()
