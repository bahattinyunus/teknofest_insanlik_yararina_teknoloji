"""
Teknofest Humanity Technology Project - Utilities
Developed by: Bahattin Yunus Çetin
"""

import datetime

def get_timestamp():
    """
    Returns the current timestamp in standard format.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_message(message, level="INFO"):
    """
    Logs a message to the console with timestamp.
    """
    timestamp = get_timestamp()
    print(f"[{timestamp}] [{level}] {message}")
