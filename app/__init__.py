from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

base_path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_path, 'db.sqlite') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some_super_secret_key'
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'

db = SQLAlchemy(app)
from models import Role, User
from models import Client, Spouse, Dependent, Employer, Creditor, Business, Asset, Cashflow, Loan

migrate = Migrate(app, db)

bootstrap = Bootstrap(app)



login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



from admin import MyModelView, MyAdminIndexView, ClientView

admin = Admin(app, name="Admin", index_view=MyAdminIndexView(), base_template='my_master.html', template_mode='bootstrap4')

admin.add_view(MyModelView(Role, db.session, category='Auth'))
admin.add_view(MyModelView(User, db.session, category='Auth'))

admin.add_view(ClientView(Client, db.session))
admin.add_view(MyModelView(Spouse, db.session, category='Relations'))
admin.add_view(MyModelView(Dependent, db.session, category='Relations'))
admin.add_view(MyModelView(Employer, db.session, category='References'))
admin.add_view(MyModelView(Creditor, db.session, category='References'))
admin.add_view(MyModelView(Loan, db.session))



from app.main import AnalyticsView
admin.add_view(AnalyticsView(name='Analytics'))

# if not os.path.exists(os.path.join(base_path, 'db.sqlite')):
#     db.create_all()