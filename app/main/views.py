from . import main

@main.route('/')
def index():
    return "<h1>return from main</h1>"