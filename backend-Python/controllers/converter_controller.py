import subprocess
import os

def convert_mkv_to_mp4(input_file_path, output_file_path):
    """
    Convierte un archivo MKV a MP4 usando FFmpeg.

    Args:
        input_file_path (str): La ruta completa al archivo de entrada.
        output_file_path (str): La ruta completa deseada para el archivo MP4 de salida.
    """
    
    # Verifica si el archivo de entrada existe
    if not os.path.exists(input_file_path):
        print(f"Error: El archivo de entrada no se encontró en '{input_file_path}'")
        return False

    ffmpeg_command = [
        'ffmpeg',
        '-hide_banner',
        '-i', input_file_path,
        '-map', '0:v:0',          # primera pista de video
        '-map', '0:a:0',          # primera pista de audio
        '-c:v', 'libx264',        # H.264 para compatibilidad universal en MP4
        '-preset', 'fast',        # calidad/tiempo (puede ser 'medium' o 'fast')
        '-crf', '20',             # calidad; 18-23 es rango común
        '-c:a', 'aac',            # recodifica audio a AAC
        '-b:a', '256k',
        '-movflags', '+faststart',
        '-y',
        output_file_path
    ]

    print(f"Iniciando conversión de '{input_file_path}' a '{output_file_path}'...")
    try:
        # Ejecuta el comando FFmpeg
        # capture_output=True: Captura la salida estándar y de error
        # text=True: Decodifica la salida como texto
        # check=True: Lanza una excepción CalledProcessError si el comando retorna un código de error
        result = subprocess.run(ffmpeg_command, capture_output=True, text=True, check=True)
        
        print("Conversión completada exitosamente.")
        print("Salida de FFmpeg:")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error durante la conversión: {e}")
        print("Salida de error de FFmpeg:")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("Error: FFmpeg no se encontró. Asegúrate de que FFmpeg esté instalado y en tu PATH.")
        return False
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return False



# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Define la ruta del archivo MKV de entrada
    # Asegúrate de que esta ruta sea correcta en tu sistema
    input = 'Y:/series/pluribus/plr_1.mkv' 
    
    # Define la ruta para el archivo MP4 de salida
    # Puedes cambiar el nombre del archivo de salida si lo deseas
    output_mp4 = 'Y:/series/pluribus/plr_1.mp4' 
    # Asegúrate de que la carpeta de salida exista
    output_dir = os.path.dirname(output_mp4)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    success = convert_mkv_to_mp4(input, output_mp4)
    if success:
        print(f"El archivo '{output_mp4}' ha sido creado.")
    else:
        print("La conversión falló.")

