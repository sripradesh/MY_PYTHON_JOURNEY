# Write a program to print the square of a given integer number.

num=int(input('Enter the number to find its square: '))
result = num*num
print(f"The square of {num} is {result}")

# Write a program to find the product of two float numbers.

num1=float(input('Enter the Number to Multiply: '))
num2=float(input('Enter the Number to get the answer: '))
result=num1*num2
print(f"The answer is {result}")

# Write a program to find the area of a rectangle.

length=float(input('Enter the value of length: '))
Width=float(input('Enter the value of width: '))
area=length*Width
print(f"Area of rectangle is: {area}")

# Write a program to reverse the given string.

user_string=input('Enter the string to reverse: ')
reveresed_string=user_string[::-1]
print(f'{user_string} is reversed as {reveresed_string}')

# Write a Program to find the sum, difference, product and division.Between
# 2 integer numbers.

num1=int(input('Enter the number: '))
num2=int(input('Enter the number: '))
sum=num1+num2
difference=num1-num2
product=num1*num2
division=num1/num2
print(f"The answer is: sum:{sum}\n difference:{difference}\n product:{product}\n division:{division}")

# Write a program to find the simple interest.

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time period (in years): "))
simple_interest=(principal * rate * time) / 100
print(f'The simple interest is: {simple_interest}')

# Write a program to calculate area of triangle

base=float(input('Enter the base value: '))
height=float(input('Enter height value: '))
area_of_triangle= 0.5 * base * height
print(f'area of given triangle is: {area_of_triangle}')

# Write a Python code to swap two variables.

variable1 = 5
variable2 = 10
temp_variable = variable1
variable1 = variable2
variable2 = temp_variable
print("a:", variable1)
print("b:", variable2)

# Write a Python program to calculate the square root of a given number

import math
num = float(input('Enter the value to find the square root: '))
square_root = math.sqrt(num)
print(f'The square root of {num} is:{square_root}')

# Write a Python program to find the area of a circle.

import math
radius = float(input('Enter the 56radius of circle: '))
area_of_circle= math.pi * radius ** 2
print(f' The area of circle for given radius ({radius}) is: {area_of_circle}')