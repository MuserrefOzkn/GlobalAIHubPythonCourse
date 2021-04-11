
#Question 1
students = []
midterm_grades = []
project_grades = []
final_grades = []
passing_grades = []

for i in range(5):
  student = input("Please enter a name: ")
  students.append(student)

  midterm_grade = int(input("Midterm grade: "))

  while True:
    if midterm_grade < 0 or 100 < midterm_grade:
      midterm_grade = int(input("Midterm grade: "))
    else:
      break

  midterm_grades.append(midterm_grade)

  project_grade = int(input("Project grade: "))

  while True:
    if project_grade < 0 or 100 < project_grade:
      project_grade = int(input("Project grade: "))
    else:
      break

  project_grades.append(project_grade)
      
  final_grade = int(input("Final grade: "))

  while True:
    if final_grade < 0 or 100 < final_grade:
      final_grade = int(input("Final grade: "))
    else:
      break
  
  final_grades.append(final_grade)

  passing_grade = (midterm_grade*0.3) + (project_grade*0.3) + (final_grade*0.4)

  passing_grades.append(passing_grade)



students = {"Name: " : students,
            "Midterm: " : midterm_grades,
            "Project: " : project_grades,
            "Final: " : final_grades,
            "Passing: " : passing_grades
}

print(students)
passing_grades.reverse()
print(passing_grades)
