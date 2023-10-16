# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:34:57 2023

@author: Alumno
"""

import sqlite3
conexion = sqlite3.connect("bdbibliotecaa.db")
cursor = conexion.cursor()
consulta = """ SELECT * 
                FROM LIBRO
                WHERE
                    precio >= 55
                ORDER BY titulo
            """
cursor = conexion.cursor()
cursor.execute(consulta)
libros = cursor.fetchall()
# Acá libros es una lista... entonces utilizamos un for

for libro in libros:
    print(libro)
conexion.close()

# En este caso, vamos a eliminar la editorial de ideditorial = 5

import sqlite3
conexion = sqlite3.connect("bdbibliotecaa.db")
cursor = conexion.cursor()
consulta = """ DELETE FROM EDITORIAL
                WHERE
                    IDEDITORIAL = 5
            """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
