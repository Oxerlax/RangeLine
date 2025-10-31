"""
File Name: test_rangeline.py
Author: Kris Bali
----------

Handles testing different cases of rangeline.py data management.

Dependencies:
    unittest (standard library)
    JSON.json_file_handling (load_or_initialize_summary, delete_all_golf_data)
    Logic.update (record_distances, remove_distances)
"""

from JSON.json_file_handling import load_or_initialize_summary, delete_all_golf_data
from Logic.update import record_distances, remove_distances


def test_json_initialization():
    """Test JSON file initialization and appending distances to certain clubs."""

    # Remove golf statistics JSON file, if it exists
    delete_all_golf_data()

    # Use a dict with default golf statistics
    summary = load_or_initialize_summary()

    # Typical case
    result = record_distances(summary, "driver", [100, 200, 100, 200, 100, 200], True)
    assert result == {
        "Average Distance": 150.0,
        "Total Distance": 900,
        "Total Shots": 6,
        "Past 5 Shots": [200, 100, 200, 100, 200],
        "Past 15 Shots": [100, 200, 100, 200, 100, 200],
    }

    # Edge case: no distances added (empty list)
    result = record_distances(summary, "3w", [], True)
    assert result == {
        "Average Distance": 0.0,
        "Total Distance": 0,
        "Total Shots": 0,
        "Past 5 Shots": [],
        "Past 15 Shots": [],
    }


def test_record_distances_overflow_behavior():
    """Test that Past 5 and Past 15 lists maintain correct rolling behavior."""

    delete_all_golf_data()
    summary = load_or_initialize_summary()

    # Add 20 shots (more than 15) to test rolling window
    data = list(range(20))  # [0, 1, 2, ..., 19]
    result = record_distances(summary, "5i", data, True)

    # The average should include all shots
    assert result["Total Shots"] == 20
    assert result["Average Distance"] == round(sum(data) / 20, 2)

    # Past 5 should have the last 5 shots
    assert result["Past 5 Shots"] == [15, 16, 17, 18, 19]

    # Past 15 should have the last 15 shots
    assert result["Past 15 Shots"] == list(range(5, 20))


def test_remove_distances_behavior():
    """Test removal of specific shot distances from a list."""

    # Typical case:
    current = [100, 150, 200, 150, 100]
    delete = [150, 100]
    result = remove_distances(current, delete)
    assert result == [200, 150, 100]

    # Edge case: removing more than available
    result = remove_distances([100, 200], [100, 100, 200])
    assert result == []

    # Edge case: removing from empty list
    result = remove_distances([], [50])
    assert result == []