from datetime import datetime

def get_current_date():
    """Return today's date in DD-MM-YYYY format."""
    return datetime.now().strftime("%d-%m-%Y")


def get_current_time():
    """Return current time in HH:MM:SS format."""
    return datetime.now().strftime("%H:%M:%S")


def get_timestamp():
    """Return current timestamp in 'DD-MM-YYYY HH:MM:SS'."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def format_date(date_str):
    """
    Convert 'YYYY-MM-DD' to 'DD Mon YYYY'.
    Example: 2025-11-19 → 19 Nov 2025
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d %b %Y")
    except ValueError:
        return date_str


def validate_date(date_str):
    """
    Validate if string is a proper date in YYYY-MM-DD format.
    Returns True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
