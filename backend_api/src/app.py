from flask import Flask
from flask_cors import CORS
from .config import app_config
from .models import db

from .views.AddressView import address_api as address_blueprint

def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  app.register_blueprint(address_blueprint, url_prefix='/api/v1/addresses')

  return app

