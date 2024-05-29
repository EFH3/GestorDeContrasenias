import os
from getpass import getpass 
from tabulate import tabulate 
from Conexion import * 
import Usuario
import Contrasena

conexion = conectar()
crear_tablas(conexion)

def inicio():
    os.system('cls')
    comprobar = Usuario.comprobar_usuario()
    if len(comprobar) == 0:
        print('Bienvenido, registre su informaión...')
        nombre = input('Ingrese su nombre: ')
        apellido = input('Ingrese su apellido: ')
        edad = input('Ingrese su edad: ')
        contrasena_maestra = getpass('Ingrese su contraseña administrador: ')
        respuesta = Usuario.registrar(nombre, apellido, edad, contrasena_maestra)
        if respuesta == 'Registro correcto':
            print(f'Bienvenido {nombre}')
            menu()
        else:
            print(respuesta)
    else:
        n_intentos = 0
        while n_intentos < 3:
            contrasena_maestra = getpass('Ingrese su contraseña maestra: ')
            respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
            if len(respuesta) == 0:
                n_intentos += 1
                print('Contraseña Invalida')
                print('Solo se permiten 3 intentos')
                print('Intento ' + str(n_intentos))
            else:
                n_intentos = 3
                print('Bienvenido')
                menu()

def menu():
    while True:
        print('Seleccione una de las siguientes opciones: ')
        print('\t1- Añadir contraseña')
        print('\t2- Visualizar todas las cuentas')
        print('\t3- Visualizar una contraseña')
        print('\t4- Modificar contraseña')
        print('\t5- Eliminar contraseña')
        print('\t6- Salir')
        opcion = input('Ingrese una opción: ')
        if opcion == '1':
            nueva_contrasena()
        elif opcion == '2':
            ver_contrasenas()
        elif opcion == '3':
            ver_una_contrasena()
        elif opcion == '4':
            modificar_contrasena()
        elif opcion == '5':
            eliminar_contrasena()
        elif opcion == '6':
            break
        else:
            print('No ingresó una opción válida')

def nueva_contrasena():
    nombre = input('Digite el nombre: ')
    url = input('Digite la url: ')
    username = input('Digite el nombre de usuario: ')
    password = input('Digite la contraseña: ')
    descripcion = input('Ingrese una descripcion: ')
    respuesta = Contrasena.registrar(nombre, url, username, password, descripcion)
    print(respuesta)

def ver_contrasenas():
    datos = Contrasena.mostrar()
    nueva_lista = []
    headers = ['ID', 'NOMBRE', 'URL', 'USERNAME', 'PASSWORD', 'DESCRIPCIÓN']
    for dato in datos:
        convertido = list(dato)
        convertido[4] = '***' 
        nueva_lista.append(convertido)

    tabla = tabulate(nueva_lista, headers, tablefmt='fancy_grid')
    print('\t\t\t\tTodas las contraseñas')
    print(tabla)

def ver_una_contrasena():
    contrasena_maestra = getpass('Ingrese su contraseña maestra: ')
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if len(respuesta) == 0:
        print('Contraseña Invalida')
    else:
        id = input('Digite el id de la contraseña que desea buscar: ')
        datos = Contrasena.buscar(id)
        headers = ['ID', 'NOMBRE', 'URL', 'USERNAME', 'PASSWORD', 'DESCRIPCIÓN'] 
        tabla = tabulate(datos, headers, tablefmt='fancy_grid')
        print('\t\t\t\tTodas las contraseñas')
        print(tabla)

def modificar_contrasena():
    contrasena_maestra = getpass('Ingrese su contraseña maestra: ')
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if len(respuesta) == 0:
        print('Contraseña Invalida')
    else:
        id = input('Ingrese el id de la contraseña que desea modificar: ')
        print('Ok, Ahora ingrese los nuevos datos')
        nombre = input('Nombre: ') 
        url = input('Url: ')
        username = input('Nombre de usuario: ')
        password = input('Contraseña: ')
        descripcion = input('Descripcion: ')
        respuesta = Contrasena.modificar(nombre, url, username, password, descripcion, id)
        print(respuesta)

def eliminar_contrasena():
    id = input('Ingrese el id de la contraseña que desea eliminar: ')
    respuesta = Contrasena.eliminar(id)
    print(respuesta)

# menu()
inicio()