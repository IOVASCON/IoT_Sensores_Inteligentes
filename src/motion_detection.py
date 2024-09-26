import os
import cv2

# Função para detectar movimento em um vídeo
def detect_motion_in_video(input_video_path, output_video_path):
    # Verificar se o diretório de saída existe, se não, criar
    output_dir = os.path.dirname(output_video_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Capturar o vídeo de entrada
    cap = cv2.VideoCapture(input_video_path)

    # Verificar se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Obter o primeiro frame do vídeo para usar como referência
    ret, first_frame = cap.read()
    if not ret:
        print("Erro ao ler o primeiro frame do vídeo.")
        return

    # Converter o primeiro frame para escala de cinza e aplicar desfoque
    first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    first_gray = cv2.GaussianBlur(first_gray, (21, 21), 0)

    # Definir o codec e criar o objeto para salvar o vídeo de saída
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    # Criar diretório para salvar frames como imagens, se não existir
    frames_dir = os.path.join(output_dir, "frames")
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)

    # Inicializar o contador de frames
    frame_number = 0

    while True:
        # Ler o frame atual do vídeo
        ret, frame = cap.read()
        if not ret:
            break

        # Converter o frame para escala de cinza e aplicar desfoque
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # Calcular a diferença absoluta entre o primeiro frame e o frame atual
        delta_frame = cv2.absdiff(first_gray, gray)

        # Aplicar um limiar binário para destacar as diferenças
        thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

        # Encontrar contornos das áreas com movimento
        contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Desenhar retângulos ao redor dos contornos detectados
        for contour in contours:
            if cv2.contourArea(contour) < 1000:
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Mostrar o frame com as áreas de movimento destacadas
        cv2.imshow("Detecção de Movimento", frame)

        # Salvar o frame como uma imagem
        frame_filename = os.path.join(frames_dir, f"frame_{frame_number}.jpg")
        cv2.imwrite(frame_filename, frame)

        # Salvar o frame no vídeo de saída
        out.write(frame)

        # Incrementar o contador de frames
        frame_number += 1

        # Parar se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar os objetos de captura e gravação
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Exemplo de uso
if __name__ == "__main__":
    input_video = "L:/VSCode/ARDUINO/Sensores_Inteligentes/data/videos/input_video.mp4"  # Defina o caminho do vídeo de entrada
    output_video = "L:/VSCode/ARDUINO/Sensores_Inteligentes/data/videos/output_video.avi"  # Defina o caminho para o vídeo de saída

    detect_motion_in_video(input_video, output_video)
