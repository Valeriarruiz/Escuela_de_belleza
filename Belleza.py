print("Bienvenido a Ecipar Shop")
print("Servicios: 1: Ver catalogo de servicios, 2: Ver catalogo de productos, 3: Agendar citas, 4: Compra")
S=int(input("Digite el servicio que requiere: "))
if(S==1):
    print("Haga click en el servicio y recibira información")
    print("Cada servicio tiene su respectivo precio y horarios de atención")
    print("¿Desea conocer el precio de su elección?")
    print("1=Si o 2=No")
    P=int(input("Digite su respuesta: "))
    if(P==1):
        print("Servicios: A=Spa, B=Corte, C=Estetica")
        Se=str(input("Digite opción: "))
        A=90000
        B=15000
        C=50000
        if(Se==C):
         print("El precio del servicio es ", C)
        elif(Se==B):
         print("El precio del servicio es ", B)
        elif(Se==A):
         print("El precio del servicio es ", A)
    else: 
        print("Regrese a la pagina principal")
elif(S==2):
    print("Haga click en el producto y recibira información")
    print("¿Desea conocer el precio de los productos?")
    print("1=Si o 2=No")
    P=int(input("Digite su respuesta: "))
    if(P==1):
        print("Productos: Aa=Cabello, Bb=Uñas, Cc=Piel, Dd=Maquillaje")
        Se=str(input("Digite opción: "))
        Aa=100000
        Bb=15000
        Cc=150000
        Dd=200000
        if(Se==Aa):
         print("El precio de los combos de productos es ", Aa)
        elif(Se==Bb):
         print("El precio de los combos de productos es ", Bb)
        elif(Se==Cc):
         print("El precio de los combos de productos es ", Cc)
        elif(Se==Dd):
         print("El precio de los combos de productos es ", Dd)
    else: 
        print("Regrese a la pagina principal")
elif(S==3):
    print("¿Se encuentra registrado?")
    print("1=Si o 2=No")
    R=int(input("Digite su respuesta: "))
    if(R==1):
        ND=int(input("Ingrese su numero de documento: "))
        if(ND==123456789): 
         print("Ingreso exitoso")
         print("Servicios para agendar cita: F=Spa, E=Corte, J=Belleza")
         Ag=str(input("Digite opción: "))
         print("Su cita se encuentra en proceso")
         print("¿Desea confirmar su cita? 1=Si 2=No")
         Co=int(input("Digite su respuesta: "))
         if(Co==1): 
            print("Su cita a sido exitosamente agendada")
         else:
            print("El proceso de su cita a sido cancelada")
        else:
         print("Su numero de documento es invalido") 
    else:
        print("Registrese")
elif(S==4):
    print("¿Se encuentra registrado?")
    print("1=Si o 2=No")
    R=int(input("Digite su respuesta: "))
    if(R==1):
        ND=int(input("Ingrese su numero de documento: "))
        if(ND==123456789): 
         print("Ingreso exitoso")
         print("Seleccione los productos")
         Ag=str(input("Digite opción: "))
         print("Su compra se encuentra en proceso")
         print("¿Desea confirmar su pedido? 1=Si 2=No")
         Co=int(input("Digite su respuesta: "))
         if(Co==1): 
            print("Su compra a sido exitosamente validada, pronto podra reclamarla o sera enviada a su domicilio")
         else:
            print("El proceso de su compra a sido cancelada")
        else:
         print("Su numero de documento es invalido") 
    else:
        print("Registrese")       