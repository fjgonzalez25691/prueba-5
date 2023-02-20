from logging import exception
import time
class Agenda():
    
    datos = []

    def __init__(self, datos=[]):
        self.datos = datos
        
    #Definimos len() para la clase Agenda.    
    def __len__(self):        
        return len(self.datos)

    #Hacemos iterable la clase Agenda.
    def __iter__(self):        
        return iter(self.datos)   

    def __getitem__(self,n):
        return self.datos[n]   

    def __setitem__(self,m, n, value):    
        self.datos[n][m]= value


    def agregar_amigo(self, c):        
        self.datos.append(c)

    def borrar_amigo(self, dni):
        hay_dni = 0

        for v in self.datos:
            if dni in v:
                hay_dni += 1

        if hay_dni  !=0:
         print("Va a eliminar el siguiente amigo de la Agenda: ")        
         for v in self.datos:
            if dni in v:
                v.imprimir()
                self.datos.remove(v)
                time.sleep(2)
        else:
            print("El dni no se encuentra de la lista de amigos")

        

    def mostrar(self):
            print("{:<20} {:10} {:<15} {:<10} {:<20} {:<15} {:<15}".format("NOMBRE", "DNI", "POBLACION", "PAIS",
                     "GRUPO", "CANCION FAV.", "ESTILO"))
            print("="*111)
            for i in self.datos:
                print(i)
                print("-"*111)
                        
            time.sleep(2)
        
    def imprimir_agenda(self,v):        
            print("{:<20} {:10} ".format("NOMBRE", "DNI"))
            print("="*60)
            print("{:<20} {:10}".format(self.datos[v][0], self.datos[v][1]))
    
    def modificar_amigo(self, dni_mod):
        hay_dni = 0

        for v in self.datos:
            if dni_mod in v:
                hay_dni += 1

        if hay_dni  !=0:

            salir = False
            opcion = 0
            while not salir:
                print('''
                    1) Modificar Nombre.
                    2) Modificar Ciudad.
                    3) Modificar País.
                    4) Modificar grupo.
                    5) Modificar canción.
                    6) Modificar estilo.
                    7) Salir ''')                
                
                opcion = int(input('Elija una opción: '))
                for v in self.datos:
                    if dni_mod in v:
                        if opcion == 1:
                            nombre = input("Introduzca el nombre corregido:").title()
                            setattr(v, "nombre", nombre)
                        elif opcion ==  2:
                            ciudad = input("Introduzca la nueva ciudad: ").title()
                            setattr(v, "poblacion", ciudad)
                        elif opcion == 3:
                            pais = input("Introduzca el nuevo País: ").upper()
                            setattr(v, "pais", pais)
                        elif opcion == 4:
                            grup = input("Introduzca e nuevo grupo: ").upper()
                            setattr(v, "grupo", grup)
                        elif opcion == 5:
                            can = input("Introduzca nueva canción: ").upper()
                            setattr(v,"cancion_favorita", can )
                        elif opcion == 6:
                            est = input("Introduzca el nuevo estilo: ").upper()
                            setattr(v, "estilo", est)
                        elif opcion == 7:
                            salir = True
                        
                        else:
                             print ("Debe de introducir un número entre 1 y 7")
        else:
            print("El dni no se encuentra de la lista de amigos")
                        
        
    



    