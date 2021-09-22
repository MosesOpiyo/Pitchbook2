from app import create_app
from app.main.models import User,Role
from flask_script import Manager,Server
from app import db

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role )

if __name__ == '__main__':
    manager.run()
