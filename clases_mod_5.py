
class Amigos():

    def __init__(self, nombre, dni, poblacion, pais ):
        self.nombre = nombre
        self.dni = dni
        self.poblacion = poblacion
        self.pais = pais
        
class Gustos():
    
    def __init__(self, grupo, cancion_favorita, estilo):
        self.grupo= grupo
        self.cancion_favorita = cancion_favorita
        self.estilo = estilo

class Gusto_amigos(Amigos, Gustos):

    def __init__(self, nombre, dni, poblacion, pais, grupo, cancion_favorita, estilo):
        Amigos.__init__(self, nombre, dni, poblacion, pais)
        Gustos.__init__(self, grupo, cancion_favorita, estilo)
        
    
    def __str__(self):
        return "{:<20.20} {:10} {:<15.15} {:<10.10} {:<20.20} {:<15.15} {:<15.15}".format(self.nombre, self.dni, self.poblacion, self.pais,
                     self.grupo, self.cancion_favorita, self.estilo)
            
    #Hacemos iterables gusto amigos.
    def __iter__(self):
        lista = [self.nombre, self.dni, self.poblacion, self.pais, self.grupo, self.cancion_favorita, self.estilo]
        return iter(lista)

    def __getitem__(self, m):
        lista = [self.nombre, self.dni, self.poblacion, self.pais, self.grupo, self.cancion_favorita, self.estilo]
        return lista[m]

    
    def imprimir(self):
        print("="*50)
        print("Nombre: {}    DNI: {}".format(self.nombre, self.dni))     
        print("="*50)
        print("\n")
        

        