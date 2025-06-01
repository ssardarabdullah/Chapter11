Question 1_____________
Write a function that accepts 
two parameters: a city name and 
a country name. The function
should return a single string of 
the form City, Country, such as
Santiago, Chile. Store the
function in a module called city_
functions.py. Create a file called 
test_cities.py that tests the
function you just wrote (remember 
that youneed to import unittest and the
function you want to test)
. Write a method called test_
city_country() to verify that 
calling your function with 
values such as 'santiago' and '
chile' results in the correct
string. Run test_cities.py,
and make sure test_city_country()
passes. (continued)


solution _______________
def city_country(city, country):
    """Return a string in the format 'City, Country'."""
    return f"{city.title()}, {country.title()}"
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
