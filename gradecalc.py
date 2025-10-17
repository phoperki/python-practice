def calculate_average(scores):
    # Take a list of scores
    # Return the average (mean) as a float
    sum = 0
    for score in scores:
        sum = score + sum

    average=sum / len(scores) 
    return average


def get_letter_grade(score):
    # Convert numeric score to letter grade
    # 90+ = A, 80-89 = B, 70-79 = C, 60-69 = D, below 60 = F

    if score >= 90:
        grade="A"
    elif score >= 80:
        grade="B"
    elif score >= 70:
        grade="C"
    elif score >= 60:
        grade="D"
    else:
        grade="F"
    return grade

def analyze_class(student_scores):
    # Takes a dictionary: {"Alice": 95, "Bob": 78, "Carol": 88}
    # Returns a dictionary with:
    #   - "average": class average
    #   - "highest": name of student with highest score
    #   - "lowest": name of student with lowest score
    #   - "passing": list of names with scores >= 60

    class_stats={"average":0, "highest":0, "lowest":0, "passing":0}
    class_stats["average"]=calculate_average(student_scores.values())

    highest_score=max(student_scores.values())
    for name, score in student_scores.items():
        if score==highest_score:
            class_stats["highest"]=name

    lowest_score=min(student_scores.values())
    for name, score in student_scores.items():
        if score==lowest_score:
            class_stats["lowest"]=name
            break # Stop looking after found

    passing=[]
    for name, score in student_scores.items():
        if score >= 60:
            passing.append(name)
            break # stop looking after found

    class_stats["passing"]=passing
    return class_stats

# Test cases
print(calculate_average([85, 90, 78, 92, 88]))
# Should print: 86.6

print(get_letter_grade(95))   # A
print(get_letter_grade(85))   # B
print(get_letter_grade(75))   # C
print(get_letter_grade(65))   # D
print(get_letter_grade(55))   # F

grades = {
    "Alice": 95,
    "Bob": 78,
    "Carol": 88,
    "David": 65,
    "Eve": 92
}

result = analyze_class(grades)
print(result)
# Should print something like:
# {
#   "average": 83.6,
#   "highest": "Alice",
#   "lowest": "David",
#   "passing": ["Alice", "Bob", "Carol", "David", "Eve"]
# }