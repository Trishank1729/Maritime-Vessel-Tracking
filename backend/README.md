# Maritime Vessel Tracking - Django Backend

## Overview
Complete Django REST Framework backend with JWT authentication and user role management (Operator, Analyst, Admin).

## Features
✅ **User Authentication**: JWT-based login/logout with refresh tokens  
✅ **User Registration**: Create new users with email and password  
✅ **User Roles**: Operator, Analyst, Admin with role-based access control  
✅ **User Profiles**: View and update user profile information  
✅ **Admin Dashboard**: Admin endpoints for user management and statistics  
✅ **CORS Support**: Full CORS configuration for frontend integration  
✅ **Security**: Password hashing, token validation, permission checks  

## Project Structure
```
backend/
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── db.sqlite3
├── maritime_backend/
│   ├── settings.py       # Django configuration
│   ├── urls.py           # Main URL routing
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
└── api/
    ├── models.py         # CustomUser model with roles
    ├── views.py          # API views
    ├── serializers.py    # DRF serializers
    ├── urls.py           # API routes
    ├── admin.py          # Django admin config
    ├── apps.py
    ├── tests.py
    ├── migrations/
    └── __init__.py
```

## Installation & Setup

### 1. Prerequisites
- Python 3.8+
- pip

### 2. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Create Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Admin)
```bash
python manage.py createsuperuser
# or use the pre-configured admin account:
# Username: admin
# Password: admin123
# Email: admin@example.com
```

### 5. Run Development Server
```bash
python manage.py runserver 8000
```

Server will be available at: `http://127.0.0.1:8000`

## API Endpoints

### Authentication
- **POST** `/api/login/` - Login user (returns JWT tokens)
- **POST** `/api/token/refresh/` - Refresh access token
- **POST** `/api/register/` - Register new user

### User Profile
- **GET** `/api/profile/` - Get authenticated user's profile
- **PUT** `/api/profile/update/` - Update user profile

### User Management (Admin Only)
- **GET** `/api/users/` - List all users
- **GET** `/api/users/<id>/` - Get specific user
- **PUT** `/api/users/<id>/` - Update specific user
- **GET** `/api/stats/` - Get user statistics

## Login Request Example
```json
POST /api/login/
{
  "username": "admin",
  "password": "admin123"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "username": "admin",
  "role": "admin"
}
```

## Register Request Example
```json
POST /api/register/
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepass123",
  "password_confirm": "securepass123",
  "fullname": "John Doe"
}

Response:
{
  "detail": "User registered successfully",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "fullname": "John Doe",
    "role": "operator",
    "created_at": "2026-02-12T10:30:00Z"
  }
}
```

## Available User Roles
- **Operator** (Default): Can view and operate vessel tracking
- **Analyst**: Can view analytics and reports
- **Admin**: Full administrative access (create users, manage roles, view stats)

## Authentication Headers
All requests (except login/register) require JWT token in header:
```
Authorization: Bearer <access_token>
```

## Configuration (.env)
```env
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Important**: Change `SECRET_KEY` and set `DEBUG=False` in production!

## Frontend Connection
The frontend is configured to connect to:
- Base URL: `http://127.0.0.1:8000/api`

Frontend `.env` file:
```env
REACT_APP_API_URL=http://127.0.0.1:8000/api
```

## Admin Panel
Access Django admin: `http://127.0.0.1:8000/admin`
- Username: `admin`
- Password: `admin123`

Manage users, roles, and permissions from the admin panel.

## CORS Configuration
Allowed origins:
- http://localhost:3000
- http://127.0.0.1:3000

## Database
- SQLite (db.sqlite3) for development
- Can be changed to PostgreSQL for production

## JWT Token Expiration
- Access Token: 60 minutes
- Refresh Token: 7 days

## Testing API Endpoints

### Test Login
```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

### Test Profile (with token)
```bash
curl -X GET http://127.0.0.1:8000/api/profile/ \
  -H "Authorization: Bearer <your_access_token>"
```

## Troubleshooting

**Q: ModuleNotFoundError: No module named 'django'**
A: Run `pip install -r requirements.txt`

**Q: Connection refused on localhost:8000**
A: Make sure backend server is running: `python manage.py runserver 8000`

**Q: CORS error from frontend**
A: Check CORS_ALLOWED_ORIGINS in settings.py includes your frontend URL

**Q: Port 8000 already in use**
A: Run on different port: `python manage.py runserver 8001`

## Production Deployment
1. Set `DEBUG=False` in `.env`
2. Change `SECRET_KEY` to a secure value
3. Update `ALLOWED_HOSTS` with production domain
4. Use PostgreSQL instead of SQLite
5. Use gunicorn or similar WSGI server
6. Set up nginx as reverse proxy

## License
MIT License

## Support
For issues or questions, contact the development team.
