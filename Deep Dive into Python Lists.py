#task 1
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i in range(len(students)):
    if grades[i] >= 80:
        print(f"student: {students[i]}, has {grades[i]} and likes {activities[i]}")

#task 2
students_approved = []
for i in range(len(grades)):
    if grades[i] >= 80:
        students_approved.append(students[i])

#task 3
print(students_approved)