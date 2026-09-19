from datetime import datetime


def log_activity(message):
    """Write a timestamped activity to the log file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("activity.log", "a") as file:
        file.write(f"{timestamp} - {message}\n")