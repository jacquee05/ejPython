import csv, statistics

def procesar_cotizaciones(entrada='cotización.csv', salida='resumen.csv'):
    with open(entrada, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        columnas = {k: [] for k in reader.fieldnames}
        for fila in reader:
            for k, v in fila.items():
                columnas[k].append(v)

    with open(salida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Columna', 'Mínimo', 'Máximo', 'Media'])
        for k in columnas:
            if k == 'Nombre': continue
            try:
                nums = [float(x.replace(',', '')) for x in columnas[k]]
                writer.writerow([k, min(nums), max(nums), round(statistics.mean(nums), 2)])
            except:
                writer.writerow([k, 'ERROR', 'ERROR', 'ERROR'])

procesar_cotizaciones()
print("Resumen guardado en resumen.csv")
