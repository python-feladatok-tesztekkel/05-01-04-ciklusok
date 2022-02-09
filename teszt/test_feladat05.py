from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKettoHatvany(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.osztok_szama(20)
        elvart = 6
        self.assertEqual(elvart, aktualis, "Az osztók számát nem jól határozta meg!")

    def test_feladat02(self):
        aktualis = feladatok.osztok_szama(19)
        elvart = 2
        self.assertEqual(elvart, aktualis, "Az osztók számát nem jól határozta meg!")

    def test_feladat03(self):
        aktualis = feladatok.osztok_szama(15)
        elvart = 4
        self.assertEqual(elvart, aktualis, "Az osztók számát nem jól határozta meg!")

    def test_feladat04(self):
        aktualis = feladatok.osztok_szama(6)
        elvart = 4
        self.assertEqual(elvart, aktualis, "Az osztók számát nem jól határozta meg!")

    def test_feladat05(self):
        aktualis = feladatok.osztok_szama(3)
        elvart = 2
        self.assertEqual(elvart, aktualis, "Az osztók számát nem jól határozta meg!")

    def test_feladat06(self):
        aktualis = feladatok.osztok_szama(2)
        elvart = 2
        self.assertEqual(elvart, aktualis, "Az osztók számát nem jól határozta meg!")

    def test_feladat07(self):
        aktualis = feladatok.osztok_szama(1)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Az osztók számát nem jól határozta meg!")

    def test_feladat08(self):
        aktualis = feladatok.osztok_szama(-2)
        elvart = None
        self.assertEqual(elvart, aktualis, "Az osztók számát nem jól határozta meg!")
