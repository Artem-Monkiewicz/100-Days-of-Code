criteria = ("""
          This is the scoring criteria: 
- Scores 91 - 100: Grade = "Outstanding" 
- Scores 81 - 90: Grade = "Exceeds Expectations" 
- Scores 71 - 80: Grade = "Acceptable" 
- Scores 70 or lower: Grade = "Fail" 
         """)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# student_grades = 

# for student in student_scores:
#     print(student) # print the name of the student
#     print(student_scores[student]) # print the score of the student

# Evaluation program

# def grade_student():
#     for scories in student_scores:
#         if student_scores[scories] >= 91 and student_scores[scories] <= 100:
#             print(f"{scories} has a score of {student_scores[scories]}: Outstanding")
#         elif student_scores[scories] >= 81 and student_scores[scories] <= 90:
#             print(f"{scories} has a score of {student_scores[scories]}: Exceeds Expectations")
#         elif student_scores[scories] >= 71 and student_scores[scories] <= 80:
#             print(f"{scories} has a score of {student_scores[scories]}: Acceptable")
#         elif student_scores[scories] <= 70:
#             print(f"{scories} has a score of {student_scores[scories]}: Fail")

# grade_student()

# WRONG
# for student in student_scores:
#     score = student_scores[student]
#     if score >= 91 and score <= 100:
#         score = "Outstanding"
#     elif score >= 81 and score <= 90:
#         score = "Exceeds Expectations"
#     elif score >= 71 and score <= 80:
#         score = "Acceptable"
#     elif score <= 70:
#         score = "Fail"
#     print(student_scores)

# CORRECT
student_grades = {}

for student, score in student_scores.items():
    if score >= 91 and score <= 100:
        grade = "Outstanding"
    elif score >= 81 and score <= 90:
        grade = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        grade = "Acceptable"
    elif score <= 70:
        grade = "Fail"

    student_grades[student] = grade

print(student_grades)