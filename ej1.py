def guardar_tabla(n):
    if 1 <= n <= 10:
        with open(f"tabla-{n}.txt", "w") as f:
            f.writelines([f"{n} x {i} = {n*i}\n" for i in range(1, 11)])
        print(f"Tabla guardada en 'tabla-{n}.txt'")
    else:
        print("Número fuera de rango (1-10)")

guardar_tabla(int(input("Introduce un número entre 1 y 10: ")))
