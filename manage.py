from app import create_app
from app import db
from  flask_migrate import Migrate
from app.models import User, Pitches, Comments


app = create_app('production')

migrate  = Migrate(app,db)
@app.shell_context_processor
def make_shell_context():
    return dict(db = db,User = User,Pitches =Pitches, Comments=Comments )

