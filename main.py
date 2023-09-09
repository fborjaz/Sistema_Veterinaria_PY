from pathlib import Path

# Constante para la ruta del archivo de trabajo
Lf_File_Rute = Path("A:\Visual Studio Code\SYSTEM/UserSystem.txt")

def func_bienvenida():
    print("********************************************")
    print("¡Bienvenido al sistema de veterinaria UNEMI!")
    print("********************************************")

def func_obtener_nombre():
    Lf_nombre = input("Por favor, ingresa tu nombre: ")
    while not Lf_nombre:
        print("Nombre inválido. Inténtalo nuevamente.")
        Lf_nombre = input("Por favor, ingresa tu nombre: ")
    return Lf_nombre

def func_verificar_archivo(ruta_archivo):
    return ruta_archivo.exists()

def func_mostrar_menu():
    print("1. Ver pacientes")
    print("2. Agregar paciente")
    print("3. Registrar cita")
    print("4. Ver citas")
    print("5. Salir")

def main():
    func_bienvenida()
    Lf_nombre = func_obtener_nombre()
    print(f"¡Hola, {Lf_nombre}! Bienvenido al sistema de veterinaria UNEMI.")

    try:
        if func_verificar_archivo(Lf_File_Rute):
            print("¡Bienvenido! El sistema está listo para su uso.")
            # Aquí puedes continuar con el menú y la funcionalidad principal del sistema.
            # Puedes utilizar funciones y clases para manejar diferentes acciones.
        else:
            print("El sistema no se encuentra instalado correctamente.")
            print("Favor, contactese con el desarrollador.")
            print("Al número: 0988888888.")
            print("Al correo: contactos@unemi.edu.ec.")
    
    except Exception as Lf_err:
        print(f"Error del sistema, solicite soporte: {str(Lf_err)}")

if __name__ == "__main__":
    main()
