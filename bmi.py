#create a program that calculates your bmi

height=float(input("enter your height in m: "))
weight=float(input("enter your weight in kg: "))

bmi=weight/(height*height)

if bmi < 18.5:
    print(f"Your BMI is {bmi} underweight.")
elif bmi >= 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi} healthy.")
elif bmi >= 25 and bmi <= 30:
    print(f"Your BMI is {bmi} overweight.")
else:
    print(f"Your BMI is {bmi} obese.")


