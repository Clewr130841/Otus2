from ..Files import MediaFile
import Storage
import datetime

class S3Storage(Storage):
    def save_file(self, file: MediaFile):
        """
        Сохранить файл в S3-like хранилище.
        """
        print(f"Сохранение файла {file.name} в S3-like хранилище")

    def delete_file(self, file: MediaFile):
        """
        Удалить файл из S3-like хранилища.
        """
        print(f"Удаление файла {file.name} из S3-like хранилища")

    def get_file(self, file_name: str) -> MediaFile:
        """
        Получить файл из S3-like хранилища.
        """
        print(f"Получение файла {file_name} из S3-like хранилища")
        # Возвращаем пример файла
        return MediaFile(file_name, 0, datetime.now(), "owner")
