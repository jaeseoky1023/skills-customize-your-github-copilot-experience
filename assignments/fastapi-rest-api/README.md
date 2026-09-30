# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for school activities using FastAPI. Practice defining resource routes, accepting JSON data, and returning useful HTTP status codes.

## 📝 Tasks

### 🛠️	Read Activity Data

#### Description
Complete the starter code to let clients view all school activities or look up one activity by its ID. Run the API with `uvicorn starter-code:app --reload` and try the routes in the interactive docs at `/docs`.

#### Requirements
Completed program should:

- Return all activities as a JSON list from `GET /activities`
- Return one activity from `GET /activities/{activity_id}`
- Return an HTTP 404 error when the requested activity ID does not exist


### 🛠️	Create and Delete Activities

#### Description
Add routes that allow clients to create a school activity and delete an existing one. Use the provided `ActivityCreate` model to validate incoming JSON.

#### Requirements
Completed program should:

- Create an activity with `POST /activities`, assign it a unique ID, and return the created activity with HTTP 201
- Delete an activity with `DELETE /activities/{activity_id}`
- Return an HTTP 404 error when asked to delete an activity that does not exist

Example request body for `POST /activities`:

```json
{
  "name": "Chess Club",
  "description": "Weekly chess practice",
  "capacity": 16
}
```