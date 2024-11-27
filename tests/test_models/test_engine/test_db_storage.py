#!/usr/bin/python3
import unittest
import models
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not db")
class TestDBStorage(unittest.TestCase):
    """DB Storage test"""

    def setUp(self):
        """ Set up test environment """
        self.storage = models.storage

    def tearDown(self):
        """ Clean up after tests """
        # Clear out storage between tests
        self.storage.close()

    def test_user(self):
        """ Tests user """
        user = User(
            name="Chyna", email="chyna@gmail.com", password="Chyna12345"
        )
        user.save()
        stored_user = self.storage.all(User).get(user.id)
        self.assertIsNotNone(stored_user)
        self.assertEqual(stored_user.name, "Chyna")

    def test_city(self):
        """ test city """
        state = State(name="California")
        state.save()

        city = City(name="Batch", state_id=state.id)
        city.save()

        stored_city = self.storage.all(City).get(city.id)
        self.assertIsNotNone(stored_city)
        self.assertEqual(stored_city.name, "Batch")
        self.assertEqual(stored_city.state_id, state.id)

    def test_state(self):
        """ test state """
        state = State(name="California")
        state.save()
        stored_state = self.storage.all(State).get(state.id)
        self.assertIsNotNone(stored_state)
        self.assertEqual(stored_state.name, "California")

    def test_place(self):
        """ Test place """
        state = State(name="California")
        state.save()

        city = City(name="Batch", state_id=state.id)
        city.save()

        user = User(
            name="Chyna", email="chyna@gmail.com", password="Chyna12345"
        )
        user.save()

        place = Place(
            name="Palace", number_rooms=4, city_id=city.id, user_id=user.id
        )
        place.save()

        stored_place = self.storage.all(Place).get(place.id)
        self.assertIsNotNone(stored_place)
        self.assertEqual(stored_place.name, "Palace")
        self.assertEqual(stored_place.number_rooms, 4)

    def test_amenity(self):
        """ Test amenity """
        amenity = Amenity(name="Startlink")
        amenity.save()
        stored_amenity = self.storage.all(Amenity).get(amenity.id)
        self.assertIsNotNone(stored_amenity)
        self.assertEqual(stored_amenity.name, "Startlink")

    def test_review(self):
        """ Test review """
        state = State(name="California")
        state.save()

        city = City(name="Batch", state_id=state.id)
        city.save()

        user = User(
            name="Chyna", email="chyna@gmail.com", password="Chyna12345"
        )
        user.save()

        place = Place(
            name="Palace", number_rooms=4, city_id=city.id, user_id=user.id
        )
        place.save()

        review = Review(
            text="no comment", place_id=place.id, user_id=user.id
        )
        review.save()

        stored_review = self.storage.all(Review).get(review.id)
        self.assertIsNotNone(stored_review)
        self.assertEqual(stored_review.text, "no comment")


if __name__ == '__main__':
    unittest.main()
