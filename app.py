from flask import Flask, render_template, request, redirect
from extensions import db
import os

app = Flask(__name__)

# SQLITE DATABASE PATH
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'employee.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INITIALIZE DB
db.init_app(app)

# IMPORT MODELS
from models import Role, Department, User


# CREATE TABLES + SEED DATA
with app.app_context():

    db.create_all()

    # INSERT ROLES
    if Role.query.count() == 0:

        roles = [
            'Admin',
            'Manager',
            'Team Leader',
            'Employee'
        ]

        for role_name in roles:

            role = Role(role_name=role_name)

            db.session.add(role)

    # INSERT DEPARTMENTS
    if Department.query.count() == 0:

        departments = [
            'Operation',
            'Sales',
            'Accounts',
            'IT'
        ]

        for department_name in departments:

            department = Department(
                department_name=department_name
            )

            db.session.add(department)

    db.session.commit()


# HOME ROUTE
@app.route('/')
def home():

    return redirect('/dashboard')


# ADD EMPLOYEE
@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():

    roles = Role.query.all()

    departments = Department.query.all()

    managers = User.query.all()

    if request.method == 'POST':

        employee = User(

            first_name=request.form['first_name'],

            last_name=request.form['last_name'],

            username=request.form['username'],

            password=request.form['password'],

            email=request.form['email'],

            mobile=request.form['mobile'],

            dept_id=int(request.form['dept_id']),

            role_id=int(request.form['role_id']),

            reporting_manager_id=request.form.get('reporting_manager_id') or None,

            date_of_joining=request.form['date_of_joining']
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


# DASHBOARD
@app.route('/dashboard')
def dashboard():

    employees = User.query.all()

    return render_template(
        'dashboard.html',
        employees=employees
    )


# DELETE EMPLOYEE
@app.route('/delete/<int:id>')
def delete_employee(id):

    employee = User.query.get(id)

    if employee:

        db.session.delete(employee)

        db.session.commit()

    return redirect('/dashboard')


# UPDATE EMPLOYEE
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_employee(id):

    employee = User.query.get(id)

    roles = Role.query.all()

    departments = Department.query.all()

    managers = User.query.all()

    if request.method == 'POST':

        employee.first_name = request.form['first_name']

        employee.last_name = request.form['last_name']

        employee.username = request.form['username']

        employee.email = request.form['email']

        employee.mobile = request.form['mobile']

        employee.dept_id = int(request.form['dept_id'])

        employee.role_id = int(request.form['role_id'])

        employee.reporting_manager_id = request.form.get('reporting_manager_id') or None

        employee.date_of_joining = request.form['date_of_joining']

        db.session.commit()

        return redirect('/dashboard')

    return render_template(
        'update_employee.html',
        employee=employee,
        roles=roles,
        departments=departments,
        managers=managers
    )


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)