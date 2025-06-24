from subsystem import Subsystem

class CommSystem(Subsystem):
    def __init__(self, power_system):
        super().__init__("Comm System")
        self._power_system = power_system
        self._status = "OK"

    def send_status(self):
        if self._power_system.is_battery_low():
            self._status = "FAIL"
            print(f"[{self._name}] ERROR: Low battery, no comunication.")
        else:
            self._status = "OK"
            print(f"[{self._name}] State: Sending to earth.")

    def status(self):
        return f"{self._name} State: {self._status}"
