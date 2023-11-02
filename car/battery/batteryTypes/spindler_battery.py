from battery import Battery
from datetime import date

DAYS_IN_YEAR = 365.25
SERVICE_INTERVAL = 4

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = date(last_service_date)
        self.current_date = date(current_date)

    def needs_service(self) -> bool:
        service_interval_days = SERVICE_INTERVAL * DAYS_IN_YEAR
        return self.current_date - self.last_service_date >= service_interval_days
 