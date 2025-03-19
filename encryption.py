import sys

# Global variable to store the passkey
passkey = None

def vigenere_encrypt(plaintext, key):
    # Encrypts the plaintext using the Vigenère cipher.
    ciphertext = []
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            # Shift the character based on the corresponding key character
            shift = ord(key[i % key_length]) - ord('A')
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            # Non-alphabetic characters are not allowed
            return None
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    # Decrypts the ciphertext using the Vigenère cipher.
    plaintext = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            # Shift the character back based on the corresponding key character
            shift = ord(key[i % key_length]) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext.append(decrypted_char)
        else:
            # Non-alphabetic characters are not allowed
            return None
    return ''.join(plaintext)

def main():
    global passkey

    while True:
        # Read a command from standard input
        command = sys.stdin.readline().rstrip()

        if not command:
            continue  # Skip empty lines

        # Split the command into parts
        parts = command.split(maxsplit=1)
        cmd = parts[0].upper()
        arg = parts[1] if len(parts) > 1 else None

        if cmd == "PASS":
            # Set the passkey
            if arg and arg.isalpha():
                passkey = arg.upper()
                print("RESULT")
            else:
                print("ERROR Invalid passkey (must contain only letters)")
        elif cmd == "ENCRYPT":
            # Encrypt the argument using the current passkey
            if not passkey:
                print("ERROR No passkey set")
            elif arg and arg.isalpha():
                encrypted = vigenere_encrypt(arg.upper(), passkey)
                if encrypted:
                    print(f"RESULT {encrypted}")
                else:
                    print("ERROR Invalid input (must contain only letters)")
            else:
                print("ERROR Invalid input (must contain only letters)")
        elif cmd == "DECRYPT":
            # Decrypt the argument using the current passkey
            if not passkey:
                print("ERROR No passkey set")
            elif arg and arg.isalpha():
                decrypted = vigenere_decrypt(arg.upper(), passkey)
                if decrypted:
                    print(f"RESULT {decrypted}")
                else:
                    print("ERROR Invalid input (must contain only letters)")
            else:
                print("ERROR Invalid input (must contain only letters)")
        elif cmd == "QUIT":
            # Exit the program
            break
        else:
            # Unknown command
            print("ERROR Unknown command")

if __name__ == "__main__":
    main()