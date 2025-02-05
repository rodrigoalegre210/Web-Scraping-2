import requests

from bs4 import BeautifulSoup

URLs_BASE = [
    'https://www.mercadolibre.com.ar/c/celulares-y-telefonos#menu=categories',
    'https://www.mercadolibre.com.ar/c/computacion#menu=categories',
    'https://www.mercadolibre.com.ar/c/camaras-y-accesorios#menu=categories',
    'https://www.mercadolibre.com.ar/c/electronica-audio-y-video#menu=categories'
]

def obtener_resenias():

    resenias_individuales = []

    for url in URLs_BASE:
        pedido_obtenido = requests.get(url)

        if pedido_obtenido.status_code == 200:
            soup = BeautifulSoup(pedido_obtenido.text, "html.parser")

            enlaces_productos = soup.find_all('a', class_ = 'splinter-link')

            for enlace in enlaces_productos:
                url_producto = enlace.get('href')

                if url_producto and '/p/' in url_producto:
                    producto_pagina = requests.get(url_producto)

                    if producto_pagina.status_code == 200:
                        producto_soup = BeautifulSoup(producto_pagina.text, "html.parser")

                        