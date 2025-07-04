from flask import make_response
from flask_restful import Resource, reqparse
from flask_bcrypt import generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from sqlalchemy.exc import IntegrityError

from ..models import User
from ..utils import role_type
from ...extensions import db

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="Name must be present!")
parser.add_argument("username", type=str, required=True, help="Username must be present!")
parser.add_argument("password", type=str, required=True, help="Password must be present!")
parser.add_argument("role", type=role_type, required=True, help="Role must be valid!")

class Register(Resource):
  def post(self):
    args = parser.parse_args()
    name = args["name"]
    username = args["username"]
    password = args["password"]
    role = args["role"]

    user = db.session.execute(db.select(User).filter_by(username=username)).first()
    if user:
      return { "message": "User already exists!" }, 400 
    try:
      new_user = User(name=name, username=username, password=generate_password_hash(password=password), role=role)
      db.session.add(new_user)
      db.session.commit()
    except IntegrityError:
      db.session.rollback()
      return { "message": "Database constraint violated!" }, 409
    except Exception as e:
      db.session.rollback()
      return { "message": f"Some error occured: {e}" }, 500
    
    access_token = create_access_token(identity=username, additional_claims={ "role": role })
    refresh_token = create_refresh_token(identity=username)
    response = make_response({ "message": "User created!" }, 201)
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)
    return response