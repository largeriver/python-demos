# -*- coding: utf-8 -*-
from flask import Flask,redirect, url_for
from flask_mongoengine import MongoEngine

#Debug Toolbar Panel
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# 可用于flask_wtf CSRF保护
# 为了增强安全性，密钥不应该直接写入代码，而要保存在环境变量中。
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

# MongoEngine
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
# app.config['MONGODB_DB'] = 'project1'
# app.config['MONGODB_HOST'] = '192.168.1.35'
# app.config['MONGODB_PORT'] = 12345
# app.config['MONGODB_USERNAME'] = 'webapp'
# app.config['MONGODB_PASSWORD'] = 'pwd123'

app.debug = True
app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
db = MongoEngine(app)
toolbar = DebugToolbarExtension(app)

# flask route

@app.route('/')
def index():
    # return redirect('/posts')
    return redirect(url_for('posts.list'))

# flask blueprint
def register_blueprints(app):
    # Prevents circular imports
    from .views import posts
    from admin.admin import admin
    app.register_blueprint(posts,url_prefix="/posts")
    app.register_blueprint(admin,url_prefix="/admin")


register_blueprints(app)

# app
if __name__ == '__main__':
    app.run()
