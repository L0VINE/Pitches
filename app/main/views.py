from flask import render_template
from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from ..models import Pitches, User, Comments
from . import main
from .. import db,photos
from .forms import PitchForm,CommentForm, UpdateProfile

@main.route('/')
def index():
    '''
    my index page
    return
    '''
    message= "Hello"
    title= 'Pitched!'
    return render_template('index.html', message=message,title=title)

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch= form.pitch.data
        title=form.title.data

        # Updated pitchinstance
        new_pitch = Pitches(title=title,category= category,pitch= pitch,user_id=current_user.id)

        title='New Pitch'

        new_pitch.save_pitch()

        return redirect(url_for('main.index'))

    return render_template('pitch.html',pitch_entry= form)
