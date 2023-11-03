import unittest
from datetime import date
from car.engine.engine import Engine
from car.engine.engine_types import WilloughbyEngine, CapuletEngine, SternmanEngine

class TestCapuletEngine(unittest.TestCase):
    def test_caputlet_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30001
        CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(CapuletEngine.needs_service())

    def test_caputlet_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 29999
        CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(CapuletEngine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_sternman_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60000
        SternmanEngine(current_mileage, last_service_mileage)
        self.assertTrue(SternmanEngine.needs_service())

    def  test_sternman_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 200000
        SternmanEngine(current_mileage, last_service_mileage)
        self.assertTrue(SternmanEngine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_should_be_serviced(self):
        warning_light = True
        WilloughbyEngine(warning_light)
        self.assertTrue(WilloughbyEngine.needs_service())

    def  test_willoughby_engine_should_not_be_serviced(self):
        warning_light = False
        WilloughbyEngine(warning_light)
        self.assertTrue(WilloughbyEngine.needs_service())
