#If else statement!...
"""
num=int(input("Enter number: "))
if(num%2==0):
    print(num,"is Even")
else:
    print(num,"is odd")

username=input("Enter username: ")
password=int(input("Enter Password: "))

if(username=="admin" and password==1234):
    print("Welcome,Login Successfully")
else:
    print("Please enter valid password")
"""
marks=int(input("Enter student marks: "))
if(marks<0 and marks>100):
    print("Invalid")
elif(marks>80):
    print("first class")
elif(marks>50):
    print("Second Class")
elif(marks>35):
    print("Pass")
else:
    print("Fail")