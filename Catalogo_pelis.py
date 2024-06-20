#Catalogo de peliculas por Daniela Calderón.

import os

def mostrar_menu():
    print("\nBienvenido al catalogo de peliculas")
    print("Elige una opción")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo de películas")
    print("4. Salir")
    opcion = input()

def main():
    nombre_catalogo = input("Ingrese el nombre del catalogo de peliculas:")
    catalogo = CatalogoPeliculas(nombre_catalogo)

    while True:
        mostrar_menu()
        if opcion == "1":
            catalogo.agregar_pelicula()
        elif opcion == "2":
            catalogo.listar_peliculas()
        elif opcion == "3":
            catalogo.eliminar_catalogo()
        elif opcion == "4":
            break
        else:
            print("Opcion invalida")
