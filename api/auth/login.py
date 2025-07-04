from flask import make_response
from flask_restful import Resource, reqparse
from flask_bcrypt import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies

from ...extensions import db
from ..models import User

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="Username is required!")
parser.add_argument("password", type=str, required=True, help="Password is required!")

class Login(Resource):
  def post(self):
    args = parser.parse_args()
    username = args["username"]
    password = args["password"]

    user = db.session.execute(db.select(User).filter_by(username=username)).first()
    if not user:
      return { "message": "User not found!" }, 404
    
    if user and check_password_hash(user[0].password, password):
      response = make_response({ "message": "Log in successful!" }, 202)
      access_token = create_access_token(identity=username, additional_claims={ "role": str(user[0].role).split(".")[1].lower() })
      refresh_token = create_refresh_token(identity=username)
      set_access_cookies(response, access_token)
      set_refresh_cookies(response, refresh_token)
      return response
    
    return { "message": "Incorrect Password!" }, 401