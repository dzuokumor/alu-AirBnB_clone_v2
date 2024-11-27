#!/usr/bin/python3
"""Unittest for the State model"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class test_state(TestBaseModel):
    """Test class for the State model"""

    def __init__(self, *args, **kwargs):
        """Initialize the test class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test that name attribute is of type str"""
        new = self.value(name="California")  # Explicitly set the name
        self.assertEqual(type(new.name), str)
