## Conditional statements
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in centimeters: "))

while weight <= 0 or height <= 0 or weight > 300 or height > 300:
    print("Weight and height must be positive numbers and not exceed 300. Please try again.")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in centimeters: "))

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
        print(f"Your BMI is {bmi:.2f}. You are underweight.")

elif bmi < 25:
        print(f"Your BMI is {bmi:.2f}. You have a normal weight.")

elif bmi < 30:
        print(f"Your BMI is {bmi:.2f}. You are overweight.")

else:
        print(f"Your BMI is {bmi:.2f}. You are obese.")

