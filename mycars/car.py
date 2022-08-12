from .engine import *
from .battery import *

# Composition

class Car:
    def __init__(self):
        self.engine = Engine() 
        self.battery = Battery()

    def need_service(self):
        need_service = self.engine.need_service() and self.battery.need_service()
        return need_service

