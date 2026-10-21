unidades = ("", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve")
dieces = ("diez", "once", "doce", "trece", "catorse", "quince", "dieciseis", 
          "diecisiete", "dieciocho", "diecinueve")
veinti = ("Veinte", "veintiuno", "veintidos", "veintitres", "veinticuatro", 
          "veinticinco", "veintiseis", "veintisiete", "veintiocho", "veintinueve")
decenas = ("", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", 
           "ochenta", "noventa")
centenas = ("", "ciento", "docientos", "trecientos", "cuatrocientos", "quinientos",
             "seiscientos", "setecientos", "ochocientos", "novecientos")

def unidad (numero):
    print(unidades[numero])

def decena (numero):
    dece = numero // 10
    unidad = numero % 10

    match dece:
        case 1:
            print(dieces[unidad])
        case 2:
            print(veinti[unidad])
        case _:
            if unidad == 0:
                print(decenas[dece])
            else:
                print(decenas[dece], "y", unidades[unidad])

def centena (numero):
    cente = numero // 100
    resi_cente = numero % 100
    dece = resi_cente // 10 
    unidad = resi_cente % 10

    if dece == 0 and unidad == 0:
        if cente == 1:
            print("Cien")
        else:
            print(centenas[cente])
    elif dece == 0:
        print(centenas[cente], unidades[unidad])
    elif dece == 1:
        print(centenas[cente], dieces[unidad])
    elif dece == 2:
        print(centenas[cente], veinti[unidad])
    else:
        if unidad == 0:
            print(centenas[cente], decenas[dece])
        else:
            print(centenas[cente], decenas[dece], "y",unidades[unidad])

def millares(numero):
    mil = numero // 1000
    resi_mil = numero % 1000
    cente = resi_mil // 100
    resi_cente = resi_mil % 100
    dece = resi_cente // 10 
    unidad = resi_cente % 10

    if cente == 0 and dece == 0 and unidad == 0:
        if mil == 1:
            print("Mil")
        else:
            print(unidades[mil], "mil")
    elif cente == 0 and dece == 0:
        if mil == 1:
            print("Mil", unidades[unidad])
        else:
            print(unidades[mil], "mil", unidades[unidad])
    elif cente == 0 and dece == 1:
        if mil == 1:
            print("Mil", dieces[unidad])
        else:
            print(unidades[mil], "mil", dieces[unidad])
    elif cente == 0 and dece == 2:
        if mil == 1:
            print("Mil", veinti[unidad])
        else:
            print(unidades[mil], "mil", veinti[unidad])
    elif cente == 0:
        if mil == 1 and unidad == 0:
            print("Mil", decenas[dece])
        elif mil == 1:
            print("mil", decenas[dece], "y", unidades[unidad])
        else:
            print(unidades[mil], "mil", decenas[dece], "y", unidades[unidad])
    elif cente == 1 and dece == 0 and unidad == 0:
        if mil == 1:
            print("Mil", "cien")
        else:
            print(unidades[mil], "mil", "cien")
    elif cente >= 1 and dece == 0 and unidad >= 0:
        if mil == 1:
            print("Mil", centenas[cente], unidades[unidad])
        else:
            print(unidades[mil], "mil", centenas[cente], unidades[unidad])
    elif cente >= 1 and dece == 1:
        if mil == 1:
            print("Mil", centenas[cente], dieces[unidad])
        else:
            print(unidades[mil], "mil", centenas[cente], dieces[dece])
    elif cente >= 1 and dece == 2:
        if mil == 1:
            print("Mil", centenas[cente], veinti[unidad])
        else:
            print(unidades[mil], "mil", centenas[cente], veinti[dece])
    elif cente >= 1 and dece >= 3:
        if mil == 1 and unidad == 0:
            print("Mil", centenas[cente], decenas[dece])
        elif mil == 1:
            print("mil", centenas[cente], decenas[dece], "y", unidades[unidad])
        else:
            print(unidades[mil], "mil", centenas[cente], decenas[dece], "y", unidades[unidad])

while True:
    numero = int(input("Ingrese un numero de rango 1 al 9999, \n> "))
    if 1 <= numero <= 9999:
        break
    else:
        print(f"El sistema no asepta el dato: <{numero}>, que Ud. ingreso")

digitos = len(str(numero))
int(numero)

match digitos:
    case 1:
        unidad(numero)
    case 2:
        decena(numero)
    case 3:
        centena(numero)
    case 4:
        millares(numero)
