# Task Management API

A full-stack Task Management application with a Flask REST API backend and a JavaScript frontend.

## Features

- Create, read, update, and delete tasks
- Filter tasks by status
- Set task priorities (low, medium, high)
- Track task statuses (todo, in_progress, done)
- Clean and responsive user interface
- Input validation and error handling

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Install required Python packages:
```bash
pip install flask flask-cors
```

### Running the Application

1. Start the Flask server:
```bash
python main.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

The server will run on port 5000 by default.

## API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Get All Tasks
**GET** `/tasks`

Get all tasks with optional status filtering.

**Query Parameters:**
- `status` (optional): Filter by task status (`todo`, `in_progress`, `done`)

**Response:** `200 OK`
```json
[
  {
    "id": "string",
    "title": "string",
    "description": "string",
    "status": "todo",
    "priority": "medium",
    "created_at": "2025-12-16T10:30:00"
  }
]
```

**Example:**
```bash
curl http://localhost:5000/tasks
curl http://localhost:5000/tasks?status=todo
```

---

#### 2. Create a New Task
**POST** `/tasks`

Create a new task.

**Request Body:**
```json
{
  "title": "string (required)",
  "description": "string (required)",
  "status": "todo | in_progress | done (optional, default: todo)",
  "priority": "low | medium | high (optional, default: medium)"
}
```

**Response:** `201 Created`
```json
{
  "id": "generated-uuid",
  "title": "string",
  "description": "string",
  "status": "todo",
  "priority": "medium",
  "created_at": "2025-12-16T10:30:00"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Fix bug","description":"Fix login issue","priority":"high"}'
```

---

#### 3. Get a Specific Task
**GET** `/tasks/:id`

Get details of a specific task by ID.

**Response:** `200 OK`
```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "status": "todo",
  "priority": "medium",
  "created_at": "2025-12-16T10:30:00"
}
```

**Error Response:** `404 Not Found`
```json
{
  "error": "Task not found"
}
```

**Example:**
```bash
curl http://localhost:5000/tasks/abc-123-def
```

---

#### 4. Update a Task
**PATCH** `/tasks/:id`

Update task fields (status, title, description, or priority).

**Request Body:** (all fields optional)
```json
{
  "title": "string",
  "description": "string",
  "status": "todo | in_progress | done",
  "priority": "low | medium | high"
}
```

**Response:** `200 OK`
```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "status": "done",
  "priority": "medium",
  "created_at": "2025-12-16T10:30:00"
}
```

**Example:**
```bash
curl -X PATCH http://localhost:5000/tasks/abc-123-def \
  -H "Content-Type: application/json" \
  -d '{"status":"done"}'
```

---

#### 5. Delete a Task
**DELETE** `/tasks/:id`

Delete a task by ID.

**Response:** `200 OK`
```json
{
  "message": "Task deleted successfully"
}
```

**Error Response:** `404 Not Found`
```json
{
  "error": "Task not found"
}
```

**Example:**
```bash
curl -X DELETE http://localhost:5000/tasks/abc-123-def
```

---

## HTTP Status Codes

- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid input or validation error
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Task Model

```json
{
  "id": "string (UUID)",
  "title": "string",
  "description": "string",
  "status": "todo | in_progress | done",
  "priority": "low | medium | high",
  "created_at": "ISO 8601 timestamp"
}
```

## Frontend Features

- **Task List**: View all tasks with color-coded status badges
- **Create Form**: Add new tasks with title, description, and priority
- **Status Updates**: Change task status with dropdown menus
- **Filtering**: Filter tasks by status (All, To Do, In Progress, Done)
- **Delete**: Remove tasks with confirmation
- **Responsive Design**: Clean interface that works on all devices

## Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: JavaScript, HTML, CSS
- **Storage**: In-memory (data resets on server restart)
- **CORS**: Enabled for cross origin requests

## Notes

- No authentication is implemented (suitable for local development only)
- The application runs in debug mode for development purposes

# AI Use
- Mostly for debuggind code and improving form / efficency. Also for the html part to help make the site look better on local machine.
- Used to make the README file more redable and clear to understand.

# Limitations
- Time constraint was a big limit. I had to sacrifice functionality to ensure a solid basic program. With more time available I would work mostly on the front-end as the features are present and fully functional. However, more and better features could also be implemented with little effort as the main function is already there and working. 

# Final Note
Since my experience with APIs is quite limited I took some time at the beginning researching and looking at old projects I worked on. I then started planning each different feature provided in the requirements until it was met. Moved on until all features were present and the endpoints were all sending the correct value. 

# Work By:
# Alessandro Coatto