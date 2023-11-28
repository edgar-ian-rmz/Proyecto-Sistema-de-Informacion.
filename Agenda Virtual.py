class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class SistemaDeInformacion:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def listar_contactos(self):
        print("Lista de Contactos:")
        for i, contacto in enumerate(self.contactos):
            print(f"{i + 1}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return
        print(f"No se encontró un contacto con el nombre {nombre}")

    def borrar_contacto(self, indice):
        if 0 <= indice < len(self.contactos):
            del self.contactos[indice]
            print("Contacto eliminado con éxito.")
        else:
            print("Índice de contacto no válido.")

def main():
    print("Bienvenido a tu Agenda Electrónica")

    sistema = SistemaDeInformacion()

    while True:
        print("\nOpciones:")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto por nombre")
        print("4. Borrar contacto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono (10 dígitos): ")
            if len(telefono) != 10:
                print("El número de teléfono debe contener 10 dígitos.")
                continue

            email = input("Email (debe incluir '@'): ")
            if "@" not in email:
                print("La dirección de correo electrónico no es valido.")
                continue

            contacto = Contacto(nombre, telefono, email)
            sistema.agregar_contacto(contacto)
            print("Contacto agregado con éxito.")
        elif opcion == "2":
            sistema.listar_contactos()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto que desea buscar: ")
            sistema.buscar_contacto(nombre)
        elif opcion == "4":
            if len(sistema.contactos) == 0:
                print("No existen contactos para borrar.")
            else:
                sistema.listar_contactos()
                indice = int(input("Ingrese el número del contacto que desea eliminar: ")) - 1
                sistema.borrar_contacto(indice)
        elif opcion == "5":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
