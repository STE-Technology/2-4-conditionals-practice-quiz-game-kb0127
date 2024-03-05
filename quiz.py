"""
File: quiz.py
Author: KB
Date: 2024-03-05
Description: Multiple choice chemistry quiz
"""
score = 0

print("----- Multiple Choice Quiz -----")

#First question
print("1. What is the molar mass of water?")
print("(a) 18.02 g/mol")
print("(b) 36.00 g/mol")
print("(c) 12.01 g/mol")
print("(d) 10.00 g/mol")

#Takes user input and gives right/wrong feedback for question 1
user_answer = input("> ")
if user_answer == "a" or user_answer == "A":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

#Second question
print("1. What is the symbol for gold on the periodic table?")
print("(a) Ag")
print("(b) Cu")
print("(c) Au")
print("(d) Gold is not an element")

#Takes user input and gives right/wrong feedback for question 2
user_answer = input("> ")
if user_answer == "c" or user_answer == "C":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

#Third question
print("1. What is element number 6 on the periodic table?")
print("(a) Fire")
print("(b) Silver")
print("(c) Carbon")
print("(d) There are only 4 elements")

#Takes user input and gives right/wrong feedback for question 3
user_answer = input("> ")
if user_answer == "c" or user_answer == "C":
    print("Your answer is correct")
    score += 1
else:
    print("Your answer is incorrect")

print("Quiz complete!")
print("You answered " + str(score) + " questions correctly. Your score is " + str(score / 3 * 100) + "%.")
