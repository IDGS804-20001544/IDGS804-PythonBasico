
miDiccionario={"Matricula":123456,"Apellidos":"Cardiel"}

'''Agregar un campo y valor al diccionario'''
print(miDiccionario["Apellidos"])
miDiccionario["Materia"]="DMP"
print(miDiccionario)

'''Modificar un valor'''
miDiccionario["Matricula"]=98765
print(miDiccionario)

'''Eliminar ese elemento del diccionario'''
del miDiccionario["Apellidos"]
print(miDiccionario)