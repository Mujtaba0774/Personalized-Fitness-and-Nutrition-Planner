from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class HealthData(Base):
    __tablename__ = "health_data"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="health_data")
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    activity_level = Column(String)
    fitness_goal = Column(String)
    dietary_preference = Column(String)
    allergies = Column(String)

User.health_data = relationship("HealthData", uselist=False, back_populates="user")
