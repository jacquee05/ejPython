import urllib.request, gzip, io

def mostrar_pib_pais():
    url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_08_10?format=TSV&compressed=true"
    respuesta = urllib.request.urlopen(url)
    datos = gzip.GzipFile(fileobj=io.BytesIO(respuesta.read())).read().decode('utf-8').splitlines()

    cabecera = datos[0].split('\t')[4:]
    pais = input("Código país (ej: ES): ").strip().upper()

    for linea in datos[1:]:
        partes = linea.split('\t')
        if len(partes) > 4 and partes[3] == pais:
            valores = partes[4:]
            print(f"PIB per cápita para {pais}:")
            for año, valor in zip(cabecera, valores):
                print(f"{año}: {valor}")
            break
    else:
        print("No se encontraron datos para ese código.")
mostrar_pib_pais()


