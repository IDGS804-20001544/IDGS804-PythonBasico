
lista1=["Roberto",1,2,23,True]

print(lista1)


print(lista1[:])
print(lista1[2:4])
print(lista1[:2])
print(lista1[3:])

'''Agregar elemento al final de la lista'''
lista1.append("Cardiel")
print(lista1)

'''Agregar elemento de la lista en la posicion indicada'''
lista1.insert(0,"Mario")
print(lista1)

'''Agregar una lista a lista'''
lista1.extend([9,10,11])
print(lista1)

print(lista1.index("Cardiel"))
lista1.remove("Roberto")
print(lista1)

lista1.pop()
print(lista1)