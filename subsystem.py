from abc import ABC, abstractmethod

class Subsystem(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def status(self):
        pass