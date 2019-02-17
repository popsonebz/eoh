from marshmallow import fields, Schema
import datetime
from . import db

class AddressModel(db.Model):
 
  # table name
  __tablename__ = 'addresses'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(128), nullable=False)
  last_name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  phone_number = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.first_name = data.get('first_name')
    self.last_name = data.get('last_name')
    self.email = data.get('email')
    self.phone_number = data.get('phone_number')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_addresses():
    return AddressModel.query.all()

  @staticmethod
  def get_one_id(id):
    return AddressModel.query.get(id)

  @staticmethod
  def get_one_address(id):
    return AddressModel.query.get(id)

  @staticmethod
  def get_address_by_email(value):
    return AddressModel.query.filter_by(email=value).first()
  
  def __repr(self):
    return '<id {}>'.format(self.id)

class AddressSchema(Schema):
  id = fields.Int(dump_only=True)
  first_name = fields.Str(required=True)
  last_name = fields.Str(required=True)
  email = fields.Email(required=True)
  phone_number = fields.Str(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
