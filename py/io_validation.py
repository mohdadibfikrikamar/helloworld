## IO validation

# name = str(input("Enter your name: "))
# height = float(input("Enter your height in meters: "))

# # Input validation

# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age > 0:
#          break
#         else:
#                     print("Age must be positive!")
#     except ValueError:
#         print("Invalid input! Please enter a valid age.")

# # Output validation
# print(f"Hello, {name.upper()}! You are {age} years old and \n your height is {height} meters.")

# Exercise 1
# user input 2 numbers
# User choose operation

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

while True:
    if operation == "+":
         result = x + y
         break
    elif operation == "-":
         result = x - y
         break
    elif operation == "*":
         result = x * y
         break
    elif operation == "/":
         if y != 0:
             result = x / y
             break
         else:
             print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation! Please choose a valid operation.")
        operation = input("Choose operation (+, -, *, /): ")

## Output results
print(f"The results for {x} {operation} {y} is: {result}. \n")

## Excercise 2
# Quiz of 3 questions , at the end of the quiz, display the score and percentage of correct answers.

score = 0
print("Welcome to the quiz! Please answer the following questions:\n")
print("Question 1: What is the capital of France?")
answer1 = input("Your answer: ")
if answer1.lower() == "paris":
     score += 1

print("Question 2: What is the largest animal in the world?")
answer2 = input("Your answer: ")
if answer2.lower() == "blue whale" or answer2.lower() == "whale":
     score += 1

print(f"Your score is {score}.")
print(f"Your percentage of correct answers is {(score/2)*100}%.")