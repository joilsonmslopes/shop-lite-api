# 🛍️ ShopLite

**ShopLite** is a minimalist e-commerce backend API built with Python, FastAPI, and SQLModel.  
It was created for learning purposes, with focus on clean architecture, business logic, and backend fundamentals.

---

## 🚀 Features

- 🔐 User registration with password hashing
- 🧱 SQLite database with SQLModel ORM
- 🧰 Modular project structure (auth, models, routes, etc.)
- 📦 Ready for Docker & deployment (coming soon)
- 🔄 Version control with semantic commits and PR reviews

---

## 📁 Project Structure

```
shoplite/
├── db.py                  # Database engine and session
├── main.py                # App entry point
├── models.py              # SQLModel data models
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignored files for Git
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
└── ...
```

---

## 📦 Requirements

- Python 3.10+
- Conda (recommended) or venv
- FastAPI
- SQLModel
- passlib[bcrypt]
- Uvicorn

Install all dependencies with:

```bash
pip install -r requirements.txt

---

## ✅ Roadmap

- Setup database and base project structure
- Implement user registration
- Add user login and JWT auth
- Create product catalog
- Implement cart and orders
- Dockerize the application

---

## 🧪 Learning Goal

This project simulates a real-world backend development flow, including:

- Defining business rules
- Modeling data and relationships
- Working with authentication and APIs
- Writing clean, modular Python code
- Using GitHub like a real team (commits, PRs, reviews)

---

## 🧑‍💻 Author

Developed by **Joilson Miranda**  
Frontend Developer transitioning to backend with Python & FastAPI.
