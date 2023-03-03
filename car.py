from Serviceable import Serviceable


class car(Serviceable):
    def __init__(self, Engine, Battery, Tires):
        self.Engine = Engine
        self.Battery = Battery
        self.Tires = Tires

    def needs_service(self):
        Pick_service = self.Engine.needs_service() or self.Battery.needs_service() or self.Tires.needs_service()
        return Pick_service
