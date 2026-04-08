# RBAC Django API

A Role-Based Access Control system built with Django REST Framework.

## Tech Stack
- Python 3
- Django
- Django REST Framework
- SQLite

## Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/rbac-django-api.git
cd rbac-django-api
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/permissions/` | List & create permissions |
| GET/PUT/DELETE | `/api/permissions/{id}/` | Manage single permission |
| GET/POST | `/api/roles/` | List & create roles |
| GET/PUT/DELETE | `/api/roles/{id}/` | Manage single role |
| GET/POST | `/api/users/` | List & create users |
| GET/PUT/DELETE | `/api/users/{id}/` | Manage single user |
| GET | `/api/check-permission/{user_id}/{permission_name}/` | Check if user has permission |

## Architecture

```
core/          → Django project settings & URLs
rbac/
  models.py    → User, Role, Permission models
  serializers.py → DRF serializers
  views.py     → ViewSets + permission check endpoint
  urls.py      → API routing
```

## Key Feature — Permission Check

```
GET /api/check-permission/1/can_edit/
```
Returns whether a specific user has a given permission through their assigned role.

## Assumptions
- One user can have one role at a time
- Permissions are assigned to roles, not directly to users
- SQLite used for simplicity
