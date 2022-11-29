import os 
commando=str(input("digite el nombre que va regristrar"))
command_line='sudo useradd'+commando
linea=str(command_line)
os.system(linea)
rta='C:\Users\CRISTIAN\Documents\CRISTIAN R\Orientada a objetos\python\Descargas'+commando
rta_at=str('sudo mkdir'+rta)
os.system(rta_at)
permisos='sudo chown '+commando+':'+commando+" -R "+rta
permisos_a=str(permisos)
os.system(permisos_a)
os.system('cat /etc/passwd')
os.system('ls -lh')
print("crear usuario, le asignamos una carpeta "+rta)
