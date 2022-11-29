import csv
def llenar(vector, cnt_personas):
    for i in range(cnt_personas):
        vector.append([])
        for j in range(3):
            dato = str(input("Digite el "+vector[0][j]+" de la persona: "))
            vector[i+1].append(dato)


def creando(vector,direccion): 
    #dire = 'C:\Users\CRISTIAN\Desktop' 
    with open(direccion, 'w', newline='')as csvfile:
        lista = [['Código', 'Nombre', 'Apellido'], ['1', 'Pedro', 'Arias'], [
            '2', 'Juan', 'García']]          
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(vector)        
        print("Se ha guardado el archivo")


def leyendo(direccion):  
    # dir='C:\Users\CRISTIAN\Desktop\Untitled-2.py'
     with open(direccion, 'r', newline='')as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:  
            print(row)  

def agregando(direccion,vector): 

    #dire = 'C:\Users\CRISTIAN\Desktop' 
    with open(direccion, 'r', newline='')as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = [line for line in reader]
    with open(direccion, 'w', newline='')as csvfile:
        lista = [['3', 'Jorge', 'Moncada'], ['4', 'Lucas', 'Marulanda']]
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(data)
        writer.writerows(vector)


def eliminando(dire,search):  
    #dire = 'C:\Users\CRISTIAN\Desktop\prueba' 
    with open(dire, 'r', newline='')as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = [line for line in reader]
    with open(dire, 'w', newline='')as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        data.pop(search)
        writer.writerows(data)

x = 0

while (x != 5):
    vector = [['id', 'nombre', 'apellido']]
    print("\n Menu Principal\n Opcion 1: Crear un Archivo Csv \n Opcion 2: Leer un archivo csv \n Opcion 3: Para actualizar un archivo Csv \n Opcion 4: Para buscar y eliminar un dato dentro de un archivo Csv \n Opcion 5: Salir")

    x = (int(input(" seleccione una opcion  :")))

    if (x == 1):

        y = 1

        while (y != 0):

            y = (int(input("\n SubMenu\n   Submenu \n Opcion 1: Llenar lista por teclado \n Opcion 2: Leer lista a guardar en archivo Csv \n Opcion 0: Salir al menu principal \n Opcion a escoger:")))

            if (y == 1):
                cnt_personas = int(input("Digite la cantidad de personas a registrar: "))
                llenar(vector, cnt_personas)
            if(y==2):
                print(vector)
                t=str(input("Quieres guardar este archivo como csv: s=si n=no \n Si deseas sobre escribirlo regrese a el submenu y crea un nuevo vector: "))
                if(t=="s"):
                    ruta=str(input("Digita la ruta en la que se va a guardar el archivo: "))
                    nombre=str(input("Digita el nombre del archivo: "))
                    creando(vector, ruta+"\\"+nombre+'.csv')
    if(x==2):
        dir=str(input("Digita la ruta completa donde se encuentra el archivo a leer: "))    
        leyendo(dir)
    if(x==3):
        dir=str(input("Digita la ruta completa donde se encuentra el archivo a Actualizar: "))
        leyendo(dir)
        cnt_personas = int(input("Digite la cantidad de personas a registrar: "))
        llenar(vector, cnt_personas)
        agregando(dir, vector)
        leyendo(dir)
    if(x==4):
        dir=str(input("Digita la ruta completa donde se encuentra el archivo a editar: "))
        cnt_personas = int(input("Digite la linea de codigo a eliminar: "))
        eliminando(dir,cnt_personas)
    if(x==5):
        print((" Adios vuelva pronto "))
    