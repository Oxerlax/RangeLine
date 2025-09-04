"""
File Name: update.py
Author: Kris Bali
-----------

Handles user input, adding, and removing golf distances for certain golf clubs
from the golf statistics JSON file.

Used by:
    Tests/test_rangeline.py
    Main/rangeline.py

Dependencies:
    collections (Counter, deque)
    JSON.json_file_handling (local module)
    matplotlib.ticker.MultipleLocator
    matplotlib.pyplot
"""

from collections import Counter
from collections import deque
from JSON import json_file_handling as file
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt


def confirm(prompt, data=None):
    """
    Prompt the user for confirmation input.

    Displays a prompt (and optional data) to the user and reads their input.
    If `data` is provided, it is shown after the prompt.
    Returns True if the user enters 'y', otherwise False when `data` is given.
    If no `data` is provided, returns the user's raw lowercase response string.

    Args:
        prompt (str): The message displayed to the user.
        data (str, optional): Additional information to display alongside the prompt.

    Returns:
        bool | str: True if the user confirms ('y') when data is provided,
        otherwise the lowercase user input string.
    """

    if data is not None:
        return input(f"{prompt}\n{data}: ").strip().lower() == 'y'
    else:
        return input(f"{prompt}: ").strip().lower()


def record_distances(summary, club, distances, test=False):
    """
    Record new shot distances for a specific golf club and update statistics.

    Updates the total shots, total distance, and recalculates the average
    distance for the given club. Maintains two rolling lists of the most
    recent 5 and 15 shots. The updated data is saved to the JSON file
    through `file.save_summary()`.

    If the club has at least 15 recorded shots, prompts the user to optionally
    display a trend line of the last 15 distances using Matplotlib.

    Args:
        summary (dict): The full golf statistics data for all clubs.
        club (str): The name of the golf club being updated.
        distances (list[int | float]): The list of new shot distances to record.
        test (bool): Used for test_rangeline.py testing purposes

    Returns:
        dict: The updated statistics dictionary for the given club.
    """

    for distance in distances:
        summary[club]["Total Shots"] += 1
        summary[club]["Total Distance"] += distance

        past_5_shots = deque(summary[club]["Past 5 Shots"])
        if len(past_5_shots) == 5:
            past_5_shots.popleft()
        past_5_shots.append(distance)

        summary[club]["Past 5 Shots"] = list(past_5_shots)

        past_15_shots = deque(summary[club]["Past 15 Shots"])
        if len(past_15_shots) == 15:
            past_15_shots.popleft()
        past_15_shots.append(distance)

        summary[club]["Past 15 Shots"] = list(past_15_shots)

    if summary[club]["Total Shots"] != 0:
        summary[club]["Average Distance"] = round(summary[club]["Total Distance"] / summary[club]["Total Shots"], 2)
    else:
        summary[club]["Average Distance"] = 0

    file.save_summary(summary)

    print(f"\n{club.capitalize()} Average Distance: {summary[club]['Average Distance']} yards")

    if len(summary[club]["Past 15 Shots"]) == 15 and test:
        if confirm("Show trend line? (y/n)"):
            plt.plot([i for i in range(1, 16)], summary[club]["Past 15 Shots"])

            ax = plt.gca()
            ax.xaxis.set_major_locator(MultipleLocator(1))
            ax.yaxis.set_major_locator(MultipleLocator(50))

            plt.show()

    return summary[club]


def remove_distances(current_distances, delete_distances):
    """
    Remove specific shot distances from a list of current distances.

    Uses a counter to ensure only the specified number of matching distances
    are removed (not all occurrences). Each distance in `delete_distances`
    is removed once per count from `current_distances`, preserving order
    for the remaining values.

    Args:
        current_distances (list[int]): The list of current recorded shot distances.
        delete_distances (list[int]): The list of shot distances to remove.

    Returns:
        list[int]: A new list of distances with the specified values removed.
    """

    delete_map = Counter(delete_distances)
    new_distances = []

    i = 0
    while i < len(current_distances):
        if not delete_map:
            new_distances.extend(current_distances[i:])
            break

        if current_distances[i] in delete_map:
            if delete_map[current_distances[i]] == 1:
                del delete_map[current_distances[i]]
            else:
                delete_map[current_distances[i]] -= 1
        else:
            new_distances.append(current_distances[i])

        i += 1

    return new_distances