from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50)) 
    id_number = db.Column(db.String(100))
    id_type = db.Column(db.String(50))
    date_birth = db.Column(db.Date())
    civil_status = db.Column(db.String(20))
    nationality = db.Column(db.String(20))
    # contact information
    email = db.Column(db.String(50))
    mobile_number = db.Column(db.String(50))
    # address information
    number_unit = db.Column(db.String(100))
    street = db.Column(db.String(100))
    barangay = db.Column(db.String(100))
    city_town = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    # record data
    source = db.Column(db.String(100))
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
    # related 
    spouses = db.relationship('Spouse', backref='client', lazy='dynamic')
    dependents = db.relationship('Dependent', backref='client', lazy='dynamic')
    employers = db.relationship('Employer', backref='client', lazy='dynamic')
    businesses = db.relationship('Business', backref='client', lazy='dynamic')
    creditors = db.relationship('Creditor', backref='client', lazy='dynamic') 
    assets = db.relationship('Asset', backref='client', lazy='dynamic')
    cashflows = db.relationship('Cashflow', backref='client', lazy='dynamic')
    loans = db.relationship('Loan', backref='client', lazy='dynamic')

    def __repr__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

class Spouse(db.Model):
    __tablename__ = 'spouses'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50)) 
    date_birth = db.Column(db.Date())
    # contact information
    email = db.Column(db.String(50))
    mobile_number = db.Column(db.String(50))
    # record data
    source = db.Column(db.String(100))
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
        # related 
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))

    def __repr__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

class Dependent(db.Model):
    __tablename__ = 'dependents'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50)) 
    date_birth = db.Column(db.Date())
    education = db.Column(db.String(100))
    # record data
    source = db.Column(db.String(100))
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
        # related 
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))


    def __repr__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

class Employer(db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.Integer, primary_key=True)
    employer_name = db.Column(db.String(100))
    years_employed = db.Column(db.Integer())
    designation = db.Column(db.String(100))
    status_employment = db.Column(db.String(50))
    net_monthly_salary = db.Column(db.Numeric())
    # contact information
    email = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    # address information
    address = db.Column(db.String(100))
    street = db.Column(db.String(100))
    barangay = db.Column(db.String(100))
    city_town = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    # record data
    source = db.Column(db.String(100))
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
        # related 
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))


    def __repr__(self):
        return f'{self.employer_name}'


class Business(db.Model):
    __tablename__ = 'business'
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100))
    business_type = db.Column(db.String(100))
    business_permit_number = db.Column(db.String(100))
    estimated_assets = db.Column(db.Numeric())
    esitmated_monthly_sales = db.Column(db.Numeric())
    years_in_business = db.Column(db.Integer())
    number_employees = db.Column(db.Integer()) 
    # contact information
    email = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    # address information
    address = db.Column(db.String(100))
    street = db.Column(db.String(100))
    barangay = db.Column(db.String(100))
    city_town = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    # record data
    source = db.Column(db.String(100))
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
        # related 
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))


    def __repr__(self):
        return f'{self.business_name}'

class Creditor(db.Model):
    __tablename__ = 'creditors'
    id = db.Column(db.Integer, primary_key=True)
    creditor_name = db.Column(db.String(100))
    credit_type =  db.Column(db.String(50))
    credit_status = db.Column(db.String(50))
    outstanding_loan = db.Column(db.Numeric())
    # contact information
    email = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    # address information
    address = db.Column(db.String(100))
    street = db.Column(db.String(100))
    barangay = db.Column(db.String(100))
    city_town = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    # record data
    source = db.Column(db.String(100))
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
        # related 
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))


    def __repr__(self):
        return f'{self.creditor_name}'

class Asset(db.Model):
    __tablename__ = 'assets'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    asset_type = db.Column(db.String(50))
    brand = db.Column(db.String(50))
    model = db.Column(db.String(10))
    year = db.Column(db.String(10))
   # address information if applicable
    address = db.Column(db.String(100))
    street = db.Column(db.String(100))
    barangay = db.Column(db.String(100))
    city_town = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    # record data
    source = db.Column(db.String(100))
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
        # related 
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))


    def __repr__(self):
        return f'{self.item_name}'

class Cashflow(db.Model):
    __tablename__ = 'cashflows'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    item_type = db.Column(db.String(50))
    income_expense_type = db.Column(db.String(50))
    monthly_value = db.Column(db.Numeric())
    # record data
    source = db.Column(db.String(100))
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
        # related 
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))


    def __repr__(self):
        return f'{self.item_name}'

class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric())
    purpose= db.Column(db.String(100))
    installment = db.Column(db.String(50))
    term= db.Column(db.String(50))
    interest_rate = db.Column(db.Numeric())
    loan_type = db.Column(db.String(50))
    loan_status = db.Column(db.String(50))
    recommendation = db.Column(db.String(100))
    # record data
    source = db.Column(db.String(100))
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    updated = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
    # related 
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))

    def __repr__(self):
        return f'{self.loan_type} -- {self.amount}'


