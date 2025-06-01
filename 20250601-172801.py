# city_functions.py

def city_country(city, country):
    """Return a string in the format 'City, Country'."""
    return f"{city.title()}, {country.title()}"
    # test_cities.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the function city_country()."""

    def test_city_country(self):
        """Do city and country names like 'Santiago, Chile' work?"""
        formatted = city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()