from flask import Flask
#from flask.ext.mongoengine import MongoEngine
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
#app.config['MONGODB_DB'] = 'project1'
#app.config['MONGODB_HOST'] = '192.168.1.35'
#app.config['MONGODB_PORT'] = 12345
#app.config['MONGODB_USERNAME'] = 'webapp'
#app.config['MONGODB_PASSWORD'] = 'pwd123'

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from .views import posts
    from .admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()