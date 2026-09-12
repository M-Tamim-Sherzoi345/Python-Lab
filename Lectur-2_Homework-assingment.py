from typing import Dict, Set, TypeVar

T = TypeVar("T")


# Generic function
def add_item(items: Set[T], item: T) -> None:
    items.add(item)


# Students
students: Dict[int, dict] = {}


# Add student
def add_student(student_id: int, name: str) -> None:
    students[student_id] = {
        "name": name,
        "courses": set()
    }


# Register course
def register_course(student_id: int, course: str) -> None:
    if student_id in students:
        students[student_id]["courses"].add(course)


# Drop course
def drop_course(student_id: int, course: str) -> None:
    if student_id in students:
        students[student_id]["courses"].discard(course)


# Search student
def search_student(student_id: int) -> None:
    if student_id in students:
        print(students[student_id])
    else:
        print("Student not found")


# Add students
add_student(101, "Ahmad")
add_student(102, "Ali")
add_student(103, "Karim")

# Register courses
register_course(101, "Python")
register_course(101, "DBMS")

register_course(102, "Python")
register_course(102, "Java")

register_course(103, "DBMS")

# Drop a course
drop_course(101, "DBMS")


# Display all unique courses
all_courses = set()

for student in students.values():
    all_courses = all_courses | student["courses"]

print("All courses:", all_courses)


# Students sharing Python
python_students = [
    student["name"]
    for student in students.values()
    if "Python" in student["courses"]
]

print("Python students:", python_students)


# Sort students by name
sorted_students = sorted(
    students.values(),
    key=lambda student: student["name"]
)

print("Students:")
for student in sorted_students:
    print(student["name"], student["courses"])


# Search
print("\nSearch result:")
search_student(102)