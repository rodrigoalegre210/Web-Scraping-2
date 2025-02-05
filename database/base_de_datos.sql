CREATE DATABASE MercadoLibreDB;

USE MercadoLibreDB;

CREATE TABLE resenias (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    NombreProducto NVARCHAR(255),
    Precio NVARCHAR(50),
    Rating NVARCHAR(50),
    Resenia NVARCHAR(MAX)
);