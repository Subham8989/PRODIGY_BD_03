import functools
from flask_jwt_extended import jwt_required, get_jwt

def role_required(role: str):
  def wrapper(fn):
    @functools.wraps(fn)
    @jwt_required(locations=["cookies"])
    def decorator(*args, **kwargs):
      claims = get_jwt()
      user_role = claims.get("role", None)
      print("Role", role)
      print("User Role", user_role)
      if str(user_role) != str(role):
        return { "message": "Access Forbidden: Insufficient Role" }, 403
      return fn(*args, *kwargs)
    return decorator
  return wrapper