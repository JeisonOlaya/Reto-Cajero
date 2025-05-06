usuario={}

while True:
    id = input("Ingrese por favor el Id: ")
    nombre = input("Ingrese por favor el nombre: ")
    apellido = input("Ingrese por favor el apellido:")
    correo = input("Ingresa por favor el correo: ")
    
    usuario[id]={nombre,apellido,correo}
    
    print(usuario)
    
    continuar = int(input("Deseas continuar: 1(si) 2(no)"))
    if continuar != 1 :
        break