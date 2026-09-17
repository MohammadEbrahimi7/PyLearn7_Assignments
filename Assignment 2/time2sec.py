hours = int(input("enter your hours: "))
minutes = int(input("enter your minutes: "))
seconds = int(input("enter your seconds: "))

total_seconds = 0

for i in range(hours):
    total_seconds += 3600

for i in range(minutes):
    total_seconds += 60

total_seconds += seconds
print("total_seconds:", total_seconds)