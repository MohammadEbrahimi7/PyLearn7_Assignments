import math
print("wlcome to my calculator")

print("entekhab koni + = bealave mishavad")
print("entekhab koni - = menha mishavad")
print("entekhab koni * = zarb mishavad")
print("entekhab koni / = taghsim mishavad")
print("sin")
print("cos")
print("tan")
print("cot")
print("factorial")
print("please enter your choice and click enter= ")
op = input()

if op == "+" or op == "-" or op == "*" or op == "/":
  a = int(input("please enter your number1: "))
  b = int(input("please enter your number2: "))
else:
  a = int(input("please enter your number1: "))
  
if op == "+":
  result = a + b
if op == "-":
  result = a - b
elif op == "*":
  result = a * b
elif op == "/":
  if b == 0:
    result = "connot divide by ziro"
  else:
    result = a / b

elif op == "sin":
  result = math.sin(a)
elif op == "tan":
  result = math.tan(a)
elif op == "cot":
  result = 1 / math.tan(a)
elif op == "cos":
  result = math.cos(a)
elif op == 0 or op == 1:
  result = 1
else:
  result = math.factorial(a)

print(result)