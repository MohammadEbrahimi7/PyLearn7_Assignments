name = input("entar student name= ")
family = input("enter student family= ")
grade1 = int(input("enter first grade= "))
grade2 = int(input("enter second grade= "))
grade3 = int(input("enter thrid grade= "))

average = (grade1 + grade2 + grade3) /3
print(average)

if average >=17:
    print("Grate")
elif 17>average>12:
    print("Normal")
elif average <=12:
    print("Fail")