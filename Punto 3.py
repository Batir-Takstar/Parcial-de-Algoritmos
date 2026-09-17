# Ejercicio 3

# Pedimos al usuario cuántos términos quiere generar
n = int(input("Ingrese la cantidad de términos de Fibonacci a generar: "))

# Variables para ir guardando el término anterior y el actual.
anterior = 0
actual = 1

# Contador de cuántos términos resultaron pares
contador_pares = 0

# Repetimos el proceso n veces, una por cada término a generar
contador_terminos = 1
while contador_terminos <= n:

# En la primera vuelta, el término es "anterior" y el termino siguiente es "actual"
    if contador_terminos == 1:
        termino = anterior
    else:
        termino = actual

# Determinamos si el término es par o impar
    if termino % 2 == 0:
        paridad = "par"
        contador_pares = contador_pares + 1
    else:
        paridad = "impar"

    print("Término", contador_terminos, ":", termino, "->", paridad)

# Avanzamos la serie: calculamos el siguiente término sumando, los dos anteriores, y desplazamos las variables
    siguiente = anterior + actual
    anterior = actual
    actual = siguiente

    contador_terminos = contador_terminos + 1

# Calculamos la proporción de términos pares sobre el total.
proporcion_pares = contador_pares / (n * 1.0)

# Mostramos los resultados finales
print()
print("Cantidad de términos pares:", contador_pares, "de", n)
print("Proporción de términos pares:", proporcion_pares)