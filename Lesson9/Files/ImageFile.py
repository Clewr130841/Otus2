import MediaFile
import datetime

class ImageFile(MediaFile):
    def __init__(self, name: str, size: int, creation_date: datetime, owner: str, resolution: str, color_depth: int):
        super().__init__(name, size, creation_date, owner)
        self.resolution = resolution  # Разрешение изображения
        self.color_depth = color_depth  # Глубина цвета (бит на пиксель)

    def save(self):
        """
        Сохранить изображение на диске или в облаке.
        """
        print(f"Сохранение изображения {self.name}")

    def delete(self):
        """
        Удалить изображение.
        """
        print(f"Удаление изображения {self.name}")

    def convert(self, target_format: str):
        """
        Конвертировать изображение в другой формат (например, jpg -> png).
        """
        print(f"Конвертация изображения {self.name} в формат {target_format}")

    def extract_metadata(self):
        """
        Извлечь мета-данные изображения.
        """
        return {
            "resolution": self.resolution,
            "color_depth": self.color_depth,
        }
