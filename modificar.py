# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:40:23 2023

@author: Alumno
"""

import sqlite3
conexion = sqlite3.connect("bdbibliotecaa.db")
cursor = conexion.cursor()
consulta = """ UPDATE EDITORIAL
                SET
                    NOMBRE = 'Editorial Imprenta Unión roxaxna'
                WHERE
                    IDEDITORIAL = 1
            """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
