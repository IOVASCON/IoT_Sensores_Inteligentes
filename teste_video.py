import os

# Verificar se o arquivo de vídeo existe no diretório especificado
video_path = "L:\VSCode\PYTHON\DIO\IoT_Sensores_Inteligentes/data/videos/input_video.mp4"
if os.path.exists(video_path):
    print("O arquivo de vídeo existe.")
else:
    print("O arquivo de vídeo não foi encontrado.")
