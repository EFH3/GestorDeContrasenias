import hashlib ##Se utiliza para encriptar las contraseñas de la app
from Conexion import *

def comprobar_usuario(): #Este metodo se utilizara para verificar q exista el usuario
    conexion = conectar()
    cursor = conexion.cursor()
    sentencia_sql = 'SELECT * FROM usuarios'
    cursor.execute(sentencia_sql)
    usuario_encontrado = cursor.fetchall()  ##esta variable va almacenar todo lo que encuentre mi cursor
    conexion.close()
    return usuario_encontrado

def registrar(nombre, apellido, edad, contrasena_maestra): ##Creacion del usuario con contraseña
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'INSERT INTO usuarios (Nombre,Apellido,Edad,Contrasena_maestra) VALUES (?,?,?,?)'
        cm_cifrada = hashlib.sha256(contrasena_maestra.encode('utf-8')).hexdigest() #se crea contraseña encriptada por metodo sha256 codificado con utf-8 y hexadecimal
        datos = (nombre,apellido,edad,cm_cifrada)
        cursor.execute(sentencia_sql,datos)
        conexion.commit()
        conexion.close()
        return 'Registro correcto'
    except Error as err:
        return 'Ha ocurrido un error '+str(err)

def comprobar_contrasena(id, contrasena_maestra): #funcion o metodo para comprobar que la contraseña es correcta
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'SELECT * FROM usuarios WHERE Id = ? AND Contrasena_maestra = ?'
        cm_cifrada = hashlib.sha256(contrasena_maestra.encode('utf-8')).hexdigest() #Encriptar contraseña
        cursor.execute(sentencia_sql,(id,cm_cifrada))
        c_encontrada = cursor.fetchall() #Se pasa el registro con la c_encontrada encriptada
        conexion.close
        return c_encontrada
    except Error as err:
        return 'Ha ocurrido un error ' + str(err)

# print(comprobar_usuario())
# print(registrar('EVER','FIERRO','25','33333'))
# print(comprobar_usuario())
print(comprobar_contrasena(1,'33333'))

