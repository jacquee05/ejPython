def mostrar_linea_tabla():
    n = int(input("Número n (1-10): "))
    m = int(input("Número m (1-10): "))

    if not (1 <= n <= 10 and 1 <= m <= 10):
        print("Ambos números deben estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{n}.txt", "r") as archivo:
            lineas = archivo.readlines()
            print(lineas[m - 1].strip())
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

