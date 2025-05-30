# tasks/extract.py

import requests
from bs4 import BeautifulSoup
from prefect import task

@task
def extract_offers(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error al obtener la página: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # Este es un ejemplo general, necesitas adaptarlo a la estructura real de LinkedIn
    job_elements = soup.find_all('li', class_='result-card job-result-card')

    ofertas = []
    for job in job_elements:
        titulo = job.find('h3', class_='job-result-card__title')
        descripcion = job.find('p', class_='job-result-card__snippet')
        ubicacion = job.find('span', class_='job-result-card__location')
        fecha = job.find('time')
        enlace = job.find('a', class_='result-card__full-card-link')

        ofertas.append({
            "titulo": titulo.text.strip() if titulo else "",
            "descripcion": descripcion.text.strip() if descripcion else "",
            "ubicacion": ubicacion.text.strip() if ubicacion else "",
            "fecha": fecha['datetime'] if fecha and fecha.has_attr('datetime') else "",
            "enlace": enlace['href'] if enlace and enlace.has_attr('href') else "",
        })

    return ofertas
