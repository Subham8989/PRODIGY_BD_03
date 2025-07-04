from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from ...utils import role_required
from ...models import User
from ....extensions import db

class UserRoute(Resource):
  @role_required("admin")
  def get(self):
    user_list = list()
    try:
      users = db.session.execute(db.select(User))
      for user in users:
        user_list.append({ "name": user[0].name, "username": user[0].username, "role": str(user[0].role) })
    except IntegrityError:
      db.session.rollback()
      return { "message": "Database Constraint Violated!" }, 409
    except Exception as e:
      return { "message": f"Error Occured! {e}"}, 500

    return user_list, 200