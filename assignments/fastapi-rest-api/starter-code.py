from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="School Activities API")


class ActivityCreate(BaseModel):
    name: str
    description: str
    capacity: int


class Activity(ActivityCreate):
    id: int


activities: dict[int, Activity] = {
    1: Activity(
        id=1,
        name="Art Club",
        description="Explore drawing and painting",
        capacity=12,
    ),
    2: Activity(
        id=2,
        name="Robotics Team",
        description="Design and build robots",
        capacity=10,
    ),
}


@app.get("/activities")
def list_activities():
    # Return all activities.
    pass


@app.get("/activities/{activity_id}")
def get_activity(activity_id: int):
    # Return the matching activity, or raise an HTTP 404 error.
    pass


@app.post("/activities", status_code=status.HTTP_201_CREATED)
def create_activity(activity: ActivityCreate):
    # Assign a unique ID, save the activity, and return it.
    pass


@app.delete("/activities/{activity_id}")
def delete_activity(activity_id: int):
    # Delete the matching activity, or raise an HTTP 404 error.
    pass