Question 2__________
Modify your function so it requires
a third parameter, population.
It should now return a single 
string of the form City, Country
– population xxx, such as Santiago
, Chile – population 5000000. Run
test _cities.py again. Make sure
test_city_country() fails this
time. Modify the function so the
population parameter is optional.
Run test _cities.py again, and make
sure test_city_country() passes
again. Write a second test called
test_city_country_population()
that veri￾fies you can call you
r function with the values
'santiago', 'chile', and
'population=5000000'.
Run test_cities.py again,

solution _______
def city_country(city, country, population):
    """Return a string like 'City, Country – population xxx'."""
    return f"{city.title()}, {country.title()} – population {population}
    TypeError: city_country() missing 1 required positional argument: 'population'"
def city_country(city, country, population=None):
    """Return a string like 'City, Country – population xxx' if population is given."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
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
        
