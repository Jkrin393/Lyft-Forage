import unittest

from car.tires.tires_types import CarriganTires, OctoprimeTires



class TestCarriganTires(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        tire_wear = [.1, .6, .9, .4]
        CarriganTires(tire_wear)
        self.assertTrue(CarriganTires.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        tire_wear = [.1, .6, .7, .4]
        CarriganTires(tire_wear)
        self.assertFalse(CarriganTires.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        tire_wear = [.8, .8, .8, .8]
        OctoprimeTires(tire_wear)
        self.assertTrue(OctoprimeTires.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        tire_wear = [.1, .1, .5, .9]
        OctoprimeTires(tire_wear)
        self.assertFalse(OctoprimeTires.needs_service())




