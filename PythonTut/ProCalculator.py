#Use float if you want the input toio be a number

num1 = float(input("Enter First Number: "))
op = input("Enter operator")
num2 = float(input("Enter Third Number: "))

if op == "+":
    print(num1+num2)

elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator")