# print("A 'single quote' inside a double quote ")
# print('A "double quote" inside a single quote')
# print("Alternately you can just \"escape\" the quote")
#
# print("Hello World!")
# print("Hello World!\nHello world!\nHello World!")
# print("Hello" + "Sid")
# print("Hello" + " " +"Sid")
import math
import random

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
# print(len(input("Enter your name\n")))


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

# city = input("what is your city name\n")
# pet = input("What is your pet name\n")
# print("City name is "+city+" and pet name is "+pet)

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
#
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
# print(f"you have {weeks} weeks left.")


# age = input()
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
# print("Election voting")
# age = int(input("Enter your age\n"))
# voting_card = input("Do you have voting card? Yes or No\n").lower()
# if age >= 18:
#     print("You are elegible for vote")
#     if voting_card == "yes":
#         print("Now you can vote")
#     else:
#         print("You cant vote now")
# else:
#     print("You are not elegible for vote")

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

# print("Result")
# marks = int(input("Enter your marks\n"))
# total_marks = (marks/625)*100
# if total_marks > 80 and total_marks < 100:
#     print("Disctinction")
# elif total_marks > 60 and total_marks < 79:
#     print("First class")
# elif total_marks > 40 and total_marks < 59:
#     print("Second class")
# else:
#     print("Fail")

# student_marks = int(input("Enter your marks\n"))
# total_marks = (student_marks/625) * 100
# if total_marks >= 80:
#     print("Distinction")
# elif total_marks >= 60:
#     print("First class")
# elif total_marks >= 45:
#     print("Second class")
# elif total_marks >= 35:
#     print("Just pass")
# else:
#     print("Fail")

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
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N \n")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, You have to grow taller before you can ride.")

#Love Calculator

# print("The Love Calculator is calculating your score....")
# name1 = input("What is your name?\n")
# name2 = input("What is their name?\n")
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#     print(f"your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#     print(f"your score is {score}, you are alright together.")
# else:
#     print(f"your score is {score}.")
#

# Treasure Island project

# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You have at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
#
# if choice1 == "left":
#     choice2 = input('You have to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
#     if choice2 == "wait":
#         choice3 = input("You arrive at the island unharmed. There is a with 3 doors. One red, one yellow and one blue.\n").lower()
#         if choice3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif choice3 == "yellow":
#             print("You found the treasure! You Win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#     else:
#         print("You got attacked by an angry trout. Game Over.")
# else:
#     print("You fell into a hole. Game Over.")

# Random Module

import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_float = random.random()
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")
#
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Head")
# else:
#     print("Tail")

# [Interactive Coding Exercise] Banker Roulette - Who will pay the bill?

# names_string = input("Enter the names your friends\n")
# names = names_string.split(", ")
#
# import random
#
# num_items = len(names)
# random_choice = random.randint(0, num_items-1)
# print(names[random_choice])

# IndexErrors and Working with Nested Lists
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)


# Quiz

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])
#

# [Interactive Coding Exercise] Treasure Map

# line1 = [" ", " ", " "]
# line2 = [" ", " ", " "]
# line3 = [" ", " ", " "]
# map = [line1, line2, line3]
# print("Hiding your treasure! x marks the spot.")
# position = input("Where do you want to put the treasure\n")
#
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
#
# print(f"{line1}\n{line2}\n{line3}")

# Project: Rock Paper Scissors

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#
# computer_choice = random.randint(0, 2)
# print(f"Computer chose {computer_choice}")
#
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
# elif computer_choice > user_choice:
#     print("You lose")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw")

#Using the for loop with Python List

# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)
# element = ["Sid", "Manju", "Akansha", "Arpita"]
# for names in element:
#     print(names)

# [Interactive Coding Exercise] Average Height
#
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"total height = {total_height}")
#
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f"numbers of students = {number_of_students}")
#
# average_height = round(total_height / number_of_students)
# print(f"average height = {average_height}")


# [Interactive Coding Exercise] High Score

# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#
# print(f"The highest score in the class is :{highest_score}")
#

# for loops and the range() function
#
# for number in range(0, 101):
#     print(number)
#
#
# for number in range(0, 101, 2):
#     print(number)
#
#
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)
#


