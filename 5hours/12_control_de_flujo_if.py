# sentencia IF
# el programa responde a los datos que tiene, a los valores que se le pasa.
# en el dia a dia, resolvemos este tipo de declaraciones
# donde hay condiciones

# Cuando me levanto
# Si tengo hambre
#   me hago el desayuno

# Cuando salgo de mi casa:
# Si esta nublado
  # llevo un paraguas
# Sino
  # llevo anteojos de sol

# Cuando estoy en un restaurant:
# si Quiero comer carne
  # entonces pido un bife de lomo
# de otra manera, si quiero comer pasta
  # entonces pido ravioles con boloñesa
# Y sino
  # pido una ensalada

# Ahora si, en python

es_humano = False

if es_humano:
  print("Usted es un ser humano")
else:
  print("Usted no es un ser humano")

# Más de una condicion
# OR: uno u otro o ambos
is_male = True
is_tall = True

if is_male or is_tall:
  print("Usted es un hombre o es alto o ambos")
else:
  print("Usted no es un hombre ni alto")


# AND ambos tienen que ser verdadero
is_male = True
is_tall = False

if is_male and is_tall:
  print("Usted es un hombre y es alto")
else:
  print("Usted no es un hombre o no es alto")

# Else if
# AND ambos tienen que ser verdadero
is_male = False
is_tall = True

if is_male and is_tall:
  print("Usted es un hombre y es alto")
elif is_male and not(is_tall):
  print("Usted es un hombre petiso")
else:
  print("Usted no es un hombre o no es alto")

if is_male and is_tall:
  print("Usted es un hombre y es alto")
elif is_male and not(is_tall):
  print("Usted es un hombre petiso")
elif not(is_male) and is_tall:
  print("Usted no es hombre pero es alto")
else:
  print("Usted no es un hombre o no es alto")


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




