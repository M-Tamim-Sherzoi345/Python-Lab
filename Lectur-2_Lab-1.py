# Student scores
scores = [75, 60, 85, 45, 90, 60, 55, 80, 70, 95]

# Minimum, Maximum and Average
print("Minimum:", min(scores))
print("Maximum:", max(scores))
print("Average:", sum(scores) / len(scores))


# Scores greater than or equal to 60
passed = [score for score in scores if score >= 60]
print("Passed scores:", passed)


# Convert list to set
score_set = set(scores)
print("Set:", score_set)


# Student IDs and Names
students = {
    101: "Ahmad",
    102: "Ali",
    103: "Karim",
    104: "Omid",
    105: "Hamid"
}

# Search student by ID
student_id = 103

if student_id in students:
    print("Student:", students[student_id])
else:
    print("Student not found")


# Student records
names = ["Ahmad", "Ali", "Karim", "Omid", "Hamid"]
marks = [75, 60, 85, 90, 55]

records = list(zip(names, marks))

# Sort by score
records.sort(key=lambda x: x[1])

print("Sorted records:")
for name, score in records:
    print(name, score)


# enumerate()
print("Student list:")
for i, name in enumerate(names, 1):
    print(i, name)