#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class test_City(TestBaseModel):
    """Test class for City model"""

    def __init__(self, *args, **kwargs):
        """Initialize the test class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the type of state_id"""
        new = self.value(name="San Francisco", state_id="state123")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test the type of name"""
        new = self.value(name="San Francisco", state_id="state123")
        self.assertEqual(type(new.name), str)
