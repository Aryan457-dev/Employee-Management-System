from extensions import db


# ROLE TABLE
class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)

    role_name = db.Column(db.String(100))


# DEPARTMENT TABLE
class Department(db.Model):

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)

    department_name = db.Column(db.String(100))


# USER TABLE
class User(db.Model):

    __tablename__ = 'users'

    employee_id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(100))

    last_name = db.Column(db.String(100))

    username = db.Column(db.String(100))

    password = db.Column(db.String(255))

    email = db.Column(db.String(100))

    mobile = db.Column(db.String(15))

    dept_id = db.Column(
        db.Integer,
        db.ForeignKey('departments.id')
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey('roles.id')
    )

    reporting_manager_id = db.Column(
        db.Integer,
        db.ForeignKey('users.employee_id')
    )

    date_of_joining = db.Column(db.Date)

    # RELATIONSHIPS
    department = db.relationship(
        'Department',
        backref='employees'
    )

    role = db.relationship(
        'Role',
        backref='employees'
    )