from subsystem import Subsystem 

class PowerSystem(Subsystem):
    def __init__(self):
        super().__init__("Power System")
        self._battery_level = 100
        self._solar_input = 10

    def consume_power(self, amount):
        self._battery_level -= amount
        if self._battery_level < 0:
            self._battery_level = 0
        print(f"[{self._name}] Consuming {amount} units of energy. Battery: {self._battery_level}%")

    def charge(self):
        self._battery_level += self._solar_input
        if self._battery_level > 100:
            self._battery_level = 100
        print(f"[{self._name}] Loading with {self._solar_input} solar units. Battery: {self._battery_level}%")

    def is_battery_low(self):
        return self._battery_level < 20

    def status(self):
        return f"{self._name} Battery: {self._battery_level}%"
