from flask import Flask
from models import db
from config import Config
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={
    r"/kopeetearia-api/*": {
        "origins": "http://localhost:5173"
    }
})

db.init_app(app)

from controllers.orders_controller import order_bp

app.register_blueprint(order_bp, url_prefix='/kopeetearia-api')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="localhost", port=8082, debug=True)