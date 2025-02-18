from flask import Flask
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.route("/")
    def index():
        return "Hello from Flask!"

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
