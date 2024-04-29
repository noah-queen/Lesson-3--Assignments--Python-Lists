#task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both_submitted_and_attended = [student for student in submitted if student in attended]

print("Students who both submitted their assignments and attended the class:", both_submitted_and_attended)

#task 2

print("the lists are not the same") if sorted(submitted) != sorted(attended) else print("the lists are the same")


#task 3
attended_copy = attended[:]
for student in attended_copy:
    if student not in submitted:
        attended.remove(student)

print("Updated attended list:", attended)
