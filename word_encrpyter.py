def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted message:", encrypted)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted message:", encrypted)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
