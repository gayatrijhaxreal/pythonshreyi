# """Accept numbers from a user"""
# num = input("Enter a number: ")
# num = int(num)
# print(f"You entered: {num}")

# """ Accept age from the user and print it."""
# age = input("enter your age:")
# age= int(age)
# print(f" your age : {age}")

# """Print(126 > 130)"""

# print(126 > 130)
# print((456 == 456) != (235 == 236))
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
# print(True and bool(0))

""" Q1. Accept two numbers and print the greatest between them"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"Greatest number is: {num1}")
else:
    print(f"Greatest number is: {num2}")

""" Q2. Accept the gender from the user as char and print the 

 respective greeting message

 Ex - Good Morning Sir (on the basis of gender)"""
gender = input("Enter your gender (M/F): ")
if gender.upper() == "M":
    print("Good Morning Sir")
else:
    print("Good Morning Ma'am")

""" Q3. Accept an integer and check whether it is an even number 

 or odd"""

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

""" Accept name and age from the user. Check if the user is a 

 valid voter or not.

 Ex- “hello shery you are a valid voter”"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Hello {name}, you are a valid voter.")
else:
    print(f"Hello {name}, you are not a valid voter.")

""" Accept a year and check if it a leap year or not (google to 

 find out what is a leap year)"""
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")