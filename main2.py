# print("namaste youtube we are learning python");
# hello i am gayatri how are you 
"""hello this is multiline(doc strings)"""

"""sher = "Harsh bhaiya "

SheryiansSchool = "students" #pascal case

sheriyansSchool = "students" #camel case

sheryians_school = "students" #snake case

a = -1.2/5

b =35j 

print(type(a))
print(type(b)) """

#stringss

#st = '1234hhjhchuhh njnhchhjhjj $%^&&&$#%^&***((()))'

#print(type(st))

#b = True 

#print(type(b))

#a = "😊"

#print(ord(a))

#a = 65

#print(chr(a))

#a = "hello brother "; 

#print(a[::]);

#type conversion 
#a = 0;

#print(bool(a));

#print(type(a)) ;
 
#print("hello how are you ");
#name = input(" ");
#age = 18;
#print(name,age);
#print("hello my name is :" ,name,"and my age is:",age);
#print(f"hello my name is : {name} and my age is : {age}");
#age = input("hello my name is : ");
#print(age);

#a= 5;
#b=32;
#print(b-a);
#print(a*b);
#print(b//a);
#print(b/a);
##print(5**2);
#print(32%5);
#assignment operator 
#a = 20;
#a += 20;
#a += 40;
#a += 60;
#print (a);
#compound assinment operator 

#a=11;
#v=11;



#print(126>130);

#print((456==456)!=(235==236));

#print(12<10 or 45 == 56 or 69 > 70 or 15 != 13 );

#print(True and bool(0));

#a = 10;
 
#if a > 10 : 
#    print("i will do task A")

#else:
#    print("i will do task B")

#money = int(input("please provide me the money :- "));

#if money== 10:
 #   print("I will have chocobar icecream ")

#elif money<=10:
 #   print("no we don't have much money we can't have any Icecream sorry!!")    

#elif money == 20:
 #   print("I will have mango dolly")

#else:
#   print("I will have cone")    

# for loop 


#for i in range(-3, -16, -1):
 #   print(i)

#lets print the table of 5
#for i in range(5,51,5):
  #  print(i)

# lets print any table: 

#n = int(input("which table you want to print ? "))

#for i in range(n,(n*10)+1,n):
 #   print(i)
#


#a = "SHERYIANS TEACHES INDUSTRY THINGS"

#print(len(a))
#for i in range(len(a)):
#  print(a[i])
 
#a = "SHERIYANS IS COOL"

#for i in a:
#    print(i)

# Break :
 
#for i in range(1,21):
#    if i== 16:
 #       break
#    else:
#        print(i)
    

#for i in range(1,10):
#    if i == 5:
#        continue
#    print(i)

"""for i in range(1,21):
    if i == 5:
        print("break statement is executed")
        break 
    print(i)

else:
    print("Break statement is not executed")

"""
# n = int(input("please tell your number :- "))

# for i in range(n):
#     print("hello world")

# a=1

# while a <=30:
#     print(a)
#     a=a+1


# def hello():
#     print("this is A hello fcn so i am doing hello ")


# positional argument:

# hello()

# def sum(a,b):
#     print(f"the sum of the number is {a + b}")

# sum(10,11)

# default argument

# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")
# hello( age = 19 , name = "gayatri")

# def sum(a,b=90):
#     print(f"the sum is {a+b}")
# sum(12)



# def pallindrome(st):
#     rev =""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev +st[i]

#     if rev == st:
#         print(f"{st} is a pallindrome")
#     else:
#         print(f"{st} is not a palindrome")

# pallindrome("naman")
# pallindrome("cursor")

# // list 

# a = [12,13,14,15,16]

# #1st way using index
# for i in range(len(a)):
#     print(i)

# #2nd way using index

# for i in a :
#     print(i)

# print(dir(list))

# help(list)

# l = [1,2,3,4,5]
# l.extend([20,25,30])
# l.remove(3)
# popped_item = l.pop(4)
# l.count(5)
# l.index(3)
# print(l.count())


# a= (1,2,3,2,4,5)
# for i in range(len(a)):
#     print(a[i])


# help(tuple)


# // set 

# Creating a set
# s = {1, 2, 3, 4, 5}
# print(s)
# print(s[0])

# # Adding elements
# s.add(6)
# print(s)

# # Removing elements
# s.remove(3)
# print(s)

# Set operations
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))      # Union (a|b)
# print(a.intersection(b)) # Intersection (a&b)
# print(a.difference(b))   # Difference (a-b)
# print(a.symmetric_difference(b))  #(a^b)
# print((a^b))

# # Sets do not allow duplicate values
# dup_set = {1, 2, 2, 3}
# print(dup_set)


# b = hash("Hello")
# print(b)

# c = hash((1, 2, 344))
# print(c)



# # Creating a dictionary
# my_dict = {"name": "Gayatri", "age": 19, "city": "Delhi"}

# # Accessing values
# print(my_dict["name"])
# print(my_dict.get("age"))

# # Adding a new key-value pair
# my_dict["country"] = "India"

# # Updating a value
# my_dict["age"] = 20

# # Removing a key-value pair
# removed = my_dict.pop("city")

# # Iterating over keys and values
# for key, value in my_dict.items():
#     print(f"{key}: {value}")

# # Checking if a key exists
# if "name" in my_dict:
#     print("Name is present in the dictionary.")

# # Dictionary methods
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())



# r.write("and i am appending some content inn it")
# r.close()


