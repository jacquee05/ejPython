def mostrar_tabla():
    try:
        n = int(input("Número (1-10): "))
        with open(f"tabla-{n}.txt") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"No existe el archivo 'tabla-{n}.txt'.")
    except:
        print("Entrada inválida o número fuera de rango.")
mostrar_tabla()
