student_name = input("enter student name")
student_score = int(input("enter student score"))
if student_score >= 70 and student_score <= 100 :
    print("excellent")
    print("excellent")
    if student_score >= 90 and student_score <= 100 :
        print("offered foreign scholarship")
    elif student_score >= 80 and student_score <= 89 :
        print("offered local acholarship")
    elif student_score >= 70 and student_score <= 90 :
        print("no offer, just pass")
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
    if student_score >= 25 and student_score <= 39 :
        print("pardoned")
    elif student_score >= 0 and student_score <= 24 :
        print("retake")
else : 
    print("enter student score")  