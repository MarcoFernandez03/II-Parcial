import os
intentos = 3
saldo = 0 
opcion = 1
credenciales = {
    "usuario" : "marco",
    "contraseña" : "M4rc0"
    }

while intentos >= 1:
    print("Bienvenido al sistema de cajero automatico ")
    usuario = input("Digite su usuario ").lower()
    usuario = usuario.lstrip()
    usuario = usuario.rstrip()
    contrasenia = input("Digite su contraseña ")
    contrasenia = contrasenia.lstrip()
    contrasenia = contrasenia.rstrip()

    if usuario == credenciales["usuario"] and contrasenia == credenciales["contraseña"]:
        while opcion > 0 and opcion < 4:
            os.system("cls")
            opcion = int(input("¿Qué acción desea realizar? \n1.Depositar dinero a la cuenta \n2.Sacar dinero de la cuenta \n3.Ver el saldo \n4.Salir \n"))

            #Deposito de saldo
            if opcion == 1:
                excepcion = True
                while excepcion == True:
                    os.system("cls")
                    try:
                        deposito = int(input("¿Cuánto dinero desea depositar? \n Recuerde que solo puede depositar multiplos de 1000 \n"))
                    except:
                        print("Debe digitar el depósito en números")
                    else:
                        if deposito % 1000 == 0:
                            saldo = saldo + deposito
                            print("Usted depositó {} su saldo actual es de {}".format(deposito, saldo))
                            excepcion = False
                            opcion=int(input("¿Desea volver a la pantalla anterior? \n1.Si  \n2.No \nDigite la opcion "))
                            if opcion >= 2:
                                opcion = 4
                                print("Gracias por usar el servicio")
                        else:
                            print("No puede depositar cantidades que no sean multiplos de 1000")
            #Retiro de saldo
            elif opcion == 2:
                excepcion = True
                while excepcion == True:
                    os.system("cls")
                    retiro = int(input("Digite cuanto desea retirar \n Recuerde que solo puede retirar multiplos de 1000 \n"))
                    if retiro % 1000 == 0:
                        if saldo < retiro:
                            print(f"Usted tiene {saldo} de saldo. No es posible retirar más dinero del que tiene")
                        else:
                            saldo = saldo - retiro
                            print("Usted retiró {} su saldo actual es de {}".format(retiro, saldo))
                            excepcion = False
                            opcion=int(input("¿Desea volver a la pantalla anterior? \n1.Si  \n2.No \nDigite la opcion "))
                            if opcion >= 2:
                                opcion = 4
                                print("Gracias por usar el servicio")
                    else:
                        print("\n No puede retirar cantidades que no sean multiplos de 1000 \n")
            #Consulta de saldo
            elif opcion == 3:
                print("Su saldo es de:",saldo)
                opcion=int(input("¿Desea volver a la pantalla anterior? \n1.Si  \n2.No \nDigite la opcion "))
                if opcion >= 2:
                    opcion = 4
                    print("Gracias por usar el servicio")
            #Salida
            elif opcion == 4: 
                print("Gracias por usar el servicio")
                break

        #Comprabacion de opcion correcta
        if opcion <= 0 or opcion > 4:
            print("Error digitó una opcion no valida\nDigite una opción valida")
            opcion = 1

        if opcion == 4: 
            break
    else:
        intentos = intentos - 1
        if intentos != 0:
            print(f"Error credenciales invalidas le quedan {intentos} intento(s) antes que el sistema se bloquee")
        else:
            print("Sistema bloqueado")
