import os
from converter_controller import convert_mkv_to_mp4

# Carpeta a recorrer
folder_path = "Y:/series/pluribus/temporada_1"
    
# Recorremos todos los archivos de la carpeta
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".mkv"):
        # Ruta completa del archivo de entrada
        input_file_path = os.path.join(folder_path, filename)

        # Definir ruta de salida (misma base, extensión .mp4)
        output_file_path = os.path.splitext(input_file_path)[0] + ".mp4"

        # Ejecutar la función del convertidor
        try:
            convert_mkv_to_mp4(input_file_path, output_file_path)
            print(f"✔ Convertido: {filename} → {output_file_path}")
        except Exception as e:
            print(f"✘ Error al convertir {filename}: {e}")
