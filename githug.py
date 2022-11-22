import csv


def llenar(lista, cnt_personas):
    for i in range(cnt_personas):
        lista.append([])
        for j in range(3):
            dato = str(input("Digite el "+lista[0][j]+" de la persona: "))
            lista[i+1].append(dato)


def creando(lista,direccion):  

    """dire = 'C:\\python\\original.csv'"""
    with open(direccion, 'w', newline='')as csvfile:

        """lista = [['Código', 'Nombre', 'Apellido'], ['1', 'Pedro', 'Arias'], [
            '2', 'Juan', 'García']] """ 
        writer=csv.writer(csvfile, delimiter=',')
        writer.writerows(lista) 
        print("Se ha guardado el archivo")


def leyendo(direccion): 
    with open(direccion, 'r', newline='')as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader: 
            print(row)  


def agregando(direccion,lista): 
    "dire = 'D:\\Python\\original.csv' " 
    with open(direccion, 'r', newline='')as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = [line for line in reader]
    with open(direccion, 'w', newline='')as csvfile:
        "lista = [['3', 'Jorge', 'Moncada'], ['4', 'Lucas', 'Marulanda']]"
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(data)
        writer.writerows(lista)


def eliminando(dire,search): 
    "dire = 'C:\\Users\\labservidores\\documentos\\Sistemas_Operativos\\ted.csv' " 
    with open(dire, 'r', newline='')as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data=[line for line in reader]
    with open(dire, 'w', newline='')as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        data.pop(search)
        writer.writerows(data)
        writer.writerows(data)




x = 0

while (x != 5):
    lista = [['id', 'nombre', 'apellido']]
    print("\n Menu Principal\n Opcion 1: Crear un Archivo Csv \n Opcion 2: Leer un archivo csv \n Opcion 3: Para actualizar un archivo Csv \n Opcion 4: Para buscar y eliminar un dato dentro de un archivo Csv \n Opcion 5: Salir")

    x = (int(input(" Opcion a escoger :")))

    if (x == 1):

        y = 1

        while (y != 0):

            y = (int(input("\n SubMenu\n Has entrado al Submenu \n Opcion 1: Llenar lista por teclado \n Opcion 2: Leer lista a guardar en archivo Csv \n Opcion 0: Salir al menu principal \n Opcion a escoger:")))

            if (y == 1):
                cnt_personas = int(input("Digite la cantidad de personas a registrar: "))
                llenar(lista, cnt_personas)
            if(y==2):
                print(lista)
                t=str(input("\n Si deseas sobreescribirlo regresa al submenu y crea un nuevo vector: "))
                if(t=="s"):
                    ruta=str(input("Digita la ruta en la que se va a guardar el archivo: "))
                    nombre=str(input("Digita el nombre del archivo: "))
                    creando(lista, ruta+"\\"+nombre+'.csv')
    if(x==2):
        dire=str(input("Digita la ruta completa donde se encuentra el archivo a leer: "))   
        leyendo(dire)
    if(x==3):
        dir=str(input("Digita la ruta completa donde se encuentra el archivo a Actualizar: "))
        leyendo(dire)
        cnt_personas = int(input("Digite la cantidad de personas a registrar: "))
        llenar(lista, cnt_personas)
        agregando(dire, lista)
        leyendo(dire)
    if(x==4):
        dire=str(input("Digita la ruta completa donde se encuentra el archivo a editar: "))
        cnt_personas = int(input("Digite el id a eliminar: "))
        eliminando(dire,cnt_personas)
    if(x==5):
        print((" Hasta pronto"))