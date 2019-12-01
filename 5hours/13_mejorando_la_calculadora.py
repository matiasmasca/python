# calculadora elemental
# El usuario ingresa un numero, la operación y otro numero.
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter first number: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
   print(num1 - num2)
elif op == "/":
   print(num1 / num2)
elif op == "*":
   print(num1 * num2)

else:
  print("Operación invalida, ingrese: +, - , /, *")
