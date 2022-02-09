from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKettoPrimszamE(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.primszam_e(20)
        elvart = False
        self.assertEqual(elvart, aktualis, "A primszámok számát nem jól határozta meg!")

    def test_feladat02(self):
        aktualis = feladatok.primszam_e(19)
        elvart = True
        self.assertEqual(elvart, aktualis, "A primszámok számát nem jól határozta meg!")

    def test_feladat03(self):
        aktualis = feladatok.primszam_e(15)
        elvart = False
        self.assertEqual(elvart, aktualis, "A primszámok számát nem jól határozta meg!")

    def test_feladat04(self):
        aktualis = feladatok.primszam_e(6)
        elvart = False
        self.assertEqual(elvart, aktualis, "A primszámok számát nem jól határozta meg!")

    def test_feladat05(self):
        aktualis = feladatok.primszam_e(5)
        elvart = True
        self.assertEqual(elvart, aktualis, "A primszámok számát nem jól határozta meg!")

    def test_feladat06(self):
        aktualis = feladatok.primszam_e(2)
        elvart = True
        self.assertEqual(elvart, aktualis, "A primszámok számát nem jól határozta meg!")

    def test_feladat07(self):
        aktualis = feladatok.primszam_e(1)
        elvart = None
        self.assertEqual(elvart, aktualis, "A primszámok számát nem jól határozta meg!")

    def test_feladat08(self):
        aktualis = feladatok.primszam_e(-2)
        elvart = None
        self.assertEqual(elvart, aktualis, "A primszámok számát nem jól határozta meg!")
