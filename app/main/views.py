from app.auth.forms import RegistrationForm
from app.main.forms import CommentForm,PitchForm
from flask import render_template
from app.auth import auth
from flask_login import login_required,current_user
from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Upvote,Pitch,Comment
from .. import db,photos

# Views
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitches/new/', methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    pitches = Pitch.query.all()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        new_pitch = Pitch(user_id=current_user.id, title=title, description=description, category
        =category)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('pitches.html', form=form, pitches = pitches)

@main.route('/comment/new/<int:pitch_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', pitch_id = pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form, comment = all_comments, pitch = pitch)

@main.route('/pitches')
def show_pitches():
    pitches = Pitch.query.all()

    return render_template('pitch.html',pitches = pitches)