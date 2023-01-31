#!/usr/bin/env python3


import math
import unittest
from parameterized import parameterized, parameterized_class

class TestMathUnitTest(unittest.TestCase):
   @parameterized.expand([
       ("negative", -1.5, -2.0),
       ("integer", 1, 1.0),
       ("large fraction", 1.6, 1),
   ])
   def test_floor(self, name, input, expected):
       self.assertEqual(math.floor(input), expected)
       print("Success")