# target = int(input("Enter the between 0 to 1000\n"))
#
# even_number = 0
# for number in range(2, target + 1, 2):
#     even_number += number
# print(even_number)
#
# # or
#
# alternative = 0
# for number in range(2, target+1):
#     if number % 2 == 0:
#         alternative += number
# print(alternative)

# [Interactive Coding Exercise] The FizzBuzz Job Interview Question
#
# target = 100
# for number in range(1, target + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Project: Create a Password Generator
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator")
# nr_letters = int(input("How many latters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))
#
# Easy Level
#
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)
#
# Hard Level
#
# password_list = []
#
# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#     password += char
#
# print(f"Your password is: {password}")

# Defining and Calling Python Functions

#
# def my_function():
#     print("Hello")
#     print("Bye")

# my_function()

# The Hurdles Loop Challenge

# Indentation in Python

# While loop

# How to Check the User's Answer

# import random
# end_of_game = False
# from hangman_words import word_list
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# lives = 6
#
# from hangman_art import logo
# print(logo)
#
# # Testing code
# print(f'Pssst, the solution is {chosen_word}')
#
# display = []
# for _ in range(word_length):
#     display += "_"
# # print(display)
#
#
# while not end_of_game:
#     guess = input("Guess a letter: \n").lower()
#     if guess in display:
#         print(f"You have already guessed {guess}")
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n"
#         #       f"Current letter: {letter}\n"
#         #       f"Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that is not in the word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#
#     print(f"{' '.join(display)}")
#
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#     from hangman_art import stages
#     print(stages[lives])

# Functions with Inputs


# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
#
#
# greet()

# Function that allows for input


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#
#
# greet_with_name("Manju")

#Positional vs. Keyword Arguments

#Function with more than 1 input


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
#
# greet_with("Sid", "Karwar")

# Function with keyword arguments


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
#
# greet_with(name="Sid", location="Karwar")

# Paint Area Calculator
#
# import math
#
#
# def paint_calc(height, width, cover):
#     num_cans = (height * width) / cover
#     round_up_cans = math.ceil(num_cans)
#     print(f"You'll need {round_up_cans} cans of paint.")
#
#
# test_h = int(input("Enter your height of wall\n"))
# test_w = int(input("Enter your width of wall\n"))
# coverage = 5
#
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime Number Checker


# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
#
# n = int(input("Check this number\n"))
# prime_checker(number=n)

# Encryption

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
#             'g', 'h', 'i', 'j', 'k', 'l',
#             'm', 'n', 'o', 'p', 'q', 'r',
#             's', 't', 'u', 'v', 'w', 'x',
#             'y', 'z', 'a', 'b', 'c', 'd',
#             'e', 'f', 'g', 'h', 'i', 'j',
#             'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v',
#             'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decode text is {plain_text}")
#
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(cipher_text=text, shift_amount=shift)


# Reorganising our Code

# from art import logo
# print(logo)
#
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
#             'g', 'h', 'i', 'j', 'k', 'l',
#             'm', 'n', 'o', 'p', 'q', 'r',
#             's', 't', 'u', 'v', 'w', 'x',
#             'y', 'z', 'a', 'b', 'c', 'd',
#             'e', 'f', 'g', 'h', 'i', 'j',
#             'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v',
#             'w', 'x', 'y', 'z']
#
#
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"Here's the {direction}d result: {end_text}")
#
#
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#
#     shift = shift % 26
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#     result = input("Type 'yes' if you want to go again. Otherwise type 'no' .\n")
#     if result == "no":
#         should_continue = False
#         print("Goodbye")

# The Python Dictionary: Deep Dive

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again",
#     "Loop": "The action of doing something over and over again"
# }
#
# print(programming_dictionary["Bug"])

# Empty dictionary

# empty_dictionary = {}

# Wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary

# programming_dictionary["Bug"] = "A month in your computer."
# print(programming_dictionary)

# Loop through a dictionary

# for thing in programming_dictionary:
#     print(thing)
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
# prog_dictionary = {
#     "sid": "This message from sid",
#     "Tamse": "This is my surname",
#     "Address": "This is my address",
# }
#
# print(prog_dictionary["sid"])
#
# for item in prog_dictionary:
#     print(item)
#     print(prog_dictionary[item])
#
# prog_dictionary["sid"] = "My name is sid"
# print(prog_dictionary)

