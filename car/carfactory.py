from car import Car
from datetime import date
from car.tires.tires_types import CarriganTires, OctoprimeTires
from engine.engine_types import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery.battery_types import SpindlerBattery, NubbinBattery


class CarFactory(Car):
    @classmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        model = "Calliope"
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire_wear = OctoprimeTires(tire_wear)
        car = Car(engine, battery, tire_wear)
        return car
    
    @classmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        model = "Glissade"
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire_wear = CarriganTires(tire_wear)
        car = Car(engine, battery, tire_wear)    
        return car
    
    @classmethod
    def create_palindrome(self, current_date, last_service_date, service_light_status, tire_wear) -> Car:
        model = "Palindrome"
        engine = SternmanEngine(service_light_status)
        battery = SpindlerBattery(current_date, last_service_date)
        tire_wear = OctoprimeTires(tire_wear)
        car = Car(engine, battery, tire_wear)
        return car
    
    @classmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        model = "rorschach"
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire_wear = CarriganTires(tire_wear)
        car = Car(engine, battery, tire_wear)
        return car
    
    @classmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        model = "Thovex"
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire_wear = OctoprimeTires(tire_wear)
        car = Car(engine, battery, tire_wear)
        return car
    

