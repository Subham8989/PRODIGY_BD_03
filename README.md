# Flask REST API with JWT Authentication

This project is a RESTful API built with **Flask**, utilizing extensions like **Flask-RESTful**, **Flask-JWT-Extended**, **Flask-Migrate**, and **Flask-SQLAlchemy**. It features JWT-based authentication and role-based access control.

---

## 🚀 Features

- User **Registration**, **Login**, and **Logout** endpoints
- Passwords hashed using **bcrypt**
- JWT tokens issued on successful login
- Protected routes using JWT
- Role-based access control (admin, user, owner)

---

## 🌐 API Endpoints

| Endpoint             | Method | Description               |
| -------------------- | ------ | ------------------------- |
| `/`                  | GET    | Home route                |
| `/auth/login`        | POST   | User login                |
| `/auth/logout`       | POST   | User logout               |
| `/auth/register`     | POST   | User registration         |
| `/users`             | GET    | Get user info (Protected) |

---

## 📝 Project Structure

```
api/
├── auth/            # Auth logic (login, register)
├── migrations/      # Flask-Migrate files
├── models/          # SQLAlchemy models
├── routes/          # API route definitions
├── utils/           # Utility functions (e.g., role decorators)
├── __init__.py      # App factory
config.py            # Configurations
extensions.py        # Flask extensions setup
run.py               # Entry point
requirements.txt     # Python dependencies
```

---

## 🔐 JWT Authentication

- On **login**, a JWT token is generated and sent back.
- For protected endpoints (e.g., `/users`), the client must include the token in the response cookies.

---

## 🪮 Role-Based Access Control

Implemented using custom decorators. Example roles: `admin` and `user`

```python
@role_required("admin")
def admin_only_route():
    ...
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Subham8989/PRODGIGY_BD_03.git
cd PRODGIGY_BD_03
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file with the following:

```
FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
DATABASE_URI=mysql://user:password@localhost:port/PRODIGY_BD_03
```

### 5. Run migrations

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 6. Run the application

```bash
flask run
```

---

## 🌍 Technologies Used

- Flask
- Flask-RESTful
- Flask-JWT-Extended
- Flask-Migrate
- Flask-SQLAlchemy
- MySQL
- Bcrypt-Flask

---

## 🙏 Acknowledgements

Thanks to the Prodigy team for the challenge and resources.

---