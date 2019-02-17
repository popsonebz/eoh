#/src/views/UserView

from flask import request, json, Response, Blueprint
from ..models.AddressModel import AddressModel, AddressSchema
from flask_cors import CORS, cross_origin

address_api = Blueprint('addresses', __name__)
address_schema = AddressSchema()

@address_api.route('/', methods=['POST'])
@cross_origin()
def add_new_address():
  """
  Create Address Function
  """
  req_data = request.get_json()
  data, error = address_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  # check if user already exist in the db
  address_in_db = AddressModel.get_address_by_email(data.get('email'))
  if address_in_db:
    message = {'error': 'Contact already exist, please supply another email address'}
    return custom_response(message, 400)
  
  address = AddressModel(data)
  address.save()

  return custom_response({'message': "contact added"}, 201)
  

@address_api.route('/', methods=['GET'])
@cross_origin()
def get_all_addresses():
  addresses = AddressModel.get_all_addresses()
  ser_addresses = address_schema.dump(addresses, many=True).data
  return custom_response(ser_addresses, 200)

@address_api.route('/<int:id>', methods=['GET'])
@cross_origin()
def get_an_address(id):
  """
  Get an address by id
  """
  address = AddressModel.get_one_address(id)
  if not address:
    return custom_response({'error': 'address not found'}, 404)
  
  ser_address = address_schema.dump(address).data
  return custom_response(ser_address, 200)

@address_api.route('/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_an_address(id):
  """
  Delete an address
  """
  address = AddressModel.get_one_address(id)
  if address == None:
      return custom_response({'message': 'id not found'}, 404)
  address.delete()
  return custom_response({'message': 'deleted'}, 204)

@address_api.route('/<int:id>', methods=['PUT'])
@cross_origin()
def edit_an_address(id):
  """
  Update an address
  """
  req_data = request.get_json()
  data, error = address_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)

  address = AddressModel.get_one_address(id)
  if address == None:
      return custom_response({'message': 'id not found'}, 404)

  address.update(data)
 
  return custom_response({'message': 'address updated successfully'}, 200)

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
