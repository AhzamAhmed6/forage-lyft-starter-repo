from abc import ABC, abstractmethod
from calendar import c

# Realization

class Engine(ABC):
    def __init__(self, last_service_mileage: int=0, current_milage: int=0, warning_light: bool=False):
        self.last_service_mileage=last_service_mileage
        self.current_milage=current_milage
        self.warning_light=warning_light


    @abstractmethod
    def need_service(self):
        return False


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_milage: int):
        super().__init__(last_service_mileage, current_milage)
    
    def need_service(self):
        need_service = (self.current_milage-self.last_service_mileage)>30000
        return need_service


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_milage: int):
        super().__init__(last_service_mileage, current_milage)
    
    def need_service(self):
        need_service = (self.current_milage-self.last_service_mileage)>60000
        return need_service


class SternmanEngine(Engine):
    def __init__(self, warning_light:bool):
        super().__init__(warning_light)
    def need_service(self):        
        return self.warning_light


