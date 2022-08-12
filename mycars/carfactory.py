
from .engine import *
from .battery import *
from .car import *

class CarFactory(Engine, Battery, Car):
    def __init__(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int, warning_light_on:bool):
        super().__init__(current_date, last_service_date, current_mileage, last_service_mileage, warning_light_on)


    def create_calliope(self):
        self.last_service_date=SpindlerBattery().last_service_date
        self.current_milage=CapuletEngine().current_milage
        self.last_service_mileage=CapuletEngine().last_service_mileage

        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'current_milage':self.current_milage, 
        'last_service_date':self.last_service_mileage}
        return calliope
    
    def create_glissade(self):
        self.last_service_date=SpindlerBattery().last_service_date
        self.current_milage=WilloughbyEngine().current_milage
        self.last_service_mileage=WilloughbyEngine().last_service_mileage

        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'current_milage':self.current_milage, 
        'last_service_date':self.last_service_mileage}
        return calliope
  
    def create_palindrome(self):
        self.last_service_date=SpindlerBattery().last_service_date
        self.current_milage=SternmanEngine().warning_light

        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'warning_light':self.warning_light}
        return calliope
   
    def create_rorschach(self):
        self.last_service_date=NubbinBattery().last_service_date
        self.current_milage=WilloughbyEngine().current_milage
        self.last_service_mileage=WilloughbyEngine().last_service_mileage

        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'current_milage':self.current_milage, 
        'last_service_date':self.last_service_mileage}
        return calliope
    
    def create_thovex(self):
        self.last_service_date=NubbinBattery().last_service_date
        self.current_milage=CapuletEngine().current_milage
        self.last_service_mileage=CapuletEngine().last_service_mileage

        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'current_milage':self.current_milage, 
        'last_service_date':self.last_service_mileage}
        return calliope
        


    