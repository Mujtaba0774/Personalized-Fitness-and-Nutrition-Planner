from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = fake_hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_health_data(db: Session, health_data: schemas.HealthDataCreate, user_id: int):
    db_health_data = models.HealthData(**health_data.dict(), user_id=user_id)
    db.add(db_health_data)
    db.commit()
    db.refresh(db_health_data)
    return db_health_data
