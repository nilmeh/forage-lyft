from car import Car
from engine.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery

class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        rorschach_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        rorscharch_battery = NubbinBattery(last_service_date)

        super().__init__(rorschach_engine, rorscharch_battery)

        self.engine = rorschach_engine
        self.battery = rorscharch_battery
    
    def needs_service(self):
        return super().needs_service()