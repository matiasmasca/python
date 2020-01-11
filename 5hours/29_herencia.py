
# definimos un monton de atributos y funciones en una clase
# la herencia nos permite hacer uso de esos atributos y fucniones
# version 1
class Cocinero:
  def hacer_pollo(self):
    print("El Cocinero hizo un pollo.")

  def hacer_ensalada(self):
    print("El Cocinero hizo una ensalada.")

  def hacer_plato_del_dia(self):
    print("El Cocinero hizo un alto guiso.")



miCocinero = Cocinero()
# miCocinero.hacer_pollo()
# miCocinero.hacer_ensalada()


""" version 2
# queremos hacer un cocinero de comida china
# que tendra sus cosas en comun con un cocinero, pero no todo y puede tener sus propias recetas

class CocineroChino:
  def hacer_pollo(self):
    print("El Cocinero hizo un pollo.")

  def hacer_ensalada(self):
    print("El Cocinero hizo una ensalada.")

  def hacer_plato_del_dia(self):
    print("El Cocinero hizo pato a la naranja.")

  def hacer_arroz_frito(self):
    print("El Cocinero hizo arroz frito.")


miCocineroChino = CocineroChino()
miCocineroChino.hacer_pollo()
miCocineroChino.hacer_plato_del_dia()
miCocineroChino.hacer_arroz_frito()

# el problema es que estoy repitiendo codigo

"""

# En mi cocinero chino quiero poder ocupar lo que hace un cocinero común
class CocineroChino(Cocinero):
  def hacer_arroz_frito(self):
    print("El Cocinero hizo arroz frito.")

  def hacer_plato_del_dia(self):
    print("El cochinero hizo alto guiyo")

miCocineroChino = CocineroChino()
miCocineroChino.hacer_pollo()
miCocineroChino.hacer_arroz_frito()
miCocineroChino.hacer_plato_del_dia() # sobre-escribir la funcion del padre...
