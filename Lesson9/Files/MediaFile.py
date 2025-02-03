from abc import ABC, abstractmethod
from datetime import datetime

class MediaFile(ABC):
    def __init__(self, name: str, size: int, creation_date: datetime, owner: str):
        self.name = name  # Имя файла
        self.size = size  # Размер файла в байтах
        self.creation_date = creation_date  # Дата создания
        self.owner = owner  # Владелец файла

    @abstractmethod
    def save(self):
        """
        Сохранить файл в соответствующем хранилище (локальное, облако и т.д.).
        """
        pass

    @abstractmethod
    def delete(self):
        """
        Удалить файл из хранилища.
        """
        pass

    @abstractmethod
    def convert(self, target_format: str):
        """
        Конвертировать файл в указанный формат.
        """
        pass

    @abstractmethod
    def extract_metadata(self):
        """
        Извлечь мета-данные, специфичные для типа файла.
        """
        pass

    @abstractmethod
    def get_file_info(self):
        """
        Получить информацию о файле (например, имя, размер, дата создания).
        """
        return {
            "name": self.name,
            "size": self.size,
            "creation_date": self.creation_date,
            "owner": self.owner,
        }
