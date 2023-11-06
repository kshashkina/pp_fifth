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
