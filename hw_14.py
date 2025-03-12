"""
hw_14: В данном задании вы проведете рефакторинг предоставленного кода для сжатия изображений, применяя принципы инкапсуляции объектно-ориентированного программирования (ООП). Вы создадите класс `ImageCompressor`, который будет инкапсулировать логику сжатия изображений и обработки директорий, а также улучшите структуру кода, сделав его более гибким и модульным.
"""

import os
from typing import *
from PIL import Image
from pillow_heif import register_heif_opener


class ImageCompressor:
    """
    Класс для сжатия изображений в формат HEIF.
    """
    supported_formats: Tuple[str, ...] = ('.jpg', '.jpeg', '.png', '.jfif')
    
    def __init__(self, quality: int = 60) -> None:
        """
        Инициализирует ImageCompressor с заданным качеством сжатия.

        Args:
            quality (int): Качество сжатия (0-100). По умолчанию 50.
        """
        self.quality = quality
        
        
    @property
    def quality(self) -> int:
        """
        Возвращает качество сжатия.

        Returns:
            int: Качество сжатия.
        """
        return self.__quality
    
    
    @quality.setter
    def quality(self, quality: int) -> None:
        """
        Устанавливает качество сжатия.

        Args:
            quality (int): Новое качество сжатия (0-100).
        """
        if 0 <= quality <= 100:
            self.__quality = quality
        else:
            raise ValueError('Качество должно быть в диапазоне от 0 до 100')

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает одно изображение и сохраняет его в формате HEIF.

        Args:
            input_path (str): Путь к исходному изображению.
            output_path (str): Путь для сохранения сжатого изображения.
        """
        try:
            with Image.open(input_path) as img:
                img.save(output_path, "HEIF", quality=self.quality)
                print(f"Сжато: {input_path} -> {output_path}")
        except Exception as e:
            print(f"Ошибка при сжатии {input_path}: {e}")
    
    
    def process_directory(self,directory: str) -> NoReturn:
        """
        Рекурсивно обрабатывает все изображения в директории и её поддиректориях.

        Args:
            directory (str): Путь к директории для обработки.
        """
        for root, _, files in os.walk(directory):
            for file in files:
            # Проверяем расширение файла
                if file.lower().endswith(self.supported_formats ):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)
                
                
    def main(input_path: str) -> NoReturn:
        """
        Основная функция для обработки пользовательского ввода и запуска сжатия изображений.

        Args:
        input_path (str): Путь к файлу или директории для обработки.
        """
        register_heif_opener()
        compressor = ImageCompressor(quality=60)
        input_path = input_path.strip('"')  # Удаляем кавычки, если они есть
    
        if os.path.exists(input_path):
            if os.path.isfile(input_path):
                # Если указан путь к файлу, обрабатываем только этот файл
                print(f"Обрабатываем файл: {input_path}")
                output_path = os.path.splitext(input_path)[0] + '.heic'
                compressor.compress_image(input_path, output_path)
                
            elif os.path.isdir(input_path):
            # Если указан путь к директории, обрабатываем все файлы в ней
                print(f"Обрабатываем директорию: {input_path}")
                compressor.process_directory(input_path)
            # Функция process_directory рекурсивно обойдет все поддиректории
            # и обработает все поддерживаемые изображения
        else:
            print("Указанный путь не существует")
        

if __name__ == "__main__":
    user_input: str = input("Введите путь к файлу или директории: ")
    ImageCompressor.main(user_input)
