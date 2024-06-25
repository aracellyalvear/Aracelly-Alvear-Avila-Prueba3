import random

registro_autos = [
    {'Tipo' : "prueba tipo",
     'Patente' : "JJJJ00",
     'Marca' : "prueba marca",
     'Precio' : 5000000,
     'Cantidad Multas' : 0,
     'Detalle Multas': "No Aplica",
     'Fecha Registro Vehiculo' : "00/00/0000",
     'Rut Duenio' : "112223334",
     'Nombre Duenio' : "Lucho",}
]

multas= []
aux = 0

#función tipo auto
def tipo_auto (x) :
    if x == 1:
        return "Automóvil"
    elif x == 2 :
        return "Camión"
    elif x == 3 :
        return "Camioneta"
    else :
        return "Moto"

#random
def fun_random () :
    for i in range(3) :
        return random.randrange(1500,3500)

#funcion opción 1
def opcion_1 () :
    print("***REGISTRAR AUTO***")
    #tipo de auto
    while True :
        print('''
        Ingrese TIPO de vehículo:
        1. Automóvil.
        2. Camión.
        3. Camioneta.
        4. Moto
            ''')
        try :
            nro_tipo = int(input(">"))
        except :
            nro_tipo = 5
            
        if nro_tipo == 1 or nro_tipo == 2 or nro_tipo == 3 or nro_tipo == 4 :
            print("TIPO VEHÍCULO ingresado con éxito!")
            registro_autos['Tipo'] = tipo_auto(nro_tipo)
            break
        else :
            print("ERROR: opción ingresada no válida.")

    #patente
    while True :
        patente = input("Ingrese PATENTE de vehículo (en mayúsculas): >")
        if (len(patente) == 6) :
            print("PATENTE ingresa con éxito!")
            registro_autos['Patente'] = patente
            break
        else :
            print("ERROR: opción ingresada no válida.")
            
    #marca
    while True :
        marca = input("Ingrese MARCA de vehículo: >")
        if len(marca) < 2 or len(marca) > 15 :
            print("ERROR: opción ingresada no válida. Debe tenemos al menos 2 caracteres o máximo 15.")
        else :
            print("MARCA ingresada con éxito!")
            registro_autos['Marca'] = marca
            break
    
    #precio
    while True :
        try :
            precio = int(input("Ingrese PRECIO de vehículo: >"))
        except :
            precio = 0
        if precio < 5000000 :
            print("ERROR: opción ingresada no válida. mínimo $5.000.000.")
        else :
            print("PRECIO ingresado con éxito!")
            registro_autos['Precio'] = precio
            break
    
    #multas
    while True :
        try :
            cant_multas = int(input("Ingrese CANTIDAD DE MULTAS del vehículo: >"))
        except :
            cant_multas = -1

        if cant_multas < 0 :
            print("ERROR: opción ingresada no válida.")
        elif cant_multas == 0:
            print("MULTAS ingresadas con éxito!")
            break
        else :
            for i in range(cant_multas) :
                detalle_multas = input(f"Ingrese precio y fecha de la multa {i+1}: >")
                multas.append = detalle_multas
            
            print("MULTAS ingresadas con éxito!")
            registro_autos['Cantidad Multas'] = cant_multas
            multas.copy = registro_autos['Detalle Multas']
            break
    
    #fecha registro vehículo
    fecha_registro = input("Ingrese la fecha del Registro del Vehículo: >")
    registro_autos['Fecha Registro Vehiculo'] = fecha_registro
    
    #rut dueño
    rut = input("Ingrese rut del dueño de vehículo (sin guión, pero con dígito verificador): >")
    registro_autos['Rut Duenio'] = rut
    
    #nombre dueño
    duenio = input ("Ingrese nombre completo del dueño: >")
    registro_autos['Nombre Duenio'] = duenio
    
    print ("VEHÍCULO INGRESADO CON ÉXITO!")

#funcion opcion 2
def funcion_2 ():
    print("***BUSCAR VEHÍCULO***")
    patente_cert = input("Ingrese patente vehículo: >")
    print(registro_autos(e for e in registro_autos if e['Patente'] == patente_cert)[0])

#funcion opcion 3
def funcion_3 ():
    print("IMPRIMIR CERTIFICADOS")
    patente_cert = input("Ingrese patente vehículo: >")
    
    while True :
        print('''
        Elija opción a imprimir:
        1. Emisión de Contaminantes.
        2. Anotaciones Vigentes.
        3. Multas
            ''')
        try :
            op_cert = int(input(">"))
        except :
            op_cert = 0
        
        if op_cert == 1 :
            print(registro_autos(e for e in registro_autos if e['Patente'] == patente_cert)[0])
            print("Emisión de Contaminantes")
            print("Precio: $",fun_random)
            
        elif op_cert == 2 :
            print(registro_autos(e for e in registro_autos if e['Patente'] == patente_cert)[0])
            print("Anotaciones Vigentes")
            print("Precio: $",fun_random)
        elif op_cert == 3 :
            print(registro_autos(e for e in registro_autos if e['Patente'] == patente_cert)[0])
            print("Multas")
            print("Precio: $",fun_random)
        else :
            print("ERROR: opción ingresada no válida.")

#PROGRAMA
while True :
    print ('''
    Bienvenidos a Automotora ***AUTO SEGURO***
    Elija la opción que necesie:
    1. Grabar.
    2. Buscar.
    3. Imprimir Certificados.
    4. Salir.
        ''')
    try:
        v_opcion=int(input(">"))
    except:
        v_opcion=5
    
    #REGISTRAR AUTO    
    if v_opcion==1:
        opcion_1()   
        while True :
            print ("¿Quiere ingresar otro vehículo?")
            print("1. Si")
            print("2. No")
            
            try :
                otro = int(input(">"))
            except :
                otro = 0
            if otro == 1 :
                opcion_1()
            elif otro == 2 :
                aux = 1
                break
            else :
                print("ERROR: opción inválida")        
    
    #BUSCAR AUTO
    elif v_opcion==2:
        funcion_2()
        
    #IMPRIMIR CERTIFICADOS
    elif v_opcion==3:
        funcion_3()
        
    #SALIDA
    elif v_opcion==4:
        print("***MUCHAS GRACIAS POR OCUPAR NUESTROS SERVICIOS***")
        print("Aracelly Francisca Alvear Ávila")
        print("Versión 1.0")
        break
    else:
        print("ERROR: opción ingresada no válida.") 