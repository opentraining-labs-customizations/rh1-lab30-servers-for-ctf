import time
import os
from datetime import datetime

def read_and_prepend_timestamp(file_path):
    """
    Continuously reads the file, prepends the current timestamp to each line, and prints it.
    """
    while True:
        # Check if the file exists and is not empty
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as file:
                for line in file:
                    # Get the current UTC time in the required format
                    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                    timestamp = f"{current_time}"

                    # Print the timestamped line to the console
                    print(f"{timestamp} {line.strip()}")
                    # Sleep for 1 second before processing the next line
                    time.sleep(1.5)
        time.sleep(5)

if __name__ == '__main__':
    # Path to the log file you want to read
    file_path = "/home/1001/ghost_logs"

    # Call the function to read and prepend timestamp to each line
    read_and_prepend_timestamp(file_path)
