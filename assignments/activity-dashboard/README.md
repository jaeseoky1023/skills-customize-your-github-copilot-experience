# 📘 Assignment: School Activity Dashboard

## 🎯 Objective

Build a small browser-based dashboard that connects to the School Activities API. Practice using JavaScript `fetch()` to read JSON, send form data, update the DOM, and handle loading and error states.

## 📝 Tasks

### 🛠️ Display Activities from the API

#### Description
Complete the starter page so it requests the activities from `GET http://localhost:8000/activities` and displays each activity in the dashboard. Start the API with `uvicorn starter-code:app --reload`, then serve this assignment folder with `python3 -m http.server 5500` and open `http://localhost:5500/starter-code.html`.

#### Requirements
Completed program should:

- Fetch activities as JSON when the page loads
- Display each activity's name, description, capacity, and ID
- Show a useful loading message while the request is in progress
- Show a useful error message when the request fails

### 🛠️ Add a New Activity

#### Description
Connect the form to the API so a user can submit a new school activity. Send the form values as JSON to `POST http://localhost:8000/activities` and refresh the displayed list after a successful request.

#### Requirements
Completed program should:

- Read the activity name, description, and capacity from the form
- Send a `POST` request with a JSON request body
- Clear the form and display the newly created activity after a successful request
- Prevent submission when a required field is empty or the capacity is not a positive number

Example request body:

```json
{
  "name": "Chess Club",
  "description": "Weekly chess practice",
  "capacity": 16
}
```

### 🛠️ Remove Activities and Handle Failures

#### Description
Add a delete button to each activity and connect it to `DELETE http://localhost:8000/activities/{activity_id}`. Make the interface understandable when a request succeeds or fails.

#### Requirements
Completed program should:

- Delete the selected activity using its ID
- Refresh the list after a successful deletion
- Display a clear message when an activity cannot be created or deleted
- Keep the existing activities visible when a refresh request fails

The API may need FastAPI's `CORSMiddleware` configured to allow `http://localhost:5500`. Use the API's interactive documentation at `http://localhost:8000/docs` to inspect the available routes while you work.
