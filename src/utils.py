import os
import cv2
import numpy as np

# Função para carregar uma imagem e realizar pré-processamento
def load_and_preprocess_image(image_path, target_size=(416, 416)):
    # Carregar a imagem usando OpenCV
    image = cv2.imread(image_path)

    # Redimensionar a imagem para o tamanho alvo
    image = cv2.resize(image, target_size)

    # Converter imagem para array de NumPy
    image = np.array(image)

    # Normalizar os valores dos pixels para a faixa [0, 1]
    image = image / 255.0

    return image

# Função para salvar a imagem processada
def save_image(image, output_path):
    # Reverter a normalização
    image = np.clip(image * 255, 0, 255).astype(np.uint8)

    # Salvar a imagem usando OpenCV
    cv2.imwrite(output_path, image)

# Função para listar arquivos em um diretório
def list_files_in_directory(directory, file_extension=".jpg"):
    # Listar arquivos com a extensão fornecida no diretório especificado
    files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
    return files

# Exemplo de uso
if __name__ == "__main__":
    image_path = "data/images/sample_image.jpg"  # Caminho da imagem
    output_image_path = "data/images/processed_image.jpg"

    # Carregar e pré-processar a imagem
    image = load_and_preprocess_image(image_path)

    # Salvar a imagem processada
    save_image(image, output_image_path)

    # Listar arquivos .jpg na pasta de imagens
    image_files = list_files_in_directory("data/images")
    print(image_files)
