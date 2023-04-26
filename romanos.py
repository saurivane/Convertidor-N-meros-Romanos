romano = {1000:'M', 900:'CM',500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}


def romanos(num):
    if num < 0 or num >= 2000:
        return "No válido"
    
    miles = (num //1000)*1000
    centenares = ((num - miles) // 100)*100
    decenas = ((num - miles - centenares )//10)*10
    unidades = num - miles - centenares - decenas
    
    resultado = ''
    
    if miles in romano:
        resultado = resultado + romano[miles]

    if centenares in romano:
        resultado = resultado + romano[centenares]
    else:
        if centenares < 400:
            while centenares != 0:
                resultado = resultado + 'C'
                centenares = centenares - 100
                
        elif centenares > 500 <= 800:
            resultado = resultado + 'D'
            while centenares != 500:
                resultado = resultado + 'C'
                centenares = centenares - 100
                
    if decenas in romano:
        resultado = resultado + romano[decenas]
    else:
        if decenas < 40:
            while decenas != 0:
                resultado = resultado + 'X'
                decenas = decenas - 10
                
        elif decenas > 50 <= 80:
            resultado = resultado + 'L'
            while decenas != 50:
                resultado = resultado + 'X'
                decenas = decenas - 10
        
    if unidades in romano:
        resultado = resultado + romano[unidades]
    else:
        if unidades < 4:
            while unidades != 0:
                resultado = resultado + 'I'
                unidades = unidades - 1
                
        elif unidades > 5 <= 8:
            resultado = resultado + 'V'
            while unidades != 5:
                resultado = resultado + 'I'
                unidades = unidades - 1
        
    return resultado
