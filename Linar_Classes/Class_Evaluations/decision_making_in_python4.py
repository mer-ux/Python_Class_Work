student_name = input("enter student name")
student_score = int(input("enter student score"))
if student_score >= 70 and student_score <= 100 :
    print("excellent")
    print("excellent")
elif student_score >= 60 and student_score <= 69 :
    print("very good")
    print("very good")
elif student_score >= 50 and student_score <= 59 :
    print("good")
    print("good")
elif student_score >= 40 and student_score <= 49 :
    print("poor")
    print("poor")
elif student_score >= 0 and student_score <= 39 :
    print("fail")
    print("fail")
else :
    print("enter student score")