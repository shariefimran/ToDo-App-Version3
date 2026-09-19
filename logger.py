from datetime import datetime
from config import LOG_FILE

def log_activity(message):
    """Write a timestamped activity to the log file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("LOG_FILE", "a") as file:
        
        file.write(f"{timestamp} - {message}\n")