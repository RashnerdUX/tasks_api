# Todo API

A RESTful API for managing todo lists built with Django and Django REST Framework.

Link to Project Brief - https://roadmap.sh/projects/todo-list-api

## Overview

This Todo API allows users to create, read, update, and delete todo items. The API supports user authentication with token-based authorization, ensuring that users can only access and modify their own todo items.

## Features

- User registration and authentication
- Token-based authentication
- CRUD operations for todo items
- Permission-based access control
- User-specific todo lists

## API Endpoints

| Endpoint | Method | Description | Authentication Required |
|----------|--------|-------------|-------------------------|
| `/todolist/` | GET | Get all todos for the authenticated user | Yes |
| `/todolist/` | POST | Create a new todo | Yes |
| `/todo/<id>/` | GET | Get a specific todo | Yes |
| `/todo/<id>/` | PUT | Update a todo completely | Yes |
| `/todo/<id>/` | PATCH | Update a todo partially | Yes |
| `/todo/<id>/` | DELETE | Delete a todo | Yes |
| `/users/` | GET | Get all users | No |
| `/users/<id>/` | GET | Get a specific user | No |
| `/user/register/` | POST | Register a new user | No |
| `/user/login/` | POST | Login and get authentication token | No |
| `/api-token-auth/` | POST | Get authentication token | No |
| `/chckuser/` | GET | Check if user is authenticated | Yes |

## Getting Started

### Prerequisites

- Python 3.x
- Django 5.x
- Django REST Framework

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/todo-api.git
   cd todo-api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage Examples

### Register a new user

```
POST /user/register/
```
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword"
}
```

### Login and get token

```
POST /user/login/
```
```json
{
  "username": "testuser",
  "password": "securepassword"
}
```

Response:
```json
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Create a new todo

```
POST /todolist/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
```json
{
  "title": "Complete project",
  "description": "Finish the Django REST Framework project"
}
```

### Get all todos for current user

```
GET /todolist/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

## Project Structure

- `api/models.py`: Defines the Todo model
- `api/serializers.py`: Serializers for Todo and User models
- `api/views.py`: API views for handling requests
- `api/permissions.py`: Custom permissions for controlling access
- `api/urls.py`: URL routing for the API endpoints
- `todo_api/settings.py`: Project settings including REST Framework configuration

## Security Notes

- The project includes token-based authentication
- Users can only access and modify their own todos
- Custom permissions are implemented to ensure proper access control

## Development

### Adding New Endpoints

To add new endpoints, update the `api/urls.py` file and create corresponding view classes in `api/views.py`.

### Custom Permissions

The project uses a custom permission class called `IsOwnerReadOnly` which ensures that users can only modify their own todo items.

## Production Considerations

Before deploying to production:

1. Change the `SECRET_KEY` in settings.py
2. Set `DEBUG = False` in settings.py
3. Update `ALLOWED_HOSTS` with your domain
4. Consider using a more robust database like PostgreSQL
5. Implement HTTPS
6. Set up proper CORS configuration

## License

[MIT License](LICENSE)