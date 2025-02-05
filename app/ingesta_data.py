import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion import conexion_bd
from scraper import obtener_resenias

def insertar_resenias():

    resenias = obtener_resenias()
    conex = conexion_bd()
    cursor = conex.cursor()

    for nombre, precio, rating, resenia in resenias:
        cursor.execute(
            "INSERT INTO resenias (NombreProducto, Precio, Rating, Resenia) VALUES (?, ?, ?, ?)",
            (nombre, precio, rating, resenia)
        )

    conex.commit()
    cursor.close()
    conex.close()

    print('Datos insertados correctamente.')

if __name__ == '__main__':
    insertar_resenias()