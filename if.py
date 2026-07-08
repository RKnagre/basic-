"""
a=b=c=30
print(a)
print(b)
print(c)

a,b,c=10,20.5,"hello"
print(a)
print(b)
print(c)

#If statement programs
num=int(input("Enter number: "))
if(num%2==0 and num>0):
    print(num,"positive")
    print("even")
elif(num<0):
    print(num,"is negative")
else:
    #print("Zero")
    print("odd")

username=input("Enter username: ")
password=int(input("Enter password: "))
if(username=="Atul" and password==7480):
    print("Welcome, Login Successfully!...")
else:
    print("Please enter valid credentials")
"""
marks=int(input("Enter student marks: "))
if(marks>100):
    print("Invalid Input")
elif(marks>=90):
    print("Distinction")
elif(marks>=75):
    print("Second Class")
elif(marks>=50):
    print("Pass")
elif(marks>=0):
    print("fail")
else:
    print("invalid marks")