from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#db.Model is an attribute of the SQLAlchemy class
class User(db.Model):
    # creating the rows of the table
    # Integer, primary_key=True is equivalent of SERIAL PRIMARY KEY
    id = db.Column(db.Integer, primary_key=True)
    # VARCHAR(50) NOT NULL UNIQUE
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    # for a post:
    # p-324 is a post object
    # p-324 = Post()
    # p-324.author
    # or user.post --> p-324, p-12, p-43 etc

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # save user info method
    def save_user(self):
        db.session.add(self)
        db.session

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String)
    img_url = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, body, img_url, user_id):
        self.title = title
        self.body = body
        self.img_url = img_url
        self.user_id = user_id

    
