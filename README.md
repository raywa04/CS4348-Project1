# **CS 4348 Operating Systems Project 1**

## **Project Overview**
This project implements a **Vigenère cipher-based encryption system** using Python. It consists of three main components:

1. **Logger (`logger.py`)** – Logs system activities with timestamps.
2. **Encryption Program (`encryption.py`)** – Encrypts and decrypts messages using the **Vigenère cipher**.
3. **Driver (`driver.py`)** – Manages user interaction, spawns subprocesses, and facilitates communication between the components.

---

## **Files and Their Roles**
- **`driver.py`** - Main entry point, responsible for managing subprocesses and handling user commands.
- **`encrypt.py`** - Performs encryption and decryption using the Vigenère cipher.
- **`logger.py`** - Records all user actions and system events to a log file.
- **`README.md`** - Documentation for the project.

---

## **How to Run the Program**
To execute the program, run the following command:
```sh
python3 driver.py logger.txt
```
This starts the **driver program**, which initializes the **logger** and **encryption** processes.

### **Available Commands**
| **Command** | **Description** |
|------------|---------------|
| `password` | Sets a new encryption password. |
| `encrypt` | Encrypts user input using the stored passkey. |
| `decrypt` | Decrypts previously encrypted messages. |
| `quit` | Stops all processes and exits the program. |

---

## **Notes for the TA Before Grading**
- Ensure **Python 3.10+** is used.
- Logs should be correctly written in `logger.txt` with timestamps.
- The encryption/decryption results should match expected outputs.

This implementation follows the project requirements and handles errors efficiently.

---
