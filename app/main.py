from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from .auth import get_current_user

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register a new user
@app.post("/register/")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

# Submit health data for logged-in user
@app.post("/health-data/")
def submit_health_data(health_data: schemas.HealthDataCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    user = crud.get_user_by_username(db, current_user)
    return crud.create_health_data(db=db, health_data=health_data, user_id=user.id)

# Get workout plan (dummy)
@app.get("/get-workout-plan/")
def get_workout_plan(current_user: str = Depends(get_current_user)):
    return {"plan": ["10 pushups", "20 squats", "15 minutes running"]}
