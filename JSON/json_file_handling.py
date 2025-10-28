"""
File Name: json_file_handling.py
Author: Kris Bali
----------

Handles loading, saving, and resetting golf club statistics data stored in a JSON file.

Used by:
    Logic/update.py
    Tests/test_rangeline.py
    Main.rangeline.py

Dependencies:
    os
    json
"""


import os
import json

# File path used to store all golf club statistics in JSON format.
GOLF_DATA_FILE = "../JSON/golf_clubs_statistics.json"


# List of all golf club names tracked in the golf statistics JSON data.
CLUB_NAMES = [
    "driver", "3w", "5w", "7w",
    "0i", "0hy", "1i", "1hy", "2i", "2hy", "3i", "3hy", "4i", "4hy",
    "5i", "5hy", "6i", "6hy", "7i", "7hy", "8i", "8hy", "9i", "9hy",
    "pw", "gw", "sw", "lw", "putter"
]


# Default statistics for each club, used when no previous data exists.
DEFAULT_STATS = {
    "Average Distance": 0,
    "Total Distance": 0,
    "Total Shots": 0,
    "Past 5 Shots": [],
    "Past 15 Shots": [],
}


def save_summary(summary) -> None:
    """
    Updates the golf statistics JSON file with golf club statistics data

    Args:
        summary (dict): data to import into the json file
    """

    with open(GOLF_DATA_FILE, "w") as f:
        json.dump(summary, f, indent=2)


def delete_all_golf_data() -> None:
    """
    Deletes the golf statistics JSON file, if it exists.
    """

    if os.path.exists(GOLF_DATA_FILE):
        os.remove(GOLF_DATA_FILE)


def load_or_initialize_summary() -> dict:
    """Loads data from golf statistics JSON file if it exists, or initializes default data.

    Return:
         dict: A summary of golf club statistics.
    """

    if os.path.exists(GOLF_DATA_FILE):
        with open(GOLF_DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {club: DEFAULT_STATS.copy() for club in CLUB_NAMES}