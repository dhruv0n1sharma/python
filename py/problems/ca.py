#Write a program to store and display student details.
'''
a = input("enter the name of the student: ")
b = input("enter  roll no :")
c = input("enter the course of the student:")

print("name is ",a)
print("roll no is ",b)
print("course is ",c)
'''
#============================================================================


#Write a program to swap two numbers.
'''
a = input("enter number:")
b = input("enter number:")

print ("before swapping")

print("value of a is :",a)
print("value of b is :",b)

print ("after  swapping")

temp= a
a =b
b=temp

print("value of a is :",a)
print("value of b is :",b)
'''
#==========================================================

#Identify the data type of user input.
'''
a = input("enter any thing")
y= type(a)
print ("value is ",a)
print ("datatype is ",y)
'''

#======================================================================================

# even or odd
'''
x = int(input("Enter a number: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
    '''


#greatese number

'''
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x >= z:
    print(x, "is greater than", y, "and", z)
elif y >= x and y >= z:
    print(y, "is greater than", x, "and", z)
else:
    print(z, "is greater than", x, "and", y)
'''

#========================================================================
#Write a program to calculate simple interest.
'''
a = float(input("enter the principal :"))
b = float(input("enter the rate :"))
c = float(input("enter the time:") )     

si =(a*b*c)/100

print("Simple Interest is:", si)
'''
#===================================================================================

#Accept username and password and display them securely.

'''
print ("create user id and passward")

u1 = input("create user id :")
p1 = input("create user pass : ")
print("login ")
u2 = input("login user id :")
p2 = input("login user pass : ")


if u1 == u2 and p1 == p2:
    print("log in successfull")
else:
    print("wrong user id and pass")    
    '''

#=============================================================================

#Write a program to take two numbers and display their sum.
'''
a = int(input("enter the value of a :"))
b  = int(input("enter the value of b :"))
c = a+b
print("the sum of ",a,"and",b, "is",c)
'''

#=======================================================================================

#Check whether a number is positive, negative, or zero.
'''
a = int(input("enter the number"))
if a>0:
    print(a,"number is positive")
elif a<0:
    print(a,"number is negative ")  
else:
     print(a,"number is zero")  
'''
'''
class employee:
    def input_data(self,name, id , city , department) :  
     self.name =input("enter the name ")
     self.id =input("enter the id ",) 
     self.city = input("enter the city",)
     self.department =input("enter the depart ment name ")
    def display (self):
        print(self.name,self.id,self.city,self.department)
s1= employee()
s1.input_data()
s1.display()   '''

'''
class  car :
    def __init__(self , name , model , colour , ):
        self.name= name
        self.model= model
        self.colour= colour

    def display(self):
        print(self.name, self.model,self.colour)


    def s(self):
        print("car name",name)
        print("car nmodel",model)
        print("car colour",colour)

s1 =car("abc",2026,"white")
s1.display()  


name = input("enter the name of car:")
model = input("enter the modelof car:")
colour = input("enter the colour of car:")

s2= car(name, model ,colour)
s2.s()

'''
with open("abc.text", "rb") as file:
    for line in file:
     print(line)