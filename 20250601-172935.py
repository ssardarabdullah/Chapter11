# city_functions.py

def city_country(city, country, population):
    """Return a string like 'City, Country – population xxx'."""
    return f"{city.title()}, {country.title()} – population {population}
    TypeError: city_country() missing 1 required positional argument: 'population'"
    # city_functions.py

def city_country(city, country, population=None):
    """Return a string like 'City, Country – population xxx' if population is given."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
        # test_cities.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the function city_country()."""

    def test_city_country(self):
        """Do city and country names work without population?"""
        formatted = city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do city, country, and population work?"""
        formatted = city_country('santiago', 'chile', population=5000000)
        