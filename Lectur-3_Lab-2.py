import csv

# Create CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["student_id", "name", "midterm", "final"])

    writer.writerow([101, "Ahmad Khan", 70, 80])
    writer.writerow([102, "Ali, Ahmad", 60, 75])
    writer.writerow([103, "Karim", 40, 50])
    writer.writerow([104, "Hamid Noor", 85, 90])
    writer.writerow([105, "Omar", 55, 65])


# Read CSV file
students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        midterm = int(row["midterm"])
        final = int(row["final"])

        total = midterm + final
        average = total / 2

        row["total"] = total
        row["average"] = average

        students.append(row)


# Display students who passed
print("Passed Students:")

for student in students:
    if student["average"] >= 60:
        print(student["name"], student["average"])


# Write results to new CSV file
with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(
        ["student_id", "name", "midterm", "final", "total", "average"]
    )

    for student in students:
        writer.writerow([
            student["student_id"],
            student["name"],
            student["midterm"],
            student["final"],
            student["total"],
            student["average"]
        ])