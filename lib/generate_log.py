from datetime import datetime
import os

def generate_log(data):
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