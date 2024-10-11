#Definir constantes
PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE = 28000
IMPUESTO_TARJETA = 0.07

# Funcion para calucular el precio
def calcular_precio (tipo_hamburguesa, medio_pago, cantidad):
    #Definir precios segun el tipo de hamburguesa
    if tipo_hamburguesa == 1:
        precio =PRECIO_SENCILLA
        descripcion = "Sencilla"
    elif tipo_hamburguesa ==2:
        precio = PRECIO_DOBLE
        descripcion = "Doble"
    elif tipo_hamburguesa == 3:
        precio = PRECIO_TRIPLE
        descripcion = "Triple"
    else:
        return None #Tipo de Hamburguesainvalido
    #calcular el total sin cargos
    total_sin_cargo = precio* cantidad
    #aplica el impuesto si el medio  de pago es tarjeta
    if medio_pago == 1:
        impuesto = round(total_sin_cargo * IMPUESTO_TARJETA)
    else:
        impuesto =0

    total = round(total_sin_cargo +  impuesto)
    #retornar datos relevantes
    return descripcion, precio, cantidad, impuesto, total
#funcion para generar mensaje
def generar_mensaje(descipcion, precio, cantidad, impuesto, total):
    return (f"Tipo de Hamburguesa: {descipcion}\n"
            f"Precio: ${precio}\n"
            f"Cantidad: {cantidad}\n"
            f"Impuesto: ${impuesto}\n"
            f"Total: ${total}")
#funcion para validar los datos
def validar_datos(tipo_hamburguesa, medio_pago, cantidad):
    if 1 <= tipo_hamburguesa <= 3 and 1 <= medio_pago <= 2 and cantidad > 0:
        resultado =calcular_precio(tipo_hamburguesa, medio_pago, cantidad)
        #print ("resultado: ", resultado)
        descripcion, precio, cantidad, impuesto, total = resultado
        mensaje = generar_mensaje(descripcion, precio, cantidad, impuesto, total)
        print("----------------------\n"+ mensaje)
    else:
        print("Verifique las opciones ingresadas. ")
# entradas
tipo_hamburguesa = int( input("Ingrese tipo de hamburguesa \n1. Sencilla \n2. Doble \n3. Triple \n"))
medio_pago = int(input("Ingrese medio de pago \n1. Tarjeta \n2. Otro \n"))
catidad = int(input("Ingrese la cantidad:  "))

# salidas
validar_datos(tipo_hamburguesa, medio_pago, catidad)
