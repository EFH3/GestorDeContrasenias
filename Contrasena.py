from Conexion import *  

def registrar(nombre, url , username, password, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO contrasenas(nombre, url , username,
            password, descripcion) VALUES (?,?,?,?,?)'''
        datos = (nombre, url , username, password, descripcion)
        cursor.execute(sentencia_sql,datos)
        conexion.commit()
        conexion.close()
        return 'Registro Correcto'
    except Error as err:
        return 'Ha ocurrido un error '+ str(err)

def mostrar():
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'SELECT * FROM contrasenas'
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        print('Ha ocurrido un error '+ str(err))
    return datos

def buscar(id):
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'SELECT * FROM contrasenas WHERE id = ?'
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        print('Ha ocurrido un error '+ str(err))
    return datos

def modificar(nombre, url , username, password, descripcion, id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''UPDATE contrasenas SET Nombre=?, Url=?, Username=?,
            Password=?, Descripcion=? WHERE Id=?'''
        datos = (nombre, url , username, password, descripcion, id)
        cursor.execute(sentencia_sql,datos)
        conexion.commit()
        conexion.close()
        return 'La contraseña se actualizo correctamente'
    except Error as err:
        return('Ha ocurrido un error '+ str(err))

def eliminar(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''DELETE FROM contrasenas WHERE Id = ?'''
        cursor.execute(sentencia_sql, (id,))
        conexion.commit()
        conexion.close()
        return 'Se elimino la contraseña'
    except Error as err:
        return('Ha ocurrido un error '+ str(err))