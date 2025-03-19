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

# Devlog Entry - [03-18-2025, 7:10PM] 
### **Thoughts So Far:** 
The project involves three main components: a logger, an encryption program, and a driver program. The goal is to create a system where the driver program interacts with the user, encrypts/decrypts strings using the Vigenère cipher, and logs all actions.

I’ve been thinking about how to structure the system:
- The logger needs to handle log messages with timestamps and write them to a file. It should run continuously until it receives the "QUIT" command.
- The encryption program needs to implement the Vigenère cipher, handle commands like PASS, ENCRYPT, and DECRYPT, and respond with RESULT or ERROR.
- The driver program will act as the user interface, managing communication between the user, the logger, and the encryption program using pipes.

## **Plan for This Session:**

### **Goal:** 
Start implementing the logger program as described in the project requirements.

### **Steps:**
- Create a Python script for the logger.
- Implement functionality to accept log messages via standard input.
- Write log entries to a file in the format YYYY-MM-DD HH:MM [ACTION] MESSAGE.
- Handle the "QUIT" command to stop logging.

# Devlog Entry - [03-18-2025, 9:00PM] 
### **Accomplishments:** 
- I accomplished my goal for this session.
- Successfully implemented the logger program in Python.
- The logger accepts a log file name as a command-line argument and writes log entries in the format YYYY-MM-DD HH:MM [ACTION] MESSAGE.
- Tested the logger by manually entering log messages and verified that the log file (log.txt) was created and updated correctly.
- Also tested automated input by redirecting input from a file (input.txt), which worked as expected.

### **Problems Encountered:** 
- Initially, I wasn’t sure how to handle the "QUIT" command to stop the logger. I resolved this by checking for "QUIT" in the input loop and breaking out of the loop when it’s received.
- I also had to ensure that the log file was flushed after each write to avoid delays in writing to the file. This was fixed by calling f.flush() after each log entry.

### **Additional Accomplishments:**
- Added error handling for cases where the log message doesn’t contain both an action and a message (e.g., if the user enters an empty line or only one word).
- Tested edge cases, such as empty log messages and very long log messages, to ensure the logger handles them gracefully.

### **Goals for next session:**
- Implement encryption part of the project. 

