from controllers.renameVideo_controller import renombrar

# Ejemplo simple de uso

def ejemplo():
    # Ejemplo: Renombrar todos los archivos de una carpeta de serie
    carpeta = r"Y:\series\gameOfThrone\temporada_1"
    nombre_base = "goth"
    
    # Esto renombraría:
    # S01E01.Winter.Is.Coming.molpol.mkv → Game_of_Thrones_S01E_1.mkv
    # S01E02.The.Kingsroad.mkv → Game_of_Thrones_S01E_2.mkv
    # S01E03.Lord.Snow.mkv → Game_of_Thrones_S01E_3.mkv
    # etc.
    
    renombrar(carpeta, nombre_base)

if __name__ == "__main__":
    # Ejemplo directo
    carpeta = input("Ruta de la carpeta: ")
    nombre = input("Nombre base (ej: Serie_S01E): ")
    renombrar(carpeta, nombre)