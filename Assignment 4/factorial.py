number = int(input("enter a number: "))

x = 1
factorial = 1

while factorial < number:
    x = x + 1
    factorial = factorial * x

if factorial == number:
    print("yes")
else:
    print("no")