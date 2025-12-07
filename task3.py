# Task 3: Dictionaries and Sets

# Dictionary creation
student = {
    "name": "John",
    "age": 20,
    "course": "Data Science",
    "marks": 82
}

print("\n--- Dictionary Values ---")
for key, value in student.items():
    print(f"{key} : {value}")

# Adding new key
student["grade"] = "A"
print("\nUpdated Dictionary:", student)

# Set of unique courses
courses = {"Python", "Data Science", "AI", "Python"}  # Python will appear only once
print("\nUnique Course Set:", courses)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\n--- Set Operations ---")
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))