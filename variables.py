# -*- coding: utf-8 -*-
#
#Esto es un comentario

"""
esto es un heredoc (comentario)
"""

mensaje = """
esto es un mensaje, neta xd
"""

nombre = "Luis"
apellido = 'Vázquez' #Esta es la preferida

nombre_completo = nombre + ' ' +apellido

print(nombre_completo)


print(len(nombre.upper()))

print(nombre.lower())

print(nombre.upper())

print(nombre.replace('L', 'x'))

#Formateo de cadenas

mensaje_de_saludo = 'hola soy %s' % nombre

print(mensaje_de_saludo)



#######################################


nombre_dado = input("dime tu nombre: ")

longitud_nombre = 'hola la longitud de tu nombre es de %s letras' % len(nombre_dado)

if len(nombre_dado)>10:
    print("su nombre es demasiado largo, ingrese uno más corto")
    nombre_dado = input("dime tu nombre: ")

if len(nombre_dado)<=10:
    print(longitud_nombre)
