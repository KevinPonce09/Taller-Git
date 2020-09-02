#mutables
#Dos elementos siempre, llave y valor = key : valor

datosalum = {
    'id' : 12345,
    'nombre' : 'Juan',
    'apellido':'perez',
    'Barrio' : 'Aranjuez',
    'edad': 21
}
print(datosalum)

#Agregar un elemento, key:valor

datosalum['Empresa'] = 'LA CALLE'

print(datosalum)

#imprimir un solo elemento del diccionario
print('Cedula',datosalum['id'])

#pop() eliminar un dato, enviar la key
eliminar = datosalum.pop('Barrio')
print(datosalum, '\n')
print('Dato eliminado', eliminar)
  
#cambiar el valor de un dato 
datosalum['nombre'] = 'Juan Francisco'
print(datosalum)

#get para buscar informaciòn
print(datosalum.get('nombre','el dato no existe'))
