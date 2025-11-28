from pathlib import Path

def renombrar_archivos_en_misma_carpeta():
    # Carpeta donde está este script
    carpeta_path = Path(__file__).parent
    script_name = Path(__file__).name  # para NO renombrar este archivo

    print(f"Carpeta de trabajo: {carpeta_path}")

    for archivo in carpeta_path.iterdir():
        # Solo archivos, y que no sea el propio script
        if archivo.is_file() and archivo.name != script_name:
            nombre_actual = archivo.stem      # sin extensión
            extension = archivo.suffix        # con el punto, ej: ".html"

            # nuevo nombre: todo en minúsculas + guion antes de la extensión
            nuevo_nombre = nombre_actual.lower() + "-" + extension.lower()
            nuevo_path = archivo.with_name(nuevo_nombre)

            if nuevo_path.exists():
                print(f"⚠️ Saltando '{archivo.name}' → '{nuevo_nombre}' (ya existe)")
                continue

            print(f"Renombrando: '{archivo.name}' → '{nuevo_nombre}'")
            archivo.rename(nuevo_path)

if __name__ == "__main__":
    renombrar_archivos_en_misma_carpeta()
