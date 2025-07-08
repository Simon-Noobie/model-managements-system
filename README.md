# Model Management System

## Overview

Model Management System is a Django-based web application designed to manage metadata for machine learning models. It provides both a user interface and backend API for creating, storing, and tracking model details such as:
- Model names
- Features
- Target variables
- Data types

It supports standard CRUD operations through both web pages and REST APIs.

---

## Features

- Web-based UI for CRUD operations on ML model metadata
- REST API built with Django REST Framework
- Admin panel for managing users and models
- ASGI support (via Uvicorn or Daphne) for future WebSocket extensions

---

## Project Structure

```
modelMngSystem/
├── main/                   # Core Django app
│   ├── admin.py            # Admin panel configuration
│   ├── apps.py
│   ├── models.py           # ModelManagement model
│   ├── serializers.py      # DRF serializers
│   ├── urls.py             # App-level routing
│   ├── views.py            # View logic
│   ├── tests.py
│   └── migrations/         # Database migrations
│
├── modelMngSystem/         # Project-level configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Project-level URLs
│   ├── asgi.py             # ASGI config for async
│   └── wsgi.py             # WSGI config
│
├── static/crud op/         # HTML templates for CRUD UI
│   ├── create.html
│   ├── read.html
│   ├── update.html
│   └── delete.html
│
├── manage.py               # Django CLI entry point
└── README.md               # Project documentation
```

---

## Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd modelMngSystem
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   > For full async support, use an ASGI server:

   - With Uvicorn:
     ```bash
     uvicorn modelMngSystem.asgi:application
     ```
   - Or with Daphne:
     ```bash
     daphne modelMngSystem.asgi:application
     ```

---

## Usage

- Visit `http://127.0.0.1:8000/` to access the web interface
- Visit `/admin/` to access the Django admin dashboard
- Use CRUD pages:
  - Create: `/static/crud op/create.html`
  - Read: `/static/crud op/read.html`
  - Update: `/static/crud op/update.html`
  - Delete: `/static/crud op/delete.html`
- API endpoints:
  - GET/POST: `/api/models/`
  - GET/PUT/DELETE: `/api/models/<id>/`

---

## WebSocket Support (Optional/Future Use)

The project includes ASGI configuration for potential real-time features. To prepare:
- Ensure `ASGI_APPLICATION` is set in `settings.py`:
  ```python
  ASGI_APPLICATION = "modelMngSystem.asgi.application"
  ```

---

## Contributing

Contributions are welcome! Please fork the repo and create a pull request. Follow PEP8 and write tests where applicable.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.