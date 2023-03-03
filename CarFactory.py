from car import car
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from Tires.Tubeless_Tyre import Tube_less
from Tires.Tube_Tyre import Tube_Tyr


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, weight):
        Engine = CapuletEngine(current_mileage, last_service_mileage)
        Battery = SpindlerBattery(current_date, last_service_date)
        Tires = Tube_less(weight)
        Car = car(Engine, Battery, Tires)
        return Car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, weight):
        Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        Battery = SpindlerBattery(current_date, last_service_date)
        Tires = Tube_less(weight)
        Car = car(Engine, Battery, Tires)
        return Car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, weight):
        Engine = SternmanEngine(warning_light_is_on)
        Battery = SpindlerBattery(current_date, last_service_date)
        Tires = Tube_less(weight)
        Car = car(Engine, Battery, Tires)
        return Car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, weight):
        Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        Battery = NubbinBattery(current_date, last_service_date)
        Tires = Tube_Tyr(weight)
        Car = car(Engine, Battery, Tires)
        return Car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, weight):
        Engine = CapuletEngine(current_mileage, last_service_mileage)
        Battery = NubbinBattery(current_date, last_service_date)
        Tires = Tube_Tyr(weight)
        Car = car(Engine, Battery, Tires)
        return Car
