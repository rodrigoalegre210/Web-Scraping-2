import pyodbc

BD_CONFIGURACION = {
    'server': 'DESKTOP-637742I\PrancherC',
    'database': 'MercadoLibreDB',
    'username': 'DESKTOP-637742I\PrancherC',
    'password': 'contraseñaSQL1'
}

def conexion_bd():
    conexion = (
        'DRIVER = {SQL Server};'
        'SERVER =' + BD_CONFIGURACION['server'] + ';'
        'DATABASE =' + BD_CONFIGURACION['database'] + ';'
        'UID =' + BD_CONFIGURACION['username'] + ';'
        'PWD =' + BD_CONFIGURACION['password'] + ';'
    )

    return pyodbc.connect(conexion)