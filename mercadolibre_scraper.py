# -*- coding: utf-8 -*-
"""Copia de Evidencia de aprendizaje 1. Análisis y herramientas de extracción de datos"""

import requests
from bs4 import BeautifulSoup

def extraer_precio_mercadolibre(url):
    """Extrae el precio de un producto de Mercado Libre.

    Args:
        url: La URL del producto en Mercado Libre.

    Returns:
        El precio del producto como una cadena de texto.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra el elemento que contiene el precio (ajusta el selector según la estructura de la página)
    precio_elemento = soup.find('span', {'class': 'andes-money-amount__fraction'})

    if precio_elemento:
        precio = precio_elemento.text.strip()
        return precio
    else:
        return "No se encontró el precio"

# URL del producto en Mercado Libre
url_producto = "https://articulo.mercadolibre.com.co/MCO-1350238933-monitor-lg-24-lg-24gn65r-bawp-ultragear-ips-144hz-_JM#polycard_client=search-nordic&position=27&search_layout=stack&type=item&tracking_id=4e7f6e3c-4c7a-48db-9219-6a8190aa9c27"

precio = extraer_precio_mercadolibre(url_producto)
print("Precio:", precio)

# Extraer el título del producto
response = requests.get(url_producto)
soup = BeautifulSoup(response.content, 'html.parser')

# Encuentra el elemento meta con el atributo name="twitter:title"
titulo_elemento = soup.find('meta', {'name': 'twitter:title'})

if titulo_elemento:
    titulo = titulo_elemento['content'].strip()
    print("Título:", titulo)
else:
    print("No se encontró el título")

# Extraer la descripción del producto
# Realiza la solicitud de la página
response = requests.get(url_producto)

# Fuerza la decodificación correcta
content = response.content.decode('utf-8', 'replace')

# Usa BeautifulSoup para analizar el contenido
soup = BeautifulSoup(content, 'html.parser')

# Encuentra el elemento meta con el atributo property="og:description"
descripcion_elemento = soup.find('meta', {'property': 'og:description'})

if descripcion_elemento:
    descripcion = descripcion_elemento['content'].strip()
    print("Descripción:", descripcion)
else:
    print("No se encontró la descripción")
