import unittest
import os
import json
import sys

from ..app import create_app, db

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
    res = self.client().post('/api/v1/addresses/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.address))
    self.assertEqual(res.status_code, 201)

  def test_address_creation_duplicate_email(self):
    """ test address creation already existing email"""
    res = self.client().post('/api/v1/addresses/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.address))
    self.assertEqual(res.status_code, 201)
    res = self.client().post('/api/v1/addresses/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.address))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('error'))

  def test_address_creation_with_no_email(self):
    """ test address creation with no email """
    address = {
      'first_name': 'kim',
      'last_name' : 'cole',
    }
    res = self.client().post('/api/v1/addresses/', headers={'Content-Type': 'application/json'}, data=json.dumps(address))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('email'))

  def test_address_creation_with_empty_request(self):
    """ test address creation with empty request """
    address = {}
    res = self.client().post('/api/v1/addresses/', headers={'Content-Type': 'application/json'}, data=json.dumps(address))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)

  def tearDown(self):
    """
    Tear Down
    """
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

if __name__ == "__main__":
  unittest.main()
