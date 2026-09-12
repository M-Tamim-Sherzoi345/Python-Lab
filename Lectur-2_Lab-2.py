from typing import Dict, Set

# Student data
students: Dict[int, Dict[str, object]] = {
    101: {"name": "Ahmad", "courses": {"CS101", "DBMS"}},
    102: {"name": "Ali", "courses": {"DBMS", "Python"}}
}

# Add course
students[101]["courses"].add("Python")

# Drop course
students[101]["courses"].discard("DBMS")

# Print student courses
print("Ahmad courses:", students[101]["courses"])

# Common courses
common = students[101]["courses"] & students[102]["courses"]
print("Common courses:", common)

# All unique courses
all_courses = students[101]["courses"] | students[102]["courses"]
print("All courses:", all_courses)