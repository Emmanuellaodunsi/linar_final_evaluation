'''FINAL EVALUATION
PYTHON PROGRAMMING LANGUAGE
DURATION: 1:30 MINS
Instructions: Answers 8 questions, Number 10 is compulsory. 
Remember, this evaluation has a lot to do with your certification.'''

#1.	Variable Data Types 

#a. Create a variable called "Date_Of_Birth" and assign it the year you were born (or any random year) using the right datatype. Print the value of the variable. 

Birth_year=2004
current_year=2023
age=current_year-Birth_year
print(age)
#b.What is the difference between an integer and a floating-point number in Python? Backup your explanation with an example for each.
'''Integer is a type of data type with whole numbers.....To use integer in python we use the int()function..... it is best used in mathematical operations
Examples are: 10, 45, 142, 1000'''
'''floating-point numbers:these are numbers with decimal points
example: height=6.7, score_percentage= 76.3...etc...To use floating-point numbers in python we use the float() function.''' 
#2.	Basic Operations 
#a.Write a Python program that adds two numbers together and prints the result.
'''def sum(first_value=int(input("Enter the first value:\n")),Second_value=int(input("Enter the second value:\n"))):
    add=first_value+Second_value
    print(add)'''

#b. Write a Python program that takes a number as input and multiplies it by 10. Print the result.

value=int(input("Enter the value:\n"))
mul=value*10
print(mul)
    

#3.	Control Structures 
#a. Write a Python program that checks if a number is even or odd. If the number is even, print "Even", otherwise print "Odd". 
value=range(2,10000,2) #Range for the even numbers
numbers=int(input('Enter number: '))
if numbers in value:
    print('Even')
else:
    print('Odd')

#b. Write a Python program that takes a number as input and checks if it is positive, negative, or zero. Print the result.
number1=input('Enter number: ')
if number1=='0': 
    print('Input was 0')
elif number1.startswith('-')==True:
    print('Negative number')
elif number1.startswith('+')==True:
    print('Positive number')
elif number1.startswith('')==True:
    print('Positive number')
else:
    print('input numbers only.')

#4.	Lists and Loops 
#a. Create a list of numbers from 1 to 10. Print each number in the list using a loop.
list=[1,2,3,4,5,6,7,8,9,10] #A list from 1 to 10
for num2 in list: #Iterate between the numbers
    print(num2) #printing the numbers

#b. Write a Python program that takes a list of numbers as input and returns the sum of all the numbers in the list.
num=[1,2,3,4,5,5]
def num():
    '''iterate all numbers and them together'''
    num1=0
    for num in num1:
        num1+=num 
    return num1
print("Addition to the number is:",num())
#c. Create a dictionary ‘colleague_name’ storing all your colleague names. Hint: Use sequence of numbers as their key.  

#5.	Functions 
#a. Write a Python function that takes three numbers as input and return their multiplication. 
#b. Write a Python function that takes a list of numbers as input and returns the average of all the number
#6.	Libraries and Modules 
#a. Install and Import the "math" module and use its "sqrt" function to calculate the square root of a number. 
import math as mt
number=float(input('Input number: '))
print(mt.sqrt(number))


#b. Install and Import the "random" module and use its "randint" function to generate a random number between 1 and 10.
import random as ran
print(ran.randint(1,10))

#c. Install and Import the "pywhatkit" module and use its "whatsapp" function to send a DM to your tutor with the body “Good Day Sir”
import pywhatkit as pyw
pyw.sendwhatmsg_instantly('+2349023459712','Good Day Sir',15,False)

#7.	 Explain the following terms relating to Python programming Language with examples where needed
'''escapesequence(\):this can be used to execute certain actions in a python code'''
'''example:the (\n) can be used to create a new line'''
'''( it goes to the next line) when you input \n in your python code '''
'''keyword: are built in words in python programming that have assigned functions.''' 
'''datatypes: we have three major datatypes  string, float and integer...They all have different modes of execution.
the string datatype are words and must be put in quotes("")
the float datatype are  numbers with decimal point(6.9)
the integer datatype are datas with whole numbers(4)'''
'''dictionary are set of variables that consist of keys and values. dictionary can be changed/edited.'''
'''modules can be defined as '''
'''interpreters can be explained as a part of the computer system that helps to translate high level languages to low level languages.
high level languages are word/english-like languages that we humans understand
low level languages are machine language ( binary numbers(1,0)) that only the computer understand'''

#8.	Give a brief history of python, who built it, what led to Python and others, state the current version of python you are using.


'''python was created by Guido van rossum
Python was first launched in december in the year 1989
and the version 0.9 was launched in 1990 before version 1 was launched in 1991.....his plan was to create a programming language as simple as ABC...
that is why the python project was called the ABC language because him and 3 junior students(his colleague)
wanted the programming language to be understandable by anyone who want to study python.
The juniors couldn't do it on their own thats why they went to team with Guido to help.
Along the line the students gave up due to some issue and moved on with their lives
but guido was so interested in it that he never relented.
The name "python" was gotten from a 1970's bbc comedy show, his favourite show
The current version of python this year 2023 is python 3.11.2
'''
#9.	Mentions some tools used the career listed below, write extensively on the career you are choosing after this course. Explain what the career entails and the problem skilled professionals in the career solve in the real-world market.
#a.	Data Scientist
#b.	Software Engineer
#c.	Data Engineer
#d.	Data Analytics
#e.	Web Developer (Backend Developer)
#f.	Machine Learning Engineer

#10.	Give a feedback on this Python course, your instructor and this examination.
'''Its been a really good course and was totally worth the time, energy and money....
i actually learnt a lot in just 8 weeks'''
'''On the instructor,Mr habeeblah is really good at teaching, he explains really well
and make sure we all understand what he taught us'''
'''On this examination, the questions are really simple and all the questiona are all based on what we were all taught'''



#BEST OF LUCK










