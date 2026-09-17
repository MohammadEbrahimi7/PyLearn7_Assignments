seconds = int(input("enter yur seconds: "))

hours = 0
minutes = 0

while seconds >= 3600:
    hours += 1
    seconds -= 3600

while seconds >= 60:
    minutes += 1
    seconds -= 60

print("time: ")
print("hours", hours, "minutes", minutes, "secnds", seconds)