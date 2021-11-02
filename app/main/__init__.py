from flask import Flask
from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors
from config import config_options
from flask_bootstrap import BOOTSTRAP_VERSION, Bootstrap

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    BOOTSTRAP_VERSION.init_app(app)

    # Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app