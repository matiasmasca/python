# como los hash de ruby, guarda "clave" "valor"
# al igual que un diccionario, esta la Palabra, que es la clave y la definción que seria el valor.

# las claves tienen que ser unicas

nombre_de_diccionario = {} #curly brackets.

monthConversions = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Ago": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dic": "December",
}

# acceder a los valores del diccionario
# hay varias formas
# poner la clave entre brackets
print(monthConversions["Mar"])

# Get, permite definir que valor devuelve si no hay esa clave
print(monthConversions.get("Nov"))
print(monthConversions.get("Mat"))
print(monthConversions.get("Mat", "No es una clave valida"))

# Pueden ser claves pueden ser numericas, y los valores de diferentes tipos
monthConversions = {
  1: ("January", "Enero", "Janeiro"), # un tupla
  2: ["February", "Febrero", "Fevereiro"], #una lista
  3: "March",
  4: "April",
  5: "May",
  6: "June",
  7: "July",
  8: "August",
  9: "September",
  10: "October",
  11: "November",
  12: "December",
}

print(monthConversions[1])
print(monthConversions[1][1])
print(monthConversions[2][2])


