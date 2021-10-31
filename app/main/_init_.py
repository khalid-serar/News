from flask import Blueprint
import flask_bootstrap
main = Blueprint('main',__name__)
from . import views,errors
from config import config_options


def create_app(config_name):
    app = flask_bootstrap(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    flask_bootstrap.Bootstrap.init_app(app)

    # Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app