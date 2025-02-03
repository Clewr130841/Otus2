class LowFuelError(Exception):
    """Ошибка, когда топливо заканчивается"""
    def __init__(self, message="Топливо на исходе"):
        self.message = message
        super().__init__(self.message)

class NotEnoughFuel(Exception):
    """Ошибка, когда топлива недостаточно для выполнения операции"""
    def __init__(self, message="Недостаточно топлива для продолжения"):
        self.message = message
        super().__init__(self.message)

class CargoOverload(Exception):
    """Ошибка, когда груз превышает допустимый предел"""
    def __init__(self, message="Перегрузка! Груз превышает допустимый лимит"):
        self.message = message
        super().__init__(self.message)