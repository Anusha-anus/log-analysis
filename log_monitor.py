import logging
import os
import time

# Function to analyze the log file
def analyze_log(log_file):
    # Open the log file
    with open(log_file, 'r') as file:
        lines = file.readlines()
    
    # Example analysis: count the number of lines
    num_lines = len(lines)
    
    # Example analysis: count the occurrences of a specific keyword
    keyword = 'ERROR'
    num_errors = sum(1 for line in lines if keyword in line)
    
    return num_lines, num_errors

# Function to monitor the log file continuously
def monitor_log(log_file, interval=10):
    while True:
        num_lines, num_errors = analyze_log(log_file)
        print(f"Total lines: {num_lines}, Errors: {num_errors}")
        time.sleep(interval)

# Example usage
if __name__ == "__main__":
    log_file = 'example.log'  # Change this to the path of your log file
    monitor_log(log_file)

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define log levels
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

# Function to continuously log messages at different levels
def log_messages():
    while True:
        # Loop through log levels
        for level in log_levels:
            # Log message at current level
            if level == logging.INFO:
                logging.info("This is an INFO message")
            elif level == logging.DEBUG:
                logging.debug("This is a DEBUG message")
            elif level == logging.ERROR:
                logging.error("This is an ERROR message")
            
            # Sleep for a short interval before logging next message
            time.sleep(1)

if __name__ == "__main__":
    log_messages()
