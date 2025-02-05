from flask import Flask, jsonify
from conexion import conexion_bd

app = Flask(__name__)

@app.route('/resenias', methods = ['GET'])

def obtener_todas_las_resenias():
    conn = conexion_bd
    cursor = conn.cursor()
    cursor.execute("SELECT NombreProducto, Precio, Rating, Resenia FROM Resenia")
    resenias = cursor.fetchall()
    cursor.close()
    conn.close()

    resultados = [{'NombreProducto': row[0], 'Precio': row[1], 'Rating': row[2], 'Resenia': row[3]} for row in resenias]

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug = True)