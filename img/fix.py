from pathlib import Path

def reemplazar_guion_punto():
    # Carpeta donde está este script
    carpeta_path = Path(__file__).parent
    script_name = Path(__file__).name  # nombre del propio script

    print(f"Carpeta de trabajo: {carpeta_path}")

    for archivo in carpeta_path.iterdir():
        if archivo.is_file() and archivo.name != script_name:
            nombre_actual = archivo.name

            # Nuevo nombre reemplazando '-.' por '.'
            nuevo_nombre = nombre_actual.replace("-.", ".")

            # Si no hay cambio, continuar
            if nuevo_nombre == nombre_actual:
                continue

            nuevo_path = archivo.with_name(nuevo_nombre)

            # Evitar sobreescribir archivos existentes
            if nuevo_path.exists():
                print(f"⚠️ Saltando '{nombre_actual}' → '{nuevo_nombre}' (ya existe un archivo con ese nombre)")
                continue

            print(f"Renombrando: '{nombre_actual}' → '{nuevo_nombre}'")
            archivo.rename(nuevo_path)

if __name__ == "__main__":
    reemplazar_guion_punto()
