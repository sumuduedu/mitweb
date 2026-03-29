from flask import Flask
from .extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    # Import inside function
    from flask_login import current_user
    from app.utils.menu import get_menu

    # Blueprints
    from .routes.courses import courses_bp
    from .routes.auth import auth_bp
    from .routes.dashboard import dashboard_bp
    from .routes.students import students_bp
    from .routes.public import public_bp


    app.register_blueprint(public_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(students_bp)


    # ✅ Context processor INSIDE
    @app.context_processor
    def inject_menu():
        if current_user.is_authenticated:
            return {"menu": get_menu(current_user.role)}
        return {"menu": []}

    return app
