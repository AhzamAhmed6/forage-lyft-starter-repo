from abc import ABC, abstractmethod
import datetime

# Realization

class Battery(ABC):
    def __init__(self, last_service_date):
        self.last_service_date=last_service_date
        self.current_date = datetime.date.today()

    @abstractmethod
    def need_service(self):
        return False

class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        
        
    def need_service(self):
        is_need_service = self.current_date-self.last_service_date>datetime.timedelta(1095)
        return is_need_service


class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = datetime.date.today()
        
    def need_service(self):
        is_need_service = self.current_date-self.last_service_date>datetime.timedelta(1460)
        return is_need_service

        