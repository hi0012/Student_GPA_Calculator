"""Student GPA Calculator.

Calculates a credit-weighted GPA on the standard 4.0 scale from letter grades.
"""

GRADE_POINTS = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "D-": 0.7,
    "F": 0.0,
}


def grade_to_points(grade):
    """Convert a letter grade (e.g. 'B+') to grade points."""
    key = grade.strip().upper()
    if key not in GRADE_POINTS:
        raise ValueError(f"Invalid grade: {grade!r}")
    return GRADE_POINTS[key]


def calculate_gpa(courses):
    """Return the credit-weighted GPA for a list of (grade, credits) pairs.

    A plain list of letter grades is also accepted; each course then counts
    as equal weight (1 credit).
    """
    total_points = 0.0
    total_credits = 0.0
    for course in courses:
        if isinstance(course, str):
            grade, credits = course, 1
        else:
            grade, credits = course
        if credits <= 0:
            raise ValueError("Credits must be greater than 0.")
        total_points += grade_to_points(grade) * credits
        total_credits += credits
    if total_credits == 0:
        return 0.0
    return round(total_points / total_credits, 2)


def prompt_courses():
    """Ask the user for each course's grade and credit hours."""
    courses = []
    print("Enter each course's letter grade and credit hours.")
    print("Press Enter on an empty grade when you're done.\n")
    while True:
        grade = input(f"Course {len(courses) + 1} grade (e.g. A, B+, C-): ").strip()
        if not grade:
            break
        try:
            grade_to_points(grade)
        except ValueError as err:
            print(f"  {err}. Try again.")
            continue
        try:
            credits = float(input("  Credit hours: "))
            if credits <= 0:
                raise ValueError
        except ValueError:
            print("  Credit hours must be a positive number. Try again.")
            continue
        courses.append((grade, credits))
    return courses


def main():
    courses = prompt_courses()
    if not courses:
        print("No courses entered.")
        return
    total_credits = sum(c for _, c in courses)
    print(f"\nCourses: {len(courses)} | Credits: {total_credits:g}")
    print(f"GPA: {calculate_gpa(courses):.2f}")


if __name__ == "__main__":
    main()
