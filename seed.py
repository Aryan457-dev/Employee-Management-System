from app import app
from extensions import db
from models import Role, Department

with app.app_context():

    # ROLES
    roles = [
        'Admin',
        'Manager',
        'Team Leader',
        'Employee'
    ]

    for role_name in roles:

        role_exists = Role.query.filter_by(
            role_name=role_name
        ).first()

        if not role_exists:

            role = Role(role_name=role_name)

            db.session.add(role)

    # DEPARTMENTS
    departments = [
        'Operation',
        'Sales',
        'Accounts',
        'IT'
    ]

    for department_name in departments:

        department_exists = Department.query.filter_by(
            department_name=department_name
        ).first()

        if not department_exists:

            department = Department(
                department_name=department_name
            )

            db.session.add(department)

    db.session.commit()

    print("Database seeded successfully")