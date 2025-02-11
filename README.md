<h1 aling = "center"> API de Reseñas deon Flask y Web Scraping</h1>

> **Versión 1.0** - Última actualización: 11/02/2025

---

## Descripción del proyecto.

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