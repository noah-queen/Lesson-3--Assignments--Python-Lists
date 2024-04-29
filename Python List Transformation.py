#Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
print(grades)

#task 2

amount_of_grades = len(grades)
sum_of_grades = sum(grades)
print(sum_of_grades / amount_of_grades)

#task 3

updated_grades = ['Failed' if grade < 80 else grade for grade in grades]
print("Updated grades:", updated_grades)
