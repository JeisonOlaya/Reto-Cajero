retiro=[]
deposito=[]
historial={}
counter=0
saldo = 0 
numero_cuenta=(123456789)

menu = True

while menu:
        
    print("1.) Depositar Dinero")
    print("2.) Retirar Dinero")
    print("3.) ver saldo de cuenta")
    print("4.) ver historial de movimiento")
    print("5.) salir del programa")    
                         
                
    continuar = int(input("Ingrese el numero de la opcion que deseas realizar: "))    
    if continuar == 1:
        print("\n=======VAS A REALIZAR UN DEPOSITO=======")
        counter = counter + 1
        depositar= int(input("Por favor ingresa el monto que deseas depositar: "))

        historial[counter]={
            "valor": depositar,
            "tipo": "Deposito",
        }
        saldo = saldo + depositar
        print("\n",historial)
        
        
                        
    elif continuar == 2:
        print("\n=======VAS A REALIZAR UN RETIRO=======")
        retirar= int(input("Por favor ingresa el monto que deseas retirar: "))

        if retirar>saldo:
            print("saldo insuficiente")
        else:
            saldo= saldo - retirar
            print("\nretiro exitoso")
            print("Saldo Actual= ", saldo, "\n")
            retiro.append(retirar)

    if continuar == 3:
        print("\n=======SALDO DE CUENTA=======")
        print("Saldo Actual= ", saldo, "\n")
    if continuar == 4:
        print("\n=======HISTORIAL DE MOVIMIENTO=======")
        print("Depositos= ", deposito)
        print("Retiros= ", retiro)
        print("Saldo Actual= ", saldo, "\n")
    if continuar == 5:
        print("\n=======GRACIAS POR UTILIZAR EL BANCO=======")

menu = False