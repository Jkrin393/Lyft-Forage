from tire import Tire

class CarriganTires:
    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self):
        for wear in self.tire_wear:
            if wear>=0.9:
                return True
        return False
    
class CarriganTires:
    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self):
       if sum(self.tire_wear) >= 3:
           return True
       return False