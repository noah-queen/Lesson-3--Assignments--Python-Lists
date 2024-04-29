#task 1
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
week_2_temps = temperatures[7:14]
print(week_2_temps)

#task 2 
temperatures_over_100 = [temp for temp in temperatures if temp > 100]
print(temperatures_over_100)

#task 3
reversed_temps = temperatures[::-1]
day_5_to_10 = reversed_temps[4:10]
print(day_5_to_10)