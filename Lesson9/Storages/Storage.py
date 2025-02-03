from abc import ABC, abstractmethod
from ..Files import MediaFile

class Storage(ABC):
    @abstractmethod
    def save_file(self, file: MediaFile):
        """
        Сохранить файл в хранилище.
        """
        pass

    @abstractmethod
    def delete_file(self, file: MediaFile):
        """
        Удалить файл из хранилища.
        """
        pass

    @abstractmethod
    def get_file(self, file_name: str) -> MediaFile:
        """
        Получить файл по имени из хранилища.
        """
        pass
