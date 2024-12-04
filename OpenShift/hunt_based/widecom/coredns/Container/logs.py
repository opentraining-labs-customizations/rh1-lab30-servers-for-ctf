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
                    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
                    # Get nanoseconds by converting current time to float and multiplying by 1e9
                    nanoseconds = int((time.time() % 1) * 1e9)
                    timestamp = f"{current_time}.{nanoseconds:09d}Z"

                    # Print the timestamped line to the console
                    print(f"{timestamp} {line.strip()}")
                    # Sleep for 1 second before processing the next line
                    time.sleep(.5)

        # Sleep for a short period before checking the file again
        time.sleep(1)

if __name__ == '__main__':
    # Path to the log file you want to read
    file_path = "/home/1001/coredns_logs"

    # Call the function to read and prepend timestamp to each line
    read_and_prepend_timestamp(file_path)
