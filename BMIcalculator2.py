w = int(input("weight:"))
h = float(input("height:"))
bmi = w/h**2
bmi_2 = round(bmi, 1)

if bmi_2 < 18.5:
    print(f"Your BMI is {bmi_2}, you are underweight.")
elif bmi_2 < 25:
    print(f"Your BMI is {bmi_2}, you have a normal weight.")
elif bmi_2 < 30:
    print(f"Your BMI is {bmi_2}, you are slightly overweight.")
elif bmi_2 < 35:
    print(f"Your BMI is {bmi_2}, you are obese.")
else:
    print(f"Your BMI is {bmi_2}, you are clinically obese.")
