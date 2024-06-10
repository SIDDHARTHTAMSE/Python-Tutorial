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
# age = input()
# years = 90 - int(age)
# weeks = years * 52
# print(f"you have {weeks} weeks left.")

# age = input()
# years = 90 - int(age)
# days = years * 365
# print(F"You have total {days} days left in your life")
#

# name = input("What is your name ?")
# print("Hello, "+name)

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

# Control Flow with if / else and Conditional Operators

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm \n"))
#
# if height != 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# Odd and Even

# print("Which number do you want to check?")
# number = int(input())
#
# if number % 2 == 0:
#     print("This is even number")
# else:
#     print("This is odd number")
