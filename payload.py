from subsystem import Subsystem

class PayloadCamera(Subsystem):
    def __init__(self):
        super().__init__("Payload Camera")
        self._temperature = 25
        self._data_generated = 0

    def take_picture(self):
        self._data_generated += 5
        print(f"[{self._name}] Taking picture. Data generated: {self._data_generated}MB")

    def cool_down(self):
        self._temperature -= 1
        print(f"[{self._name}] Cooling chamber. Current temperature: {self._temperature}°C")

    def status(self):
        return f"{self._name} Temperature: {self._temperature}°C, Data: {self._data_generated}MB"

