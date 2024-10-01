student = {90: "Lukas",80: "Evan",95: "Arvid",75: "Nino",85: "Emilio"}

grades=student.keys()
print(grades)

sorted_student = sorted(student, reverse=True)
print(sorted_student)

sorted_student_new=sorted(student)
print(sorted_student_new)

best_student=max(student)
print(best_student)

best_student_name=student[best_student]



print(best_student_name)

