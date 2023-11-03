import unittest
from datetime import date
from car.battery.battery import Battery
from car.battery.battery_types import SpindlerBattery, NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        last_service_date = date(2022,4,1)
        current_date = date(2020,3,11)
        NubbinBattery(current_date, last_service_date)
        self.assertTrue(NubbinBattery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        last_service_date = date(2022,4,1)
        current_date = date(2022,3,11)
        NubbinBattery(current_date, last_service_date)
        self.assertFalse(NubbinBattery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        last_service_date = date(2022,4,1)
        current_date = date(2018,3,11)
        SpindlerBattery(current_date, last_service_date)
        self.assertTrue(NubbinBattery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        last_service_date = date(2022,4,1)
        current_date = date(2022,3,11)
        SpindlerBattery(current_date, last_service_date)
        self.assertFalse(NubbinBattery.needs_service())




