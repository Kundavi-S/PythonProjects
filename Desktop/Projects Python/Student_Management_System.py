n = int(input("Enter the number of students: "))
students = {}
student = 1
while student <= n:
    print("Student number:", student)
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    subject = 1
    total = 0
    marks_list = []
    while subject <= 5:
        marks = int(input("Enter marks for Subject " + str(subject) + ": "))
        marks_list.append(marks)
        total += marks
        subject += 1
    percentage = total / 5
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 50:
        grade = "E"
    else:
        grade = "F"
    if percentage >= 50:
        result = "PASS"
    else:
        result = "FAIL"
    students[rollno] = {"name": name, "marks": marks_list, "total": total, "percentage": percentage, "grade": grade, "result": result}
    student += 1
print("===================================")
print("Report Card")
print("===================================")
roll = input("Enter the Roll Number: ")
if roll in students:
    print("Name:", students[roll]["name"])
    print("Roll Number:", roll)
    print("SUBJECT WISE MARKS")
    subject = 1
    while subject <= 5:
        print("Subject", subject, ":", students[roll]["marks"][subject - 1])
        subject += 1
    print("Total Marks:", students[roll]["total"])
    print("Percentage:", students[roll]["percentage"], "%")
    print("Grade:", students[roll]["grade"])
    print("Result:", students[roll]["result"])
else:
    print("Student not found.")
print("===================================")
print("SUBJECT WISE ANALYTICS")
print("===================================")
subject = 1
while subject <= 5:
    total_marks = 0
    for roll in students:
        total_marks += students[roll]["marks"][subject - 1]
    average = total_marks / n
    print("Subject", subject, "Average:", average)
    subject += 1



