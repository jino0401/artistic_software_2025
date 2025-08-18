from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bluelink.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes.timetable_api import timetable_bp
    from .routes.attendance_api import attendance_bp

    app.register_blueprint(timetable_bp, url_prefix='/api')
    app.register_blueprint(attendance_bp, url_prefix='/api')

    return app