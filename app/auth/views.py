from . import auth

@auth.route('/login')
def index():
    return "<h1>return from auth</h1>"