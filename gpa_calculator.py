def calculate_gpa(grades):
    total_points = 0
    for grade in grades:
        if grade.upper() == "A":
            total_points += 4.0
        elif grade.upper() == "B":
            total_points += 3.0
        elif grade.upper() == "C":
            total_points += 2.0
        elif grade.upper() ==
