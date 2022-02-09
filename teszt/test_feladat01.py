from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestFaktorialis(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.faktorialis(5)
        elvart = 120
        self.assertEqual(elvart, aktualis, "A faktoriális nem jól határozta meg!")

    def test_feladat02(self):
        aktualis = feladatok.faktorialis(3)
        elvart = 6
        self.assertEqual(elvart, aktualis, "A faktoriális nem jól határozta meg!")

    def test_feladat03(self):
        aktualis = feladatok.faktorialis(2)
        elvart = 2
        self.assertEqual(elvart, aktualis, "A faktoriális nem jól határozta meg!")

    def test_feladat04(self):
        aktualis = feladatok.faktorialis(1)
        elvart = 1
        self.assertEqual(elvart, aktualis, "A faktoriális nem jól határozta meg!")

    def test_feladat05(self):
        aktualis = feladatok.faktorialis(0)
        elvart = 1
        self.assertEqual(elvart, aktualis, "A faktoriális nem jól határozta meg!")

    def test_feladat06(self):
        aktualis = feladatok.faktorialis(-2)
        elvart = None
        self.assertEqual(elvart, aktualis, "A faktoriális nem jól határozta meg!")
