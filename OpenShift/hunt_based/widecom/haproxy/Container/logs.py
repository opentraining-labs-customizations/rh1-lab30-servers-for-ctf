import time
import os
from datetime import datetime

def generate_timestamps():
    """
    Generates two timestamps:
    - timestamp1: Month Date HH:MM:SS (e.g., Aug 10 21:12:44)
    - timestamp2: [DD/Month/Year:HH:MM:SS] (e.g., [10/Aug/2024:21:12:44])
    """
    current_time = datetime.utcnow()

    # Format the first timestamp: "Month Date HH:MM:SS"
    timestamp1 = current_time.strftime('%b %d %H:%M:%S')

    # Format the second timestamp: "[DD/Month/Year:HH:MM:SS]"
    timestamp2 = current_time.strftime('[%d/%b/%Y:%H:%M:%S]')

    return timestamp1, timestamp2

def process_log_file(file_path):
    """
    Reads the log file, replaces the timestamp placeholders with dynamic timestamps, and prints the updated log line.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return

    # Read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Get dynamic timestamps
            timestamp1, timestamp2 = generate_timestamps()

            # Replace the placeholders with the generated timestamps
            modified_line = line.replace("timestamp1", timestamp1).replace("timestamp2", timestamp2)

            # Print the modified line to stdout
            print(modified_line.strip())
            time.sleep(.5)

if __name__ == "__main__":
    # Path to the log file
    file_path = "/home/1001/haproxy_logs"  # Modify this to the actual file path

    while True:
        # Process the log file
        process_log_file(file_path)
        time.sleep(1)
