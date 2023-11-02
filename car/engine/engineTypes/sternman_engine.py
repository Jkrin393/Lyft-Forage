from car import Car


class SternmanEngine(Car):
    def __init__(self,  warning_light_is_on):
        super().__init__()
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        return self.warning_light_is_on