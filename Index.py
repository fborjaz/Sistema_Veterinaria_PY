import tkinter as tk
from pathlib import Path

# 1. Definimos la ruta de trabajo y archivo de arranque
FL_RUTA_FILE = Path("A:\Visual Studio Code\SYSTEM/UserSystem.txt")
FL_RUTA_SECC = Path("A:\Visual Studio Code\SYSTEM/Control_Secuencia.txt")

# Funciones para manejar el registro del usuario
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

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Veterinaria UNEMI")
ventana.geometry("800x500")

# Etiqueta de bienvenida
etiqueta_bienvenida = tk.Label(ventana, text="¡Bienvenido al sistema de veterinaria UNEMI!")
etiqueta_bienvenida.pack()

# Solicitar los datos del usuario
dcc_user_system = {
    "Cod_Usuario": "",
    "Nombre_Usuario": "",
    "Password": "",
    "Cod_Rol": "",
    "Estado": ""
}

def guardar_datos():
    dcc_user_system["Nombre_Usuario"] = nombre_usuario.get()
    dcc_user_system["Password"] = password.get()
    dcc_user_system["Cod_Rol"] = cod_rol.get()
    dcc_user_system["Estado"] = estado.get()

    secuencia_actual = obtener_secuencia_registro("Us")
    dcc_user_system["Cod_Usuario"] = f"Us{secuencia_actual:04}"

    guardar_usuario(dcc_user_system)
    etiqueta_confirmacion.config(text="¡Usuario registrado con éxito!")

# Solicitar el nombre del usuario
nombre_usuario = tk.StringVar()
etiqueta_nombre = tk.Label(ventana, text="Nombre de Usuario:")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana, textvariable=nombre_usuario)
entrada_nombre.pack()

# Solicitar la contraseña
password = tk.StringVar()
etiqueta_password = tk.Label(ventana, text="Contraseña:")
etiqueta_password.pack()
entrada_password = tk.Entry(ventana, textvariable=password, show="*")
entrada_password.pack()

# Solicitar el código de rol
cod_rol = tk.StringVar()
etiqueta_cod_rol = tk.Label(ventana, text="Rol del usuario:")
etiqueta_cod_rol.pack()
entrada_cod_rol = tk.Entry(ventana, textvariable=cod_rol)
entrada_cod_rol.pack()

# Solicitar el estado
estado = tk.StringVar()
etiqueta_estado = tk.Label(ventana, text="Estado:")
etiqueta_estado.pack()
entrada_estado = tk.Entry(ventana, textvariable=estado)
entrada_estado.pack()

# Botón para guardar los datos
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
boton_guardar.pack()

# Etiqueta de confirmación
etiqueta_confirmacion = tk.Label(ventana, text="")
etiqueta_confirmacion.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
