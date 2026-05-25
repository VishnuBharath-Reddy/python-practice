name = "Vikky"
age = 25
height = 5.11
is_student = False

#  string combinations

last = "Aekasi"
print("Vishnu " + last)

print(last.upper())
print(last.lower())

name = input("Whats your name ?")

print("My name is " + name)


# practice

# Name greeting

name = input("what is your name ")
print("Hello ! " + name) 

# Color
color = input("What is your Favourite color ")
print("My favourite color is " + color)

# Upper and lower case

name = input("Write your name  ")
print("your name in upper case " + name.upper())
print("your name in lower case " + name.lower())

# full name

first_name = input(("Enter your first name: "))
last_name = input(("Enter your last name : "))

print("My full name is " + first_name + " " + last_name)

# Age

age = (input("Enter your Age : "))
print("I am  " + age + " years old ")

# Repeat a word

word = input("Enter your word ")
print("your word three time is " + word*3)


# Complex Challenge

first = input("Enter your first name: ")

last = input("Enter your last name: ")

age = int(input("Enter your Age: "))

prog = input("Enter your favorite programming language: ")

color = input("Enter your fovourite color: ")

dream = input("Enter your dream company: ")


print("-------------------- Student Profile -------------------------")

print("Full Name : " + first +" "+ last)

print("you are " + str(age) + " years old.")

print("Next year you will be " + str(age+1) + " years old ")

print("Favorite Programming Langauge: " + prog)

print("Favorite color : " + color*3)

print("Dream Company: " + dream)