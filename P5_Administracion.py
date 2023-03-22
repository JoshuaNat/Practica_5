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

def primer_ajuste(lista):
    mem_temp = MEMORIA.copy()
    list_temp = lista.copy()
    while list_temp:
        tam_bloque = 0
        pro_actual = list_temp.pop(0)
        for i in range(len(mem_temp)):
            if pro_actual.tam <= mem_temp[i]:
                tam_bloque = mem_temp[i]
                mem_temp[i] = 0
                break
        if tam_bloque != 0:
            print(f"El proceso {pro_actual.nombre} de {pro_actual.tam}kb se acomodó en el bloque de {tam_bloque}kb")
        else:
            print(f"El proceso {pro_actual.nombre} de {pro_actual.tam}kb no pudo colocarse en memoria")

def mejor_ajuste(lista):
    mem_temp = MEMORIA.copy()
    list_temp = lista.copy()
    indices = []
    while list_temp:
        tam_bloque = 0
        pro_actual = list_temp.pop(0)
        res = -1
        for i in range(len(mem_temp)):
            if pro_actual.tam <= mem_temp[i] and i not in indices:
                if res == -1:
                    tam_bloque = mem_temp[i]
                    res = tam_bloque - pro_actual.tam
                    index = i
                else:
                    if mem_temp[i] - pro_actual.tam < res:
                        tam_bloque = mem_temp[i]
                        res = tam_bloque - pro_actual.tam
                        index = i   
        indices.append(index)
        if tam_bloque != 0:
            print(f"El proceso {pro_actual.nombre} de {pro_actual.tam}kb se acomodó en el bloque de {tam_bloque}kb")
        else:
            print(f"El proceso {pro_actual.nombre} de {pro_actual.tam}kb no pudo colocarse en memoria")

def peor_ajuste(lista):
    mem_temp = MEMORIA.copy()
    list_temp = lista.copy()
    indices = []
    while list_temp:
        tam_bloque = 0
        pro_actual = list_temp.pop(0)
        res = -1
        for i in range(len(mem_temp)):
            if pro_actual.tam <= mem_temp[i] and i not in indices:
                if res == -1:
                    tam_bloque = mem_temp[i]
                    res = tam_bloque - pro_actual.tam
                    index = i
                else:
                    if mem_temp[i] - pro_actual.tam > res:
                        tam_bloque = mem_temp[i]
                        res = tam_bloque - pro_actual.tam
                        index = i   
        indices.append(index)
        if tam_bloque != 0:
            print(f"El proceso {pro_actual.nombre} de {pro_actual.tam}kb se acomodó en el bloque de {tam_bloque}kb")
        else:
            print(f"El proceso {pro_actual.nombre} de {pro_actual.tam}kb no pudo colocarse en memoria")

def sig_ajuste(lista):
    mem_temp = MEMORIA.copy()
    list_temp = lista.copy()
    cont = 0
    while list_temp:
        tam_bloque = 0
        pro_actual = list_temp.pop(0)
        for i in range(len(mem_temp)):
            if cont > len(mem_temp):
                cont = 0
            if pro_actual.tam <= mem_temp[cont]:
                tam_bloque = mem_temp[cont]
                mem_temp[cont] = 0
                cont = i + 1
                break
            else:
                cont = i + 1
        if tam_bloque != 0:
            print(f"El proceso {pro_actual.nombre} de {pro_actual.tam}kb se acomodó en el bloque de {tam_bloque}kb")
        else:
            print(f"El proceso {pro_actual.nombre} de {pro_actual.tam}kb no pudo colocarse en memoria")


def menu():
    while True:
        procesos = lista_procesos("archivos.txt")
        print("Seleccione un algoritmo")
        print("1)Primer ajuste\n2)Mejor ajuste\n3)Peor ajuste\n4)Siguiente ajuste\n5)Salir")
        opcion = int(input("Ingrese un numero"))
        if opcion == 1:
            primer_ajuste(procesos)
        elif opcion == 2:
            mejor_ajuste(procesos)
        elif opcion == 3:
            peor_ajuste(procesos)
        elif opcion == 4:
            sig_ajuste(procesos)
        elif opcion == 5:
            break
        else:
            print("Ingrese un valor valido")

menu()