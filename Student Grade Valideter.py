# ==========================================
# Practical Lab 2 - Student Grade Validator
# Course: Advanced Programming
# Topic: Exception Handling
# ==========================================

# Custom Exception
class InvalidGradeError(Exception):
    """Raised when the grade is outside the valid range (0-100)."""
    pass


def validate_grade(value):
    """
    Validates the student's grade.
    Converts input to a numeric value safely.
    Accepts only grades between 0 and 100.
    """

    try:
        grade = float(value)
    except ValueError:
        raise ValueError("Grade must be a numeric value.")

    if grade < 0:
        raise InvalidGradeError("Grade cannot be negative.")

    if grade > 100:
        raise InvalidGradeError("Grade cannot be greater than 100.")

    return grade


def display_result(grade):
    """Displays the validated grade."""
    print(f"\nValid Grade: {grade}")

    if grade >= 90:
        print("Letter Grade: A")
    elif grade >= 80:
        print("Letter Grade: B")
    elif grade >= 70:
        print("Letter Grade: C")
    elif grade >= 60:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")


def main():
    print("=" * 45)
    print("      STUDENT GRADE VALIDATOR")
    print("=" * 45)

    while True:

        user_input = input("\nEnter student's grade (0-100): ")

        try:
            grade = validate_grade(user_input)
            display_result(grade)

        except ValueError as e:
            print("\nError:", e)

        except InvalidGradeError as e:
            print("\nError:", e)

        except Exception as e:
            print("\nUnexpected Error:", e)

        choice = input("\nDo you want to validate another grade? (Y/N): ").strip().lower()

        if choice != "y":
            print("\nThank you for using Student Grade Validator!")
            break


# Program starts here
if __name__ == "__main__":
    main()