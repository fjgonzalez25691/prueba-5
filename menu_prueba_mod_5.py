from typing import Iterable
from clases_mod_5 import *
from datos_amigos import *

c = Agenda([])

def añadir_amigo():
    global c

    nom = input("Nombre de amigo: ").title()
    
    contador = 0
    while(True):
        dni=input("Introduzca el dni: ")
        '''vamos a asegurarnos que el dni es una clave única porque 
        lo vamos a utilizar para borrar y modificar los amigos'''
        dni_en_lista = 0
        for i in c:
            if dni in i:
                dni_en_lista = 1
                contador +=1         
                     
            
        #Damos 3 oporturnidades para que el dni sea correcto, si no, salimos del bucle.
        if contador> 3:
         print("Asegurese del DNI de su amigo y vuelva a intentarlo")
         break
        #nos aseguramos que el dni tiene 9 dígitos
        if len(dni)!=9:
            print("El DNI tiene que tener 9 dígitos")
            contador +=1
        #obligamos a que tenga 8 números y una letra al final.
        elif dni[0:8].isnumeric() == False or dni[8].isnumeric()==True:
            print("El DNI se compone de 8 números y una letra\nIntroduzca un DNI correcto")
            contador +=1  
        elif dni_en_lista == 1: 
            print("El dni existe en la lista de amigos")
            contador +=1
        # si todo es correcto, ponemos la letra en mayúsculas y seguimos introduciendo datos.
        else:
            dni=dni.upper()
            break
    # Si excedemos los tres intentos, damos el control al menú.
    if contador>3:
        return True

    pob = input("Población: ").title()
    pa = input("País: ").upper()
    grup = input("Grupo preferido: ").upper()
    can = input("Canción: ").upper()
    est = input("Estilo: ").upper()
    #agregamos el nuevo amigo a la lista
    c.agregar_amigo(Gusto_amigos(nom,dni,pob, pa, grup, can, est))

    return True

def modificar_amigo():
    global c
    
    dni_mod = input("Introduzca el DNI del amigo que quiere modificar: ")
    dni_mod = dni_mod.upper()
    c.modificar_amigo(dni_mod)
    
    return True

def eliminar_amigo():
    global c

    dni_eliminar = input("Introduzca el dni del amigo que quiere borrar: ").upper()
    c.borrar_amigo(dni_eliminar)
    
    return True

def listado_amigos():
    global c

    c.mostrar()
    #c.imprimir_agenda()

    return True

def salir():
    print("Hasta luego")

    return False

c.agregar_amigo(Gusto_amigos("Juan", "01234567A", "Torrejón", "España".upper(), "OMD","Enola Gay".upper(), "Tecno".upper()))
c.agregar_amigo(Gusto_amigos("Miguel Angel", "12345678A", "Ciempozuelos", "España".upper(), "Queen".upper(), "Killer Queen".upper(), "Rock-pop".upper() ))



def switch(opcion):
    menu = {
        '1' : 'añadir_amigo()',
        '2' : 'modificar_amigo()',
        '3' : 'eliminar_amigo()',
        '4' : 'listado_amigos()',
        '5' : 'salir()'
    }
    return eval(menu.get(opcion))


continuar = True

while(continuar):
    cadena = "BASE DE DATOS DE AMIGOS"
    print (cadena.center(50,"="))
    print('''
    Seleccione una opción:
    1) Añadir amigo.
    2) Modificar amigo.
    3) Eliminar amigo.
    4) Listado de amigos.
    5) Salir''')
    opcion=input()
    try:
        continuar = switch(opcion)
               
    except TypeError:
       print("Debe elegir un número entre 1 y 5")
    except Exception as e:
        print(e)
    
