# ==========================================
# Practical Lab 1 - Safe Calculator
# Course: Advanced Programming
# Topic: Exception Handling
# ==========================================

# Custom Exception
class InvalidOperationError(Exception):
    """Raised when an unsupported operator is entered."""
    pass


def calculate(num1, num2, operator):
    """Performs the requested calculation."""

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2

    else:
        raise InvalidOperationError(
            "Invalid operator! Please use +, -, *, or /."
        )


def main():
    print("=" * 40)
    print("        SAFE CALCULATOR")
    print("=" * 40)

    while True:

        try:
            # Get numeric input
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Get operator
            operator = input("Enter operation (+, -, *, /): ").strip()

            # Perform calculation
            result = calculate(num1, num2, operator)

            print(f"\nResult: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("\nError: Please enter valid numeric values.")

        except ZeroDivisionError as e:
            print("\nError:", e)

        except InvalidOperationError as e:
            print("\nError:", e)

        except Exception as e:
            print("\nUnexpected Error:", e)

        finally:
            print("\nCalculation attempt completed.")
            print("-" * 40)

        # Retry option
        choice = input("Do you want to perform another calculation? (Y/N): ").strip().lower()

        if choice != "y":
            print("\nThank you for using Safe Calculator!")
            break


# Program starts here
if __name__ == "__main__":
    main()