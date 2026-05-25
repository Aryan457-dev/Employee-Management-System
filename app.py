from flask import Flask, render_template, request, redirect
from datetime import datetime

from extensions import db
from models import Role, Department, User

app = Flask(__name__)

# DATABASE CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# CREATE TABLES
with app.app_context():
    db.create_all()

    # ADD DEFAULT ROLES
    roles = ['Admin', 'HR', 'Manager', 'Employee']

    for role_name in roles:
        existing_role = Role.query.filter_by(role_name=role_name).first()

        if not existing_role:
            role = Role(role_name=role_name)
            db.session.add(role)

    # ADD DEFAULT DEPARTMENTS
    departments = [
        'Operation',
        'Sales',
        'Accounts',
        'IT'
    ]

    for department_name in departments:
        existing_department = Department.query.filter_by(
            department_name=department_name
        ).first()

        if not existing_department:
            department = Department(
                department_name=department_name
            )

            db.session.add(department)

    db.session.commit()


# HOME ROUTE
@app.route('/')
def home():
    return redirect('/dashboard')


# DASHBOARD ROUTE
@app.route('/dashboard')
def dashboard():

    employees = User.query.all()

    return render_template(
        'dashboard.html',
        employees=employees
    )


# ADD EMPLOYEE ROUTE
@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():

    roles = Role.query.all()
    departments = Department.query.all()
    managers = User.query.all()

    if request.method == 'POST':

        # CONVERT STRING DATE TO PYTHON DATE
        joining_date = datetime.strptime(
            request.form['date_of_joining'],
            '%Y-%m-%d'
        ).date()

        employee = User(

            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            username=request.form['username'],
            password=request.form['password'],
            email=request.form['email'],
            mobile=request.form['mobile'],

            dept_id=int(request.form['dept_id']),
            role_id=int(request.form['role_id']),

            reporting_manager_id=request.form.get(
                'reporting_manager_id'
            ) or None,

            date_of_joining=joining_date
        )

        db.session.add(employee)
        db.session.commit()

        return redirect('/dashboard')

    return render_template(
        'add_employee.html',
        roles=roles,
        departments=departments,
        managers=managers
    )


if __name__ == '__main__':
    app.run(debug=True)