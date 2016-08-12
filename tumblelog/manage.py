# -*- coding: utf-8 -*-
# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from tumblelog import app

manager = Manager(app)

# just demo
@manager.command
def hello():
    '''
    just say hello!
    '''
    print "hello"

@manager.option('-n', '--name', help='Your name')
def hello(name):
    print "hello", name

# Turn on debugger by default and reloader
# http://localhost:5000/
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

if __name__ == "__main__":
    manager.run()