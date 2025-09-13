import unittest
from location import *

class TestLab1(unittest.TestCase):
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location(SLO, 35.3, -120.7)")

    def test_repr_1(self):
        loc = Location("", -1, 0)
        self.assertEqual(repr(loc), "Location(, -1, 0)")

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SLO", 35.0 + 0.1 + 0.1 + 0.1, -120.7)
        loc4 = Location("Paris", 48.9, 2.4)
        self.assertEqual(loc1, loc2)
        self.assertEqual(loc1, loc3)
        self.assertNotEqual(loc2, loc4)

        loc5 = Location("", 48.9, 2.40)
        loc4.name = ""
        self.assertEqual(loc4, loc5)


    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name, "SLO")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.long, -120.7)

    def test_init_1(self):
        loc = Location(4, 4.31111, 3.1116)
        self.assertEqual(loc.name, 4)
        self.assertEqual(loc.lat, 4.311)
        self.assertEqual(loc.long, 3.112)


if __name__ == "__main__":
        unittest.main()
