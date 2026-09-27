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


# =====================================================================
#  ATM Simulator

print("--- 21. ATM SIMULATION ---")
balance = 1000.0

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        print("Your balance is: Rs.", balance)
        
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid amount! Cannot deposit negative or zero.")
        else:
            balance = balance + amount
            print("Deposited successfully. Current balance:", balance)
            
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient balance! You don't have enough money.")
        else:
            balance = balance - amount
            print("Withdrawal successful. Remaining balance:", balance)
            
    elif choice == "4":
        print("Thank you for using our ATM!")
        break
    else:
        print("Invalid choice. Try again.")




# =====================================================================
#  Password Attempts
print("\n--- 22. PASSWORD ATTEMPTS ---")
saved_password = "mysecretpass"
attempts = 3

while attempts > 0:
    entered_pass = input("Enter password: ")
    
    if entered_pass == saved_password:
        print("Login successful! Welcome.")
        break
    else:
        attempts = attempts - 1
        if attempts > 0:
            print("Wrong password. Attempts left:", attempts)
        else:
            print("Account locked! Too many failed attempts.")



# =====================================================================
#  Number Guessing Game
print("\n--- 23. NUMBER GUESSING GAME ---")
import random
target_number = random.randint(1, 100)
total_guesses = 0

print("Guess a number between 1 and 100")

while True:
    user_guess = int(input("Your guess: "))
    total_guesses = total_guesses + 1
    
    if user_guess < target_number:
        print("Too Low! Try a bigger number.")
    elif user_guess > target_number:
        print("Too High! Try a smaller number.")
    else:
        print("Correct! You guessed it in", total_guesses, "attempts.")
        break

# =====================================================================
# Q24: Student Marks Analyzer
print("\n--- 24. STUDENT MARKS ANALYZER ---")
total_students = int(input("How many students? "))

highest_pct = -1.0
lowest_pct = 101.0
sum_of_all_percentages = 0.0

for i in range(total_students):
    print("\nEnter details for student", i + 1)
    name = input("Name: ")
    
    total_marks = 0.0
    for j in range(5):
        sub_marks = float(input("Enter marks for subject " + str(j+1) + ": "))
        total_marks = total_marks + sub_marks
        
    pct = (total_marks / 500.0) * 100
    sum_of_all_percentages = sum_of_all_percentages + pct
    

    if pct > highest_pct:
        highest_pct = pct
    if pct < lowest_pct:
        lowest_pct = pct
        

    if pct >= 90:
        grade = "A"
    elif pct >= 80:
        grade = "B"
    elif pct >= 70:
        grade = "C"
    elif pct >= 50:
        grade = "D"
    else:
        grade = "F"
        
    # Pass or Fail
    if pct >= 40:
        status = "Pass"
    else:
        status = "Fail"
        
    print(name, "- Total:", total_marks, "| Percentage:", pct, "% | Grade:", grade, "| Result:", status)

if total_students > 0:
    class_average = sum_of_all_percentages / total_students
    print("\n--- Class Summary ---")
    print("Highest Percentage in class:", highest_pct, "%")
    print("Lowest Percentage in class:", lowest_pct, "%")
    print("Overall Class Average:", class_average, "%")




# =====================================================================
#  Shopping Bill
print("\n--- 25. SHOPPING BILL ---")
total_amount = 0.0

while True:
    price = float(input("Enter item price: "))
    qty = int(input("Enter item quantity: "))
    
    total_amount = total_amount + (price * qty)
    
    more = input("Add more items? (y/n): ")
    if more == "n" or more == "N":
        break


discount = 0
if total_amount >= 10000:
    discount = 20
elif total_amount >= 5000:
    discount = 10
elif total_amount >= 2000:
    discount = 5
else:
    discount = 0

discount_value = (total_amount * discount) / 100
final_bill = total_amount - discount_value

print("\n--- Bill Details ---")
print("Total Price: Rs.", total_amount)
print("Discount Applied:", discount, "%")
print("Discount Amount Saved: Rs.", discount_value)
print("Final Payable Bill: Rs.", final_bill)

