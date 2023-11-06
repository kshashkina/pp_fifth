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


def main():
    text = input("Enter the text: ")
    key = int(input("Enter the key value: "))

    encrypted_text = caesar_encrypt(text, key)
    decrypted_text = caesar_decrypt(encrypted_text, key)

    print("Original text:", text)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()
