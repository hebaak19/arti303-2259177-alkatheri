"""this module contains functions for working with letter grades and GPAs."""


def letter_grade(gpa):
    """Return the letter grade for a GPA (out of 5.00)."""
    # TODO: your if/elif chain here
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
