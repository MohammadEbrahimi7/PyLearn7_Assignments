n = int(input("enter n: "))

a = 1
b = 1
i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1