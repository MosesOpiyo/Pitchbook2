from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import db
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch',backref = 'pitch', lazy = 'dynamic')

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)   


    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__= 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments_id = db.relationship('Comment',backref='comment',lazy = 'dynamic')
    
    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.order_by(pitch_id=id).desc().all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.description}'


class Comment(db.Model):

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.Text)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))

    def __repr__(self):
        return f'Comment : id: {self.id} comment: {self.description}'