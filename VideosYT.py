from yt_dlp import YoutubeDL
from sys import argv

# Obtener el enlace del video desde los argumentos de la línea de comandos
link = argv[1]

# Función para mostrar el progreso de la descarga
def on_progress(d):
    """Función para mostrar el progreso de la descarga."""
    if d['status'] == 'downloading':
        print(f"Descargando... {d['_percent_str']} completado")

# Configuración de yt-dlp para 1080p60 con audio en AAC
ydl_opts = {
    'outtmpl': 'C:/Users/57314/Desktop/Scripts_Piolas/Downloads_YT/%(title)s.%(ext)s',  # Ruta de descarga
    'progress_hooks': [on_progress],  # Barra de progreso
    'format': 'bestvideo[height<=1080][fps>=60]+bestaudio/best',  # Priorizar 1080p60
    'merge_output_format': 'mp4',  # Formato de salida
    'postprocessors': [
        {
            'key': 'FFmpegVideoConvertor',  # Convertir el video a MP4
            'preferedformat': 'mp4',
        },
    ],
}

def download_video():
    """Descargar el video en 1080p60 con audio."""
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def download_audio():
    """Descargar solo el audio en formato MP3."""
    audio_opts = {
        **ydl_opts,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(audio_opts) as ydl:
        ydl.download([link])

def download_captions():
    """Descargar subtítulos en español."""
    caption_opts = {
        **ydl_opts,
        'writesubtitles': True,
        'subtitleslangs': ['es'],# Subtítulos en español
        'writeautomaticsub': True,
        'skip_download': True,  # No descargar el video
        'postprocessors': [
            {
                'key': 'FFmpegSubtitlesConvertor',  # Convertir subtítulos a .txt
                'format': 'srt',  # Primero convertimos a SRT (formato intermedio)
            },
            {
                'key': 'FFmpegSubtitlesConvertor',  # Convertir SRT a TXT
                'format': 'txt',
            },
        ],
    }
    with YoutubeDL(caption_opts) as ydl:
        ydl.download([link])

def main():
    """Función principal para manejar la interacción del usuario."""
    print("¿Qué quieres hacer?")
    print("1. Descargar Video")
    print("2. Descargar Audio")
    print("3. Descargar Subtítulos")

    choice = input("Ingresa el número de la opción deseada (1/2/3): ")

    if choice == '1':
        download_video()
    elif choice == '2':
        download_audio()
    elif choice == '3':
        download_captions()
    else:
        print("Opción no válida. Por favor elige 1, 2 o 3.")

if __name__ == "__main__":
    main()