from flask import Flask, render_template, request, redirect

from extensions import db

app = Flask(__name__)

# DATABASE CONFIGURATION
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/employee_management'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INITIALIZE DB
db.init_app(app)

# IMPORT MODELS
from models import Role, Department, User


# HOME ROUTE
@app.route('/')
def home():

    return redirect('/dashboard')


# ADD EMPLOYEE ROUTE
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

            dept_id=request.form['dept_id'],

            role_id=request.form['role_id'],

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


# DASHBOARD ROUTE
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

        employee.dept_id = request.form['dept_id']

        employee.role_id = request.form['role_id']

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
    app.run(debug=True)