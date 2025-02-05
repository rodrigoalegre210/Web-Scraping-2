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

                        nombre_producto = producto_soup.find('h1', class_ = 'ui-pdp-title')
                        precio_producto = producto_soup.find('span', class_ = 'andes-money-amount__fraction')
                        rating_producto = producto_soup.find('span', class_ = 'ui-pdp-review__rating')
                        resenia_producto = producto_soup.find_all('p', class_ = 'ui-review-capability-comments__comment__content')

                        nombre_producto = nombre_producto.text.strip() if nombre_producto else 'Sin nombre'
                        precio_producto = precio_producto.text.strip() if precio_producto else 'Sin precio'
                        rating_producto = rating_producto.text.strip() if rating_producto else 'Sin rating'

                        for resenia in resenia_producto:
                            texto_resenia = resenia.text.strip()
                            resenias_individuales.append((nombre_producto,
                                                         precio_producto,
                                                         rating_producto,
                                                         texto_resenia))
                            
    return resenias_individuales