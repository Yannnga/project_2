"""
Program: Solar System Explorer - Unit Test
Author: Xinyi Yang
Purpose: Test planetary data using Python's unittest module.
Starter/resources: Python Crash Course, Chapter 11
Date: November 2026
"""
import unittest
import json
from pathlib import Path

class TestPlanetFunction(unittest.TestCase):

   def test_earth_radius(self):
       # Load the JSON data from the file
       file_path = Path(__file__).parent / "data" / "planets.json"
       with open(file_path, 'r') as f:
           planet_data = json.load(f)

       # Assert that the radius of Earth is as expected (km）
       self.assertEqual(planet_data["Earth"]["radius_km"], 6371)



if __name__ == '__main__':
    unittest.main()