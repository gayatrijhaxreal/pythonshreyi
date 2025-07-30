"""accept the numbers from a user""";

"""number = int(input("write a number : "));

print(number);"""

"""accept age from the user and print it """;

"""age = int(input("my age is : ")); 

print(age);"""

"""Q.1) Accept two numbers nd print the greatest between them."""

#num1 = int(input("Put your first number here: "))
#num2 = int(input("Put your second number here:"))
#   print(num1)

#else:
#    print(num2)

"""Q2.) Accept the gender from the user as char and print the respective greeting message  """

#print("Please put your gender in sir and madam form ")
#gender = input("Your gender: ");

#if gender == "Sir": 
 #   print("Good Morning Sir")

#elif gender =="Madam":
 #   print("Good Morning Madam")

#else:
#    print("INVALID GENDER")

"""Q3.)Accept an Integer and check Whether it is an even number or odd. """

#num = int(input("Enter your number :- "));

#if num % 2 == 0:
 #   print("Even ")

#else :
 #   print("Odd")

"""Accept name and age from the user. Check if the user is a valid voter or not ."""

#name = input("please enter your name:- ");
#age = int(input("please put your age here:- "));

#if age >= 18:
#    print(f" hello {name} you are a valid voter ")

#else:
#    print(f"Sorry!! {name} you are not a valid voter ")
""" Accept a year and check if it a leap year or not """

#year = int(input("put your year :-"));

#if year % 4 ==0:
 #   print(f"Congrats!! {year} is a leap year ") 

#else:
#    print(f"sorry !! {year} is not a leap year ")

"""print natural number upto n ."""

#n = int(input("Tell me the number :- "))
#for i in range(n):
#    if i == 0:
#        continue
#    print(i+1)

"""reverse for loop . print n to 1 ."""

#n = int(input("Tell me the number :- "))

#for i in range(0,n+1):
#    print(i)

"""take a number as input and print its table."""

#n = int(input("tell me the number :-"))

#for i in range(n,0,-1):
#    print(i)

"""Take a number as input and print its table ."""

#n = int(input("tell me the number :- "))

#for i in range(1,11):
#    print(f"{n}*{i} = {n*i}")

"""Sum up to n terms """

#n = int(input(" tell me the number :- "))

#sum = 0 

#for i in range(1,n+1):

#    sum = sum  +  i 

#print(f"your sum is {sum} ") 

"""print the factorial of nth term :"""
#n = int(input("tell me the number :- "))

#product = 1

#for i in range(1, n+1 ):
#   product = product * i
#print(f"your factorial is {product}")

"""Print the sum of all even and odd numbers in a range seperately."""

#n = int(input("tell your number:- "))
#even = 0
#odd = 0
#for i in range(1,n+1):
#    if i %2==0:
#        even += i
#    else:
 #       odd +=i

#print(f"your even and odd sum are {even},{odd}")


"""print allthe factors of a number """

#n = int (input("please tell me your number:-"))
#for i in range(1,n+1):
#    if n%i == 0:
#        print(i)

"""Accept a number and check if it a perfect number or not.
A number whose sum of factors is equal to the number itself
Ex : 6 =1,2,3 =6 """

# n = int (input("please tell me your number:-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum+i    
# print(sum)   

# if sum==n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")

"""Check whether the number is prime or not"""

# n = int(input("please tell me your number:- "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count = count + 1

# if count == 2:
#     print("number is prime ")
# else:
#     print("number is not prime")

"""Reverse the strings without using the functions:"""

# a = str(input("write your String here:- "))
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b=b+(a[i])
# print(b)

"""Check whether the string is pallindrome or not:- """

# a = str(input("write your String here:- "))
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b=b+(a[i])
# print(b)

# if a==b:
#     print("your string is pallindrome")
# else:
#     print("your String is not pallindrome")
"""Seperate each digit of a number and print it on the new line."""


# a = int(input("tell your number:"))

# while a>0:
#     print(a%10)
#     a=a//10

"""Accept the number and print its reverse: """

# a = int(input("tell your number:"))
# rev = 0
# while a > 0:
#     rev= rev*10 + a % 10
#     a =a//10

# print(rev)

"""Accept the number and check it it is a pallindromic number (if number and its reverse are equal)"""

# a = int(input("tell your number:"))

# copy =a
# rev = 0
# while a>0:
#     rev = rev*10 + a % 10
#     a =a//10

# if copy == rev:
#         print("your number is pallindromic")
# else:
#      print("it is not")

"""Create a random number guessing game with python"""

# import random
# num = random.randint(1,100)

# tries = 0 

# while True:
#     guess = int(input("please guess your number between 1 to 100 :- "))

#     if num == guess:
#         tries += 1
#         print(f"you are right you guessed the number in {tries} tries")
#         break 

#     elif num < guess:
#         print("go to a little lower")
#         tries += 1

#     elif num > guess:
#         print("go a little higher")
#         tries += 1
#     else:
#         tries += 1
#         print ("sorry you are wrong") 

    
"""Print positive and negative elements of an list."""

# l =[-45,67,12,-68,-69-34]

# largest = l[0]
# index = 0 

# for i in range(len(l)):
#     if l[i] > largest:
#         largest =l[i]
#         index = i
# print(f"your largest number is {largest} at index {index}")


# l = [12,16,13,19,17]

# largest =l[0]
# sec_largest = l[0]

# for i in l: 
#     if i >largest:
#         sec_largest = largest
#         largest = i 

#     elif i > sec_largest:
#         sec_largest = i
# print(sec_largest,largest)

# a= [12,13,14,15,16]

# for i in range(len(a)-1):
#     if a[i]< a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break 
# else:
#     print("your list is sorted")

# // tupple

"""Write a python script to merge two python dictonaries"""

# d1 = {10:100, 20:200, 30:300}
# d2 = {40:400, 50:500, 60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

"""Write a python program to sum all the values in a dictonary"""


# d1 = {10:100, 20:200, 30:300}

# sum = 0 

# for i in d1:
#     sum = sum + d1[i]
# print(sum)


"""Count the frequency of each element """

# a =[1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,8,5,6,6,6,6,7,7,7,7,7,8,8,8,8]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else: 
#         d[i]=1
# print(d)

"""Write a python program to combine two dictonary by adding values for common keys. """

# d1 = {10:100, 20:200, 30:300}
# d2 = {40:400, 50:500, 60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else: 
#         d1[i] = d2[i]
# print(d1)

