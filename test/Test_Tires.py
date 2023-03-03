import unittest
from Tires.Tubeless_Tyre import Tube_less
from Tires.Tube_Tyre import Tube_Tyr


class TubeLessTest(unittest.TestCase):
    def test_needs_service_true(self):
        weight = 12
        tyre = Tube_less(weight)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        weight = 25
        tyre = Tube_less(weight)
        self.assertTrue(tyre.needs_service())


class TubeTest(unittest.TestCase):
    def test_needs_service_true(self):
        weight = 30
        tyre = Tube_Tyr(weight)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        weight = 14
        tyre = Tube_Tyr(weight)
        self.assertTrue(tyre.needs_service())