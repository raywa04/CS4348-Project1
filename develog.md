# Devlog Entry - [03-18-2025, 7:05PM] 
This project involves creating three programs: a **logger**, an **encryption program**, and a **driver program**. The logger records all actions in a log file with timestamps. The encryption program uses the **Vigenère cipher** to encrypt/decrypt strings based on a passkey. The driver program acts as the user interface, allowing users to set passwords, encrypt/decrypt strings, and view history, while logging all actions.

### Key Points:
1. **Logger**: Logs actions with timestamps. Stops on "QUIT".
2. **Encryption Program**: Handles `PASS`, `ENCRYPT`, `DECRYPT`, and `QUIT` commands. Uses Vigenère cipher (letters only, case-insensitive).
3. **Driver Program**: Manages user interaction, communicates with logger and encryption program via pipes, and maintains a history of strings (except passwords).

### Plan:
- Use **Python** for simplicity and `subprocess` for inter-process communication.
- Implement Vigenère cipher, ensuring it handles only letters and errors on invalid input.
- Build each program separately, then integrate and test for robustness.

### Challenges:
- Managing pipe communication between programs.
- Ensuring correct handling of edge cases in encryption/decryption.
- Implementing history without storing passwords.

Next steps: Research Vigenère cipher, prototype each program, integrate, and test thoroughly.
