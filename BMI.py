weight = int(input("enter your weight= "))
height = int(input("enter your height= "))

bmi = (weight / height) **2
print(bmi)

if bmi < 18.5:
    print("underweight")
elif 18.5>bmi>24.9:
    print("normal weight")
elif 25>bmi>29.9:
    print("overweight")
elif bmi>30:
    print("obese")