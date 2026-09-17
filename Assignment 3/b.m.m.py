a = int(input("enter a: "))
b = int(input("enter b: "))

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        b_m_m = i

print(b_m_m)
