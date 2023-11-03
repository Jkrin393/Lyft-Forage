from battery import Battery
from datetime import date, timedelta

DAYS_IN_YEAR = 365.25
SERVICE_INTERVAL_NUBBIN = 2
SERVICE_INTERVAL_SPINDLER = 4 
class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_interval_days = SERVICE_INTERVAL_NUBBIN * DAYS_IN_YEAR
        time_since_service = self.current_date - self.last_service_date


        if time_since_service >= timedelta(days=service_interval_days):
            return True
        else:
            return False

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_interval_days = SERVICE_INTERVAL_SPINDLER * DAYS_IN_YEAR
        time_since_service = self.current_date - self.last_service_date

        if time_since_service >= timedelta(days=service_interval_days):
            return True
        else:
            return False
 