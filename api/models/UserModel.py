import enum
from uuid import uuid4
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, DateTime, Enum
from datetime import datetime, timezone

from ...extensions import db

class Role(enum.Enum):
  user = "user"
  admin = "admin"

class User(db.Model):
  __tablename__ = "users"

  id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
  password: Mapped[str] = mapped_column(String(100), nullable=False)
  role: Mapped[Role] = mapped_column(Enum(Role), nullable=False)

  created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=timezone.utc))
  updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=timezone.utc), onupdate=datetime.now(tz=timezone.utc))