# Task 2: Lists and Arrays
import numpy as np

# Creating a list of 10 numbers
numbers = [12, 45, 7, 89, 23, 56, 9, 34, 67, 11]

print("\n--- List Operations ---")
print(f"List Length: {len(numbers)}")
print(f"Maximum Value: {max(numbers)}")
print(f"Minimum Value: {min(numbers)}")

# Add an element
numbers.append(100)
# Remove an element
numbers.remove(7)

print(f"Updated List: {numbers}")

# Sorting
asc = sorted(numbers)
desc = sorted(numbers, reverse=True)

print(f"Ascending Order: {asc}")
print(f"Descending Order: {desc}")

# Convert to NumPy array
arr = np.array(numbers)

print("\n--- NumPy Calculations ---")
print(f"Mean: {np.mean(arr)}")
print(f"Median: {np.median(arr)}")
print(f"Standard Deviation: {np.std(arr)}")
