# Para 28_

class Student:
# todo lo que esta identado es parte de la clase
  def __init__(self, name, carrera, promedio, en_aprobacion):
    # una funcion que inicializa la clase y define de alguna manera que valores tendrá nuestro alumnos
    # le asignamos valores iniciales a esos valores
    self.name = name
    self.carrera = carrera
    self.promedio = promedio
    self.en_aprobacion = en_aprobacion

  # una funcion que todos los objetos de la clase puedan usar
  # provee un servicio a la clase
  def mantener_beca(self): #dice si un estudiante tiene un promedio alto
    if self.promedio >= 6:
      return True
    else:
      return False
