from ..Files import MediaFile
import Storage
import datetime

class CloudStorage(Storage):
    def save_file(self, file: MediaFile):
        """
        Сохранить файл в облачное хранилище.
        """
        print(f"Сохранение файла {file.name} в облачное хранилище")

    def delete_file(self, file: MediaFile):
        """
        Удалить файл из облачного хранилища.
        """
        print(f"Удаление файла {file.name} из облачного хранилища")

    def get_file(self, file_name: str) -> MediaFile:
        """
        Получить файл из облачного хранилища.
        """
        print(f"Получение файла {file_name} из облачного хранилища")
        # Возвращаем пример файла
        return MediaFile(file_name, 0, datetime.now(), "owner")
