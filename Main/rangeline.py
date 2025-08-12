"""
File Name: rangeline.py
Author: Kris Bali
------------

The main program to track golf distances provided by the user and save into a JSON file.

Dependencies:
    time (standard library)
    Logic.update (local module)
    JSON.json_file_handling (local module)
"""

import time
from Logic import update as upd
from JSON import json_file_handling as file


CLUB_NAMES = ("\n"
                  "Club Names:\n\n"
                  "Driver\n"
                  "A fairway wood such as a 3w, 5w, 7w\n"
                  "An iron from 0-9 (Ex: 4i)\n"
                  "A hybrid from 0-9 (Ex: 6hy)\n"
                  "A wedge such as a Pw, Gw, Sw, Lw\n"
                  "Putter\n")


def handle_quit_delete():
    """
    Handles user input for if the user wants to quit the program, delete all of
    their golf data, or simply continue.

    Returns:
        str | None: "quit" if the user entered the letter Q or q, "deleted" if the user entered
        the letter D or d, or None if they entered anything else
    """

    user_choice = input("\nEnter 'q' for quit, 'd' for delete all golf data, or anything else to continue: ").strip().lower()
    if user_choice == "q":
        return "quit"
    elif user_choice == "d":
        file.delete_all_golf_data()
        print("\nAll golf data deleted.")
        time.sleep(1)
        return "deleted"
    else:
        return None


def get_converted_distances(prompt):
    """
    Attempts to convert the string golf distances into a list of integer distances.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
         list[int] | None: a list of integers representing the user's most recently
         entered golf distances for their specific golf club, or None if the user did
         not properly enter in correct distances.

         Distances will not be converted if they can't physically be converted from a string to
         an int or if any of the distances are outside the range between 0-600, inclusive.
         The 0-600 range is used to account for all distances that could be hit
         by a golf club, both now and in the future.
    """

    try:
        shortened = input(prompt).strip().split(" ")
        return [int(distance) for distance in shortened if 0 <= int(distance) <= 600]
    except ValueError:
        print("\nInvalid input. Please type valid integer numbers with spaces between them.")
        return None


def confirm_club(summary, club_name):
    """
    Confirms if the club entered by the user is a valid club name.

    Args:
         summary (dict): golf data statistics to be imported into the JSON file
         club_name (str): the name of the golf club entered by the user

    Returns:
        bool: True if the club is a key of the summary, meaning it is a valid club name
        to modify statistics for inside of summary, or False otherwise.
    """
    if club_name not in summary:
        print("\nInvalid/no club name given. Please check spelling based on the club names provided.")
        time.sleep(1)
        return False
    else:
        return True


def is_quit(action):
    """
    Used for determining whether to break out of the main function loop or to continue

    Returns:
        True if the action is the string "quit", which will then break out of the
        main function's while loop and end the function, and false otherwise, which will continue
        the main program's while loop.
    """
    return action == "quit"


def main():
    """
    Runs the RangeLine golf statistics tracker.

    Loads or initializes club shot distance data, collects new distances from
    the user with validation, allows optional deletion of the newly entered
    distances, saves the updated statistics to JSON, and finally prompts the
    user to quit, reset all data, or continue.
    """

    while True:
        summary = file.load_or_initialize_summary()
        print(CLUB_NAMES)

        club_input = input("Club to track: ").strip().lower()
        valid_club = confirm_club(summary, club_input)
        if not valid_club:
            if is_quit(handle_quit_delete()):
                break
            else:
                continue

        converted_distances = get_converted_distances(
            "\nWhen entering distances, order them from oldest to newest with spaces between\n"
            "Distances must be realistic integers (the range of accepted distances is between 0-600 yards)\n"
            "Any distances outside of this range will be discarded\n"
            "Ex: 190 210 187 200 204\n"
            f"Distance(s) previously shot from {club_input} (yards): "
        )
        if not converted_distances or not upd.confirm("\nConfirm distances (y/n)", converted_distances):
            if is_quit(handle_quit_delete()):
                break
            else:
                continue

        distances = converted_distances
        if input(f"\nScores entered: {converted_distances}\n" f"If you mistyped or want to delete any of these scores, please enter 'd': ").strip().lower() == 'd':
            converted_delete = get_converted_distances("\nDistances to delete: ")
            while converted_delete is None:
                converted_delete = get_converted_distances("\nDistances to delete: ")
            if upd.confirm("\nConfirm distances to delete (y/n)", converted_delete):
                distances = upd.remove_distances(converted_distances, converted_delete)

        upd.record_distances(summary, club_input, distances)

        action = handle_quit_delete()
        if is_quit(action):
            break
        elif action == "deleted":
            continue


if __name__ == "__main__":
    main()