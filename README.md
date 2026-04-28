# Task Management System

This is a task management web application built with Python and Django. It allows users to create, manage, and track their tasks efficiently. The project also uses Redis and Celery for handling background tasks asynchronously.

---

## Features

- User authentication (signup, login)
- Create tasks
- View all tasks
- Update and edit tasks
- Delete tasks
- User-specific task management (users can manage their own tasks)
- Background task processing using Celery
- Redis used as a message broker for task queue

---

## API Endpoints (if applicable)

| Method | URL          | Description         |
|--------|-------------|---------------------|
| POST   | /register/  | Register a new user |
| POST   | /login/     | Login user          |
| GET    | /tasks/     | List all tasks      |
| POST   | /tasks/     | Create a new task   |
| PUT    | /tasks/{id}/| Update a task       |
| DELETE | /tasks/{id}/| Delete a task       |

---

## Technologies Used

- Python  
- Django  
- SQLite (database)  
- Redis (message broker)  
- Celery (for asynchronous task processing)  
- Django Authentication System  

---

## How to Run Locally

### Clone the repository

```bash
git clone https://github.com/Nishant18-gif/Task_management.git
Navigate to the project directory
cd Task_management
Create and activate a virtual environment
python -m venv venv
On Windows
venv\Scripts\activate
On macOS/Linux
source venv/bin/activate
Install dependencies
pip install -r requirements.txt
Setup Redis

Make sure Redis is installed and running on your system.

On Windows
redis-server
On macOS/Linux
sudo service redis start
Run Migrations
python manage.py migrate
Start Celery Worker

Open a new terminal and run:

celery -A Task_management worker --loglevel=info
Run the Development Server
python manage.py runserver

Open your browser and go to:

http://127.0.0.1:8000/
Notes
Make sure Python is installed on your system
Ensure virtual environment is activated before installing dependencies
Redis server must be running before starting Celery
Run Celery worker in a separate terminal
Update .env file if required
Author

Nishant Pareek

GitHub: https://github.com/Nishant18-gif
