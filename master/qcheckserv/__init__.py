from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from qcheckserv.config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from qcheckserv import models

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from qcheckserv.users.routes import users
    from qcheckserv.servers.routes import servers
    from qcheckserv.alerts.routes import alerts
    from qcheckserv.main.routes import main
    from qcheckserv.api.routes import api
    from qcheckserv.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(servers)
    app.register_blueprint(alerts)
    app.register_blueprint(main)
    app.register_blueprint(api)
    app.register_blueprint(errors)

    return app