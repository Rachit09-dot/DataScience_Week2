# Task 4: File Handling
# Creating and writing to file
with open("student_data.txt", "w") as file:
    file.write("Ravi, Data Science, 78\n")
    file.write("Meera, AI, 84\n")
    file.write("Karan, Python, 65\n")
    file.write("Anita, ML, 92\n")
    file.write("Suresh, Data Analytics, 88\n")

# Reading file and printing students with marks > 75
print("\n--- Students with Marks > 75 ---")
with open("student_data.txt", "r") as file:
    for line in file:
        name, course, marks = line.strip().split(", ")
        marks = int(marks)

        if marks > 75:
            print(f"{name} - {course} - {marks}")