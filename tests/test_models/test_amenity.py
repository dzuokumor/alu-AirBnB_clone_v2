#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity
from models import storage

class TestAmenity(TestBaseModel):
    """Test cases for the Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test the type of name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_storage_retrieval(self):
        """Test retrieving an Amenity from storage"""
        new_amenity = Amenity(name="WiFi")
        storage.new(new_amenity)
        storage.save()

        stored_amenities = storage.all(Amenity)

        amenity_key = f"Amenity.{new_amenity.id}"

        self.assertIn(amenity_key, stored_amenities)

        stored_amenity = stored_amenities.get(amenity_key)
        self.assertEqual(stored_amenity.name, "WiFi")
        self.assertEqual(stored_amenity.id, new_amenity.id)
