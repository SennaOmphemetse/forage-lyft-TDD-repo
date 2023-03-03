from Tires.Tyres import Tyres


class Tube_less(Tyres):
    def __init__(self, Weight):
        super().__init__(Weight)
        self.Weight = Weight

    def Is_Tube_Tyre(self):
        if self.Weight <= 20:
            return True
        else:
            return False
