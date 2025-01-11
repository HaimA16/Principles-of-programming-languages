from functools import reduce


def students_with_high_grades(grades):
    # Step 1: Filter grades above 90
    high_grades = list(filter(lambda x: x[2] > 90, grades))
    print("High grades (above 90):", high_grades)

    # Step 2: Map to (student_name, 1)
    student_scores = map(lambda x: (x[0], 1), high_grades)

    # Step 3: Reduce to count scores per student
    score_counts = {}
    for student, count in student_scores:
        score_counts[student] = score_counts.get(student, 0) + count
    print("Score counts:", score_counts)

    # Step 4: Filter students with at least 3 high scores
    result = list(filter(lambda x: x[1] >= 3, score_counts.items()))
    print("Students with at least 3 high scores:", result)

    return [student for student, _ in result]


# Example Data
grades = [("Alice", "Math", 95), ("Alice", "Science", 92), ("Alice", "History", 88),
          ("Bob", "Math", 93), ("Bob", "Science", 91), ("Bob", "History", 90),
          ("Charlie", "Math", 89)]

# Call Function
print(students_with_high_grades(grades))
