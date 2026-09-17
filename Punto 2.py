# Ejercicio 2

# Pedimos al usuario el número n que desea analizar
n = int(input("Ingrese un número entero positivo n: "))

# Acumulamos la cantidad de primos encontrados
contador_primos = 0

# Recorremos todos los números desde 2 hasta n (0 y 1 no son primos)
numero_actual = 2
while numero_actual <= n:
    #    es_primo = True

    # Para saber si numero_actual es primo, probamos si tiene algún
    #    divisor entre 2 y su raíz cuadrada. 
    divisor = 2
    while divisor * divisor <= numero_actual and es_primo == True:
        if numero_actual % divisor == 0:
            # Si el residuo es 0, encontramos un divisor exacto, entonces el número NO es primo
            es_primo = False
        divisor = divisor + 1
    if es_primo == True:
        contador_primos = contador_primos + 1
    numero_actual = numero_actual + 1

# 8. Mostramos el resultado final
print("La cantidad de números primos menores o iguales a", n, "es:", contador_primos)
