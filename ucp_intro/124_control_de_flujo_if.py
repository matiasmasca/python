
# Comparaciones: Operadores de comparación.
# operador de comparacion: >, <, >=, <=, ==, !=

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

resultado = max_num(3,1,9)
print("El mayor es " + str(resultado))




