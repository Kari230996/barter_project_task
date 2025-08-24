# 📦 Barter Platform — Django REST Application for Item Exchange

This is a Django web application implementing a platform for exchanging goods. Users can create ads, make exchange offers, filter listings, register, and interact visually with the site through a responsive interface.

---

## 🚀 Features

* User registration and authentication
* Create, edit, and delete ads
* Attach images via URLs
* Browse all ads and filter by:

  * category
  * condition (new/used)
  * keyword
* Exchange offers:

  * choose your item and another user's item
  * add a comment
  * track status (pending, accepted, rejected)
* Modal window for enlarged image and description
* Responsive Bootstrap 5 interface

---

## ⚙️ Local Setup with Docker

### 1. Clone the repository

```bash
git clone https://github.com/Kari230996/barter_project_task.git
cd barter_project_task
```

### 2. Run with Docker

1. Before starting, rename `.env.example` to `.env`
2. Open `.env` and replace `SECRET_KEY` with your own:

```bash
SECRET_KEY=django-insecure-replace-with-unique-key
```

3. Generate a new key (Windows example):

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

4. Start the project:

```bash
docker-compose up --build
```

### 3. Apply migrations

```bash
docker-compose exec web python manage.py migrate
```

### 4. Create a superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

The project will be available at: [http://localhost:8000](http://localhost:8000)

---

## 🚫 Alternative Setup without Docker (optional)

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🛠 Technologies

* Python 3.10+
* Django 5.x
* Django REST Framework
* drf-yasg (Swagger documentation)
* SQLite (default)
* Bootstrap 5 (responsive design)

---

## 🧪 Testing

### 📁 Pytest + Django: `tests/test_ads.py`

Run all tests:

```bash
pytest
```

Tests cover:

* Creating an ad
* Editing an ad
* Deleting an ad
* Keyword search
* Creating an exchange offer

---

## 🧾 API Documentation

Automatic Swagger documentation available at:

[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

⚠️ All API endpoints are prefixed with `/api/`.
Example request: `GET http://localhost:8000/api/ads/`

---

## ✨ Author

Developed as part of a test assignment. Visual emphasis — simplicity, clarity, and usability.

**📧 Contact:** [karina.apaeva96@gmail.com](mailto:karina.apaeva96@gmail.com)

---
