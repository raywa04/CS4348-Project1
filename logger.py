import sys
from datetime import datetime

def main():
    # Check if the log file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: logger.py <log_file>")
        sys.exit(1)

    # Get the log file name from the command-line argument
    log_file = sys.argv[1]

    # Open the log file in append mode
    with open(log_file, "a") as f:
        while True:
            # Read a log message from standard input
            message = sys.stdin.readline().rstrip()

            # Check for the "QUIT" command
            if message == "QUIT":
                break

            # Extract the action and message
            parts = message.split(maxsplit=1)
            if len(parts) < 2:
                action = "UNKNOWN"
                log_message = "No message provided"
            else:
                action, log_message = parts[0], parts[1]

            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

            # Write the log entry to the file
            log_entry = f"{timestamp} [{action}] {log_message}\n"
            f.write(log_entry)
            f.flush()  # Ensure the log entry is written immediately

if __name__ == "__main__":
    main()