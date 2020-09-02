'''
PONCE ARRIETA
KEVIN ALEJANDRO
GRUPO 3
'''



resp= "Si"
while (resp!="No"):
    name=input("Ingrese su nombre: ")
    Dudadifano=int(input("¿Cuantas diferencias entre años desea calcular? "))
    for i in range (1,Dudadifano+1):
        amayor=int(input("Ingrese el año mayor que desea calcular: "))
        amenor=int(input("Ingrese el año menor que desea calcular: "))
        atrans= amayor-amenor
        mesestrans=atrans*12
        print("Hola ",name," la cantidad de meses transcurridos entre ambos años ingresados es: ",mesestrans)
    resp=input("¿Desea ingresar más años a calcular? (Si/No)")

    