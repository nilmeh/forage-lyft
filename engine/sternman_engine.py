from engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_indicator_on):
        super().__init__(0, 0, warning_indicator_on)
        self.warning_indicator_on = warning_indicator_on
        
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000
