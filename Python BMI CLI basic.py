print("Welcome to BMI Calculator")
weight = int(input("Your weight in pound? \n"))
height = float(input("Your height in feet imches? \n"))
bmi = weight / (height ** 2)
print(round(bmi, 2))
if bmi == 29.9:
   print("overweight")
elif bmi <= 25:
   print("normal weight")
elif bmi == 18.5:
       print("normal weight")
elif bmi < 18.5:
    print("underweight")
else:
    print("BMI Error Cal")



    