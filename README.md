# Employee Management System

A professional Employee Management System built using Flask, Python, SQLite, SQLAlchemy, and Bootstrap 5.

This project was developed as part of an internship assignment and demonstrates CRUD operations, database integration, and responsive UI design.

---

# Features

- Add Employee
- View Employee Dashboard
- Update Employee Details
- Delete Employee
- Dynamic Role & Department Dropdowns
- SQLite Database Integration
- Responsive Bootstrap UI
- Professional Dashboard Design
- Auto Database Table Creation
- Automatic Role & Department Seeding
- Flask Backend with SQLAlchemy ORM

---

# Tech Stack

## Backend
- Python
- Flask
- SQLAlchemy

## Frontend
- HTML5
- CSS3
- Bootstrap 5

## Database
- SQLite

---

# Project Structure

```bash
employee-management-system/
│
├── app.py
├── models.py
├── extensions.py
├── requirements.txt
├── Procfile
├── employee.db
│
├── templates/
│   ├── add_employee.html
│   ├── dashboard.html
│   └── update_employee.html
│
├── static/
│
└── venv/
```

---

# Installation

## Clone Repository

```bash
https://github.com/Aryan457-dev/Employee-Management-System
```

## Navigate to Project

```bash
cd employee-management-system
```

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python3 app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# Functionalities

## Add Employee
Users can add employees with:
- First Name
- Last Name
- Username
- Password
- Email
- Mobile Number
- Department
- Role
- Reporting Manager
- Date of Joining

---

## Dashboard
Displays:
- Employee Details
- Department
- Role
- Joining Date

---

## Update Employee
Users can update:
- Employee Information
- Department
- Role
- Contact Details

---

## Delete Employee
Users can delete employee records directly from dashboard.

---

# UI Features

- Responsive Layout
- Bootstrap Components
- Clean Professional Design
- Mobile-Friendly Dashboard
- Styled Forms & Tables

---

# Future Improvements

- Login Authentication
- Password Hashing
- Search Employees
- Employee Profile Page
- Pagination
- Role-Based Access Control
- REST API Integration
- Cloud Database Integration

---

# Deployment

This project is deployed using:

- Render
- Gunicorn

Live Demo:
https://employee-management-system-anf9.onrender.com/dashboard

---

# Author

Aryan Dabholkar

GitHub:
https://github.com/Aryan457-dev

---

# License

This project is developed for educational and internship purposes.
