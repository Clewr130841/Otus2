from ..Files import MediaFile
import Storage
import datetime

class LocalStorage(Storage):
    def save_file(self, file: MediaFile):
        """
        Сохранить файл в локальном хранилище.
        """
        print(f"Сохранение файла {file.name} в локальное хранилище")

    def delete_file(self, file: MediaFile):
        """
        Удалить файл из локального хранилища.
        """
        print(f"Удаление файла {file.name} из локального хранилища")

    def get_file(self, file_name: str) -> MediaFile:
        """
        Получить файл из локального хранилища.
        """
        print(f"Получение файла {file_name} из локального хранилища")
        # Здесь можно возвращать пример файла (пока без конкретной реализации)
        return MediaFile(file_name, 0, datetime.now(), "owner")
