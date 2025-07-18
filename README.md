````markdown
# Developing a Platform to Assist in Learning Programming with Integrated AI Assistant 

An educational platform built with Django. This project was developed as part of a university graduation project to assist users in learning programming through interactive tasks, assessments, and guided lessons.

## 📚 Project Overview

The platform allows:
- User registration and login
- Viewing and solving programming problems
- Admin panel for managing content and users
- Use of Django templating for frontend rendering

---

## 🔧 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Django Templates
- **Database**: SQLite (default)
- **Tools**: Cisco Packet Tracer (for networking simulations), Git

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/hassanmok/final_edu_2.git
cd final_edu_2
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Project Structure

```
final_edu_2/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── README.md
├── your_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── your_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
```

---

## 🔒 Admin Panel

After creating a superuser, access the Django admin panel at:

```
http://127.0.0.1:8000/admin/
```

Use your superuser credentials to log in and manage content.

---

## 📬 Contact

Developed by **Hassan Abdulhadi Kadhim**
For inquiries: \[[hassanmok2002@gmail.com](mailto:hassanmok2002@gmail.com)]
