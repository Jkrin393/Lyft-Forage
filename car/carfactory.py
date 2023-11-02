from car import Car
from engine.engineTypes import capulet_engine, sternman_engine, willoughby_engine
from battery.batteryTypes import nubbin_battery, spindler_battery


class CarFactory(Car):
    @classmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "Calliope"
        return Car(model)
    
    @classmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "Glissade"
        return Car(model)
    
    @classmethod
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "Palindrome"
        return Car(model)
    
    @classmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "rorschach"
        return Car(model)
    
    @classmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        model = "Thovex"
        return Car(model)
    

