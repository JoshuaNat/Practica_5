class Proceso:
	"""Una clase simple para almacenar procesos"""

	def __init__(self, nombre, tam):
		"""Inicializa los atributos de la clase"""
		self.nombre = nombre
		self.tam = tam


#Memoria
MEMORIA = [1000, 400, 1800, 700, 900, 1200, 1500]

def lista_procesos(filename):
	"""Funcion para obtener la lista de procesos"""
	lista = []
	with open(filename) as file_obj:
		for procesos in file_obj:
			datos = procesos.split(',')
			nombre = datos[0]
			tamano = datos[1].strip()
			tam_num = int(tamano[:-2])
			lista.append(Proceso(nombre, tam_num))
	return lista

def menu():
	procesos = lista_procesos("archivos.txt")
	for obj in procesos:
		print(obj.tam)

menu()