import unittest

from utils import get_all_countries, get_country_info, encrypt_string
from database import DataBase


class TestApp(unittest.TestCase):
    def test_api(self):
        self.assertIsNotNone(get_all_countries())

    def test_get_country_info_invalid(self):
        self.assertIsNone(
            get_country_info({
                'name': {'stuff': 'more_stuff'},
                'region': 'some_region',
                'languages': {'lng':'rnd_lng'}
            })
        )

        self.assertIsNone(
            get_country_info({
                'name': {'common': 'Germany'},
                'regioon': 'some_region',
                'languages': {'lng':'rnd_lng'}
            })
        )

        self.assertIsNone(
            get_country_info({
                'name': {'official': 'Germany'},
                'regioon': 'some_region',
                'languages': {'lng':'rnd_lng'}
            })
        )

    def test_get_country_info_valid(self):
        self.assertEqual(
            get_country_info({
                'name': {'common': 'Germany'},
                'region': 'Europe',
                'languages': {'deu':'German'}
            }), ('Germany', 'Europe', ['German'])
        )

        self.assertEqual(
            get_country_info({
                'name': {'common': 'Belgium'},
                'region': 'Europe',
                'languages': {
                    'deu': 'German',
                    'fra': 'French',
                    'nld': 'Dutch'
                }
            }), ('Belgium', 'Europe', ['German', 'French', 'Dutch'])
        )

    def test_encrypt_function(self):
        self.assertEqual(
            encrypt_string('español'),
            'd2a8463fbad311860c107dc5e0d3755482ff0dca'
        )
    
class TestDB(unittest.TestCase):
    def test_db(self):
        db = DataBase()

if __name__ == "__main__":
    unittest.main()