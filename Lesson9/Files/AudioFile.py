import MediaFile
import datetime

class AudioFile(MediaFile):
    def __init__(self, name: str, size: int, creation_date: datetime, owner: str, bitrate: int, duration: float):
        super().__init__(name, size, creation_date, owner)
        self.bitrate = bitrate  # Битрейт
        self.duration = duration  # Длительность в секундах

    def save(self):
        """
        Сохранить аудиофайл на диске или в облаке.
        """
        print(f"Сохранение аудиофайла {self.name}")

    def delete(self):
        """
        Удалить аудиофайл.
        """
        print(f"Удаление аудиофайла {self.name}")

    def convert(self, target_format: str):
        """
        Конвертировать аудиофайл в другой формат (например, mp3 -> wav).
        """
        print(f"Конвертация аудиофайла {self.name} в формат {target_format}")

    def extract_metadata(self):
        """
        Извлечь мета-данные аудиофайла.
        """
        return {
            "bitrate": self.bitrate,
            "duration": self.duration,
        }
