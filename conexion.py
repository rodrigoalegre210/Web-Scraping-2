import pyodbc

BD_CONFIGURACION = {
    'server': 'DESKTOP-637742I',
    'database': 'MercadoLibreDB',
}

def conexion_bd():
    conexion_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-637742I;"
        "DATABASE=MercadoLibreDB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conexion_str)