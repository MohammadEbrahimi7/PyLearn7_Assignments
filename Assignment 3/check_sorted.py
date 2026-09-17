numbers = []
n = int(input("enter n: "))

for i in range(n):
    x = int(input("enter number: "))
    numbers.append(x)
print(numbers)

sorted_array = True

for i in range(n - 1):
    if numbers[i] > numbers[i + 1]:
        sorted_array = False
        break

if sorted_array:
    print("sorted")
else:
    print("not sorted")
