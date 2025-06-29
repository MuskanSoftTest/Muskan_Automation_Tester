# BMI Calculator

# Input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculation
bmi = weight / (height ** 2)

# Output BMI
print("Your BMI is: {:.2f}".format(bmi))

# Determine category
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
