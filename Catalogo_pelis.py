#Catalogo de peliculas por Daniela Calderón.

import os  #archivos en la compu
class Pelicula: #Primera clase: atributos privados
    def __init__(self, nombre, director, año, genero):
        self.__nombre = nombre
        self.__director = director
        self.__año = año
        self.__genero = genero
   
    def __str__(self):
        return f"{self.__nombre} ({self.__director} {self.__año} {self.__genero})"
   
    def get_nombre(self):
        return self.__nombre
   
    def get_director(self):
        return self.__director

    def get_año(self):
        return self.__año
   
    def get_genero(self):
        return self.__genero
   
class CatalogoPeliculas: #Segunda clase: atributo nombre, ruta_archivo y metodos (agregar, listar y eliminar)
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w") as archivo:
                pass 
    
    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo, "a") as archivo:
          archivo.write(f"{pelicula.get_nombre()},{pelicula.get_director()},{pelicula.get_año()},{pelicula.get_genero()}\n")
        print(f"Pelicula '{pelicula.get_nombre()}' agregada al catalogo.")

    def listar_peliculas(self):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "r") as archivo:
                peliculas = archivo.readlines()
                if peliculas:
                    print("Peliculas en el catalogo: ")
                    for pelicula in peliculas:
                        print(pelicula.strip())
                else:
                    print("No hay peliculas en el catalogo.")
        else:
            print("El catalogo no existe.")
    
    def listar_genero(self):
        peliculas_genero = {}
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "r") as archivo:
                peliculas = archivo.readlines()
                for pelicula in peliculas:
                    nombre, director, año, genero = [campo.strip() for campo in pelicula.strip().split(",")]
                    if genero not in peliculas_genero:
                        peliculas_genero[genero] = []
                    peliculas_genero[genero].append(f"{nombre} ({director} {año})")
            if peliculas_genero:
                print("Peliculas por genero: ")
                for genero, nombres in peliculas_genero.items():
                    print(f"{genero}:")
                    for nombre in nombres:
                        print(f" - {nombre}")
            else:
                print("No hay peliculas en el catalogo")
        else:
            print("El catalogo no existe")

    def eliminar_peliculas(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print("catalogo eliminado")
        else:
            print("El catalogo no existe")

def mostrar_menu(): #opciones a  mostrar
    print("\nBienvenido al catalogo de peliculas!\n")
    
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catalogo de películas")
    print("4. Listar peliculas por genero")
    print("5. Salir")

def main():  #condiciones para el funcionamiento del catalogo
    nombre_catalogo = input("Ingrese el nombre del catalogo de peliculas:")
    catalogo = CatalogoPeliculas(nombre_catalogo)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            director = input("Ingrese el nombre del director: ")
            año = input("Ingrese el año de estreno: ")
            genero = input("Ingrese el genero: ")
            pelicula = Pelicula(nombre, director, año, genero)
            catalogo.agregar_pelicula(pelicula)
        elif opcion == "2":
            catalogo.listar_peliculas()
        elif opcion == "3":
            catalogo.eliminar_peliculas()
        elif opcion == "4":
            catalogo.listar_genero()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
   main()