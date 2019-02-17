import unittest
import os
import json
import sys

from app import create_app, db

class AddressesTest(unittest.TestCase):
  """
  Addressbook Test Case
  """
  def setUp(self):
    """
    Test Setup
    """
    self.app = create_app("testing")
    self.client = self.app.test_client
    self.address = {
      'first_name': 'kim',
      'last_name' : 'cole',
      'email' : 'kim@mail.com',
      'phone_number': '123456789'
    }

    with self.app.app_context():
      # create all tables
      db.create_all()

  def test_address_creation(self):
    """ test address creation """
    res = self.client().post('/api/v1/address/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.address))
    self.assertEqual(res.status_code, 201)

  def tearDown(self):
    """
    Tear Down
    """
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

if __name__ == "__main__":
  unittest.main()
