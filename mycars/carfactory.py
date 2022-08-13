
from array import array
from typing_extensions import Required
from .engine import *
from .battery import *
from .car import *

class CarFactory(Engine, Battery, Car):
    def __init__(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int, warning_light_on:bool):
        super().__init__(current_date, last_service_date, current_mileage, last_service_mileage, warning_light_on)


    def create_calliope(self, tire_array:array, tire_name):
        self.last_service_date=SpindlerBattery().last_service_date
        self.current_milage=CapuletEngine().current_milage
        self.last_service_mileage=CapuletEngine().last_service_mileage

        sum=0
        if tire_name=='Carrigan':
            for i in tire_array:
                if i>0.9:
                    need_serviec={"need_service":True}
        elif tire_name=='Octoprime':
            for i in tire_array:
                sum+=i
            if sum>3:
                need_serviec={"need_service":True}


        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'current_milage':self.current_milage, 
        'last_service_date':self.last_service_mileage}.update(need_serviec)
        return calliope
    
    def create_glissade(self, tire_array:array, tire_name):
        self.last_service_date=SpindlerBattery().last_service_date
        self.current_milage=WilloughbyEngine().current_milage
        self.last_service_mileage=WilloughbyEngine().last_service_mileage

        sum=0
        if tire_name=='Carrigan':
            for i in tire_array:
                if i>0.9:
                    need_serviec={"need_service":True}
        elif tire_name=='Octoprime':
            for i in tire_array:
                sum+=i
            if sum>3:
                need_serviec={"need_service":True}

        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'current_milage':self.current_milage, 
        'last_service_date':self.last_service_mileage}.update(need_serviec)
        return calliope
  
    def create_palindrome(self, tire_array:array, tire_name):
        self.last_service_date=SpindlerBattery().last_service_date
        self.current_milage=SternmanEngine().warning_light

        sum=0
        if tire_name=='Carrigan':
            for i in tire_array:
                if i>0.9:
                    need_serviec={"need_service":True}
        elif tire_name=='Octoprime':
            for i in tire_array:
                sum+=i
            if sum>3:
                need_serviec={"need_service":True}

        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'warning_light':self.warning_light}.update(need_serviec)
        return calliope
   
    def create_rorschach(self, tire_array:array, tire_name):
        self.last_service_date=NubbinBattery().last_service_date
        self.current_milage=WilloughbyEngine().current_milage
        self.last_service_mileage=WilloughbyEngine().last_service_mileage

        sum=0
        if tire_name=='Carrigan':
            for i in tire_array:
                if i>0.9:
                    need_serviec={"need_service":True}
        elif tire_name=='Octoprime':
            for i in tire_array:
                sum+=i
            if sum>3:
                need_serviec={"need_service":True}

        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'current_milage':self.current_milage, 
        'last_service_date':self.last_service_mileage}.update(need_serviec)
        return calliope
    
    def create_thovex(self, tire_array:array, tire_name):
        self.last_service_date=NubbinBattery().last_service_date
        self.current_milage=CapuletEngine().current_milage
        self.last_service_mileage=CapuletEngine().last_service_mileage

        sum=0
        if tire_name=='Carrigan':
            for i in tire_array:
                if i>0.9:
                    need_serviec={"need_service":True}
        elif tire_name=='Octoprime':
            for i in tire_array:
                sum+=i
            if sum>3:
                need_serviec={"need_service":True}

        calliope={'current_date':self.current_date, 
        'last_service_date':self.last_service_date, 
        'current_milage':self.current_milage, 
        'last_service_date':self.last_service_mileage}.update(need_serviec)
        return calliope
        


    