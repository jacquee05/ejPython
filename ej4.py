import urllib.request

def contar_palabras_en_url(url):
    try:
        respuesta = urllib.request.urlopen(url)
        contenido = respuesta.read().decode('utf-8')

        palabras = contenido.split()
        print(f"El archivo contiene {len(palabras)} palabras.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

url = input("Introduce la URL del archivo de texto: ")
contar_palabras_en_url(url)
