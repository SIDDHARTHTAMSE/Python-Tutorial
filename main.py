# print("A 'single quote' inside a double quote ")
# print('A "double quote" inside a single quote')
# print("Alternately you can just \"escape\" the quote")
#
# print("Hello World!")
# print("Hello World!\nHello world!\nHello World!")
# print("Hello" + "Sid")
# print("Hello" + " " +"Sid")

#what is syntax error and indentation error
#The word debugging means

#The python input Function

# input("What is your name?")
#
# print("Hello " + input("What is your name?"))

# Comment the code

#[Interactive Coding Exercise] Input Function

# nameofletters = len("Siddharth")
# print(nameofletters)
#
# print(len(input()))



# Python Variables

# name = input("What is your name?")
# print(name)
#
#
# name = "Sid"
# print(name)
#
# name = "manju"
# print(name)
#
# name = input("What is your name?")
# length = len(name)
# print(length)
#
# city = input("what is your city name\n")
# pet = input("What is your pet name\n")
# print("City name is "+city+" and pet name is

# print(len(input("What is Your name ? \n")))

#Pyhton Primitive data types

#String

# print("Siddharth" [4])

#Integer

# print(12+45)

#Large Number
 # 12_34_98

#Float

# 1465.8

#Boolean

# True
# False

#
# num_char = len(input("What is your name \n"))
# print(type(num_char))
#
# num_char_1 = "Hello"
# print(type(num_char_1))



# num_char = len(input("What is your name \n"))
# new_num_char = str(num_char)
# print("My name has "+new_num_char+" characters")

# print(70 + float("100.5"))

# print(str(70) + str(100))


# two_digit_number = input()
#
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
#
# three_digit_number = first_digit + second_digit
#
# print(three_digit_number)

# Mathematical Operation in Python
# PENDASLR
# ()
# **
# */
# +-

# height = input()
# weight = input()
#
# weight_as_int = int(weight)
# height_as_float = float(height)

# using the exponent operator **
# bmi = weight_as_int / height_as_float ** 2

# or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)
#
# bmi_as_int = int(bmi)
# print(bmi_as_int)
#

# Number Manipulation and F Strings in Python
# print(round(8/3, 3))
# print(int(8/3))
#

# score = 0
# height = 1.8
# isWinning = True
#
# # f-String
# print(f"Your score is {score},"
#       f" your height is {height},"
#       f" you are winning is {isWinning}"
#       )


# How many years you have left in your life program
#
# age = input()
# years = 90 - int(age)
# weeks = years * 52
# age = input()
# print(f"you have {weeks} weeks left.")
#
# years = 90 - int(age)
# days = years * 365
# print(F"You have total {days} days left in your life")
#
#
# name = input("What is your name ?")
# print("Hello, "+name)
#
# print("Welcome to the tip Calculator !")
# bill = float(input("What was the total bill ? \n"))
# tips = int(input("How much tip would you like to give ? \n"))
# people = int(input("How many people to split the bill ?\n"))
# tip_as_percent = tips / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# final_amount1 = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay {final_amount1}")
#
# Control Flow with if / else and Conditional Operators
#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm \n"))
#
# if height != 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#
# Odd and Even
#
# print("Which number do you want to check?")
# number = int(input())
#
# if number % 2 == 0:
#     print("This is even number")
# else:
#     print("This is odd number")

# Nested if statements and elif statements

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"))
# age = int(input("What is your age? \n"))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, You have to grow taller before you can ride.")
#
#
#
#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"))
# age = int(input("What is your age? \n"))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, You have to grow taller before you can ride.")

# BMI 2.0

# height = float(input())
# weight = int((input()))
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you are normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

# Leap year or not
#
# year = int(input())
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")


#Multiple If Statements in Succession

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"))
# age = int(input("What is your age? \n"))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken ? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, You have to grow taller before you can ride.")

# Pizza

# print("Thank you for choosing Python Pizza deliveries!\n")
# size = input("What size pizza do you want? S,M or L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra chees? Y or N\n")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}")

#Logical Operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
age = int(input("What is your age? \n"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N \n")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, You have to grow taller before you can ride.")

#Love Calculator

print("The Love Calculator is calculating your score....")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"your score is {score}, you are alright together.")
else:
    print(f"your score is {score}.")


# Treasure Island project

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You have at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You have to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a with 3 doors. One red, one yellow and one blue.\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

# Random Module
import random
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

random_side = random.randint(0, 1)
if random_side == 1:
    print("Head")
else:
    print("Tail")
