import romanos

try:
    numero = int(input('Introduce el número a convertir entre 0 y 1999: '))
    
    # Controlamos que el número introducido esté en el rango solicitado
    if numero < 0 or numero >= 2000:
        print("Valor introducido no válido. Vuelva a intentarlo")
    else:
        x = romanos.romanos(numero)
        print(f"El numero " + str(numero) + " en números romanos es: " + str(x))
except:
    print("Valor introducido no válido. Vuelva a intentarlo")