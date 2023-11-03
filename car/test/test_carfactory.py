import unittest
from datetime import date
from carfactory import CarFactory
from car.car import Car

class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        current_mileage = 40000
        last_service_mileage = 10000
        tire_wear = [.1, .6, .7, .4]
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertIsInstance(car, Car)

    def test_create_calliope(self):
        # Test the create_calliope method of CarFactory
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        current_mileage = 40000
        last_service_mileage = 10000
        tire_wear = [.1, .6, .7, .4]
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertIsInstance(car, Car)

    def test_create_glissade(self):
        # Test the create_glissade method of CarFactory
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        current_mileage = 70000
        last_service_mileage = 10000
        tire_wear = [.1, .6, .7, .4]
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertIsInstance(car, Car)

    def test_create_palindrome(self):
        # Test the create_palindrome method of CarFactory
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        service_light_status = True
        tire_wear = [.1, .6, .7, .4]
        car = CarFactory.create_palindrome(current_date, last_service_date, service_light_status, tire_wear)
        self.assertIsInstance(car, Car)

    def test_create_rorschach(self):
        # Test the create_rorschach method of CarFactory
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        current_mileage = 70000
        last_service_mileage = 10000
        tire_wear = [.1, .6, .7, .4]
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertIsInstance(car, Car)

    def test_create_thovex(self):
        # Test the create_thovex method of CarFactory
        current_date = date(2023, 1, 1)
        last_service_date = date(2022, 1, 1)
        current_mileage = 40000
        last_service_mileage = 10000
        tire_wear = [.1, .6, .7, .4]
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertIsInstance(car, Car)

if __name__ == '__main__':
    unittest.main()