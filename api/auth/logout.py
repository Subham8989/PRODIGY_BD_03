from flask import make_response
from flask_restful import Resource
from flask_jwt_extended import unset_jwt_cookies, get_jwt_identity, jwt_required

class Logout(Resource):
  @jwt_required(locations=["cookies"])
  def post(self):
    username = get_jwt_identity()
    response = make_response({ "message": f"{str(username).capitalize()} logged out!" }, 202)
    unset_jwt_cookies(response)
    return response