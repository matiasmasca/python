# Diccionarios.
# al igual que un diccionario, esta la Palabra, que es la clave y la definción que seria el valor.

# Es una estructura de datos para guardar "clave" "valor"

# las claves tienen que ser unicas

nombre_de_diccionario = {} #curly brackets.

mesesEnPalabras = {
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
print(mesesEnPalabras["Mar"])

# Get, permite definir que valor devuelve si no hay esa clave
print(mesesEnPalabras.get("Nov"))
print(mesesEnPalabras.get("Mat"))
print(mesesEnPalabras.get("Mat", "No es una clave valida"))



