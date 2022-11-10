from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template

from flask_marshmallow import Marshmallow
import os
app= Flask(__name__)
baseDir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(baseDir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
db= SQLAlchemy(app)
ma = Marshmallow(app)
class userInfo(db.Model):
    name=db.Column(db.String(100))
    email=db.Column(db.String(50),primary_key=True)
    password=db.Column(db.String(100))
    def __init__(self,name, email, password):
        self.name = name
        self.email = email
        self.password=password
with app.app_context():
    db.create_all()
class UserSchema(ma.Schema):
    class Meta:
        fields=('name','email','password')
user_schema = UserSchema()
users_schema = UserSchema()
if __name__ == "__main__" :
    app.run(debug=True)
    
    main = Blueprint('main', __name__)
    

    @main.route('/')
    def index():
        return render_template('templates/index.html')

    @main.route('/profile')
    def profile():
        return render_template('profile.html')
    app.register_blueprint(main)
    auth = Blueprint('auth', __name__)

    @auth.route('/login')
    def login():
        return render_template('login.html')

    @auth.route('/signup')
    def signup():
        return render_template('signup.html')

    @auth.route('/logout')
    def logout():
        return 'Logout'

    app.register_blueprint(auth)

    
    
