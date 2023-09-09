from pathlib import Path

# Rutas de archivos (constantes)
FL_RUTA_FILE = Path("A:\Visual Studio Code\SYSTEM/UserSystem.txt")
FL_RUTA_SECC = Path("A:\Visual Studio Code\SYSTEM/Control_Secuencia.txt")

# Funciones
def obtener_secuencia_registro(iv_registro):
    with open(FL_RUTA_SECC, "r") as archv_secc:
        for registros in archv_secc:
            nomenclatura, secuencia = registros.strip().split(":")
            if nomenclatura == iv_registro:
                return int(secuencia) + 1
    return 1  # Si no se encuentra el registro, se asume secuencia 1

def actualizar_secuencia_registro(iv_registro, in_secuencia):
    lineas = []
    with open(FL_RUTA_SECC, "r") as archv_secc:
        for registros in archv_secc:
            nomenclatura, secuencia = registros.strip().split(":")
            if nomenclatura == iv_registro:
                secuencia = str(in_secuencia)
            lineas.append(f"{nomenclatura}:{secuencia}\n")

    with open(FL_RUTA_SECC, "w") as archiv_secc_w:
        archiv_secc_w.writelines(lineas)
    return True

def guardar_usuario(dcc_usuario):
    ln_secuencia = obtener_secuencia_registro("Us")
    usuario_codigo = f"Us{ln_secuencia:04}"

    with open(FL_RUTA_FILE, "a") as arch_user:
        linea = f"Usuario{ln_secuencia}:"
        for clave, valor in dcc_usuario.items():
            if clave == "Cod_Usuario":
                linea += f"{clave} = {usuario_codigo},"
            else:
                linea += f"{clave} = {valor},"
        linea = linea.rstrip(",") + "\n"
        arch_user.write(linea)

    if actualizar_secuencia_registro("Us", ln_secuencia):
        print("La secuencia ha sido actualizada con éxito.")
        print("El registro del usuario ha sido actualizado.")
    else:
        print("No se pudo actualizar la secuencia, informar a sistemas.")

# Diccionario para almacenar los datos del usuario
dcc_user_system = {
    "Cod_Usuario": "",
    "Nombre_Usuario": "",
    "Password": "",
    "Cod_Rol": "",
    "Estado": ""
}

# Inicio del sistema
print("Ingrese los datos del usuario:")
# Ingresar datos desde teclado
for clave in dcc_user_system:
    if clave == "Cod_Usuario":
        print(f"{clave}: ---")
        valor = "---"
    else:
        valor = input(f"{clave}: ")
    dcc_user_system[clave] = valor

while True:
    lv_guardar = input("Desea guardar los datos del usuario? (S/N): ").upper()
    if lv_guardar == "S":
        guardar_usuario(dcc_user_system)
        break
    elif lv_guardar == "N":
        # No desea guardar
        print("Los registros no serán actualizados, el proceso fue cancelado.")
        break
    else:
        # No salimos del proceso hasta que seleccione algo correcto
        print("Por favor, seleccione una opción válida (S/N).")
