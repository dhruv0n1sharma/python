#Write a program to store and display student details.

a = input("enter the name of the student: ")
b = input("enter  roll no :")
c = input("enter the course of the student:")

print("name is ",a)
print("roll no is ",b)
print("course is ",c)

#============================================================================


#Write a program to swap two numbers.

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

#==========================================================

#Identify the data type of user input.

a = input("enter any thing")
y= type(a)
print ("value is ",a)
print ("datatype is ",y)


#======================================================================================

# even or odd

x = int(input("Enter a number: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
    


#greatese number


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x >= z:
    print(x, "is greater than", y, "and", z)
elif y >= x and y >= z:
    print(y, "is greater than", x, "and", z)
else:
    print(z, "is greater than", x, "and", y)


#========================================================================
#Write a program to calculate simple interest.

a = float(input("enter the principal :"))
b = float(input("enter the rate :"))
c = float(input("enter the time:") )     

si =(a*b*c)/100

print("Simple Interest is:", si)

#===================================================================================

#Accept username and password and display them securely.


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
    

#=============================================================================

#Write a program to take two numbers and display their sum.

a = int(input("enter the value of a :"))
b  = int(input("enter the value of b :"))
c = a+b
print("the sum of ",a,"and",b, "is",c)


#=======================================================================================

#Check whether a number is positive, negative, or zero.

a = int(input("enter the number"))
if a>0:
    print(a,"number is positive")
elif a<0:
    print(a,"number is negative ")  
else:
     print(a,"number is zero")  
#===========================================================================
#constructor


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
 # =====================================================================
# file handling
with open("abc.text", "rb") as file:
    for line in file:
     print(line)
 # =====================================================================
.# CHECK LEAP YEAR

print("--- 1. Leap Year Checker ---")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.\n")
else:
    print(f"{year} is not a leap year.\n")


# =====================================================================
#  DISPLAY GRADES USING IF-ELIF-ELSE

print("--- 2. Grade Display ---")
score = float(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A\n")
elif score >= 80:
    print("Grade: B\n")
elif score >= 70:
    print("Grade: C\n")
elif score >= 60:
    print("Grade: D\n")
else:
    print("Grade: F\n")


# =====================================================================
#  PRINT NUMBERS FROM 1 TO 10

print("--- 3. Numbers from 1 to 10 ---")
for i in range(1, 11):
    print(i)
print() # Khali line spacing ke liye


# =====================================================================
# . PRINT EVEN NUMBERS BETWEEN 1 AND 50

print("--- 4. Even Numbers Between 1 and 50 ---")
for i in range(2, 51, 2):
    print(i, end=" ") # end=" " se saare numbers ek hi line me print honge
print("\n")


# =====================================================================
# . PRINT MULTIPLICATION TABLE

print("--- 5. Multiplication Table ---")
num = int(input("Enter a number for its table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()


# =====================================================================
#  COUNT DIGITS OF A NUMBER

print("--- 6. Count Digits ---")
digit_num = int(input("Enter a number to count its digits: "))
digit_count = len(str(abs(digit_num))) 
print(f"The number of digits is: {digit_count}\n")


# =====================================================================
#  FUNCTION TO FIND FACTORIAL

print("--- 7. Factorial Function ---")
def find_factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial


print("Factorial of 5 is:", find_factorial(5))
print()


# =====================================================================
#  FUNCTION TO CHECK PRIME NUMBER

print("--- 8. Prime Number Checker ---")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

check_prime = 17
if is_prime(check_prime):
    print(f"{check_prime} is a prime number.\n")
else:
    print(f"{check_prime} is not a prime number.\n")


# =====================================================================
#  FUNCTION TO REVERSE A STRING

print("--- 9. Reverse a String ---")
def reverse_string(text):
    return text[::-1]

mystr = "Python"
print(f"Original: {mystr}")
print(f"Reversed: {reverse_string(mystr)}\n")
