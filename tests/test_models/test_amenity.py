#!/usr/bin/python3
""" """
from datetime import datetime
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity
import models


class TestAmenity(TestBaseModel):
    """ Test for amenity"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def setUp(self):
        self.storage = models.storage

    def test_name2(self):
        new = self.value()
        new.name = "amenity"
        self.assertEqual(type(new.name), str)

    def test_created_at(self):
        amenity = Amenity(name="WiFi")
        amenity.save()

        stored_amenity = self.storage.all(Amenity).get(amenity.id)

        self.assertIsInstance(stored_amenity.created_at, datetime)

        self.assertEqual(stored_amenity.created_at, amenity.created_at)
