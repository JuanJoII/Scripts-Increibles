from cryptography.fernet import Fernet
from tkinter import filedialog, Tk

#Genera una clave
def generar_clave():
    global clave_global
    clave = Fernet.generate_key()
    archivo_clave = filedialog.asksaveasfilename(
        title="Guardar clave",
        defaultextension=".key",
        filetypes=[("Archivos de clave", "*.key")]
    )
    if archivo_clave:
        with open(archivo_clave, "wb") as f:
            f.write(clave)
        clave_global = clave
        print(f"Clave generada y guardada en: {archivo_clave}") 

# Cargar la clave desde un archivo
def cargar_clave():
    global clave_global
    archivo_clave = filedialog.askopenfilename(
        title="Cargar clave",
        filetypes=[("Archivos de clave", "*.key")]
    )
    if archivo_clave:
        with open(archivo_clave, "rb") as f:
            clave_global = f.read()
        print("Clave cargada correctamente.")
    else:
        print("No se seleccionó ninguna clave.")

# Encriptar un archivo
def encriptar_archivo():
    global clave_global
    if not clave_global:
        print("Por favor, carga o genera una clave antes de encriptar.")
        return

    archivo_a_encriptar = filedialog.askopenfilename(
        title="Seleccionar archivo a encriptar"
    )
    if archivo_a_encriptar:
        fernet = Fernet(clave_global)
        with open(archivo_a_encriptar, "rb") as f:
            datos = f.read()

        datos_encriptados = fernet.encrypt(datos)

        archivo_encriptado = filedialog.asksaveasfilename(
            title="Guardar archivo encriptado",
            defaultextension=".txt",
            filetypes=[("Archivos encriptados", "*.txt")]
        )
        if archivo_encriptado:
            with open(archivo_encriptado, "wb") as f:
                f.write(datos_encriptados)
            print(f"Archivo encriptado y guardado en: {archivo_encriptado}")

# Desencriptar un archivo
def desencriptar_archivo():
    global clave_global
    if not clave_global:
        print("Por favor, carga o genera una clave antes de desencriptar.")
        return

    archivo_a_desencriptar = filedialog.askopenfilename(
        title="Seleccionar archivo a desencriptar",
        filetypes=[("Archivos encriptados", "*.enc")]
    )
    if archivo_a_desencriptar:
        fernet = Fernet(clave_global)
        with open(archivo_a_desencriptar, "rb") as f:
            datos_encriptados = f.read()

        try:
            datos_desencriptados = fernet.decrypt(datos_encriptados)
            archivo_desencriptado = filedialog.asksaveasfilename(
                title="Guardar archivo desencriptado",
                defaultextension=".txt"
            )
            if archivo_desencriptado:
                with open(archivo_desencriptado, "wb") as f:
                    f.write(datos_desencriptados)
                print(f"Archivo desencriptado y guardado en: {archivo_desencriptado}")
        except Exception as e:
            print(f"Error al desencriptar el archivo: {e}")

# Función principal
if __name__ == "__main__":
    Tk().withdraw()

    while True:
        # Menú de opciones
        print("\nOpciones:")
        print("1. Generar clave")
        print("2. Cargar clave desde un archivo")
        print("3. Encriptar archivo")
        print("4. Desencriptar archivo")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            generar_clave()
        elif opcion == "2":
            cargar_clave()
        elif opcion == "3":
            encriptar_archivo()
        elif opcion == "4":
            desencriptar_archivo()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
