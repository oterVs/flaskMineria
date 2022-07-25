from flask import Flask 

from .extensions import mongo

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI']='mongodb+srv://OtterFox:1XTQqHNw9X7XvkXs@cluster0.uwltrza.mongodb.net/mineria'
    mongo.init_app(app)


    app.register_blueprint(contacts)

    return app