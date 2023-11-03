from .engine import Engine

CAPULET_SERVICE_MILAGE = 30000
WILLOUGHBY_SERVICE_MILEAGE = 60000


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__() # super() calls parent class
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) ->bool:
        return self.current_mileage - self.last_service_mileage >= CAPULET_SERVICE_MILAGE

class SternmanEngine(Engine):
    def __init__(self,  warning_light_is_on):
        super().__init__()
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        return self.warning_light_is_on
    
class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage >= WILLOUGHBY_SERVICE_MILEAGE




