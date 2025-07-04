from flask import Flask

from ..config import Config

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  from ..extensions import api, jwt, db, migrate, bcrypt
  from .auth import Login, Register, Logout
  from .routes import UserRoute, HomeRoute
  api.add_resource(Login, "/auth/login")
  api.add_resource(Logout, "/auth/logout")
  api.add_resource(Register, "/auth/register")
  api.add_resource(HomeRoute, "/")
  api.add_resource(UserRoute, "/users")
  api.init_app(app)
  jwt.init_app(app)
  db.init_app(app)
  bcrypt.init_app(app)
  migrate.init_app(app, db, directory="api/migrations")
  return app