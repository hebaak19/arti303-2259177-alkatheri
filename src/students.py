"""Student record utilities for ARTI 303."""


class Student:
    """A single student record."""

    def __init__(self, name, age, gpa, is_enrolled=True):
        if not (0.0 <= gpa <= 4.0):
            raise ValueError(f"GPA must be between 0.0 and 4.0, got {gpa}")
        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_enrolled = is_enrolled

    def is_dean_list(self):
        """Return True if this student's GPA qualifies for the Dean's list."""
        return self.gpa >= 3.5

    def report_line(self):
        """Return a one-line, human-readable summary of this student."""
        status = "made the Dean's list" if self.is_dean_list() else "did not make the Dean's list"
        enrollment = "is enrolled" if self.is_enrolled else "is not enrolled"
        return f"{self.name} (age {self.age}, GPA {self.gpa:.2f}) {enrollment} and {status}."
    
    def __repr__(self):
        # !r uses repr() on the name to ensure it's properly quoted
        return f"Student(name={self.name!r}, age={self.age}, gpa={self.gpa})"



def average_gpa(students):
    """Return the average GPA of a list of students."""
    if not students:
        # raise ValueError("The list of students is empty.")
        return 0.0
    total_gpa = sum(student.gpa for student in students)
    return total_gpa / len(students)


def dean_list_students(students):
    return [student for student in students if student.is_dean_list()]


def letter_grade(gpa):
    """Return the letter grade corresponding to a GPA."""
    if gpa >= 3.7:
        return 'A'
    elif gpa >= 2.7:
        return 'B'
    elif gpa >= 1.7:
        return 'C'
    elif gpa >= 1.0:
        return 'D'
    else:
        return 'F'


def oldest_student(students):
    """Return the oldest student from a list of students."""
    max_age=0
    oldest_student=None
    if not students:
        raise ValueError("The list of students is empty.")

    for student in students:
        if student.age > max_age:
            max_age = student.age
            oldest_student = student
    return oldest_student

    
def group_by_enrollment(students):
    """return two list as a tuple, one for enrolled students and one for not enrolled students."""
    enrolled = [student for student in students if student.is_enrolled]
    not_enrolled = [student for student in students if not student.is_enrolled]
    return (enrolled, not_enrolled)


def sort_students_by_gpa(students, reverse=False):
    """Return a new list of students sorted by GPA."""
    return sorted(students, key=lambda s: s.gpa, reverse=reverse)