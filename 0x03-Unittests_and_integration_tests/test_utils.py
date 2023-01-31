#!/usr/bin/env python3
"""
Test module for utils
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized, parameterized_class
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    Class to implement tests for the function
    test_access_neseted_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Method to test that the method returns
        what is is supposed to
        """
        value = access_nested_map(nested_map, path)
        self.assertEqual(value, expected)
