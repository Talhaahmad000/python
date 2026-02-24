# Get weight in kg
weight = float(input("Enter weight in kg: "))

# Ask for height unit
print("Enter height unit: 1 for feet, 0 for meters")
ch = int(input("Enter your choice: "))

# Get height
if ch == 0:
    # Height in meters
    height = float(input("Enter height in meters: "))
elif ch == 1:
    # Height in feet → convert to meters
    feet = float(input("Enter height in feet: "))
    height = feet / 3.28084  # convert feet to meters
else:
    print("Invalid choice")
    exit()

# Calculate BMI
bmi = weight / (height ** 2)

# Print BMI
print(f"Your BMI is {bmi:.2f}")  # .2f to show 2 decimal places

# BMI classification
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You have obesity")
else:
    print("You need to visit hospital for obesity")
