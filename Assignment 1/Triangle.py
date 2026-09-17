side1 = int(input("enter the first side= "))
side2 = int(input("enter the second side= "))
side3 = int(input("enter the third side= "))

# first + second > third
# second + third > first
# first + third > second

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
     print("a triangle can be formed")
else:
     print("a triangle cannat be formed")