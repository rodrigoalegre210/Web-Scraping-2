import pyodbc

BD_CONFIGURACION = {
    'server': 'DESKTOP-637742I\PrancherC',
    'database': 'MercadoLibreDB',
    'username': 'DESKTOP-637742I\PrancherC',
    'password': 'contraseñaSQL1'
}

def conexion_bd():
    conexion = (
        f'DRIVER = {{SQL Server}};'
        f'SERVER = {BD_CONFIGURACION['server']};'
        f'DATABASE = {BD_CONFIGURACION['database']}'
        f'UID = {BD_CONFIGURACION['username']}'
        f'PWD = {BD_CONFIGURACION['password']}'
    )

    return pyodbc.connect(conexion_bd)