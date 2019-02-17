from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()

from .AddressModel import AddressModel, AddressSchema
