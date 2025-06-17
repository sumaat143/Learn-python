# Step 1: Student dictionary
students = {
    "Sumant": 88,
    "Aryan": 76,
    "Nikhil": 91
}

# Step 2: Find topper (max marks)
topper = max(students, key=students.get)
print("Topper is:", topper)

# Step 3: Calculate average
total_marks = sum(students.values())
average = total_marks / len(students)
print("Average marks:", average)