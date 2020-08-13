#Condicional Simple
'''
if condition:
    pass
else:
    pass

'''

edad =int(input("Edad es: "))

if edad >= 18:
    print("Eres mayor de edad. Puedes ingresar")
else:
    print("Eres menor de edad. No puedes ingresar")

print('**************NOTA DEFINITIVA*************************∖n')

nombre = input("Ingrese su nombre completo: ")
nd = float(input("ingrese su nota definitiva: "))

if nd >= 3:
    print (nombre," Felicidades, has aprobado el modúlo (❁´◡`❁), con una nota de: ",nd)
else:
    print(nombre," Lo siento, no has aprobado el modulo (┬┬﹏┬┬), con una nota de: ",nd)
