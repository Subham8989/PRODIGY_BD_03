from flask_restful import Resource

class HomeRoute(Resource):
  def get(self):
    return { "message": "Welcome to our API!" }, 200