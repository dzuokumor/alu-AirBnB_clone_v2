from datetime import datetime

from models.amenity import Amenity


def test_created_at(self):
    """ Test that created_at is properly set """
    amenity = Amenity(name="WiFi")
    amenity.save()

    # Debugging output
    print("All amenities in storage:", self.storage.all(Amenity))  # Print all amenities in storage

    stored_amenity = self.storage.all(Amenity).get(amenity.id)

    # Debugging output
    print("Stored amenity:", stored_amenity)

    # Check that created_at is a datetime object
    self.assertIsInstance(stored_amenity.created_at, datetime)
    self.assertEqual(stored_amenity.created_at, amenity.created_at)
