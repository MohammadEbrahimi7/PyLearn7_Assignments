a = int(input("enter a: "))
b = int(input("enter b: "))

for i in range(max(a, b) + 1):
    if i % a == 0 and i % b == 0:
        k_m_m = i
        break

print(k_m_m)