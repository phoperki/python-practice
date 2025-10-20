import csv  # You'll need this built-in module

def read_grades(filename):
    # Read the CSV file
    # Return a list of dictionaries:
    # [
    #   {"name": "Alice", "math": "95", "science": "88", "english": "92"},
    #   {"name": "Bob", ...},
    #   ...
    # ]

    grades_list = []
    try:
        with open(filename, "r") as csvfile:
            grades_dict = csv.DictReader(csvfile)
            for i in grades_dict:
                grades_list.append(i)
    except FileNotFoundError:
        print(f"{filename} does not exist.")

    return grades_list

def calculate_student_average(student):
    # Take one student dict
    math = int(student["math"])
    science = int(student["science"])
    english = int(student["english"])
    # Calculate their average across all subjects
    avg = (math + science + english) / 3
    # Return the average as a float
    return avg


def find_top_student(filename):
    # Find student with highest overall average
    # Return their name and average
    students = read_grades(filename)
    
    for student in students:
        avg = calculate_student_average(student)
        student["avg"] = avg
    
    # Returns "avg" index of first dictionary  list[index][dictionary index]
    top_avg = students[0]["avg"]
    top_name = students[0]["name"]

    for student in students:
        if student["avg"] > top_avg:
            top_avg = student["avg"]
            top_name = student["name"]
    
    return top_name, top_avg

def save_report(filename, students):
    # Write a new CSV with students and their averages
    # Columns: name, math, science, english, average
    with open(filename, 'w', newline="") as csvfile:
        fieldnames = students[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

# Test cases
students = read_grades("grades.csv")
print(students)
# Should print list of dicts

for student in students:
    avg = calculate_student_average(student)
    print(f"{student['name']}: {avg:.2f}")

top_name, top_avg = find_top_student("grades.csv")
print(f"Top student: {top_name} with {top_avg:.2f} average")

# Create report with averages
save_report("grade_report.csv", students)
# Check the new file!