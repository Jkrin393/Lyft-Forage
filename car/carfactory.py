from car import Car
from engine.engineTypes import capulet_engine, sternman_engine, willoughby_engine
from battery.batteryTypes import nubbin_battery, spindler_battery


class CarFactory(Car):
    @classmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "Calliope"
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        return Car(model)
    
    @classmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "Glissade"
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage        
        return Car(model)
    
    @classmethod
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "Palindrome"
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        return Car(model)
    
    @classmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "rorschach"
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        return Car(model)
    
    @classmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "Thovex"
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        return Car(model)
    

