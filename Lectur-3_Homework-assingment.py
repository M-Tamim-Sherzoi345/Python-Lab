import csv
from pathlib import Path
import shutil

file = Path("students.csv")
backup = Path("students_backup.csv")


# Read students
def read_students():
    students = []

    if not file.exists():
        return students

    try:
        with open(file, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
    except:
        print("File is corrupted.")

    return students


# Save students
def save_students(students):
    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "name", "department", "semester"]
        )
        writer.writeheader()
        writer.writerows(students)


# Add student
def add_student():
    student_id = input("Enter ID: ")

    if not student_id.isdigit():
        print("Invalid ID.")
        return

    students = read_students()

    for student in students:
        if student["id"] == student_id:
            print("ID already exists.")
            return

    name = input("Enter name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    if name == "" or department == "" or semester == "":
        print("All fields are required.")
        return

    students.append({
        "id": student_id,
        "name": name,
        "department": department,
        "semester": semester
    })

    save_students(students)
    print("Student added.")


# List students
def list_students():
    students = read_students()

    for s in students:
        print(s)


# Search student
def search_student():
    student_id = input("Enter ID: ")
    students = read_students()

    for student in students:
        if student["id"] == student_id:
            print(student)
            return

    print("Student not found.")


# Update student
def update_student():
    student_id = input("Enter ID: ")
    students = read_students()

    for student in students:
        if student["id"] == student_id:

            # Backup before changing
            if file.exists():
                shutil.copy(file, backup)

            student["name"] = input("New name: ")
            student["department"] = input("New department: ")
            student["semester"] = input("New semester: ")

            save_students(students)
            print("Student updated.")
            return

    print("Student not found.")


# Delete student
def delete_student():
    student_id = input("Enter ID: ")
    students = read_students()

    for student in students:
        if student["id"] == student_id:

            # Backup before deleting
            if file.exists():
                shutil.copy(file, backup)

            students.remove(student)
            save_students(students)

            print("Student deleted.")
            return

    print("Student not found.")


# Menu
while True:
    print("\n1. Add")
    print("2. List")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        list_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")