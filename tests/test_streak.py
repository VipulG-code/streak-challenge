# tests/test_streak.py
import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks_longest_in_middle():
    """Test that the longest of multiple streaks is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive_numbers():
    """Test a list containing only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_zeros_and_negatives():
    """Test that zeros and negative numbers correctly break streaks."""
    assert longest_positive_streak([1, 2, 0, 3, -5, 4, 5, 6]) == 3

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_streak_at_the_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 0, 2, 3, 4, 5]) == 4
