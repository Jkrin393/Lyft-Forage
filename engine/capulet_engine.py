from abc import ABC

from engine import Engine


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__() # super() calls parent class
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) ->bool:
        return self.current_mileage - self.last_service_mileage > 30000
