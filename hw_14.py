"""
hw_14: В данном задании вы проведете рефакторинг предоставленного кода для сжатия изображений, применяя принципы инкапсуляции объектно-ориентированного программирования (ООП). Вы создадите класс `ImageCompressor`, который будет инкапсулировать логику сжатия изображений и обработки директорий, а также улучшите структуру кода, сделав его более гибким и модульным.
"""

import os
from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener


class ImageCompressor:
    """
    Класс для сжатия изображений в формат HEIF.
    """
    supported_formats = ('.jpg', '.jpeg', '.png', '.jfif')
    
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
    
    
