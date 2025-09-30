# PIA PROGRAMACION

class Calificaciones:
    def __init__(self):
        self.lista = []

    # 1. Agregar calificación
    def agregar(self):
        try:
            calificacion = float(input("Ingresa la calificación (0 - 100): "))
            if 0 <= calificacion <= 100:
                self.lista.append(calificacion)
                print("Calificación agregada correctamente.")
            else:
                print("Ingresa un valor entre 0 y 100.")
        except ValueError:
            print("Ingresa un número válido.")

    # 2. Mostrar calificaciones
    def mostrar(self):
        if self.lista:
            print("\n Lista de calificaciones:")
            for i, c in enumerate(self.lista, 1):
                print(f"{i}. {c}")
        else:
            print("\n No hay calificaciones registradas.")

    # 3. Calcular promedio
    def promedio(self):
        if self.lista:
            prom = sum(self.lista) / len(self.lista)
            print(f"\n El promedio es: {prom:.2f}")
        else:
            print("\n No hay calificaciones para calcular el promedio.")

    # 4. Eliminar todas las calificaciones
    def limpiar(self):
        self.lista.clear()
        print("Todas las calificaciones han sido eliminadas.")

class Programa:
    def __init__(self):
        self.calificaciones = Calificaciones()

    def menu(self):
        while True:
            print("\n--- MENÚ DE CALIFICACIONES ---")
            print("1. Agregar calificación")
            print("2. Mostrar calificaciones")
            print("3. Calcular promedio")
            print("4. Eliminar todas las calificaciones")
            print("5. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.calificaciones.agregar()
            elif opcion == "2":
                self.calificaciones.mostrar()
            elif opcion == "3":
                self.calificaciones.promedio()
            elif opcion == "4":
                self.calificaciones.limpiar()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")


app = Programa()
app.menu()
