from flask import Flask,redirect
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

# MongoEngine
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
# app.config['MONGODB_DB'] = 'project1'
# app.config['MONGODB_HOST'] = '192.168.1.35'
# app.config['MONGODB_PORT'] = 12345
# app.config['MONGODB_USERNAME'] = 'webapp'
# app.config['MONGODB_PASSWORD'] = 'pwd123'

db = MongoEngine(app)


# flask route

@app.route('/')
def index():
    return redirect('/post')

# flask blueprint
def register_blueprints(app):
    # Prevents circular imports
    from .views import posts
    from .admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)


register_blueprints(app)

# app
if __name__ == '__main__':
    app.run()
