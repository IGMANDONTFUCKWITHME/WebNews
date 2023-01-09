from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def noticias():
    # Hacemos una solicitud a la página web de noticias que queremos scrapear
    respuesta = requests.get('https://www.xataka.com/')
    # Convertimos el contenido de la respuesta en un objeto BeautifulSoup
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    # Buscamos todos los elementos que contienen las noticias en la página web
    noticias = soup.find_all('div', class_='abstract-content')
    # Creamos una lista vacía para almacenar las noticias recopiladas
    lista_noticias = []
    # Recorremos cada uno de los elementos que contienen las noticias
    for noticia in noticias:
        # Extraemos el título, la fecha y la descripción de cada noticia
        titulo = noticia.find('h2', class_='abstract-title').text
        fecha = noticia.find('time', class_='abstract-date').text
        descripcion = noticia.find('div', class_='abstract-excerpt').text
        # Añadimos la noticia a la lista como un diccionario con los datos extraídos
        lista_noticias.append({'titulo': titulo, 'fecha': fecha, 'descripcion': descripcion})
    # Renderizamos la plantilla HTML pasándole la lista de noticias como argumento
    return render_template('noticias.html', noticias=lista_noticias)

if __name__ == '__main__':
    app.run()
