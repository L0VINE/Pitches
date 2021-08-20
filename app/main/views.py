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