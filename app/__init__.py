from flask import Flask
from config import Config
from .extensions import db, login_manager
from .models import User, Product, Order
from app.routes import auth, shop, admin

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(shop, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/admin")

    with app.app_context():
        db.create_all()  # Ensure tables are created

    return app
