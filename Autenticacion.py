from Configuracion_Inicial import usuario
from Configuracion_Inicial import pin

def autenticacion() :
    DigiteUsuario = input("Usuario: ")
    DigitePin = input("Pin: ")

    if usuario==DigiteUsuario and pin==DigitePin:
        print("Correcto")