import os
from flask import Flask, send_file, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from models import db, User
import platform
from pprint import pprint


app = Flask(__name__, static_folder='public')
CORS(app, origins=['*'])
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


"""
Create an endpoint that maps "/json_data" to return a user object that has 
an email and a password value

"""

@app.get('/info')
def info():
    print(dir(platform))
    return {'machine': platform.node()}


@app.get('/')
def home():
    return send_file('welcome.html')


@app.get('/example')
def example():
    return {'message':'Your app is running Python'}

@app.post('/users')
def users():
    # pprint(dir(request))
    data = request.form
    user = User(data['username'], data['email'], data['password'])
    print(data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@app.get('/users/<int:id>/')
def show(id):
    user = User.query.get(id)
    # posts = Post.query.filter_by(user_id = user.id)
    if user:
        return jsonify(user.to_dict())
    else:
        return {}, 404

@app.get('/users')
def all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


# @app.patch('/users/<int:id>/')
# def update_user(id):
#     user = User.query.get(id)
#     if user:



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))
