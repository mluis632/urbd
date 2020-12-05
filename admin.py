# from app import admin
from models import User
from app import db
from flask import redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from flask_admin import helpers, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from forms import LoginForm, RegistrationForm


# Create customized index view class that handles login & registration
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = url_for('.register_view')
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()
            form.populate_obj(user)
            user.password = form.password.data
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))




class MyModelView(ModelView):
    column_exclude_list = ['created', 'updated']
    form_excluded_columns = ['created', 'updated']
    create_template = 'create.html'
    edit_template = 'edit.html'
    create_template = "create.html"
    edit_template = "edit.html"
    list_template = "list.html"
    details_template = "details.html"
    
    # def is_accessible(self):
    #     return current_user.is_authenticated


from models import Spouse, Dependent, Employer, Business, Creditor, Asset, Cashflow, Loan

civil_status = [
    ('single', 'Single'),
    ('married', 'Married')
          ]
id_type = [
    ('SSS', 'SSS'),
    ('GSIS', 'GSIS'),
    ('LTO', 'LTO'),
    ('TIN', 'TIN')
]
from wtforms.fields import StringField
from wtforms.validators import Email

class ClientView(ModelView):
    inline_models = (Spouse, Dependent, Employer, Business, Creditor, Asset, Cashflow, Loan, )
    form_choices = {'civil_status': civil_status, 'id_type': id_type}
    column_exclude_list = ['created', 'updated', 'middle_name', 'id_number', 
    'id_type', 'nationality', 'date_birth', 'country', 'source', 'civil_status']
    form_excluded_columns = ['created', 'updated']
    
    can_view_details = True
    create_template = "create.html"
    edit_template = "edit.html"
    list_template = "list.html"
    details_template = "details.html"
    # create_modal = True
    # edit_modal = True
    
    # create_template = 'create.html'
    form_args = {
    'email': {
        'validators': [Email(), ]
    },
    'city_town': {
        'label': 'City/Town',
    }
}
    column_labels = dict(city_town='City/Town',
                            unit_number='Number/Building/Unit')
    