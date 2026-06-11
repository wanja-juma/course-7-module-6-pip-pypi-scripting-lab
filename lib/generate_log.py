from datetime import datetime
import os

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename

   # lib/generate_log.py
    """
    Writes log entries to a dated text file and returns the filename.
    """

    """
    Creates a log file from a list of entries and returns filename.
    """

    # Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # Create filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Required confirmation message (tests expect print)
    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    sample = ["User logged in", "User updated profile"]
    generate_log(sample)