from subsystem import Subsystem

class EventManager:
    def __init__(self, power_system, attitude_system):
        self._power_system = power_system
        self._attitude_system = attitude_system
        self._eclipse = False

    def trigger_eclipse(self):
        self._eclipse = True
        print("[EventManager] Eclipse starting. Without solar charging.")

    def end_eclipse(self):
        self._eclipse = False
        print("[EventManager] Eclipse ending. Solar charging reactivated.")

    def handle_events(self):
        if self._eclipse:
            self._power_system._solar_input = 0
            self._power_system.consume_power(5)
        else:
            self._power_system._solar_input = 10
            self._power_system.charge()

        if abs(self._attitude_system._attitude) > 180:
            print("[EventManager] Acttitude out of range, correcting...")
            self._attitude_system.adjust_attitude(-self._attitude_system._attitude)
