# Learning Management System (LMS)

A Django-based Learning Management System with MySQL database.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure MySQL database:
- Create a MySQL database named 'lms_db'
- Update database settings in lms/settings.py

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Features
- Student Management
- Teacher Management
- Course Management
- Study Material Management
- Quiz Management
- Admin Panel for CRUD operations 