import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify
from conexion import conexion_bd

app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    return obtener_todas_las_resenias()


@app.route('/resenias', methods = ['GET'])

def obtener_todas_las_resenias():
    conn = conexion_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT NombreProducto, Precio, Rating, Resenia FROM Resenias")
    resenias = cursor.fetchall()
    cursor.close()
    conn.close()

    resultados = [{'NombreProducto': row[0],
                   'Precio': row[1],
                   'Rating': row[2],
                   'Reseña': row[3]}
                   for row in resenias]
    
    return jsonify(resultados)
    
if __name__ == '__main__':
    app.run(debug = True)