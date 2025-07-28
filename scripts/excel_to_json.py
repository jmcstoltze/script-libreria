import uuid
import pandas as pd
import json
from datetime import datetime
import os
from collections import defaultdict

# Configuración de paths
DIR_PROYECTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_PATH = os.path.join(DIR_PROYECTO, 'scripts', 'Proyecto-Biblioteca.xlsx')
JSON_OUTPUT = os.path.join(DIR_PROYECTO, 'assets', 'data', 'biblioteca.json')

# Funciones para metadata
def calcular_decadas(anios):
    decadas = defaultdict(int)
    for anio in anios:
        decada = f"{str(anio)[:3]}0s"
        decadas[decada] += 1
    return dict(sorted(decadas.items()))

def calcular_por_genero(libros):
    generos = defaultdict(int)
    for libro in libros:
        for genero in libro['genero']:
            generos[genero] += 1
    return dict(sorted(generos.items()))
    
def calcular_por_editorial(libros):
    editoriales = defaultdict(int)
    for libro in libros:
        editorial = libro['editorial']
        editoriales[editorial] += 1
    return dict(sorted(editoriales.items(), key=lambda x: x[1], reverse=True))

def calcular_por_estado(libros):
    estados = defaultdict(int)
    for libro in libros:
        estado = libro['estado']
        estados[estado] += 1
    # Asegurar todos los estado posibles
    for estado in ['Disponible', 'Prestado', 'Leído']:
        if estado not in estados:
            estados[estado] = 0
    return dict(sorted(estados.items()))

def calcular_por_idioma(libros):
    idiomas = defaultdict(int)
    for libro in libros:
        idioma = libro['idioma']
        idiomas[idioma] += 1
    return dict(sorted(idiomas.items()))

def calcular_sistemas_identificacion(libros):
    con_isbn = sum(1 for libro in libros if libro['isbn'] != "")
    return {
        "conISBN": con_isbn,
        "sinISBN": len(libros) - con_isbn
    }

def main():
    # Leer Excel, forzando la columna UUID como string
    df = pd.read_excel(EXCEL_PATH, dtype={'UUID': str})
    df['UUID'] = df['UUID'].fillna('') # Convertir NaN a string vacíos

    # Estructura base JSON
    biblioteca = {
        "biblioteca": {
            "nombre": "Biblioteca Personal",
            "descripcion": "Colección personal de literatura política, histórica y filosófica",
            "creacion": "2025-07-25",
            "ultimaActualizacion": datetime.now().strftime('%Y-%m-%d'),
            "libros": [],
            "metadata": {}
        }
    }

    # Procesar libros
    anios_publicacion = []
    for i, row in df.iterrows():
        # Generar UUID si no existe
        libro_uuid = row['UUID'] if row['UUID'] else str(uuid.uuid4())
        df.at[i, 'UUID'] = libro_uuid # Actualiza el DataFrame

        libro = {
            "id": i + 1,
            "uuid": libro_uuid, # Usamos el UUID generado o existente
            "titulo": row['Título'],
            "autor": row['Autor'],
            "otrosAutores": [x.strip() for x in str(row['Otros Autores']).split(';')] if pd.notna(row['Otros Autores']) else [],
            "anioPublicacion": int(row['Año de Publicación']),
            "editorial": row['Editorial'],
            "coleccion": row['Colección'] if pd.notna(row['Colección']) else "",
            "genero": [x.strip() for x in row['Género'].split('/')],
            "isbn": str(row['ISBN']) if pd.notna(row['ISBN']) else "",
            "estado": row['Estado'],
            "portada": row['Portada'],
            "descripcion": row['Descripción'],
            "paginas": int(row['Páginas']),
            "idioma": row['Idioma']
        }
        biblioteca["biblioteca"]["libros"].append(libro)
        anios_publicacion.append(int(row['Año de Publicación']))

    # Calcular metadatos
    libros = biblioteca["biblioteca"]["libros"]

    biblioteca["biblioteca"]["metadata"] = {
        "totalLibros": len(libros),
        "totalPaginas": sum(libro['paginas'] for libro in libros),
        "decadas": calcular_decadas(anios_publicacion),
        "estadisticas": {
            "porGenero": calcular_por_genero(libros),
            "porEditorial": calcular_por_editorial(libros),
            "porEstado": calcular_por_estado(libros),
            "porIdioma": calcular_por_idioma(libros),
            "sistemasIdentificacion": calcular_sistemas_identificacion(libros)
        }
    }

    # Guardar JSON
    with open(JSON_OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(biblioteca, f, ensure_ascii=False, indent=2)

    # Guarda el Excel actualizado
    df.to_excel(EXCEL_PATH, index=False)

    print(f"JSON actualizado correctamente en {JSON_OUTPUT}")
    print(f"Excel actualizado correctamente en {EXCEL_PATH}")

if __name__ == "__main__":
    main()