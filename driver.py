#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

def main():
    # Check if the log file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: driver.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    # Start the logger process
    logger = Popen(['python3', 'logger.py', log_file], stdin=PIPE, encoding='utf8')

    # Start the encryption process
    encryption = Popen(['python3', 'encryption.py'], stdin=PIPE, stdout=PIPE, encoding='utf8')

    # Log the start of the driver program
    logger.stdin.write(f"START Driver program started.\n")
    logger.stdin.flush()

    # History of strings entered during the session
    history = []

    while True:
        # Print the menu
        print("\nMenu:")
        print("1. Set password")
        print("2. Encrypt a string")
        print("3. Decrypt a string")
        print("4. Show history")
        print("5. Quit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Set password
            password = input("Enter a new password (letters only): ").strip().upper()
            if password.isalpha():
                # Send the PASS command to the encryption program
                print(f"Sending PASS command: PASS {password}", file=sys.stderr)  # Debugging
                encryption.stdin.write(f"PASS {password}\n")
                encryption.stdin.flush()

                # Read the response
                print("Waiting for response...", file=sys.stderr)  # Debugging
                response = encryption.stdout.readline().rstrip()
                print(f"Received response: {response}", file=sys.stderr)  # Debugging

                if response == "RESULT":
                    print("Password set successfully.")
                    logger.stdin.write(f"PASS Password set.\n")
                else:
                    print("Error setting password.")
                    logger.stdin.write(f"ERROR Failed to set password.\n")
                logger.stdin.flush()
            else:
                print("Error: Password must contain only letters.")
                logger.stdin.write(f"ERROR Invalid password (non-letter characters).\n")
                logger.stdin.flush()

        elif choice == "2":
            # Encrypt a string
            string = input("Enter a string to encrypt (letters only): ").strip().upper()
            if string.isalpha():
                # Send the ENCRYPT command to the encryption program
                print(f"Sending ENCRYPT command: ENCRYPT {string}", file=sys.stderr)  # Debugging
                encryption.stdin.write(f"ENCRYPT {string}\n")
                encryption.stdin.flush()

                # Read the response
                print("Waiting for response...", file=sys.stderr)  # Debugging
                response = encryption.stdout.readline().rstrip()
                print(f"Received response: {response}", file=sys.stderr)  # Debugging

                if response.startswith("RESULT"):
                    encrypted_string = response.split(maxsplit=1)[1]
                    print(f"Encrypted string: {encrypted_string}")
                    history.append(f"Encrypted: {string} -> {encrypted_string}")
                    logger.stdin.write(f"ENCRYPT Encrypted '{string}' to '{encrypted_string}'.\n")
                else:
                    print("Error encrypting string.")
                    logger.stdin.write(f"ERROR Failed to encrypt '{string}'.\n")
                logger.stdin.flush()
            else:
                print("Error: String must contain only letters.")
                logger.stdin.write(f"ERROR Invalid input for encryption (non-letter characters).\n")
                logger.stdin.flush()

        elif choice == "3":
            # Decrypt a string
            string = input("Enter a string to decrypt (letters only): ").strip().upper()
            if string.isalpha():
                # Send the DECRYPT command to the encryption program
                print(f"Sending DECRYPT command: DECRYPT {string}", file=sys.stderr)  # Debugging
                encryption.stdin.write(f"DECRYPT {string}\n")
                encryption.stdin.flush()

                # Read the response
                print("Waiting for response...", file=sys.stderr)  # Debugging
                response = encryption.stdout.readline().rstrip()
                print(f"Received response: {response}", file=sys.stderr)  # Debugging

                if response.startswith("RESULT"):
                    decrypted_string = response.split(maxsplit=1)[1]
                    print(f"Decrypted string: {decrypted_string}")
                    history.append(f"Decrypted: {string} -> {decrypted_string}")
                    logger.stdin.write(f"DECRYPT Decrypted '{string}' to '{decrypted_string}'.\n")
                else:
                    print("Error decrypting string.")
                    logger.stdin.write(f"ERROR Failed to decrypt '{string}'.\n")
                logger.stdin.flush()
            else:
                print("Error: String must contain only letters.")
                logger.stdin.write(f"ERROR Invalid input for decryption (non-letter characters).\n")
                logger.stdin.flush()

        elif choice == "4":
            # Show history
            print("\nHistory:")
            for entry in history:
                print(entry)
            logger.stdin.write(f"HISTORY Displayed history.\n")
            logger.stdin.flush()

        elif choice == "5":
            # Quit the program
            print("Exiting...")
            logger.stdin.write(f"QUIT Driver program exiting.\n")
            logger.stdin.flush()

            # Send QUIT to the encryption program
            encryption.stdin.write("QUIT\n")
            encryption.stdin.flush()

            # Wait for the processes to finish
            encryption.wait()
            logger.wait()
            break

        else:
            print("Invalid choice. Please try again.")
            logger.stdin.write(f"ERROR Invalid menu choice.\n")
            logger.stdin.flush()

if __name__ == "__main__":
    main()