from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class HealthDataCreate(BaseModel):
    age: int
    weight: float
    height: float
    activity_level: str
    fitness_goal: str
    dietary_preference: str
    allergies: str
