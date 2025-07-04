def role_type(role: str): 
  if role.lower() not in ["user", "admin"]:
    raise ValueError("Invalid value of role given!")
  return role