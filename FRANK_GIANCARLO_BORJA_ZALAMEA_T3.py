############################################################
#    Creacion de la carpeta con user SGA       #
############################################################

# Importación de librerías.
import os
from pathlib import Path

# Ruta de la carpeta a crear en el disco C:/
dir_user_sga = "C:/FBORJAZ";

# Verificar si la carpeta existe; de lo contrario, crearla
if not os.path.exists(dir_user_sga):
    print("La carpeta no existe. Se creará para que puedas continuar.");
    try:
        os.makedirs(dir_user_sga)
        print("La carpeta se ha creado correctamente.");
        print("Continúa con el desarrollo.");
    except Exception as err:
        print(f"Error del sistema. Por favor, solicita soporte: {str(err)}");
        exit();

############################################################
#    Creacion del archivo ModProv.txt      #
############################################################

# Ruta del archivo a crear y validar
ruta_ModProv_cont = Path("C:/FBORJAZ/ModProv.txt");
ruta_secc = Path("C:/FBORJAZ/ControlSecuencia.txt");

# Verificacion del a existencia de los archivos
if ruta_ModProv_cont.exists():
  print("El arvhivo ya existe, continuamos");
else:
    print("El archivo ModProv.txt no existe, pero se creará para que puedas continuar.");
    try:
        ruta_ModProv_cont.touch();
        print("El archivo ModProv.txt se ha creado correctamente.");
        print("Continúa con el desarrollo.");
    except Exception as err:
        print(f"Error del sistema, por favor, solicita soporte: {str(err)}");

############################################################
#        Obtiene la secuencia de control txt              #
############################################################

# Proceso para obtener la secuencia 
def prc_cntr_secc(iv_registro):
    on_secuencia = 0

    with open(ruta_secc, "r") as arvch_secc:
        for registros in arvch_secc:
            nomenclatura, secuencia = registros.strip().split(":");
            if nomenclatura == iv_registro:
                on_secuencia = int(secuencia) + 1
                break
    return on_secuencia

############################################################
#      Actualizacion de la secuencia en el txt      #
############################################################

# Actualizacion de la secuencia
def prc_upd_secuencia(iv_registro, in_secuencia):
    ov_mensaje = "";
    linea_file_sec = "";

    with open(ruta_secc, "r") as archv_secc:
        for registros in archv_secc:
            nomenclatura, secuencia = registros.strip().split(":");
            if nomenclatura == iv_registro:
                secuencia = str(in_secuencia);
            linea_file_sec += nomenclatura + ":" + secuencia + "\n"

    with open(ruta_secc, "w") as arch_secc_w:
        arch_secc_w.write(linea_file_sec);
        ov_mensaje = "Si";

    return ov_mensaje;

####################################
#     DICCIONARIO #
###################################

dcc_Provedor = {
    "IDProveedor": "",
    "Nombre_empresa": "",
    "Persona_contacto": "",
    "Direccion": "",
    "Teléfono": "",
    "Correo_electronico": "",
    "Categoria_productos": "",
    "Ciudad": "",
    "UsuarioIngreso": "",
    "FechaIngreso": "",
    "PcIngreso": "",
    "UsuarioModifica": "",
    "FechaModifica": "",
    "PcModifica": ""
}

print("Ingrese los datos de");
# Ingrese datos para el diccionario 
for clave in dcc_Provedor:
    if clave == "IDProveedor":
        print(f"{clave}: ---");
        valor = "---"
    else:
        valor = input(f"{clave}: ");
    dcc_Provedor[clave] = valor

# Ciclo padre para la condicional para guardar o no los datos
while True:
    lv_guardar = input("Desea Guardar los datos de S/N: ").upper();
    # Guarda los datos si escogue S
    if lv_guardar == "S":
      # Recupera la secuna desde el text
        ln_secc = 0;
        lv_nomenclatura = "Prov";
        ln_secc = prc_cntr_secc("Prov");

        # Guarda la información en el archivo txt
        with open(ruta_ModProv_cont, "a") as arch_user:
          # Crea la línea del registro con la nomenclatura y secuencia
            linea = f"IDProveedor{str(ln_secc)}:";
          # Recorre el diccionario
            for clave, valor in dcc_Provedor.items():
            # Si es la clave "000000000"
                if clave == "Nombre_empresa":
                # Agrega la nomenclatura y secuencia formateada
                    linea += f"{clave} = {lv_nomenclatura + str(ln_secc).zfill(4)},";
                else:
                    # Agrega la clave y valor al registro
                    linea += f"{clave} = {valor},";
            # Elimina la última coma y agrega un salto de línea
            linea = linea.rstrip(",") + "\n";
            # Escribe la línea en el archivo
            arch_user.write(linea);
      
        # Escribimos la secuencia una a 1
        lv_confirmacion = prc_upd_secuencia("Prov", ln_secc);

      # MEnsaje de confirmacaion para la actualizacion del control se secuencia
        if lv_confirmacion == "Si":
            print("La secuencia ha sido actualizada con éxito.");
        else:
            print("No se pudo actualizar la secuencia. Por favor comnicarse con soporte.");

        print("El registro del usuario ha sido actualizado.");
        break

    elif lv_guardar == "N":
        # No desea guardar
        print("Los datos no serán actualizados. El proceso fue cancelado.");
        break

    else:
        # No salimos del proceso hasta que seleccione algo correcto
        print("El sistema no se cierra hasta que escoja una opcion valida");


