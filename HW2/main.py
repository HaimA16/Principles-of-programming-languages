from functools import reduce
from itertools import groupby


def students_with_high_grades(grades):
    # Step 1: Filter grades above 90
    high_grades = list(filter(lambda x: x[2] >= 90, grades))
    print("High grades (above 90):", high_grades)

    # Step 2: Map to (student_name, 1)
    student_scores = map(lambda x: (x[0], 1), high_grades)

    # Step 3: Reduce to count scores per student
    score_counts = {}
    for student, count in student_scores:
        score_counts[student] = score_counts.get(student, 0) + count
    # Step 4: Filter students with at least 3 high scores
    result = list(filter(lambda x: x[1] >= 3, score_counts.items()))

    return [student for student, _ in result]


# Example Data
grades = [("Alice", "Math", 95), ("Alice", "Science", 92), ("Alice", "History", 98),
          ("Bob", "Math", 93), ("Bob", "Science", 91), ("Bob", "History", 90),
          ("Charlie", "Math", 89)]

# Call Function
print(students_with_high_grades(grades))


def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def square_of_primes(numbers):
    primes = filter(is_prime, numbers)
    squared_primes = map(lambda x: x ** 2, primes)
    return list(squared_primes)


# Example
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
print(square_of_primes(numbers))  # Output: [4, 9, 25, 49]
def most_expensive_per_category(products):
    # Sort products by category
    products = sorted(products, key=lambda x: x[1])

    # Group by category
    grouped = groupby(products, key=lambda x: x[1])

    # Find the most expensive product in each category
    result = map(lambda x: max(x[1], key=lambda y: y[2]), grouped)
    return [(product[0], product[2]) for product in result]


# Example
products = [("Laptop", "electronics", 1200), ("Table", "furniture", 300),
            ("Chair", "furniture", 150), ("Phone", "electronics", 700),
            ("Pen", "stationery", 5)]
print(most_expensive_per_category(products))
# Output: [('Laptop', 1200), ('Table', 300), ('Pen', 5)]


def product_of_divisibles(numbers):
    # Filter numbers divisible by 5 or 3
    divisibles = filter(lambda x: x % 5 == 0 or x % 3 == 0, numbers)

    # Reduce to find the product
    result = reduce(lambda x, y: x * y, divisibles, 1)
    return result


# Example
numbers = [1, 2, 3, 4, 5, 6, 10, 15]
print(product_of_divisibles(numbers))  # Output: 1350

import re

def long_words(text):
    # Remove punctuation and split into words
    words = re.sub(r'[^\w\s]', '', text).split()

    # Filter words longer than 7 characters
    long_words = filter(lambda x: len(x) > 7, words)
    return list(long_words)


# Example
text = "Python, programming: is fun! Enjoy coding."
print(long_words(text))  # Output: ['programming']
