from flask import Flask 
from .main.main import main

from .enroll.enroll import enroll
def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.register_blueprint(enroll)
    return app

# Trying to learn how to implement blueprints
# Blueprints is a way to organise a group of related views and other code. Rather than registering views and other code within an applicatio directly, they are registered with a blueprint.