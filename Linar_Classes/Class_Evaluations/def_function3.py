# creating a code that accurately acknowledges a user'''
def time_category(time) :
    if time >= 1.00 and time <= 11.59 :
        return "morning"
    elif time >= 12.00 and time <= 16.59 :
        return "afternoon"
    elif time >= 17.00 and time <= 19.59 :
        return "evening"
    elif time >= 20.00 and time <= 24.59 :
        return ("night")
    else : 
        return "enter valid time"
#print(time_category(13))
def age_category(age) :
    if age >= 0 and age <= 18 :
        return "kid"
    elif age >= 19 and age <= 36 :
        return "dear"
    elif age >= 36 and age <= 80 :
        return "sir"
#print(age_category(23))
def greeting(name, time, age):
    print("Hello " + str(name))
    print("Good " + time_category(time)+ " " + age_category(age)+ "\n") 



#Calling the main function
greeting("Ade", 4.00, 34)
greeting("Perpetual", 10.27,56)

greeting("Mrs Nancy", 19,6)