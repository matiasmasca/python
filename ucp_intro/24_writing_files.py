# veremos como agregar y como escribir nuevas lineas en el archivo.

archivo_empleados = open("23_reading_files_employees.txt", "r")
print(archivo_empleados.read())
archivo_empleados.close()


archivo_empleados = open("23_reading_files_employees.txt", "a") # a de append para agregar al final del archivo

archivo_empleados.write("\nTobby - Human Resources")

archivo_empleados.close()

# Ojo cuando escribirmos, porque es permanente lo que cambiemos.
# Si queremos que salte una linea dbeemos usar el caracter de salto de linea: \n

# Si usamos "w" va a remplazar todo el archivo, en lugar de agregar.
# pero tambien nos sirve para crear un nuevo archivo.

archivo_empleados = open("24_writting_new_files_employees.txt", "w")
archivo_empleados.write("\nKelly - Customer Service")
archivo_empleados.close()
