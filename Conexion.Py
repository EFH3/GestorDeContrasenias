import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conexion = sqlite3.connect('database_gestor.db')
        return conexion
    except Error:
        print('Ocurrio un error al intentar conectar')

def crear_tablas(conexion):
    cursor = conexion.cursor()
    sentencia_sql = '''CREATE TABLE IF NOT EXISTS usuarios(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Apellido TEXT NOT NULL,
        Edad TEXT,
        Contrasena_maestra TEXT NOT NULL
    )'''

    sentencia_sql2 = '''CREATE TABLE IF NOT EXISTS contrasenas(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Url TEXT NOT NULL,
        Username TEXT NOT NULL,
        Password TEXT NOT NULL,
        Descripcion TEXT
    )'''
    cursor.execute(sentencia_sql)
    cursor.execute(sentencia_sql2)
    conexion.commit()
    conexion.close()