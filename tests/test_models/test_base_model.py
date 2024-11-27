#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
from models.base_model import BaseModel
import unittest
import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize test case with default attributes."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up test environment."""
        pass

    def tearDown(self):
        """Clean up test environment."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test default instantiation of BaseModel."""
        instance = self.value()
        self.assertEqual(type(instance), self.value)

    def test_id(self):
        """Test that the id attribute is a string."""
        instance = self.value()
        self.assertIsInstance(instance.id, str)

    def test_created_at(self):
        """Test that created_at is a datetime object."""
        instance = self.value()
        self.assertIsInstance(instance.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test that updated_at is a datetime object."""
        instance = self.value()
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        data = instance.to_dict()
        new_instance = BaseModel(**data)
        self.assertAlmostEqual(
            new_instance.created_at.timestamp(),
            new_instance.updated_at.timestamp(),
            delta=1
        )

    def test_todict(self):
        """Test that to_dict returns the correct dictionary."""
        instance = self.value()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['__class__'], self.name)
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_kwargs(self):
        """Test instantiation with a dictionary of attributes."""
        instance = self.value()
        instance_dict = instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertFalse(new_instance is instance)
        self.assertEqual(new_instance.id, instance.id)

    def test_kwargs_incomplete(self):
        """Test instantiation with missing attributes in kwargs."""
        instance = self.value()
        instance_dict = instance.to_dict()
        del instance_dict['updated_at']  # Remove updated_at
        new_instance = BaseModel(**instance_dict)
        self.assertIsInstance(new_instance.updated_at, datetime.datetime)

    def test_kwargs_none(self):
        """Test instantiation with None as kwargs."""
        with self.assertRaises(TypeError):
            BaseModel(**{None: None})

    def test_kwargs_int(self):
        """Test instantiation with invalid kwargs (int key)."""
        instance = self.value()
        instance_dict = instance.to_dict()
        instance_dict.update({1: 2})  # Invalid key
        with self.assertRaises(TypeError):
            BaseModel(**instance_dict)

    def test_save_updates_updated_at(self):
        """Test that save updates the updated_at attribute."""
        instance = self.value()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)

    def test_str_representation(self):
        """Test the string representation of BaseModel."""
        instance = self.value()
        string = str(instance)
        self.assertIn(f"[{self.name}]", string)
        self.assertIn(f"({instance.id})", string)
        self.assertIn(str(instance.__dict__), string)


if __name__ == '__main__':
    unittest.main()
