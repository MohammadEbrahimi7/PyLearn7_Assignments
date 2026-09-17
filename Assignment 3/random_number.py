import random

n = int(input("enter n: "))
number = []

for i in range(n):
    x = random.randint(0, 100)

    while x in number:
        x = random.randint(0, 100)

    number.append(x)

print(number)