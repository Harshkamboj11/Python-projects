student_name = input("enter the student's name: ")


score1 = float(input("enter the marks in first subject: "))
score2 = float(input("enter the marks in second subject: "))
score3 = float(input("enter the marks in third subject: "))

average_score = int(score1 + score2 + score3)/3

if average_score >= 90:
    grade =  'A'
elif 80<= average_score <90:
    grade = 'B'
elif 70<= average_score <80:
    grade = 'C'
elif 60<= average_score <70:
    grade = 'D'
elif average_score <60:
    grade = 'F'

print()
print()
print("the name of the student is ",student_name)
print("the average score of the student is ",average_score)
print("the grade of the student is ",grade)