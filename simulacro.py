retiro=[]
deposito=[]
numero_cuenta=(123456789)
saldo = 0 

menu = True

while menu:
        
    print("1.) Depositar Dinero")
    print("2.) Retirar Dinero")
    print("3.) ver saldo de cuenta")
    print("4.) ver historial de movimiento")
    print("5.) salir del programa")    
                       
    proceso={
        "saldo": saldo,
        "retiro": retiro,
        "deposito": deposito
    }  
                
    continuar = int(input("Ingrese el numero de la opcion que deseas realizar: "))    
    if continuar == 1:
        print("\n=======VAS A REALIZAR UN DEPOSITO=======")
        depositar= int(input("Por favor ingresa el monto que deseas depositar: "))
        saldo= depositar + saldo
        proceso["saldo"]={saldo}      
        print("deposito exitoso a la cuenta",{numero_cuenta})
        deposito.append(depositar)
        print("Saldo Actual= ", saldo)
        
                        
    if continuar == 2:
        print("VAS A REALIZAR UN RETIRO")
        retiro= int(input("Por favor ingresa el monto que deseas retirar: "))
        if retiro>saldo:
            print("saldo insuficiente")
        else:
            saldo= saldo - retiro
            print("retiro exitoso")
            print("Saldo Actual= ", saldo)