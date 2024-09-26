from imageai.Detection import VideoObjectDetection
import os
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

# Função para detecção de objetos em vídeos
def detect_objects_in_video(input_video_path, output_video_path, model_path, frames_per_second=20):
    # Criação da instância do detector de vídeo
    detector = VideoObjectDetection()

    # Definindo o tipo de modelo como YOLOv3
    detector.setModelTypeAsYOLOv3()

    # Definindo o caminho do modelo YOLO
    detector.setModelPath(model_path)

    # Carregando o modelo
    detector.loadModel()

    # Iniciando a detecção de objetos no vídeo de entrada
    video_path = detector.detectObjectsFromVideo(
        input_file_path=input_video_path,
        output_file_path=output_video_path,
        frames_per_second=frames_per_second,
        log_progress=True
    )

    print(f"Video saved at {video_path}")
    return video_path

# Exemplo de uso
if __name__ == "__main__":
    input_video = "L:\VSCode\PYTHON\DIO\IoT_Sensores_Inteligentes/data/videos/input_video.mp4"  # Defina o caminho do vídeo de entrada
    output_video = "L:\VSCode\PYTHON\DIO\IoT_Sensores_Inteligentes/data/videos/output_video.mp4"    # Caminho para o vídeo de saída
    model_path = 'L:\VSCode\PYTHON\DIO\IoT_Sensores_Inteligentes/data/models/yolo.h5'   # Caminho para o modelo YOLO

    detect_objects_in_video(input_video, output_video, model_path)
