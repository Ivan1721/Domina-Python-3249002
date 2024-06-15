lista_nombres = ["Ana", "Paco", "Javier", "Emilio"] #objeto 1
lista_edades = [25, 27, 25, 26]                     #objeto 2

#                objeto 1       objeto 2
datos_zip = zip(lista_nombres, lista_edades)

print(zip(lista_nombres, lista_edades))
#no se puede visualizar
print(datos_zip)

# Se imprime como lista
print(list(datos_zip)) # lista de 4 tuplas(obejeto iterable con menor cantidad de tuplas)

#numero de valores / de / objeto zip()   
for nombre, edad in zip(lista_nombres, lista_edades):
    print(nombre, edad)

#   Esto no funciona :/
for dato_zip in datos_zip:
    print(nombre, edad)
