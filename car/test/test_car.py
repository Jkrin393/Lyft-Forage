import unittest
from datetime import date
from car.battery.battery_types import NubbinBattery, SpindlerBattery
from car.car import Car

from car.carfactory import CarFactory
from car.engine.engine_types import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestCarFactory(unittest.TestCase):
    def test_create_calliope_needs_service_true(self):
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        current_mileage = 40000
        last_service_mileage = 10000
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertTrue(car.needs_service())

    def test_create_calliope_needs_service_false(self):
        # Test the create_calliope method of CarFactory when the car doesn't need service
        current_date = date(2023, 1, 1)
        last_service_date = date(2023, 1, 1)
        current_mileage = 40000
        last_service_mileage = 40000
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertFalse(car.needs_service())

    def test_create_glissade_needs_service_true(self):
        # Test the create_glissade method of CarFactory when the car needs service
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        current_mileage = 70000
        last_service_mileage = 10000
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertTrue(car.needs_service())

    def test_create_glissade_needs_service_false(self):
        # Test the create_glissade method of CarFactory when the car doesn't need service
        current_date = date(2023, 1, 1)
        last_service_date = date(2023, 1, 1)
        current_mileage = 70000
        last_service_mileage = 70000
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertFalse(car.needs_service())

    def test_create_palindrome_needs_service_true(self):
        # Test the create_palindrome method of CarFactory when the car needs service
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        service_light_status = True
        car = CarFactory.create_palindrome(current_date, last_service_date, service_light_status)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertTrue(car.needs_service())

    def test_create_palindrome_needs_service_false(self):
        # Test the create_palindrome method of CarFactory when the car doesn't need service
        current_date = date(2023, 1, 1)
        last_service_date = date(2023, 1, 1)
        service_light_status = False
        car = CarFactory.create_palindrome(current_date, last_service_date, service_light_status)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)
        self.assertFalse(car.needs_service())

    def test_create_rorschach_needs_service_true(self):
        # Test the create_rorschach method of CarFactory when the car needs service
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        current_mileage = 70000
        last_service_mileage = 10000
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
        self.assertTrue(car.needs_service())

    def test_create_rorschach_needs_service_false(self):
        # Test the create_rorschach method of CarFactory when the car doesn't need service
        current_date = date(2023, 1, 1)
        last_service_date = date(2023, 1, 1)
        current_mileage = 70000
        last_service_mileage = 70000
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
        self.assertFalse(car.needs_service())

    def test_create_thovex_needs_service_true(self):
        # Test the create_thovex method of CarFactory when the car needs service
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        current_mileage = 40000
        last_service_mileage = 10000
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
        self.assertTrue(car.needs_service())

    def test_create_thovex_needs_service_false(self):
        # Test the create_thovex method of CarFactory when the car doesn't need service
        current_date = date(2023, 1, 1)
        last_service_date = date(2023, 1, 1)
        current_mileage = 40000
        last_service_mileage = 40000
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, NubbinBattery)
        self.assertFalse(car.needs_service())