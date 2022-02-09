from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKettoSzorzatOsszeg2(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.szorzat_es_osszeg(10)
        elvart = 385
        self.assertEqual(elvart, aktualis, "A szorzat összeget nem jól határozta meg!")

    def test_feladat02(self):
        aktualis = feladatok.szorzat_es_osszeg(5)
        elvart = 55
        self.assertEqual(elvart, aktualis, "A szorzat összeget nem jól határozta meg!")

    def test_feladat03(self):
        aktualis = feladatok.szorzat_es_osszeg(3)
        elvart = 14
        self.assertEqual(elvart, aktualis, "A szorzat összeget nem jól határozta meg!")
    def test_feladat04(self):
        aktualis = feladatok.szorzat_es_osszeg(1)
        elvart = 1
        self.assertEqual(elvart, aktualis, "A szorzat összeget nem jól határozta meg!")

    def test_feladat05(self):
        aktualis = feladatok.szorzat_es_osszeg(0)
        elvart = None
        self.assertEqual(elvart, aktualis, "A szorzat összeget nem jól határozta meg!")