# [Interactive Coding Exercise] Grading Program

# student_score = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_grade = {}
#
# for student in student_score:
#     score = student_score[student]
#     if score > 90:
#         student_grade[student] = "Outstanding"
#     elif score > 80:
#         student_grade[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grade[student] = "Acceptable"
#     else:
#         student_grade[student] = "Fail"
# print(student_grade)


# program

# name_student = {
#     "first_name": "",
#     "middle_name": "",
#     "last_name": "",
#     "id": 1
# }
#
# name_student1 = {}
#
# for name in name_student:
#     if name == "first_name":
#         name_student1[name] = "Siddharth"
#     elif name == "middle_name":
#         name_student1[name] = "Shripad"
#     elif name == "last_name":
#         name_student1[name] = "Tamse"
#     elif name == 1:
#         name_student1[name] = 2
# print(name_student1)

# Nesting Lists and Dictionaries

# travel_log = {
#     "France": {
#         "cities_visited": [
#             "Paris",
#             "Lille",
#             "Dijon"
#         ],
#         "total_visits": 12
#     },
#     "Germany": {
#         "cities_visited": [
#             "Berlin",
#             "Hamburg",
#             "Stuttgart"
#         ],
#         "total_visits": 5
#     },
# }
#
#
# travel_logs = [
#     {
#         "country": "France",
#         "cities_visited": [
#             "Paris",
#             "Lille",
#             "Dijon"
#         ],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": [
#             "Berlin",
#             "Hamburg",
#             "Stuttgart"
#         ],
#         "total_visits": 5
#     }
# ]

# [Interactive Coding Exercise] Dictionary in List

# country = input("Add country name\n")
# visits = int(input("Number of visits\n"))
# list_of_cities = eval(input("create list from formatted string\n"))
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#
#
# def add_new_country(name, time_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = name
#     new_country["visits"] = time_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
#
#
# add_new_country(name=country, time_visited=visits, cities_visited=list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favorites city was {travel_log[2]['cities'][0]}")

# Simple Example

# country = input("Add country name\n")
# visits = int(input("Number of visits\n"))
# list_of_cities = eval(input("create list from formatted string\n"))
#
#
# def add_new_country(name, time_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = name
#     new_country["visits"] = time_visited
#     new_country["cities"] = cities_visited
#     print(new_country)
#
#
# add_new_country(name=country, time_visited=visits, cities_visited=list_of_cities)

# Solution and Complete Code for the Secret Auction Program

# from replit import clear
# from art import logo
# print(logo)
#
# bids = {}
# bidding_finished = False
#
#
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")
#
#
# while not bidding_finished:
#     name = input("What is your name\n")
#     price = int(input("What is  your bid $\n"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         clear()

# Functions with Outputs

# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
#
#
# format_name("siddharth", "TAMSE")
#
#
# def formate_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     print(f"{formated_f_name} {formated_l_name}")
#
#
# formate_name("SiDDhartH", "tAMse")


# Function with Output using return type


# def formate_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(formate_name("SidDHartH", "tAmSE"))

#
# def formate_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"
#
#
# print(formate_name(input("What is your first name?\n"),
#                    input("What is your last name?\n"))
#       )

# [Interactive Coding Exercise] Days in Month


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 ==0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and is_leap(year):
#         return 29
#     else:
#         return month_days[month - 1]
#
#
# year = int((input("Enter a year\n")))
# month = int(input("Enter a month\n"))
# days = days_in_month(year, month)
# print(days)

# Quiz question 1


# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# print(add(2, multiply(5, divide(8, 4))))

# Quiz question 2


# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#
#     return inner_function(a, b)
#
#
# result = outer_function(5, 10)
# print(result)


# Quiz question 3

# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
#
#
# print(my_function(25))


# Calculator

# from art import logo
#
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }
#
#
# def calculator():
#     print(logo)
#     num1 = float(input("What's the first number?:\n"))
#     for symbol in operations:
#         print(symbol)
#     should_continue = True
#
#     while should_continue:
#         operations_symbol = input("Pick an operation\n")
#         num2 = float(input("What's the next number?:\n"))
#         calculation_function = operations[operations_symbol]
#         answer = calculation_function(num1, num2)
#
#         print(f"{num1} {operations_symbol} {num2} = {answer}")
#
#         if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculating :") == "y":
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()
#
#
# calculator()

