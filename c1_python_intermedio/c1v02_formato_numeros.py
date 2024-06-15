# Dar formato como número entero
a = 'amigo{:.0f}'.format(2.5)+'{:0<5}'.format(2.5)
print(a)

# Dar formato como número decimal 
print('{:.2f}'.format(2.8))
print('{:.2f}'.format(2.888888))

# Dejar ceros a al izquierda = >>>>>
print('{:0>5}'.format(.5))

# Dejar ceros a al derecha = <<<<<
print('{:0<5}'.format(2.5))

# Separador de miles con coma
print('{:,}'.format(1000000))

# Dar formato usando f-string
print(f'{2.5:.2f}')

