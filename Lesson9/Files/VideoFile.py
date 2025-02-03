import MediaFile
import datetime


class VideoFile(MediaFile):
    def __init__(self, name: str, size: int, creation_date: datetime, owner: str, resolution: str, duration: float):
        super().__init__(name, size, creation_date, owner)
        self.resolution = resolution  # Разрешение видео
        self.duration = duration  # Длительность в секундах

    def save(self):
        """
        Сохранить видеофайл на диске или в облаке.
        """
        print(f"Сохранение видеофайла {self.name}")

    def delete(self):
        """
        Удалить видеофайл.
        """
        print(f"Удаление видеофайла {self.name}")

    def convert(self, target_format: str):
        """
        Конвертировать видеофайл в другой формат (например, mp4 -> avi).
        """
        print(f"Конвертация видеофайла {self.name} в формат {target_format}")

    def extract_metadata(self):
        """
        Извлечь мета-данные видеофайла.
        """
        return {
            "resolution": self.resolution,
            "duration": self.duration,
        }
