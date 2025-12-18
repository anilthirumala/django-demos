from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        "mssql+pyodbc://@localhost/bookfinderdb"
        "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
    #app.config.from_object('config')
    db.init_app(app)

    from app.routes.book_routes import book_bp
    app.register_blueprint(book_bp)

    return app