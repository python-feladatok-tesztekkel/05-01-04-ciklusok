from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKettoHatvany(TestCase):
    def test_feladat00(self):
        aktualis = feladatok.ketto_hatvany(8)
        elvart = 256
        self.assertEqual(elvart, aktualis, "A kettő hatványt nem jól határozta meg!")
    def test_feladat01(self):
        aktualis = feladatok.ketto_hatvany(5)
        elvart = 32
        self.assertEqual(elvart, aktualis, "A kettő hatványt nem jól határozta meg!")
    def test_feladat02(self):
        aktualis = feladatok.ketto_hatvany(2)
        elvart = 4
        self.assertEqual(elvart, aktualis, "A kettő hatványt nem jól határozta meg!")
    def test_feladat03(self):
        aktualis = feladatok.ketto_hatvany(1)
        elvart = 2
        self.assertEqual(elvart, aktualis, "A kettő hatványt nem jól határozta meg!")
    def test_feladat04(self):
        aktualis = feladatok.ketto_hatvany(0)
        elvart = 1
        self.assertEqual(elvart, aktualis, "A kettő hatványt nem jól határozta meg!")
    def test_feladat05(self):
        aktualis = feladatok.ketto_hatvany(-2)
        elvart = None
        self.assertEqual(elvart, aktualis, "A kettő hatványt nem jól határozta meg!")
