def convertir_a_romano(numero):
    if numero < 1 or numero > 1999:
        return "El número debe estar entre 1 y 1999"
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    resultado = ""
    for i in range(len(valores)):
        while numero >= valores[i]:
            resultado += simbolos[i]
            numero -= valores[i]
    return resultado

numero = int(input("Ingresa un número entre 0 y 1999: "))
print(convertir_a_romano(numero))