# Blackjack program

# from replit import clear
# from art import logo
#
#
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
#
# def calculate_score(cards):
#     """Take a list of cards and return the score calculated from the cards"""
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)
#
#
# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return "Draw"
#     elif computer_score == 0:
#         return "Lose, opponent has Blackjack"
#     elif user_score == 0:
#         return "Win with a Blackjack"
#     elif user_score > 21:
#         return "You went over. You lose"
#     elif computer_score > 21:
#         return "Opponent went over. You win"
#     elif user_score > computer_score:
#         return "You win"
#     else:
#         return "You lose"
#
#
# def play_game():
#     print(logo)
#     user_cards = []
#     computer_cards = []
#     is_game_over = False
#
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#
#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"   Your cards: {user_cards}, current score: {user_score}")
#         print(f"   Computer's first card: {computer_cards[0]}")
#
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True
#
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)
#
#     print(f"  Your final hand: {user_cards}, final score: {user_score}")
#     print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))
#
#
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     clear()
#     play_game()

# Namespaces: Local vs. Global Scope

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f" enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f" enemies outside function: {enemies}")

# Local scope


# def drink_position():
#     position_strength = 2
#     print(position_strength)
#
#
# drink_position()

# Global variable

# player_health = 10


# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
#
# drink_potion()
# print(player_health)

# There is no Block Scope

# game_level = 3
#
#
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)
#

# How to Modify a Global Variable

# enemies = 1
#
#
# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
#
#
# ene = increase_enemies()
# print(f"enemies outside function: {ene}")

# The Number Guessing Game

# from random import randint
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
#
# def check_answer(guess, answer, turns):
#     """checks answer against guess. Return the number of turns remaining."""
#     if guess > answer:
#         print("Too high")
#         return turns - 1
#     elif guess < answer:
#         print("Too low")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {answer}.")
#
#
# def set_defficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
#
#
# def game():
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100")
#     answer = randint(1, 100)
#
#     turns = set_defficulty()
#
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         guess = int(input("Make a guess:"))
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("you've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")
#
#
# game()


# Debugging

# Describe Problem


# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
#
#
# my_function()


# solution

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# Reproduce the Bug

# from random import randint
#
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Solution

# from random import randint
#
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Play Computer

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("you are a Gen Z.")

# Solution

# year = int(input("What's your year of birth?\n"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("you are a Gen Z.")

# Fix the Error

# age = input("How old are you\n")
# if age < 18:
#     print("You can drive at age {age}")

# Solution

# age = int(input("How old are you\n"))
# if age < 18:
#     print(f"You can drive at age {age}")

# Print is Your Friend

# pages = 0
# word_per_pages = 0
# pages = int(input("Number of pages: \n"))
# word_per_pages == int(input("Number of words per pages\n"))
# total_words = pages * word_per_pages
# print(total_words)

# Solution

# pages = 0
# word_per_pages = 0
# pages = int(input("Number of pages: \n"))
# word_per_pages = int(input("Number of words per pages\n"))
# total_words = pages * word_per_pages
# print(f"pages = {pages}")
# print(f"words_per_pages = {word_per_pages}")
# print(total_words)


# Use a Debugger

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])


# Solution


# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

# Higher Lower Game

# from art import logo, vs
# from game_data import data
# from replit import clear
#
#
# def format_data(account):
#     """Takes the account data and return the printable format."""
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}"
#
#
# def check_answer(guess, a_followers, b_followers):
#     """Take the user guess and follower counts and return if they got it right"""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# print(logo)
# score = 0
# game_should_continue = True
# account_b = random.choice(data)
#
# while game_should_continue:
#     account_a = account_b
#     account_b = random.choice(data)
#     while account_a == account_b:
#         account_b = random.choice(data)
#
#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
#
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#     clear()
#     print(logo)
#
#     if is_correct:
#         score += 1
#         print(f"You're right! Current score: {score}")
#     else:
#         game_should_continue = False
#         print(f"Sorry, that's wrong. Final score: {score}")


# Coffee Machine Code

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.23
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: &{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])








