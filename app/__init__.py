from flask import Flask
from config import Config
from .extensions import db, login_manager
from .models import User
from app.routes import auth, shop, admin


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Tell Flask-Login which view to redirect to if user not logged in

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(shop, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/admin")

    with app.app_context():
        db.create_all()  # Ensure tables are created

    return app
