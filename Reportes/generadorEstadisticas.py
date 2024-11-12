import matplotlib.pyplot as plt
from datetime import datetime, timedelta

import os
import sys

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from Persistencia.databaseSingleton import DatabaseSingleton 

db = DatabaseSingleton()

def prestamos_vencidos():
    query = """
    SELECT prestamos.id_prestamo, usuarios.nombre, usuarios.apellido, libros.titulo, prestamos.fecha_prestamo, prestamos.fecha_devolucion
    FROM prestamos
    JOIN usuarios ON prestamos.id_usuario = usuarios.id_usuario
    JOIN libros ON prestamos.isbn = libros.isbn
    WHERE prestamos.fecha_devolucion < DATE('now') AND prestamos.devuelto = 0;
    """
    return db.fetch_query(query)

def libros_mas_prestados_ultimo_mes():
    fecha_hace_un_mes = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    query = """
    SELECT libros.titulo, COUNT(prestamos.id_prestamo) AS cantidad
    FROM prestamos
    JOIN libros ON prestamos.isbn = libros.isbn
    WHERE prestamos.fecha_prestamo >= ?
    GROUP BY libros.isbn
    ORDER BY cantidad DESC
    LIMIT 5;
    """
    return db.fetch_query(query, (fecha_hace_un_mes,))

def usuarios_con_mas_prestamos():
    query = """
    SELECT usuarios.nombre, usuarios.apellido, COUNT(prestamos.id_prestamo) AS cantidad
    FROM prestamos
    JOIN usuarios ON prestamos.id_usuario = usuarios.id_usuario
    GROUP BY usuarios.id_usuario
    ORDER BY cantidad DESC
    LIMIT 5;
    """
    return db.fetch_query(query)

def grafico_libros_mas_prestados():
    data = libros_mas_prestados_ultimo_mes()
    libros = [row[0] for row in data]
    cantidades = [row[1] for row in data]
    
    plt.figure(figsize=(10, 6))
    plt.barh(libros, cantidades, color='skyblue')
    plt.xlabel("Cantidad de Préstamos")
    plt.title("Libros Más Prestados en el Último Mes")
    plt.gca().invert_yaxis()
    plt.savefig("DAO-2024/Reportes/reportes/img/libros_mas_prestados.png")
    plt.close()

def grafico_usuarios_mas_prestamos():
    data = usuarios_con_mas_prestamos()
    usuarios = [f"{row[0]} {row[1]}" for row in data]
    cantidades = [row[2] for row in data]
    
    plt.figure(figsize=(10, 6))
    plt.barh(usuarios, cantidades, color='coral')
    plt.xlabel("Cantidad de Préstamos")
    plt.title("Usuarios con Más Préstamos")
    plt.gca().invert_yaxis()
    plt.savefig("DAO-2024/Reportes/reportes/img/usuarios_mas_prestamos.png")
    plt.close()
