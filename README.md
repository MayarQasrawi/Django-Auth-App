# Django Auth App with JWT & Profile

A simple Django authentication app using **Django REST Framework** and **JWT tokens**, with a separate **Profile model** for extra user information.

## Features

- Register user with email, username, password
- Automatic Profile creation on registration
- JWT-based authentication (access + refresh tokens)
- User login
- View logged-in user info (`/me/`)
- Update profile info (bio, phone, avatar)
- Logout (blacklist refresh token)
- Refresh access token

## Tech Stack

- **Django 4.2**
- **Django REST Framework**
- **djangorestframework-simplejwt** for JWT
- **PostgreSQL** as database
- **python-decouple** for environment variable management

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up `.env` file with:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME=mydb
   DB_USER=myuser
   DB_PASSWORD=mypassword
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Method  | Endpoint                 | Description                                        |
| ------- | ------------------------ | -------------------------------------------------- |
| POST    | /api/auth/register/      | Register new user (creates profile automatically) |
| POST    | /api/auth/login/         | Login user and get access + refresh JWT tokens    |
| POST    | /api/auth/logout/        | Logout user (blacklist refresh token)             |
| POST    | /api/auth/token/refresh/ | Refresh JWT access token                           |
| GET     | /api/auth/me/            | Get logged-in user info                            |
| GET/PUT | /api/auth/profile/       | View or update user profile info                   |

## Notes

- Use **Authorization: Bearer \<access_token>** header for authenticated endpoints.
- Profile is linked one-to-one with User.
- Tokens follow **JWT standard** using `rest_framework_simplejwt`.
