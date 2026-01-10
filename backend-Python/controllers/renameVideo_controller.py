import os
from pathlib import Path

def renombrar(path_carpeta, nombre_nuevo):
    """
    Renombra todos los archivos de una carpeta secuencialmente
    
    Args:
        path_carpeta (str): Ruta de la carpeta que contiene los archivos
        nombre_nuevo (str): Nombre base para los archivos (sin extensión)
    
    Returns:
        bool: True si todo se renombró exitosamente
    """
    try:
        carpeta = Path(path_carpeta)
        
        # Verificar que la carpeta existe
        if not carpeta.exists():
            print(f"Error: La carpeta '{path_carpeta}' no existe")
            return False
        
        if not carpeta.is_dir():
            print(f"Error: '{path_carpeta}' no es una carpeta")
            return False
        
        # Obtener todos los archivos y ordenarlos por nombre
        archivos = [f for f in carpeta.iterdir() if f.is_file()]
        archivos = sorted(archivos, key=lambda x: x.name.lower())
        
        if not archivos:
            print("No hay archivos en la carpeta")
            return False
        
        print(f"Se encontraron {len(archivos)} archivos")
        
        # Renombrar cada archivo
        exitosos = 0
        for i, archivo in enumerate(archivos, 1):
            extension = archivo.suffix
            nuevo_nombre = f"{nombre_nuevo}_{i}{extension}"
            nuevo_path = carpeta / nuevo_nombre
            
            # Verificar si ya existe un archivo con ese nombre
            if nuevo_path.exists():
                print(f"Advertencia: Ya existe '{nuevo_nombre}', saltando...")
                continue
            
            try:
                archivo.rename(nuevo_path)
                print(f"Renombrado: '{archivo.name}' → '{nuevo_nombre}'")
                exitosos += 1
            except OSError as e:
                print(f"Error al renombrar '{archivo.name}': {e}")
        
        print(f"\nProceso completado: {exitosos}/{len(archivos)} archivos renombrados")
        return exitosos == len(archivos)
        
    except Exception as e:
        print(f"Error general: {e}")
        return False

# Ejemplo de uso
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 3:
        # Uso: python renameVideo_controller.py "C:\ruta\carpeta" "NuevoNombre"
        path_carpeta = sys.argv[1]
        nombre_nuevo = sys.argv[2]
        renombrar(path_carpeta, nombre_nuevo)
    else:
        # Modo interactivo
        path_carpeta = input("Ingresa la ruta de la carpeta: ").strip()
        nombre_nuevo = input("Ingresa el nombre base para los archivos: ").strip()
        renombrar(path_carpeta, nombre_nuevo)