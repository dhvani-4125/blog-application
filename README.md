# Blog Application API

A RESTful Blog Application built using Django REST Framework and PostgreSQL.

## Features

- User Authentication using JWT
- Create and View Categories
- Create and View Blog Posts
- Search Blog Posts by Title
- Search Categories by Name
- PostgreSQL Database Integration
- Swagger API Documentation
- Docker Support

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Swagger (drf-yasg)
- Docker

## Project Structure

```text
backend/
│
├── blog/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd BLOG_APPLICATION
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Setup

Create a PostgreSQL database named:

```text
blog_db
```

Update database credentials in:

```text
config/settings.py
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

## Running the Project

```bash
python manage.py runserver
```

Server runs on:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | `/api/token/` |
| POST | `/api/token/refresh/` |

### Categories

| Method | Endpoint |
|---------|----------|
| GET | `/api/categories/` |
| POST | `/api/categories/` |

Search Category:

```text
/api/categories/?name=Technology
```

### Blog Posts

| Method | Endpoint |
|---------|----------|
| GET | `/api/posts/` |
| POST | `/api/posts/` |

Search Posts:

```text
/api/posts/?search=django
```

## Swagger Documentation

Swagger UI:

```text
http://127.0.0.1:8000/swagger/
```

ReDoc:

```text
http://127.0.0.1:8000/redoc/
```

## Docker

Build Image:

```bash
docker build -t blog-api .
```

Run Container:

```bash
docker run -p 8000:8000 blog-api
```

## Author

Dhvani Vanzwala