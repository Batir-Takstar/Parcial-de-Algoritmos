# Ejercicio 1

# Definimos la variable "numero" que permite ingresar un numero decimal para poder convertirlo a binario
numero = int(input(f"Ingrese un numero decimal positivo "))  

#Definimos las condiciones especiales (tales como cuando sea menor que 0, o cuando sea 0)
if numero < 0:
    print("Error no se aceptan numeros negativos")
else:
    if numero == 0:
        print("El numero", numero, "es binario e igual a 0")
    else:

# Definimos una variable "auxiliar" y "binario" para no modificar el numero original puesto y poder operar con él,
# y para almacenar el resultado de la conversion a binario
        auxiliar = numero
        binario = ""

# Definimos el ciclo while para realizar un bucle de operaciones para convertir el numero decimal a un numero en binario
        while auxiliar > 0:
            residuo = auxiliar % 2
            binario = str(residuo) + binario
            auxiliar = auxiliar // 2 
# Por ultimo, demostramos el resultado obtenido de la conversion a binario del numero decimal ingresado
print("El numero", numero, "en binario es:", binario)