from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

api = Api()
jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()