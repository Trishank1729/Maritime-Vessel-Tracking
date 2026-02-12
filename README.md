# Maritime Vessel Tracking

A full-stack web application for tracking maritime vessels with user authentication, profile management, and administrative dashboard.

## Live Demo
- **Frontend**: https://maritime-vessel-tracking.vercel.app
- **Backend API**: https://maritime-vessel-tracking.onrender.com
- **API Docs**: https://maritime-vessel-tracking.onrender.com/api/

## Features

✅ User Registration & Authentication  
✅ JWT Token-based Login  
✅ User Profile Management  
✅ Admin Dashboard  
✅ User Statistics  
✅ Role-based Access (Operator, Analyst, Admin)  
✅ CORS Support for cross-origin requests  
✅ Responsive React UI  

## Tech Stack

### Backend
- Django 6.0.2
- Django REST Framework 3.16.1
- SimpleJWT (JWT Authentication)
- Django CORS Headers
- Gunicorn (Production Server)

### Frontend
- React 19.2.4
- React Router DOM
- Axios (HTTP Client)
- React Scripts

### Database
- SQLite (Development)
- PostgreSQL (Production recommended)

## Project Structure

```
Maritime-Vessel-Tracking/
├── backend/
│   ├── api/
│   │   ├── models.py         # User model with roles
│   │   ├── views.py          # API endpoints
│   │   ├── serializers.py    # Data serialization
│   │   ├── urls.py           # API routing
│   │   └── migrations/
│   ├── maritime_backend/
│   │   ├── settings.py       # Django configuration
│   │   ├── urls.py           # Main URL config
│   │   └── wsgi.py
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── pages/            # Login, Register, Profile
│   │   ├── components/       # Navbar, etc
│   │   ├── services/         # API calls
│   │   └── App.js           # Main component
│   ├── public/
│   └── package.json
└── README.md
```

## Installation

### Prerequisites
- Python 3.13+
- Node.js 18+
- Git

### Local Development

**1. Clone Repository**
```bash
git clone https://github.com/YOUR_USERNAME/Maritime-Vessel-Tracking.git
cd Maritime-Vessel-Tracking
```

**2. Setup Backend**
```bash
cd backend

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Backend runs on: `http://localhost:8000`

**3. Setup Frontend**
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend runs on: `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/login/` - Get JWT tokens
- `POST /api/register/` - Create new user
- `POST /api/token/refresh/` - Refresh JWT token

### User Profile
- `GET /api/profile/` - Get your profile
- `PUT /api/profile/update/` - Update your profile

### User Management (Admin)
- `GET /api/users/` - List all users
- `GET /api/users/<id>/` - Get specific user
- `PUT /api/users/<id>/` - Update specific user

### Statistics (Admin)
- `GET /api/stats/` - Get user statistics

## Admin Credentials

Default admin account:
- **Username**: admin
- **Password**: admin123

Access admin panel: `http://localhost:8000/admin/`

## Deployment

### Deploy to Render

1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create Web Service from GitHub repository
4. Configure:
   - Build Command: `pip install -r backend/requirements.txt && python backend/manage.py migrate`
   - Start Command: `gunicorn maritime_backend.wsgi`
5. Deploy!

### Deploy Frontend to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Select frontend folder as root directory
4. Add environment variable:
   ```
   REACT_APP_API_URL=https://your-backend-url.onrender.com
   ```
5. Deploy!

## Environment Variables

Create `.env` file in backend folder:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
DATABASE_URL=your-database-url
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://your-frontend.vercel.app
```

## Testing

Run backend tests:
```bash
cd backend
python manage.py test api --verbosity=2
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Contact

For questions or support, please open an issue on GitHub or contact the maintainer.

## Roadmap

- [ ] Add vessel tracking map
- [ ] Real-time location updates
- [ ] Mobile app
- [ ] Advanced analytics dashboard
- [ ] Export reports to PDF

---

**Made with ❤️ for Maritime Vessel Tracking**
