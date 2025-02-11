<h1 align = "center"> API de Reseñas deon Flask y Web Scraping</h1>

> **Versión 1.0** - Última actualización: 11/02/2025

---

## Descripción del Proyecto.

Este proyecto permite **extraer reseás de productos de MercadoLibre** usando Web Scraping con
**BeautifulSoup** y almacenar la información en **SQL Server**. Posteriormente, expone estos datos
a través de una **API REST** hecha en **Flask**.

**Funcionalidades principales:**
- Obtención de **reseñas de productos** mediante **Web Scraping**.
- Almacenamiento de datos en **SQL Server**.
- API con Flask para consultar las reseñas en formato **JSON**.

---

## Tecnologías usadas.

| Tecnología | Descripción |
|------------|-------------|
| **Python** | Lenguaje principal para scraping y API|
| **Flask** | Framework para la API REST |
| **Beautiful Soup** | Librería para Web Scraping |
| **SQL Server** | Base de datos relacional |
| **PyODBC** | Conector para interactuar con SQL Server |

---

## Base de Datos SQL Server.

Principalmente hay que tener **SQL Server** instalado y configurado.

>[!IMPORTANT]
>La configuración de la conexión a la base de datos puede variar dependiendo del sistema operativo,
>la versión de SQL Server, y el método de autenticación.

1. **Creación de la Base de Datos**

Para este proyecto hay que crear una base de datos y una tabla compatible con los datos a scrapear:

```sql
CREATE DATABASE MercadoLibreDB;

USE MercadoLibreDB;

CREATE TABLE resenias (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    NombreProducto NVARCHAR(255),
    Precio NVARCHAR(50),
    Rating NVARCHAR(50),
    Resenia NVARCHAR(MAX)
);

```

>[!TIP]
>Si ya tenés una base de datos con otro nombre, cambia la configuración en `conexion.py`

2. **Explicación del Archivo 'conexion.py'**

Este archivo maneja la conexión con **SQL Server** usando PyODBC.

*El archivo fue eliminado del repositorio por protección de credenciales.*

```python
import pyodbc

# Configuración de la base de datos.
BD_CONFIGURACION = {
    'server': 'TU_SERVIDOR',
    'database': 'MercadoLibreDB', # O el nombre de tu base de datos.
}

# Establecemos una conexión a la base de datos SQL Server y la devuelve.
def conexion_bd():

    conexion = (
        "DRIVER={ODBC Driver 17 for SQL Server};" # Especifica el driver de conexión.
        "SERVER=TU_SERVIDOR;" # Nombre del servidor (modificar según tu configuración)
        "DATABASE=MercadoLibreDB;" #Nombre de la base de datos.
        "Trusted_Connection=yes;" # Usar autenticación de Windows (modificar si es necesario)
        "TrustServerCertificate=yes;" # Evita problemas de certificados SSL en entornos locales.
    )

    return pyodbc.connect(conexion)

```

>[!IMPORTANT]
>Si usas autenticación con usuario y contraseña, cambia la linea `Trusted_Connection=yes;` por:
>```python
>"UID=tu_usuario;PWD=tu_contraseña;"
>```