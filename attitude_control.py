from subsystem import Subsystem

class AttitudeControlSystem(Subsystem):
    def __init__(self):
        super().__init__("Attitude Control System")
        self._attitude = 0

    def adjust_attitude(self, degrees):
        self._attitude += degrees
        print(f"[{self._name}] Adjusting attitude in {degrees} degrees. New attitude: {self._attitude}")

    def status(self):
        return f"{self._name} current attitude: {self._attitude}°"