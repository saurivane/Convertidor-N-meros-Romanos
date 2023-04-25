import romanos

numero = int(input('Introduce el número a convertir entre 0 y 1999: '))

x = romanos.romanos(numero)

print(f"El numero " + str(numero) + ", en números romanos es: " + str(x))