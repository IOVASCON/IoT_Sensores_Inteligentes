import cv2

# Caminho do vídeo
video_path = "L:/VSCode/ARDUINO/Sensores_Inteligentes/data/videos/input_video.mp4"

# Tenta abrir o vídeo
cap = cv2.VideoCapture(video_path)

# Verifica se conseguiu abrir o vídeo
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
else:
    print("Vídeo aberto com sucesso.")

    # Lê o primeiro frame do vídeo
    ret, frame = cap.read()
    if ret:
        print("Frame capturado com sucesso.")
    else:
        print("Erro ao capturar frame.")

    cap.release()
