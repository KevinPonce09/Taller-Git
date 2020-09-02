'''
PONCE ARRIETA
KEVIN ALEJANDRO
GRUPO 3
'''

#------------------------------------------listas--------------------------------------------
Planetas = ['Venus','Marte','Tierra','Jupiter']
print(Planetas)

Planetas.append('Saturno')
print(Planetas)

Planetas.append('Saturno')
Planetas.count('Saturno')
print(Planetas)

Planetas.sort()
print(Planetas)

del(Planetas[0])
del(Planetas[1])
del(Planetas[2])
del(Planetas[3])
del(Planetas[4])
del(Planetas[5])

print(Planetas)

#--------------------------------------Diccionarios-------------------------------------------------
DaftPunk = {
    'id' : 55555,
    'nombre' : 'DAFT PUNK',
    'Album':'Intersella5555',
    'Best Song Album' : 'Digital Love'
}
print(DaftPunk)

DaftPunk['Secon Song'] = 'Face to Face'
print(DaftPunk)

eliminar = DaftPunk.pop('Second Song')
print(DaftPunk, '\n')
print('Dato eliminado', eliminar)

 
DaftPunk['Best Song Album'] = 'One More Time'
print(DaftPunk)


print(DaftPunk.get('id','el id que busca no existe'))