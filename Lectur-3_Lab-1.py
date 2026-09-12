import os

file_name = "students.txt"

# Create file and write 5 students
if not os.path.exists(file_name):
    with open(file_name, "w") as file:
        file.write("101, Ahmad\n")
        file.write("102, Ali\n")
        file.write("103, Karim\n")
        file.write("104, Hamid\n")
        file.write("105, Omar\n")

# Read and display all students
try:
    with open(file_name, "r") as file:
        records = file.readlines()

    print("All Students:")
    for record in records:
        print(record.strip())

    # Search student by ID
    search_id = input("\nEnter Student ID: ")

    found = False
    for record in records:
        if record.startswith(search_id + ","):
            print("Student found:", record.strip())
            found = True

    if not found:
        print("Student not found")

    # Append a new student
    with open(file_name, "a") as file:
        file.write("106, Hassan\n")

    # Count total records
    with open(file_name, "r") as file:
        total = len(file.readlines())

    print("Total records:", total)

except FileNotFoundError:
    print("File does not exist")